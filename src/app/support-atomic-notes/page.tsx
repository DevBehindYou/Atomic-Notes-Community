import type { Metadata } from "next";
import { SiteNav } from "@/components/SiteNav";
import { SiteFooter } from "@/components/SiteFooter";
import { SupportReactor } from "@/components/SupportReactor";
import { KOFI_URL, PATREON_URL } from "@/lib/content";
import { MEMBERSHIPS, formatUsd } from "@/lib/supportPricing";
import { pageMetadata } from "@/lib/seo";

export const metadata: Metadata = pageMetadata({
  title: "Support Atomic Notes: power the build, get Atomic Coins",
  description:
    "Help keep Atomic Notes independent. Support it once on Ko-fi or monthly on Patreon, and get Atomic Coins as a thank-you. Your notes stay yours either way.",
  path: "/support-atomic-notes",
  socialTitle: "Support Atomic Notes: power the build",
});

const GOES_TO: { t: string; d: string }[] = [
  { t: "Sync infrastructure", d: "The server and database that keep your devices in step." },
  { t: "Testing and bug fixes", d: "Real phones, real networks, and the bugs they find." },
  { t: "Security and reliability", d: "The vault, sync safety, and the boring work that keeps them sound." },
  { t: "Future releases", d: "New features, more platforms, and wider distribution." },
];

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
    t: "Support once or monthly",
    d: (
      <>
        One-time support goes through <b>Ko-fi</b>, where you enter the amount. Monthly support is a <b>Patreon</b>{" "}
        membership. Both reach the same developer.
      </>
    ),
  },
  {
    t: "Send your email",
    d: (
      <>
        On Ko-fi, paste the message from the reactor, add your email, and mark it private. On Patreon, send the
        developer a message. Never send a password, recovery phrase, or sign-in code.
      </>
    ),
  },
  {
    t: "Get your coins",
    d: (
      <>
        The developer checks the payment and adds the coins to that account by hand, so it can take a little time.
        They show up in Atomic Energy after the next refresh.
      </>
    ),
  },
];

const FAQ: { q: string; a: React.ReactNode }[] = [
  {
    q: "Do I need to support to use Atomic Notes?",
    a: "No. Writing, editing, and keeping notes on your phone never depends on a payment or a membership.",
  },
  {
    q: "What do Atomic Coins do?",
    a: "They're in-app credits. You can turn them into Atomic Energy for cloud sync, or use them to make room for more notes.",
  },
  {
    q: "Are coins added instantly?",
    a: "Not yet. The developer adds them by hand after checking the payment and the account email, so they can take a little time. These steps will be updated if delivery becomes automatic.",
  },
  {
    q: "Which amounts go to Patreon and which to Ko-fi?",
    a: "$2, $4, and $10 are the monthly memberships on Patreon: Atomic Spark, Atomic Catalyst, and Atomic Reactor. Any other amount from $1 to $10 is a one-time payment on Ko-fi, where you enter the amount yourself.",
  },
  {
    q: "What if I pay a different amount on Ko-fi?",
    a: "Coins follow the amount you actually paid, using the reactor's table for $1 to $10. For more than $10, message the developer before paying.",
  },
  {
    q: "Can I support without getting coins?",
    a: "Yes. Choose Support only in the reactor, or just leave a tip on Ko-fi without an email.",
  },
  {
    q: "What if I sent the wrong account email?",
    a: "Message the developer on the platform you used, with your payment reference. Never share your password, recovery phrase, or a one-time code.",
  },
  {
    q: "Can I cancel a Patreon membership?",
    a: "Yes, at any time on Patreon. Monthly coins are tied to each month that's actually paid.",
  },
];

