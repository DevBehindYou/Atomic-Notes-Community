#!/usr/bin/env node
// Rebuilds the Rank One plan documents from keyword-registry.json, so the topic map, the social
// matrix and the keyword map can never disagree with the registry.
//
//   node scripts/cluster-docs.mjs
//
// Writes 02_ATOMIC_NOTES_MAIN_AND_SUPPORT_TOPIC_MAP.md, 05_ATOMIC_NOTES_KEYWORD_MAP.md, and the
// 45 support sections of 03_ATOMIC_NOTES_SOCIAL_SUPPORT_POSTS_MATRIX.md (its header and footer
// are kept as written).
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { join, resolve } from "node:path";

const DIR = join(resolve(import.meta.dirname, ".."), "Atomic-Notes-Blogs-Cluster-Rank-One-System");
const reg = JSON.parse(readFileSync(join(DIR, "keyword-registry.json"), "utf8"));
const evidencePath = join(DIR, "research", "autocomplete-evidence.json");
const evidence = existsSync(evidencePath) ? JSON.parse(readFileSync(evidencePath, "utf8")) : { keywords: {} };
const SITE = "https://atomic-notes.devbehindyou.com";

const pages = reg.pages;
const byId = new Map(pages.map((p) => [p.id, p]));
const mains = pages.filter((p) => p.role === "main");
const supportsOf = (id) => pages.filter((p) => p.mainId === id);
const PILLARS = ["PRIVACY", "LOCAL FIRST", "SECURITY"];

/** Autocomplete presence as "G B D": a letter when that engine suggested the exact phrase. */
function signal(k) {
  const e = evidence.keywords[k.toLowerCase()];
  if (!e) return "n/a";
  return `${e.google ? "G" : "·"} ${e.bing ? "B" : "·"} ${e.ddg ? "D" : "·"}`;
}
const kw = (k) => `\`${k}\` (${signal(k)})`;
const url = (p) => (p.slug ? `${SITE}/blog/${p.slug}` : null);
const write = (name, text) => writeFileSync(join(DIR, name), text.replace(/\r\n/g, "\n"), "utf8");

// ---------- 02 topic map ----------

const crossLinks = {
  P1: "P5, S4, P2", P2: "P1, L2, S2", P3: "P1, S3, S5", P4: "P5, S4, P2", P5: "P1, S4, P4",
  L1: "L3, L5, P5", L2: "L1, L4, P2", L3: "L1, L4, L5", L4: "L3, L2, P2", L5: "L1, S1, P5",
  S1: "S4, S2, L5", S2: "S1, P2, S4", S3: "P3, S5, S1", S4: "S1, P5, P1", S5: "S3, P1, L1",
};

function sourceLine(p) {
  if (p.status === "new") return "New";
  return `Existing draft: \`${p.source}\` (work: ${p.work})`;
}

let t02 = `# Atomic Notes Main and Support Topic Map

Generated from \`keyword-registry.json\` by \`node scripts/cluster-docs.mjs\`. Edit the registry, not this file.

## Structure

• 3 pillars
• 5 Main Blogs per pillar
• 3 Support Blogs per Main Blog
• 15 Main Blogs total
• 45 Support Blogs total

Main Blogs belong on the Atomic Notes website. Support Blogs are unique external articles that link contextually to their assigned Main Blog.

Keyword rules (checked by \`node scripts/cluster-check.mjs\`):

• Main Blog: 1 primary, 2 secondary, up to 10 LSI
• Support Blog: 1 primary, 4 secondary, up to 10 LSI
• A primary or secondary keyword belongs to exactly one URL in the whole cluster
• An LSI term may repeat across pages, but never as another page's primary or secondary

Research evidence and every change from the original plan are in \`05_ATOMIC_NOTES_KEYWORD_MAP.md\`.

`;

