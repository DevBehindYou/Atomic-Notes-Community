"use client";

import { useEffect, useState } from "react";
import { usePathname } from "next/navigation";
import { DISCORD_URL } from "@/lib/site";

const DELAY_MS = 5000;

// Bottom-left invite to the community Discord. It lives in the root layout, so it mounts once per
// full page load: it appears 5 s after every load or refresh, and closing it lasts until the next one.
// Nothing is stored. Never shown on the secret Controller.
export function CommunityPopup() {
  const pathname = usePathname() ?? "";
  const onController = pathname === "/controller" || pathname.startsWith("/controller/");
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    if (onController) return;
    const timer = window.setTimeout(() => setVisible(true), DELAY_MS);
    return () => window.clearTimeout(timer);
  }, [onController]);

  useEffect(() => {
    if (!visible) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") setVisible(false);
    };
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, [visible]);

  if (onController) return null;

  return (
    <aside
      className={"community-pop" + (visible ? " is-visible" : "")}
      aria-label="Atomic Notes community"
      aria-hidden={!visible}
      inert={!visible}
    >
      <button type="button" className="community-pop-close" aria-label="Close" onClick={() => setVisible(false)}>
        &times;
      </button>
      <div className="community-pop-head">
        <DiscordMark />
        <div className="community-pop-brand">
          <b>Atomic Notes Community</b>
          <span className="community-pop-live">Server is live</span>
        </div>
      </div>
      <div className="community-pop-card">
        <p className="community-pop-title">
          We just opened our <span className="sig">Discord.</span>
        </p>
        <p className="community-pop-copy">
          <strong>The Atomic Notes Community Server is live.</strong> Join for feature discussions, app updates,
          and release news, straight from the developer.
        </p>
        <a className="community-pop-cta" href={DISCORD_URL} target="_blank" rel="noopener noreferrer">
          <span className="community-pop-cta-text">
            <span className="community-pop-label">Discord · free to join</span>
            <span className="community-pop-go">Join the server</span>
          </span>
          <span className="community-pop-arrow" aria-hidden="true">
            &rarr;
          </span>
        </a>
      </div>
    </aside>
  );
}

function DiscordMark() {
  return (
    <svg viewBox="0 0 64 64" aria-hidden="true" className="community-pop-mark">
      <path
        d="M17 12 L24 10 L27.5 15.5 Q32 14.6 36.5 15.5 L40 10 L47 12 Q55.5 23 57 44 Q51 51 44 53 L41 47.5 Q32 50.5 23 47.5 L20 53 Q13 51 7 44 Q8.5 23 17 12 Z"
        fill="#9c94e4"
        stroke="#0b0c0e"
        strokeWidth="3.6"
        strokeLinejoin="round"
      />
      <path d="M20.5 21.5 Q32 17.5 43.5 21.5" fill="none" stroke="#0b0c0e" strokeWidth="3.4" strokeLinecap="round" />
      <path d="M20.5 40.5 Q32 45.5 43.5 40.5" fill="none" stroke="#0b0c0e" strokeWidth="3.4" strokeLinecap="round" />
      <ellipse cx="24.5" cy="31" rx="4.6" ry="5.2" fill="#eef0ea" stroke="#0b0c0e" strokeWidth="3" />
      <ellipse cx="39.5" cy="31" rx="4.6" ry="5.2" fill="#eef0ea" stroke="#0b0c0e" strokeWidth="3" />
    </svg>
  );
}
