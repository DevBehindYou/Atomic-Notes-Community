"use client";

import { OfflineSimulator } from "./OfflineSimulator";
import { LocalFirstScorecard } from "./LocalFirstScorecard";
import { RedFlagChecker } from "./RedFlagChecker";
import { PolicyDecoder } from "./PolicyDecoder";

// Interactive components a post can place with `:::widget <name>` on its own line.
const WIDGETS: Record<string, () => React.ReactElement> = {
  "offline-simulator": OfflineSimulator,
  "local-first-scorecard": LocalFirstScorecard,
  "red-flag-checker": RedFlagChecker,
  "policy-decoder": PolicyDecoder,
};

export const WIDGET_NAMES = Object.keys(WIDGETS);

export function BlogWidget({ name }: { name: string }) {
  const W = WIDGETS[name];
  return W ? <div className="bw-slot"><W /></div> : null;
}
