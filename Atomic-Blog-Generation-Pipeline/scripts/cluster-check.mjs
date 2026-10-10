#!/usr/bin/env node
// Guards the Rank One cluster against keyword cannibalization and duplicate text.
//
//   node scripts/cluster-check.mjs                 registry check (counts, owners, overlaps)
//   node scripts/cluster-check.mjs --overlap       duplicate-text scan across every article in the corpus
//   node scripts/cluster-check.mjs --draft <md>    one draft against the registry and the corpus
//
// Exit code 1 means a rule is broken. Warnings print but never fail the run.
import { readFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { join, resolve, relative } from "node:path";

const ROOT = resolve(import.meta.dirname, "..");
const REGISTRY = join(ROOT, "Atomic-Notes-Blogs-Cluster-Rank-One-System", "keyword-registry.json");
const CORPUS_DIRS = [join(ROOT, "Atomic Notes Blogs"), join(ROOT, "..", "content", "blog")];

// Words that never change what a query means.
const STOP = new Set("a an the to for in of on my your and with it its".split(" "));
// Question words do change intent ("is the notes app encrypted" asks about an app you have,
// "encrypted notes app" looks for one), so a match without them only warns.
const QUESTION = new Set("is are do does can i you what how be".split(" "));
// A shared run of this many words or more counts as copied text.
const SPAN_MIN = 12;

/** A keyword's identity: lowercased, stopwords out, plurals folded, order ignored. */
export function keyOf(phrase, { loose = false } = {}) {
  const words = phrase
    .toLowerCase()
    .replace(/\bf[\s-]?droid\b/g, "fdroid")
    .replace(/[^a-z0-9]+/g, " ")
    .split(" ")
    .filter((w) => w.length > 1 && !STOP.has(w) && !(loose && QUESTION.has(w)))
    .map((w) => (w.length > 3 && w.endsWith("s") && !w.endsWith("ss") ? w.slice(0, -1) : w));
  return [...new Set(words)].sort().join(" ");
}

const isSubset = (a, b) => {
  const B = new Set(b.split(" "));
  return a.split(" ").every((w) => B.has(w));
};

function loadRegistry() {
  return JSON.parse(readFileSync(REGISTRY, "utf8"));
}

function checkRegistry(reg) {
  const errors = [];
  const warnings = [];
  const pages = reg.pages;
  const byId = new Map(pages.map((p) => [p.id, p]));

  // Shape: counts per role, and every support hangs off a real Main Blog.
  for (const p of pages) {
    const rule = reg.rules[p.role];
    if (!rule) { errors.push(`${p.id}: unknown role "${p.role}"`); continue; }
    if (!p.primary) errors.push(`${p.id}: no primary keyword`);
    if ((p.secondary ?? []).length !== rule.secondary) errors.push(`${p.id}: ${p.secondary?.length ?? 0} secondary keywords, needs ${rule.secondary}`);
    if ((p.lsi ?? []).length > rule.lsiMax) errors.push(`${p.id}: ${p.lsi.length} LSI keywords, max ${rule.lsiMax}`);
    if (p.role === "support" && byId.get(p.mainId)?.role !== "main") errors.push(`${p.id}: mainId "${p.mainId}" is not a Main Blog`);
  }
  const mains = pages.filter((p) => p.role === "main");
  const supports = pages.filter((p) => p.role === "support");
  if (mains.length !== 15) errors.push(`${mains.length} Main Blogs, the plan needs 15`);
  if (supports.length !== 45) errors.push(`${supports.length} Support Blogs, the plan needs 45`);
  for (const m of mains) {
    const n = supports.filter((s) => s.mainId === m.id).length;
    if (n !== 3) errors.push(`${m.id}: ${n} Support Blogs, needs 3`);
  }
  const slugs = new Map();
  for (const p of pages.filter((x) => x.slug)) {
    if (slugs.has(p.slug)) errors.push(`slug "${p.slug}" used by ${slugs.get(p.slug)} and ${p.id}`);
    slugs.set(p.slug, p.id);
  }

  // Ownership: every primary and secondary has exactly one owning URL.
  const owner = new Map(); // strict key -> {id, phrase, kind}
  const looseOwner = new Map(); // key without question words -> [{id, phrase, kind}]
  for (const p of pages) {
    const own = [[p.primary, "primary"], ...(p.secondary ?? []).map((s) => [s, "secondary"])];
    const seenHere = new Set();
    for (const [phrase, kind] of own) {
      const k = keyOf(phrase);
      if (seenHere.has(k)) warnings.push(`${p.id}: "${phrase}" repeats another of its own keywords`);
      seenHere.add(k);
      const prev = owner.get(k);
      if (prev && prev.id !== p.id) errors.push(`CANNIBALIZATION: "${phrase}" (${p.id} ${kind}) = "${prev.phrase}" (${prev.id} ${prev.kind})`);
      else if (!prev) owner.set(k, { id: p.id, phrase, kind });
      const lk = keyOf(phrase, { loose: true });
      for (const o of looseOwner.get(lk) ?? []) {
        if (o.id !== p.id && keyOf(o.phrase) !== k) warnings.push(`question form: "${phrase}" (${p.id}) and "${o.phrase}" (${o.id}) differ only by question words. Keep the intents distinct`);
      }
      looseOwner.set(lk, [...(looseOwner.get(lk) ?? []), { id: p.id, phrase, kind }]);
    }
  }
  // LSI terms support a page. They may repeat across pages, but never claim another page's target.
  const lsiUse = new Map();
  for (const p of pages) {
    for (const term of p.lsi ?? []) {
      const k = keyOf(term);
      const o = owner.get(k);
      if (o && o.id !== p.id) errors.push(`${p.id}: LSI "${term}" is ${o.id}'s ${o.kind} keyword "${o.phrase}"`);
      if (o && o.id === p.id) warnings.push(`${p.id}: LSI "${term}" repeats its own ${o.kind} keyword`);
      lsiUse.set(k, [...(lsiUse.get(k) ?? []), p.id]);
    }
  }
  for (const [k, ids] of lsiUse) if (ids.length > 3) warnings.push(`LSI "${k}" is used on ${ids.length} pages (${ids.join(", ")}). Fine if natural, but vary it`);

  // Containment: a primary that sits inside another page's keyword competes for the same words.
  // Allowed when the intents differ (a definition vs a "best" list), so this only warns.
  // Pairs reviewed by a person and listed in acceptedOverlaps (with the reason) stay quiet.
  const targets = pages.flatMap((p) => [p.primary, ...(p.secondary ?? [])].map((phrase) => ({ p, phrase, k: keyOf(phrase) })));
  const accepted = new Set((reg.acceptedOverlaps ?? []).flatMap(({ pair: [x, y] }) => [`${x}|${y}`, `${y}|${x}`]));
  let acceptedHits = 0;
  for (const a of pages) {
    const ka = keyOf(a.primary);
    for (const t of targets) {
      if (t.p.id === a.id || t.k === ka || !isSubset(ka, t.k)) continue;
      if (accepted.has(`${a.id}|${t.p.id}`)) { acceptedHits++; continue; }
      const same = a.intent.split(/[ /+]/)[0] === t.p.intent.split(/[ /+]/)[0];
      warnings.push(`${same ? "SAME INTENT " : ""}overlap: ${a.id} primary "${a.primary}" sits inside ${t.p.id} "${t.phrase}" (${a.intent} vs ${t.p.intent})`);
    }
  }
  if (acceptedHits) console.log(`${acceptedHits} reviewed overlap(s) skipped, see acceptedOverlaps in the registry.`);
  return { errors, warnings };
}

// ---------- duplicate-text scan ----------

function walk(dir, out = []) {
  if (!existsSync(dir)) return out;
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p, out);
    else if (name.endsWith(".md")) out.push(p);
  }
  return out;
}