for (const pillar of PILLARS) {
  t02 += `# ${pillar}\n\n`;
  for (const m of mains.filter((x) => x.pillar === pillar)) {
    t02 += `## ${m.id}. ${m.title}\n\n`;
    t02 += `**Role:** Main Blog\n**Source status:** ${sourceLine(m)}\n`;
    t02 += `**Primary keyword:** \`${m.primary}\`\n**Secondary keywords:** ${m.secondary.map((s) => `\`${s}\``).join(", ")}\n`;
    t02 += `**LSI keywords:** ${m.lsi.join(", ")}\n**Search intent:** ${m.intent}\n`;
    t02 += `**Atomic Notes URL:** \`/blog/${m.slug}\`${m.draftSlug ? ` (current draft slug \`${m.draftSlug}\`, change it before first publish)` : ""}\n`;
    t02 += `**Angle:** ${m.angle}\n**Why this is a Main Blog:** ${m.why}\n`;
    if (m.change) t02 += `**Changed from the original plan:** ${m.change}\n`;
    t02 += `\n### Support Blogs\n\n`;
    for (const s of supportsOf(m.id)) {
      t02 += `#### ${s.id}. ${s.title}\n\n`;
      if (s.previousTitle) t02 += `**Original plan title:** ${s.previousTitle}\n`;
      t02 += `**Primary keyword:** \`${s.primary}\`\n**Secondary keywords:** ${s.secondary.map((x) => `\`${x}\``).join(", ")}\n`;
      t02 += `**LSI keywords:** ${s.lsi.join(", ")}\n**Source status:** ${sourceLine(s)}\n`;
      t02 += `**Platform:** ${s.platform}\n**Search intent:** ${s.intent}\n**Purpose:** ${s.angle}\n`;
      t02 += `**Required destination link:** \`/blog/${m.slug}\`\n`;
      if (s.change) t02 += `**Changed from the original plan:** ${s.change}\n`;
      t02 += `\n`;
    }
    t02 += `### Internal Link Targets\n\n• Link to the Atomic Notes by DevBehindYou hub (\`/blog/${byId.get("HUB").slug}\`) when Atomic Notes is discussed.\n• Contextual Main Blog links: ${crossLinks[m.id]}.\n• Link to the official GitHub repository when architecture or source claims need verification.\n\n---\n\n`;
  }
}

t02 += `# Brand Hub and Side Cluster

`;
for (const id of ["HUB", "ECON"]) {
  const p = byId.get(id);
  t02 += `## ${p.id}. ${p.title}\n\n**Source status:** ${sourceLine(p)}\n**Primary keyword:** \`${p.primary}\`\n**Secondary keywords:** ${p.secondary.map((s) => `\`${s}\``).join(", ")}\n**LSI keywords:** ${p.lsi.join(", ")}\n**URL:** \`/blog/${p.slug}\`\n`;
  if (p.change) t02 += `**Note:** ${p.change}\n`;
  t02 += `\n`;
}

t02 += `# Recommended Main-Blog Cross-Link Graph

| Main | Contextual Main-Blog Links |
|---|---|
${Object.entries(crossLinks).map(([a, b]) => `| ${a} | ${b} |`).join("\n")}

Use these as suggestions, not exact-match link rules. Link only where the section genuinely helps the reader.

# Support Blog Publication Guidance

Choose platforms by topic fit rather than rotating mechanically.

• Medium: editorial privacy, consumer education, comparisons
• WordPress: evergreen search-focused support articles
• DEV Community: architecture, encryption, sync, engineering comparisons
• Hashnode: technical local-first and security architecture
• Substack: opinion and analysis pieces such as open source, lock-in, data ownership, and recovery tradeoffs

Do not use low-quality publishing sites solely because they allow a backlink.
`;
write("02_ATOMIC_NOTES_MAIN_AND_SUPPORT_TOPIC_MAP.md", t02);

// ---------- 03 social matrix: regenerate the 45 support sections ----------

const m03Path = join(DIR, "03_ATOMIC_NOTES_SOCIAL_SUPPORT_POSTS_MATRIX.md");
const m03 = readFileSync(m03Path, "utf8").replace(/\r\n/g, "\n");
const headEnd = m03.indexOf("\n---\n\n# P1-S1");
const tailStart = m03.indexOf("# Required CTA and Tracking Convention");
if (headEnd < 0 || tailStart < 0) throw new Error("03 matrix layout changed: header or footer marker not found");
const head = m03.slice(0, headEnd).replace("Concise open-web, privacy, FOSS, or architecture angle.", "Concise open-web, privacy, or architecture angle.");
const tail = m03.slice(tailStart);