export default function SupportPage() {
  return (
    <>
      <SiteNav current="support" />
      <main className="support-page">
        <section className="hero lp-hero dotgrid">
          <div className="wrap support-hero">
            <p className="eyebrow">ATOMIC NOTES / INDEPENDENT DEVELOPMENT</p>
            <h1 className="support-title">
              Help keep Atomic Notes <span className="sig">independent.</span>
            </h1>
            <p className="lp-lead">
              Atomic Notes is a source-available, local-first notes app built by one developer, with no ads, no
              trackers, and no AI. Your support funds sync infrastructure, security work, real-device testing, and
              future releases. As a thank-you, supporters get Atomic Coins.
            </p>
            <p className="support-promise">Your notes stay yours, whether or not you support.</p>
            <div className="hero-actions">
              <a href="#reactor" className="btn-signal">
                Open the reactor
              </a>
              <a href="#monthly" className="btn-ghost">
                Compare memberships
              </a>
              <a href="#how" className="btn-ghost">
                How coins arrive
              </a>
            </div>
          </div>
        </section>

        <section id="reactor" className="lp-dark rx-section">
          <div className="wrap">
            <p className="eyebrow">ATOMIC NOTES / SUPPORT SYSTEM 01</p>
            <h2>
              Power the <span className="sig-light">build.</span>
            </h2>
            <p className="lp-lead lp-lead-dark rx-intro">
              Pick an amount and see your Atomic Coins. $2, $4, and $10 are the monthly memberships on Patreon. Any
              other amount is a one-time payment on Ko-fi.
            </p>
            <div className="rx-grid">
              <SupportReactor />
              <aside className="rx-side" aria-label="Where support goes">
                <p className="rx-side-label">WHERE SUPPORT GOES</p>
                <ol className="rx-goes">
                  {GOES_TO.map((g, i) => (
                    <li key={g.t}>
                      <span className="rx-goes-num">{String(i + 1).padStart(2, "0")}</span>
                      <div>
                        <h3>{g.t}</h3>
                        <p>{g.d}</p>
                      </div>
                    </li>
                  ))}
                </ol>

                <p className="rx-side-label">MONTHLY ON PATREON</p>
                <ul className="rx-tiers">
                  {MEMBERSHIPS.map((m) => (
                    <li key={m.id} className={`rx-tier rx-tier-${m.id}`}>
                      <span className="rx-tier-name">{m.name.replace("Atomic ", "")}</span>
                      <span className="rx-tier-price">{formatUsd(m.cents).replace(".00", "")}</span>
                      <span className="rx-tier-coins">{m.coins} / MONTH</span>
                    </li>
                  ))}
                </ul>
                <a href="#monthly" className="rx-side-link">
                  Compare memberships
                </a>

                <div className="rx-promise">
                  <p className="rx-side-label">YOUR NOTES STAY YOURS</p>
                  <p>
                    No subscription is required to write, keep, or open your notes. Coins only add sync energy and room
                    for more notes.
                  </p>
                </div>
              </aside>
            </div>
          </div>
        </section>

        <section id="monthly">
          <div className="wrap">
            <p className="eyebrow">MONTHLY ON PATREON</p>
            <h2>
              Choose your <span className="sig">orbit.</span>
            </h2>
            <p className="lp-lead tier-intro">
              Three memberships, each with Atomic Coins for every month that&apos;s paid. Cancel on Patreon at any time.
            </p>
            <div className="tier-grid">
              {MEMBERSHIPS.map((m) => (
                <article key={m.id} className={`tier-card tier-${m.id}`}>
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img src={m.cover} alt="" width={920} height={400} loading="lazy" className="tier-cover" />
                  <div className="tier-body">
                    <p className="tier-level">
                      TIER {m.level} · {m.tagline.toUpperCase()}
                      {m.badge ? <span className="tier-badge">{m.badge.toUpperCase()}</span> : null}
                    </p>
                    <h3>{m.name}</h3>
                    <p className="tier-price">
                      {formatUsd(m.cents).replace(".00", "")}
                      <span>/ MONTH</span>
                    </p>
                    <p className="tier-coins">{m.coins} ATOMIC COINS EACH PAID MONTH</p>
                    <p className="tier-impact">{m.impact}</p>
                    <ul className="support-list">
                      {m.benefits.map((b) => (
                        <li key={b}>{b}</li>
                      ))}
                    </ul>
                    <a href={PATREON_URL} className="btn-signal" target="_blank" rel="noreferrer">
                      {m.cta}
                    </a>
                  </div>
                </article>
              ))}
            </div>

            <div className="tier-table-wrap">
              <table className="tier-table">
                <caption className="sr-only">Patreon memberships compared</caption>
                <thead>
                  <tr>
                    <th scope="col">Membership</th>
                    <th scope="col">Price</th>
                    <th scope="col">Coins each paid month</th>
                    <th scope="col">Also included</th>
                  </tr>
                </thead>
                <tbody>
                  {MEMBERSHIPS.map((m) => (
                    <tr key={m.id}>
                      <th scope="row">{m.name}</th>
                      <td>{formatUsd(m.cents)} a month</td>
                      <td>{m.coins}</td>
                      <td>{m.benefits.slice(1).join(", ")}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </section>

        <section id="how">
          <div className="wrap">
            <p className="eyebrow">FOUR STEPS</p>
            <h2>
              How the coins <span className="sig">reach you.</span>
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
                  Coins go to the email you write, not to your Patreon or Ko-fi name. A wrong or misspelled email means
                  the coins can&apos;t reach you. If you signed in with more than one Google account, use the one that
                  holds your notes. On Ko-fi, mark the message private so your email isn&apos;t shown on the public page.
                </p>
              </div>
              <div className="feature">
                <p className="num">GOOD TO KNOW</p>
                <ul className="support-list">
                  <li>
                    Patreon or Ko-fi handles the payment. Atomic Notes never sees your card, PayPal, or bank details.
                  </li>
                  <li>Each platform charges its own fees, under its own terms.</li>
                  <li>Coins are added by hand after the payment is checked, so they can take a little time.</li>
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
          </div>
        </section>

        <section id="faq">
          <div className="wrap">
            <p className="eyebrow">FAQ</p>
            <h2>
              Straight <span className="sig">answers.</span>
            </h2>
            <div className="faq">
              {FAQ.map((f, i) => (
                <details key={f.q} open={i === 0}>
                  <summary>
                    <h3>{f.q}</h3>
                    <span aria-hidden="true" className="faq-mark">
                      +
                    </span>
                  </summary>
                  <p>{f.a}</p>
                </details>
              ))}
            </div>
            <div className="hero-actions support-end">
              <a href="#reactor" className="btn-signal">
                Open the reactor
              </a>
              <a href={PATREON_URL} className="btn-ghost" target="_blank" rel="noreferrer">
                Join on Patreon
              </a>
              <a href={KOFI_URL} className="btn-ghost" target="_blank" rel="noreferrer">
                Open Ko-fi
              </a>
            </div>
            <p className="support-sign">EVERY ELECTRON HELPS.</p>
          </div>
        </section>
      </main>
      <SiteFooter />
    </>
  );
}
