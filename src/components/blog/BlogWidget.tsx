"use client";

import { OfflineSimulator } from "./OfflineSimulator";
import { LocalFirstScorecard } from "./LocalFirstScorecard";
import { RedFlagChecker } from "./RedFlagChecker";
import { PolicyDecoder } from "./PolicyDecoder";
import { EncryptionPlayground } from "./EncryptionPlayground";
import { WhoCanRead } from "./WhoCanRead";
import { AirplaneTest } from "./AirplaneTest";
import { WaitCalculator } from "./WaitCalculator";
import { MetadataInference } from "./MetadataInference";
import { SyncStepper } from "./SyncStepper";
import { AppFinder } from "./AppFinder";
import { LocalFirstMatcher } from "./LocalFirstMatcher";
import { ShutdownTest } from "./ShutdownTest";
import { RecoveryCheck } from "./RecoveryCheck";
import { GuessTime } from "./GuessTime";
import { OfflineFinder } from "./OfflineFinder";
import { PermissionReader } from "./PermissionReader";
import { AiScanner } from "./AiScanner";
import { AiPath } from "./AiPath";
import { HabitAudit } from "./HabitAudit";
import { ApkChecker } from "./ApkChecker";
import { BlastRadius } from "./BlastRadius";
import { SecretScanner } from "./SecretScanner";
import { ThreatMatrix } from "./ThreatMatrix";
import { KeyCustody } from "./KeyCustody";
import { SwitchCheck } from "./SwitchCheck";
import { CountCheck } from "./CountCheck";

// Interactive components a post can place with `:::widget <name>` on its own line.
const WIDGETS: Record<string, () => React.ReactElement> = {
  "offline-simulator": OfflineSimulator,
  "local-first-scorecard": LocalFirstScorecard,
  "red-flag-checker": RedFlagChecker,
  "policy-decoder": PolicyDecoder,
  "encryption-playground": EncryptionPlayground,
  "who-can-read": WhoCanRead,
  "airplane-test": AirplaneTest,
  "wait-calculator": WaitCalculator,
  "metadata-inference": MetadataInference,
  "sync-stepper": SyncStepper,
  "app-finder": AppFinder,
  "local-first-matcher": LocalFirstMatcher,
  "shutdown-test": ShutdownTest,
  "recovery-check": RecoveryCheck,
  "guess-time": GuessTime,
  "offline-finder": OfflineFinder,
  "permission-reader": PermissionReader,
  "ai-scanner": AiScanner,
  "ai-path": AiPath,
  "habit-audit": HabitAudit,
  "apk-checker": ApkChecker,
  "blast-radius": BlastRadius,
  "secret-scanner": SecretScanner,
  "threat-matrix": ThreatMatrix,
  "key-custody": KeyCustody,
  "switch-check": SwitchCheck,
  "count-check": CountCheck,
};

export const WIDGET_NAMES = Object.keys(WIDGETS);

export function BlogWidget({ name }: { name: string }) {
  const W = WIDGETS[name];
  return W ? <div className="bw-slot"><W /></div> : null;
}