/** Article prose as a word list: no front matter, images, byline, link URLs, or Sources section. */
function proseWords(file) {
  let t = readFileSync(file, "utf8").replace(/\r\n/g, "\n");
  t = t.replace(/^---\n[\s\S]*?\n---\n/, "");
  t = t.split(/\n## Sources\b/)[0];
  t = t
    .split("\n")
    .filter((l) => !/^\s*!\[/.test(l) && !/^\*By .*Last updated/.test(l))
    .join("\n")
    .replace(/\]\([^)]*\)/g, "]")
    .replace(/<[^>]+>/g, " ")
    .toLowerCase()
    .replace(/[^a-z0-9' ]+/g, " ");
  return t.split(/\s+/).filter(Boolean);
}

function shingles(words, n = 8) {
  const m = new Map();
  for (let i = 0; i + n <= words.length; i++) {
    const s = words.slice(i, i + n).join(" ");
    if (!m.has(s)) m.set(s, i);
  }
  return m;
}

/** Shared runs of at least SPAN_MIN words between two word lists. */
function sharedSpans(aw, bw, bShingles, n = 8) {
  const spans = [];
  let i = 0;
  while (i + n <= aw.length) {
    const s = aw.slice(i, i + n).join(" ");
    if (!bShingles.has(s)) { i++; continue; }
    let j = bShingles.get(s);
    let len = n;
    while (i + len < aw.length && j + len < bw.length && aw[i + len] === bw[j + len]) len++;
    if (len >= SPAN_MIN) spans.push(aw.slice(i, i + len).join(" "));
    i += len;
  }
  return spans;
}

function compare(fa, fb, cache) {
  const get = (f) => cache.get(f) ?? (cache.set(f, { w: proseWords(f) }), cache.get(f));
  const A = get(fa), B = get(fb);
  A.s ??= shingles(A.w);
  B.s ??= shingles(B.w);
  let common = 0;
  for (const s of A.s.keys()) if (B.s.has(s)) common++;
  const containment = common / Math.max(1, Math.min(A.s.size, B.s.size));
  return { containment, spans: common ? sharedSpans(A.w, B.w, B.s) : [] };
}

const rel = (f) => relative(ROOT, f).replace(/\\/g, "/");
const pct = (x) => `${(x * 100).toFixed(1)}%`;

function overlapScan(files, against = files) {
  const cache = new Map();
  const hits = [];
  for (const a of files) {
    for (const b of against) {
      if (a === b || (files === against && a > b)) continue;
      const r = compare(a, b, cache);
      if (r.containment >= 0.03 || r.spans.length) hits.push({ a, b, ...r });
    }
  }
  return hits.sort((x, y) => y.containment - x.containment);
}

function frontmatter(file) {
  const m = readFileSync(file, "utf8").replace(/\r\n/g, "\n").match(/^---\n([\s\S]*?)\n---\n/);
  const fm = {};
  for (const line of (m?.[1] ?? "").split("\n")) {
    const kv = line.match(/^([A-Za-z]+):\s*"?(.*?)"?\s*$/);
    if (kv) fm[kv[1]] = kv[2];
  }
  return fm;
}

// ---------- main ----------

const args = process.argv.slice(2);
const reg = loadRegistry();
const { errors, warnings } = checkRegistry(reg);
let failed = errors.length > 0;

if (args[0] === "--overlap") {
  const files = CORPUS_DIRS.flatMap((d) => walk(d));
  const hits = overlapScan(files);
  console.log(`Duplicate-text scan: ${files.length} articles, 8-word shingles, runs of ${SPAN_MIN}+ words reported.\n`);
  for (const h of hits) {
    const bad = h.containment >= 0.1 || h.spans.some((s) => s.split(" ").length >= 25);
    if (bad) failed = true;
    console.log(`${bad ? "FAIL" : "note"}  ${pct(h.containment)}  ${rel(h.a)}\n            vs ${rel(h.b)}`);
    for (const s of h.spans.slice(0, 4)) console.log(`      "${s.slice(0, 160)}${s.length > 160 ? "…" : ""}"`);
  }
  if (!hits.length) console.log("No shared passages found.");
} else if (args[0] === "--draft") {
  const draft = resolve(args[1] ?? "");
  if (!existsSync(draft)) { console.error(`No such file: ${args[1]}`); process.exit(1); }
  const fm = frontmatter(draft);
  const page = reg.pages.find((p) => p.slug === fm.slug || p.draftSlug === fm.slug || (p.title === fm.title));
  console.log(`Draft: ${rel(draft)}\nRegistry page: ${page ? `${page.id} (${page.role})` : "none found by slug or title"}`);
  if (page) {
    const first = (fm.keywords ?? "").split(",")[0]?.trim();
    if (first && keyOf(first) !== keyOf(page.primary)) { failed = true; console.log(`FAIL  keywords start with "${first}", the registry primary is "${page.primary}"`); }
    const titleKey = keyOf(fm.title ?? "");
    for (const other of reg.pages) {
      if (other.id === page.id) continue;
      const k = keyOf(other.primary);
      if (k.split(" ").length >= 3 && isSubset(k, titleKey)) console.log(`warn  title contains ${other.id}'s primary "${other.primary}"`);
    }
  }
  const corpus = CORPUS_DIRS.flatMap((d) => walk(d)).filter((f) => resolve(f) !== draft);
  const hits = overlapScan([draft], corpus);
  for (const h of hits) {
    const bad = h.containment >= 0.1 || h.spans.some((s) => s.split(" ").length >= 25);
    if (bad) failed = true;
    console.log(`${bad ? "FAIL" : "note"}  ${pct(h.containment)} shared with ${rel(h.b)}`);
    for (const s of h.spans.slice(0, 4)) console.log(`      "${s.slice(0, 160)}${s.length > 160 ? "…" : ""}"`);
  }
  if (!hits.length) console.log("No shared passages with any other article.");
} else {
  const pages = reg.pages;
  const kw = pages.reduce((n, p) => n + 1 + p.secondary.length + p.lsi.length, 0);
  console.log(`Registry: ${pages.length} pages, ${kw} keywords (${pages.filter((p) => p.role === "main").length} Main, ${pages.filter((p) => p.role === "support").length} Support).`);
}

for (const w of warnings) console.log(`warn  ${w}`);
for (const e of errors) console.log(`ERROR ${e}`);
console.log(failed ? "\nFAILED" : `\nPASSED${warnings.length ? ` with ${warnings.length} warning(s)` : ""}`);
process.exit(failed ? 1 : 0);
