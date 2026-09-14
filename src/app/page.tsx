import Link from "next/link";
import { SiteNav } from "@/components/SiteNav";
import { AtomMark } from "@/components/AtomMark";
import { Reveal } from "@/components/Reveal";
import { Compare } from "@/components/Compare";
import { Gallery, type Shot } from "@/components/Gallery";
import { EnergyDemo } from "@/components/EnergyDemo";
import { CURRENT_PHASE, FEATURES, ROADMAP, type NotificationRow } from "@/lib/content";
import { fetchActiveNotifications } from "@/lib/atomicServer";

export const dynamic = "force-dynamic";

const APK =
  process.env.NEXT_PUBLIC_APK_URL ||
  "https://github.com/DevBehindYou/Project-Atomic-Notes-New/releases/tag/ci-latest";

// All 19 app mockups, ordered as a product tour.
const SHOTS: Shot[] = [
  { src: "/mockups/atomic-notes-mockup-image-03.png", label: "Notes" },
  { src: "/mockups/atomic-notes-mockup-image-05.png", label: "Editor · Note" },
  { src: "/mockups/atomic-notes-mockup-image-19.png", label: "Writing a Note" },
  { src: "/mockups/atomic-notes-mockup-image-04.png", label: "Editor · Checklist" },
  { src: "/mockups/atomic-notes-mockup-image-06.png", label: "Select & Delete" },
  { src: "/mockups/atomic-notes-mockup-image-13.png", label: "Energy Popup" },
  { src: "/mockups/atomic-notes-mockup-image-14.png", label: "Atomic Energy" },
  { src: "/mockups/atomic-notes-mockup-image-15.png", label: "Convert Coins" },
  { src: "/mockups/atomic-notes-mockup-image-16.png", label: "Coin Store" },
  { src: "/mockups/atomic-notes-mockup-image-18.png", label: "Notifications" },
  { src: "/mockups/atomic-notes-mockup-image-12.png", label: "Encryption" },
  { src: "/mockups/atomic-notes-mockup-image-17.png", label: "Recovery Phrase" },
  { src: "/mockups/atomic-notes-mockup-image-09.png", label: "Security" },
  { src: "/mockups/atomic-notes-mockup-image-08.png", label: "Cloud Sync" },
  { src: "/mockups/atomic-notes-mockup-image-07.png", label: "Database" },
  { src: "/mockups/atomic-notes-mockup-image-02.png", label: "Settings" },
  { src: "/mockups/atomic-notes-mockup-image-11.png", label: "Account" },
  { src: "/mockups/atomic-notes-mockup-image-01.png", label: "Profile" },
  { src: "/mockups/atomic-notes-mockup-image-10.png", label: "Danger Zone" },
];

async function latestUpdates(): Promise<NotificationRow[]> {
  try {
    const rows = (await fetchActiveNotifications()) as NotificationRow[];
    return rows.slice(0, 3);
  } catch {
    return [];
  }
}