function section(s) {
  const m = byId.get(s.mainId);
  const q = s.primary;
  return `# ${s.id} • ${s.title}

**Pillar:** ${s.pillar}
**Supports Main Blog:** ${m.id} • ${m.title}
**Support Blog platform:** ${s.platform}
**Primary keyword:** \`${q}\`
**Secondary keywords:** ${s.secondary.map((x) => `\`${x}\``).join(", ")}
**Core angle:** ${s.angle}

## X.com

Hook: "${s.title}" as a curiosity or checklist post. Lead with one surprising distinction from the article. CTA: read the Support Blog for the full breakdown.

## LinkedIn

Frame the topic as a product-design or digital-trust lesson. Core point: ${s.angle} Close by asking how teams should evaluate this issue, then link to the Support Blog.

## Instagram

Carousel or Reel: first slide "${s.title}". Use 5 educational frames that simplify the article, then a final "Read the full guide" CTA. Visual style should match Atomic Notes technical-editorial branding. Write alt text for every frame.

## Reddit

Discussion title based on the real question behind \`${q}\`. Give the useful answer in the post itself. Ask for disagreement or real-world experience. Disclose that you build Atomic Notes by DevBehindYou if you mention it, and link only if the subreddit rules allow.

## Threads

Start with a conversational version of the central idea: ${s.angle} Use 2 to 5 short posts or one compact post, then point readers to the Support Blog.

## Facebook

Use a practical "before you trust, switch, or enable this, check these things" angle around \`${q}\`. Add a short checklist and link to the Support Blog.

## Pinterest

Pin title: "${s.title}". Create a checklist, comparison, or diagram graphic built for saves. The description should naturally include \`${q}\` and link directly to the Support Blog.

## Bluesky

Use a concise privacy, open-web, or architecture angle around \`${q}\`. State one clear takeaway, avoid hype, and link to the Support Blog.

---

`;
}

const supports = PILLARS.flatMap((pl) => mains.filter((m) => m.pillar === pl).flatMap((m) => supportsOf(m.id)));
write("03_ATOMIC_NOTES_SOCIAL_SUPPORT_POSTS_MATRIX.md", `${head}\n---\n\n${supports.map(section).join("")}${tail}`);

// ---------- 05 keyword map ----------

const all = [...mains.flatMap((m) => [m, ...supportsOf(m.id)]), byId.get("HUB"), byId.get("ECON")];
const owners = all.flatMap((p) => [[p.primary, p.id, "primary"], ...p.secondary.map((s) => [s, p.id, "secondary"])]).sort((a, b) => a[0].localeCompare(b[0]));
const noSignal = owners.filter(([k]) => signal(k) === "· · ·");
const changed = all.filter((p) => p.change);

let t05 = `# Atomic Notes Keyword Map, Research, and Cannibalization Guard

Generated from \`keyword-registry.json\` by \`node scripts/cluster-docs.mjs\` on ${new Date().toISOString().slice(0, 10)}. Edit the registry, then rerun the generator and \`node scripts/cluster-check.mjs\`.

## How the research was done

• **Demand.** ${evidence.meta?.method ?? "No evidence file found."} ${evidence.meta?.probes ? `${evidence.meta.probes} queries were probed.` : ""}
• **Intent.** Live search results were reviewed for the head terms and for every keyword whose intent was in doubt. Findings are in the "Changes" section below.
• **What the marks mean.** \`G B D\` means Google, Bing and DuckDuckGo all suggested the exact phrase. A dot means that engine didn't. \`· · ·\` means no autocomplete signal: kept only as a title-match or brand term, never as the reason a page exists.
• **What this is not.** These are not search volumes. No volume, difficulty or traffic numbers were invented. For volumes, export this keyword list into Google Search Console (after launch) or Keyword Planner.

## Rules this map enforces

• Main Blog: 1 primary, 2 secondary, up to 10 LSI. Support Blog: 1 primary, 4 secondary, up to 10 LSI.
• Each primary and secondary keyword has exactly one owner URL in the whole cluster (see the ownership index).
• LSI terms are supporting vocabulary. They may repeat across pages, never as another page's target.
• Matching ignores case, plurals, word order, and small words (a, the, for, your). Question words count, because "is the notes app encrypted" and "encrypted notes app" are different searches.
• Overlaps a person reviewed and accepted are listed below with the reason. Anything else that overlaps fails \`cluster-check.mjs\`.

## Duplicate content (plagiarism) guard

• \`node scripts/cluster-check.mjs --overlap\` compares every article in \`Atomic Notes Blogs/\` and \`content/blog/\` using 8-word shingles. A pair fails at 10% shared text or any shared run of 25+ words.
• \`node scripts/cluster-check.mjs --draft <file.md>\` checks one new draft against the corpus and confirms its first keyword matches the registry primary.
• Baseline on 2026-10-07: 28 articles, highest overlap 1.7%, no failures. The repeated listicle disclosure line ("Atomic Notes is my app, so it goes first") should be reworded per article before the listicles go live on the same site.
• External check: before publishing, search two or three distinctive sentences in quotes. A spot check of three existing drafts on 2026-10-07 found no copies online. Support Blogs must be written fresh, not reworded from their Main Blog.
• Never publish the same article on the site and on Medium. A Main Blog republished elsewhere must carry a canonical link to the site.

## Overview

| ID | Role | Title | Primary keyword | Signal |
|---|---|---|---|---|
${all.map((p) => `| ${p.id} | ${p.role} | ${p.title.replace(/\|/g, "/")} | \`${p.primary}\` | ${signal(p.primary)} |`).join("\n")}

