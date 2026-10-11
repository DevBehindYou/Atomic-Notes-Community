"use client";

import { useEffect, useRef, useState } from "react";
import { KOFI_URL, PATREON_URL } from "@/lib/content";
import {
  DEFAULT_CENTS,
  MAX_CENTS,
  MIN_CENTS,
  PRESET_CENTS,
  REWARD_STEPS,
  STEP_CENTS,
  formatUsd,
  quote,
  supportMessage,
} from "@/lib/supportPricing";

const CX = 200;
const CY = 200;
const SEG_R = 182;
const SEGMENTS = REWARD_STEPS.length;

/** One arc of the outer dial, for dollar step [i]. */
function segmentPath(i: number): string {
  const span = 360 / SEGMENTS;
  const gap = 5;
  const a0 = ((i * span + gap / 2 - 90) * Math.PI) / 180;
  const a1 = (((i + 1) * span - gap / 2 - 90) * Math.PI) / 180;
  const x0 = CX + SEG_R * Math.cos(a0);
  const y0 = CY + SEG_R * Math.sin(a0);
  const x1 = CX + SEG_R * Math.cos(a1);
  const y1 = CY + SEG_R * Math.sin(a1);
  return `M ${x0.toFixed(2)} ${y0.toFixed(2)} A ${SEG_R} ${SEG_R} 0 0 1 ${x1.toFixed(2)} ${y1.toFixed(2)}`;
}

function usePrefersReducedMotion(): boolean {
  const [reduced, setReduced] = useState(false);
  useEffect(() => {
    const mq = window.matchMedia("(prefers-reduced-motion: reduce)");
    const update = () => setReduced(mq.matches);
    update();
    mq.addEventListener("change", update);
    return () => mq.removeEventListener("change", update);
  }, []);
  return reduced;
}