export default async function Home() {
  const updates = await latestUpdates();

  return (
    <>
      <SiteNav />
      <main id="top">
        {/* HERO */}
        <section className="hero">
          <div className="wrap hero-grid">
            <div>
              <p className="eyebrow">LOCAL-FIRST · PRIVATE · YOURS</p>
              <h1>
                <span className="offset" data-text="ATOMIC NOTES">
                  ATOMIC NOTES
                </span>
              </h1>
              <p className="sub">Notes that stay on your device</p>
              <p className="lead">
                A privacy-first notes app. No ads, no trackers, no reading your
                notes. Optional encrypted cloud sync, powered by a renewable
                energy allowance.
              </p>
              <div className="hero-actions">
                <a href={APK} className="btn-signal">
                  Download the APK
                </a>
                <Link href="/updates" className="btn-ghost">
                  See updates
                </Link>
              </div>
              <div className="hero-badges">
                <div>
                  <b>AES-256</b>GCM encryption
                </div>
                <div>
                  <b>0</b>trackers · ads
                </div>
                <div>
                  <b>120</b>energy cap
                </div>
              </div>
            </div>
            <AtomMark />
          </div>
        </section>

        {/* CURRENT PHASE */}
        <section id="why">
          <div className="wrap">
            <Reveal>
              <div className="module dark">
                <p className="eyebrow" style={{ color: "#b9b4ff" }}>
                  {CURRENT_PHASE.label}
                </p>
                <h2 style={{ fontSize: "clamp(1.9rem,4.4vw,2.8rem)" }}>
                  {CURRENT_PHASE.title}
                </h2>
                <p style={{ marginTop: 14, color: "rgba(244,245,241,.72)", maxWidth: "60ch" }}>
                  {CURRENT_PHASE.body}
                </p>
              </div>
            </Reveal>

            <Reveal className="grid g2" >
              {FEATURES.map((f) => (
                <div className="module" key={f.k} style={{ marginTop: 18 }}>
                  <p className="num">{f.k}</p>
                  <h3 style={{ fontSize: "1.6rem", marginTop: 6 }}>{f.t}</h3>
                  <p style={{ color: "var(--slate)", marginTop: 8 }}>{f.d}</p>
                </div>
              ))}
            </Reveal>
          </div>
        </section>

        {/* ENERGY (interactive) */}
        <section id="energy">
          <div className="wrap">
            <Reveal>
              <p className="eyebrow">ATOMIC ENERGY · TRY IT</p>
              <h2>
                Energy powers <span className="sig">sync.</span>
              </h2>
              <p className="lead" style={{ marginTop: 12, marginBottom: 24 }}>
                Local notes are always free. Energy only powers cloud sync — earn
                it daily, or top up with coins. Play with the real economy below.
              </p>
            </Reveal>
            <Reveal>
              <EnergyDemo />
            </Reveal>
          </div>
        </section>

        {/* INTERFACE (gallery) */}
        <section id="interface">
          <div className="wrap">
            <Reveal>
              <p className="eyebrow">THE INTERFACE</p>
              <h2>
                Ink on paper. One <span className="sig">signal.</span>
              </h2>
              <p className="lead" style={{ marginTop: 12, marginBottom: 8 }}>
                A restrained Technical Editorial design. Tap any screen to zoom.
              </p>
            </Reveal>
            <Gallery shots={SHOTS} />
          </div>
        </section>

        {/* COMPARE */}
        <section id="compare">
          <div className="wrap">
            <Reveal>
              <p className="eyebrow">THE THESIS</p>
              <h2>
                Your notes became <span className="sig">training data.</span>
              </h2>
              <p className="lead" style={{ margin: "12px 0 20px" }}>
                Atomic Notes is built to be structurally incapable of that model.
              </p>
              <Compare />
            </Reveal>
          </div>
        </section>

        {/* ROADMAP */}
        <section id="roadmap">
          <div className="wrap">
            <Reveal>
              <p className="eyebrow">DEVELOPMENT PHASES</p>
              <h2>
                Where it&apos;s <span className="sig">going.</span>
              </h2>
              <ul className="tl" style={{ marginTop: 22 }}>
                {ROADMAP.map((r) => (
                  <li key={r.phase}>
                    <span className="num">{r.phase}</span>
                    <span style={{ flex: 1 }}>{r.title}</span>
                    <span className={"tag " + (r.state === "done" ? "done" : r.state === "now" ? "now" : "")}>
                      {r.state === "done" ? "Shipped" : r.state === "now" ? "Now" : "Next"}
                    </span>
                  </li>
                ))}
              </ul>
            </Reveal>
          </div>
        </section>

        {/* LATEST UPDATES */}
        <section id="updates-strip">
          <div className="wrap">
            <Reveal>
              <div style={{ display: "flex", alignItems: "baseline", justifyContent: "space-between", gap: 12, flexWrap: "wrap" }}>
                <div>
                  <p className="eyebrow">LATEST UPDATES</p>
                  <h2>
                    Straight from <span className="sig">the build.</span>
                  </h2>
                </div>
                <Link href="/updates" className="btn-ghost">
                  All updates
                </Link>
              </div>
              <div className="grid" style={{ marginTop: 20 }}>
                {updates.length === 0 && (
                  <div className="module">No active updates right now — check back soon.</div>
                )}
                {updates.map((n) => (
                  <div className="module" key={n.id} style={{ borderLeft: "4px solid var(--signal)" }}>
                    <p className="num">{n.type.replace(/_/g, " ")} · {n.priority}</p>
                    <h3 style={{ fontSize: "1.4rem", marginTop: 6 }}>{n.subject}</h3>
                    <p style={{ color: "var(--slate)", marginTop: 6 }}>{n.description}</p>
                  </div>
                ))}
              </div>
            </Reveal>
          </div>
        </section>

        {/* GET */}
        <section id="get">
          <div className="wrap">
            <Reveal>
              <p className="eyebrow">GET IT</p>
              <h2>
                Sideload it. Keep <span className="sig">control.</span>
              </h2>
              <p className="lead" style={{ margin: "12px 0 22px" }}>
                Download the latest signed APK from GitHub Releases. On most
                phones, use <span className="mono">app-arm64-v8a-release.apk</span>.
              </p>
              <div className="hero-actions">
                <a href={APK} className="btn-signal">
                  Download the APK
                </a>
                <a
                  href="https://github.com/DevBehindYou/Project-Atomic-Notes"
                  className="btn-ghost"
                  target="_blank"
                  rel="noreferrer"
                >
                  View the project
                </a>
              </div>
            </Reveal>
          </div>
        </section>
      </main>

      <footer className="footer">
        <div className="wrap">
          <p className="mono" style={{ fontSize: ".72rem", letterSpacing: "1px", color: "var(--slate)" }}>
            ATOMIC NOTES · DEVBEHINDYOU · LOCAL-FIRST · SYNCED · YOURS
          </p>
        </div>
      </footer>
    </>
  );
}
