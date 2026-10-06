import type { Metadata } from "next";
import { SiteNav } from "@/components/SiteNav";
import { SiteFooter } from "@/components/SiteFooter";
import { KOFI_URL, PATREON_URL } from "@/lib/content";
import { pageMetadata } from "@/lib/seo";

export const metadata: Metadata = pageMetadata({
  title: "Support Atomic Notes, get Atomic Coins early",
  description:
    "Support Atomic Notes on Patreon or Ko-fi at the amount you choose. Send your Atomic Notes account email, and the developer sends you Atomic Coins as an early-supporter reward.",
  path: "/support-atomic-notes",
  socialTitle: "Support Atomic Notes, get Atomic Coins early",
});

const STEPS: { t: string; d: React.ReactNode }[] = [
  {
    t: "Find your email",
    d: (
      <>
        It&apos;s the Google email you sign in to Atomic Notes with. In the app, open <b>Atomic Energy</b> and tap{" "}
        <b>Get Atomic Coins</b> to see it.
      </>
    ),
  },
  {
    t: "Pick a platform",
    d: (
      <>
        Support the DevBehindYou page on <b>Patreon</b> or <b>Ko-fi</b>, at the amount you choose. Both reach the same
        developer and earn the same reward.
      </>
    ),
  },
  {
    t: "Send your email",
    d: (
      <>
        On Patreon, send the developer a message. On Ko-fi, write it in the message box when you pay and mark the
        message private. Check it letter by letter: the coins go to exactly that account.
      </>
    ),
  },
  {
    t: "Get your coins",
    d: (
      <>
        The developer adds your early-supporter Atomic Coins to that account by hand. They show up in Atomic Energy
        after the next refresh.
      </>
    ),
  },
];

const PLATFORMS: { name: string; tag: string; url: string; label: string; points: string[] }[] = [
  {
    name: "Patreon",
    tag: "MEMBERSHIP",
    url: PATREON_URL,
    label: "Support on Patreon",
    points: [
      "Usually a monthly membership",
      "Send your account email in a Patreon message",
      "Cancel on Patreon at any time",
    ],
  },
  {
    name: "Ko-fi",
    tag: "ONE-TIME OR MONTHLY",
    url: KOFI_URL,
    label: "Support on Ko-fi",
    points: [
      "Good for a single payment",
      "Put your account email in the message and mark it private",
      "Monthly support is also available on Ko-fi",
    ],
  },
];

export default function SupportPage() {
  return (
    <>
      <SiteNav current="support" />
      <main>
        <section className="hero lp-hero dotgrid">
          <div className="wrap support-hero">
            <p className="eyebrow">SUPPORT ATOMIC NOTES</p>
            <h1 className="support-title">
              Support the build. <span className="sig">Get coins early.</span>
            </h1>
            <p className="lp-lead">
              Atomic Notes is built by one developer, with no ads and no trackers. Coins aren&apos;t sold in the app
              yet. Support the project on Patreon or Ko-fi, and the developer sends Atomic Coins to your account as an
              early-supporter reward.
            </p>
            <div className="hero-actions">
              <a href={PATREON_URL} className="btn-signal" target="_blank" rel="noreferrer">
                Support on Patreon
              </a>
              <a href={KOFI_URL} className="btn-signal" target="_blank" rel="noreferrer">
                Support on Ko-fi
              </a>
              <a href="#how" className="btn-ghost">
                How it works
              </a>
            </div>
          </div>
        </section>

        <section id="platforms">
          <div className="wrap">
            <p className="eyebrow">TWO WAYS TO SUPPORT</p>
            <h2>
              Pick the one <span className="sig">that suits you.</span>
            </h2>
            <div className="support-platforms">
              {PLATFORMS.map((p) => (
                <div key={p.name} className="feature support-platform">
                  <p className="num">{p.tag}</p>
                  <h3>{p.name}</h3>
                  <ul className="support-list">
                    {p.points.map((pt) => (
                      <li key={pt}>{pt}</li>
                    ))}
                  </ul>
                  <a href={p.url} className="btn-signal" target="_blank" rel="noreferrer">
                    {p.label}
                  </a>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section id="how">
          <div className="wrap">
            <p className="eyebrow">FOUR STEPS</p>
            <h2>
              How the reward <span className="sig">reaches you.</span>
            </h2>
            <ol className="steps">
              {STEPS.map((s, i) => (
                <li key={s.t}>
                  <span className="num">{String(i + 1).padStart(2, "0")}</span>
                  <h3>{s.t}</h3>
                  <p>{s.d}</p>
                </li>
              ))}
            </ol>

            <div className="support-grid">
              <div className="support-note">
                <p className="num">IMPORTANT</p>
                <h3>Use the exact account email</h3>
                <p>
                  The reward is sent to the email you write, not to your Patreon or Ko-fi name. A wrong or misspelled
                  email means the coins can&apos;t reach you. If you signed in with more than one Google account, use the
                  one that holds your notes. On Ko-fi, mark the message private so your email isn&apos;t shown on the
                  public page.
                </p>
              </div>
              <div className="feature">
                <p className="num">GOOD TO KNOW</p>
                <ul className="support-list">
                  <li>
                    Patreon or Ko-fi handles the payment. Atomic Notes never sees your card, PayPal, or bank details.
                  </li>
                  <li>Each platform charges its own fees, under its own terms.</li>
                  <li>The developer sends rewards by hand, so they can take a little time to arrive.</li>
                  <li>Writing notes stays free. Coins only buy sync energy and room for more notes.</li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        <section>
          <div className="wrap">
            <p className="eyebrow">WHAT COINS DO</p>
            <h2>
              One coin, <span className="sig">40 energy.</span>
            </h2>
            <dl className="facts support-facts">
              <div>
                <dt>Convert</dt>
                <dd>1 Atomic Coin adds 40 energy, enough for 8 automatic syncs</dd>
              </div>
              <div>
                <dt>Antimatter</dt>
                <dd>10 coins, room for 40 notes</dd>
              </div>
              <div>
                <dt>Monopole</dt>
                <dd>20 more coins, room for 50 notes</dd>
              </div>
              <div>
                <dt>Strangelet</dt>
                <dd>30 more coins, room for 100 notes</dd>
              </div>
            </dl>
            <div className="hero-actions">
              <a href={PATREON_URL} className="btn-signal" target="_blank" rel="noreferrer">
                Support on Patreon
              </a>
              <a href={KOFI_URL} className="btn-signal" target="_blank" rel="noreferrer">
                Support on Ko-fi
              </a>
            </div>
          </div>
        </section>
      </main>
      <SiteFooter />
    </>
  );
}