/** Counts from the shown value to [target] in about 300 ms, or jumps when motion is reduced. */
function useRollingNumber(target: number, reduced: boolean): number {
  const [shown, setShown] = useState(target);
  const from = useRef(target);
  useEffect(() => {
    if (reduced) {
      from.current = target;
      setShown(target);
      return;
    }
    const start = performance.now();
    const begin = from.current;
    let raf = 0;
    const tick = (now: number) => {
      const p = Math.min(1, (now - start) / 300);
      const eased = 1 - Math.pow(1 - p, 3);
      const v = Math.round(begin + (target - begin) * eased);
      from.current = v;
      setShown(v);
      if (p < 1) raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
    // requestAnimationFrame pauses in background tabs: make sure the final number still lands.
    const settle = window.setTimeout(() => {
      from.current = target;
      setShown(target);
    }, 360);
    return () => {
      cancelAnimationFrame(raf);
      window.clearTimeout(settle);
    };
  }, [target, reduced]);
  return shown;
}

export function SupportReactor() {
  const [cents, setCents] = useState(DEFAULT_CENTS);
  const [supportOnly, setSupportOnly] = useState(false);
  const [pulse, setPulse] = useState(0);
  const [copied, setCopied] = useState(false);
  const reduced = usePrefersReducedMotion();

  const q = quote(cents);
  const steps = cents / STEP_CENTS;
  const full = cents === MAX_CENTS;
  const monthly = q.channel === "patreon" && !supportOnly;
  const coinsShown = useRollingNumber(q.coins, reduced);
  const usd = formatUsd(cents);
  const where = monthly ? "Patreon" : "Ko-fi";

  function choose(next: number) {
    if (next === cents) return;
    setCents(next);
    setPulse((p) => p + 1);
    setCopied(false);
  }

  async function copyMessage() {
    try {
      await navigator.clipboard.writeText(supportMessage(q));
      setCopied(true);
      window.setTimeout(() => setCopied(false), 2400);
    } catch {
      setCopied(false);
    }
  }

  const sparkAngle = ((steps - 0.5) * 360) / SEGMENTS;

  return (
    <div className={`reactor${full ? " is-full" : ""}${monthly ? " is-monthly" : ""}`}>
      <div className="reactor-head">
        <p className="reactor-label">ATOMIC COIN REACTOR</p>
        <p className="reactor-tag">{full ? "FULL POWER" : `STEP ${String(steps).padStart(2, "0")} / 10`}</p>
      </div>

      <div className="reactor-dial">
        <svg viewBox="0 0 400 400" role="img" aria-label={`Reactor gauge at ${steps} of 10 steps`}>
          <defs>
            <radialGradient id="rx-core" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stopColor="#ffffff" />
              <stop offset="45%" stopColor="#b3abff" stopOpacity="0.9" />
              <stop offset="100%" stopColor="#3a2ff0" stopOpacity="0" />
            </radialGradient>
            <radialGradient id="rx-core-full" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stopColor="#ffffff" />
              <stop offset="40%" stopColor="#ffb040" stopOpacity="0.95" />
              <stop offset="100%" stopColor="#ff8a00" stopOpacity="0" />
            </radialGradient>
          </defs>

          {REWARD_STEPS.map((s, i) => (
            <path
              key={s.cents}
              d={segmentPath(i)}
              className={`rx-seg${i < steps ? " on" : ""}${s.membership ? " member" : ""}`}
            />
          ))}

          <circle cx={CX} cy={CY} r="158" className="rx-ring" />

          <circle
            key={`glow-${pulse}`}
            cx={CX}
            cy={CY}
            r="118"
            fill={full ? "url(#rx-core-full)" : "url(#rx-core)"}
            className="rx-core"
          />

          <g className="rx-atom">
            {[0, 60, 120].map((deg) => (
              <g key={deg} transform={`rotate(${deg} ${CX} ${CY})`}>
                <ellipse cx={CX} cy={CY} rx="124" ry="44" className="rx-orbit" />
                <circle cx={CX + 124} cy={CY} r="6.5" className="rx-electron" />
              </g>
            ))}
          </g>

          <circle cx={CX} cy={CY} r="64" className="rx-disc" />
        </svg>

        <span
          key={`spark-${pulse}`}
          className="rx-spark"
          style={{ "--a": `${sparkAngle}deg` } as React.CSSProperties}
          aria-hidden="true"
        />

        <div className="reactor-count" aria-hidden="true">
          <span className="reactor-num">{supportOnly ? `$${cents / 100}` : coinsShown}</span>
          <span className="reactor-unit">{supportOnly ? "SUPPORT ONLY" : monthly ? "COINS A MONTH" : "ATOMIC COINS"}</span>
        </div>
      </div>

      <p className="sr-only" aria-live="polite">
        {supportOnly
          ? `${usd} one-time support on Ko-fi, no coins`
          : monthly
            ? `${usd} a month on Patreon, ${q.membership?.name}: ${q.coins} Atomic Coins each paid month`
            : `${usd} one-time on Ko-fi: ${q.coins} Atomic Coins`}
      </p>

      <div className="reactor-slider">
        <label htmlFor="reactor-amount" className="sr-only">
          Support amount in US dollars
        </label>
        <input
          id="reactor-amount"
          type="range"
          min={MIN_CENTS / 100}
          max={MAX_CENTS / 100}
          step={1}
          value={cents / 100}
          onChange={(e) => choose(Number(e.target.value) * 100)}
          aria-valuetext={`${usd}, ${q.coins} Atomic Coins`}
          style={{ "--fill": `${((steps - 1) / 9) * 100}%` } as React.CSSProperties}
        />
        <div className="reactor-scale" aria-hidden="true">
          <span>$1 MIN</span>
          <span>$10 MAX</span>
        </div>
      </div>

      <div className="reactor-presets" role="group" aria-label="Monthly memberships">
        {PRESET_CENTS.map((p) => {
          const m = quote(p).membership;
          return (
            <button key={p} type="button" aria-pressed={cents === p} onClick={() => choose(p)}>
              <span className="rp-price">${p / 100}</span>
              <span className="rp-name">{m ? m.name.replace("Atomic ", "") : ""}</span>
            </button>
          );
        })}
      </div>

      <div className="reactor-mode" role="radiogroup" aria-label="Reward">
        <button type="button" role="radio" aria-checked={!supportOnly} onClick={() => setSupportOnly(false)}>
          With Atomic Coins
        </button>
        <button type="button" role="radio" aria-checked={supportOnly} onClick={() => setSupportOnly(true)}>
          Support only
        </button>
      </div>

      <dl className="reactor-data">
        <div>
          <dt>{monthly ? "MONTHLY ON PATREON" : "ONE-TIME ON KO-FI"}</dt>
          <dd>
            {usd}
            {monthly ? <span className="reactor-per"> / MO</span> : null}
          </dd>
          {monthly ? <p className="reactor-route">{q.membership?.name.toUpperCase()}</p> : null}
        </div>
        <div>
          <dt>{monthly ? "EACH PAID MONTH" : "YOU RECEIVE"}</dt>
          <dd>{supportOnly ? "OUR THANKS" : `${q.coins} COINS`}</dd>
          {!supportOnly && q.bonusCoins > 0 ? (
            <p key={`bonus-${cents}`} className="reactor-bonus">
              +{q.bonusCoins} BONUS COINS
            </p>
          ) : null}
        </div>
      </dl>

      <div className="reactor-cta">
        {supportOnly ? (
          <>
            <a href={KOFI_URL} className="reactor-go" target="_blank" rel="noreferrer">
              Support {usd} on Ko-fi
            </a>
            <p className="reactor-fine">
              No coins and no account email needed. Enter {usd} on Ko-fi, where the payment happens.
            </p>
          </>
        ) : monthly ? (
          <>
            <a href={PATREON_URL} className="reactor-go" target="_blank" rel="noreferrer">
              Join {q.membership?.name} on Patreon
            </a>
            <button type="button" className="reactor-copy" onClick={copyMessage}>
              {copied ? "Copied. Send it to the developer on Patreon" : "Copy the Patreon message"}
            </button>
            <p className="reactor-fine">
              A monthly membership: {usd} a month and {q.coins} Atomic Coins each paid month. Cancel any time on
              Patreon. After joining, send the message with your Atomic Notes account email. Coins are added by hand
              after the developer checks the payment.
            </p>
          </>
        ) : (
          <>
            <a href={KOFI_URL} className="reactor-go" target="_blank" rel="noreferrer">
              Support {usd} on Ko-fi &amp; get {q.coins} coins
            </a>
            <button type="button" className="reactor-copy" onClick={copyMessage}>
              {copied ? "Copied. Paste it in the Ko-fi message" : "Copy the Ko-fi message"}
            </button>
            <p className="reactor-fine">
              A one-time payment. On Ko-fi, enter {usd}, paste the message, add your Atomic Notes account email, and
              mark it private. Coins are added by hand after the developer checks the payment.
            </p>
          </>
        )}
        <p className="reactor-where">PAYMENT ON {where.toUpperCase()} · THIS PAGE ONLY PREVIEWS THE REWARD</p>
      </div>
    </div>
  );
}
