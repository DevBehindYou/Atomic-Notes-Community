"use client";

import { useState } from "react";

const THEM = [
  "Read your notes to target ads",
  "Use your content as AI training data",
  "Lock basic features behind a subscription",
  "Track behavior with analytics SDKs",
];
const US = [
  "No ads — nothing reads your notes",
  "No AI training on your content, ever",
  "Local note-taking is free, forever",
  "Zero trackers, zero analytics",
];

export function Compare() {
  const [tab, setTab] = useState<"them" | "us">("them");
  const items = tab === "them" ? THEM : US;
  return (
    <div>
      <div className="toggle">
        <button className={tab === "them" ? "on" : ""} onClick={() => setTab("them")}>
          What most apps take
        </button>
        <button className={tab === "us" ? "on" : ""} onClick={() => setTab("us")}>
          What Atomic takes
        </button>
      </div>
      <ul key={tab} className={"cmp panel " + (tab === "them" ? "bad" : "good")}>
        {items.map((t, i) => (
          <li key={i}>
            <span className="mark">{tab === "them" ? "✕" : "→"}</span>
            <span>{t}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