`;

for (const pillar of PILLARS) {
  t05 += `## ${pillar}\n\n`;
  for (const m of mains.filter((x) => x.pillar === pillar)) {
    for (const p of [m, ...supportsOf(m.id)]) {
      t05 += `### ${p.id} · ${p.title}\n\n`;
      t05 += `• **Role:** ${p.role === "main" ? `Main Blog on ${url(p)}` : `Support Blog on ${p.platform}, links to ${m.id}`}\n`;
      t05 += `• **Status:** ${p.status === "new" ? "new article" : `existing draft, ${p.work}`}\n`;
      t05 += `• **Intent:** ${p.intent}\n`;
      t05 += `• **Primary:** ${kw(p.primary)}\n`;
      t05 += `• **Secondary:** ${p.secondary.map(kw).join(", ")}\n`;
      t05 += `• **LSI (${p.lsi.length}):** ${p.lsi.join(", ")}\n`;
      if (p.change) t05 += `• **Changed:** ${p.change}\n`;
      t05 += `\n`;
    }
  }
}

t05 += `## Brand hub and side cluster\n\n`;
for (const id of ["HUB", "ECON"]) {
  const p = byId.get(id);
  t05 += `### ${p.id} · ${p.title}\n\n• **Primary:** ${kw(p.primary)}\n• **Secondary:** ${p.secondary.map(kw).join(", ")}\n• **LSI:** ${p.lsi.join(", ")}\n${p.change ? `• **Note:** ${p.change}\n` : ""}\n`;
}

t05 += `## Accepted overlaps

These pairs share words, but a person reviewed each one and the intents differ.

| Pages | Why it's allowed |
|---|---|
${(reg.acceptedOverlaps ?? []).map((o) => `| ${o.pair.join(" and ")} | ${o.reason} |`).join("\n")}

## Keywords without autocomplete signal

Kept on purpose, never as a page's only reason to exist:

${noSignal.map(([k, id, kind]) => `• \`${k}\` (${id} ${kind})`).join("\n")}

## Keyword ownership index

Before using any of these as the focus of a new article, check who owns it.

| Keyword | Owner | As |
|---|---|---|
${owners.map(([k, id, kind]) => `| ${k} | ${id} | ${kind} |`).join("\n")}

## Changes from the original plan (${changed.length})

${changed.map((p) => `• **${p.id}**${p.previousTitle ? ` (was "${p.previousTitle}")` : ""}: ${p.change}`).join("\n")}
`;
write("05_ATOMIC_NOTES_KEYWORD_MAP.md", t05);

console.log(`Wrote 02 (${mains.length} Main, ${supports.length} Support), 03 (${supports.length} sections), 05 (${owners.length} owned keywords, ${noSignal.length} without signal, ${changed.length} changes).`);
