// Static site content + shared types. Notifications come from the Atomic
// Notes Server (src/lib/atomicServer.ts); the roadmap/features here are
// editorial content for the community site.

export type NotificationRow = {
  id: string;
  type: string;
  subject: string;
  description: string;
  priority: "low" | "normal" | "high" | "critical";
  status: "active" | "resolved" | "expired";
  action: string | null;
  action_url: string | null;
  icon: string | null;
  target_audience: string | null;
  min_app_version: string | null;
  max_app_version: string | null;
  created_at: string;
  expires_at: string | null;
};

export const NOTIFICATION_TYPES = [
  "server_down",
  "server_restored",
  "maintenance",
  "new_update",
  "update_required",
  "bug_report",
  "bug_fixed",
  "new_feature",
  "upcoming_feature",
  "security",
  "account",
  "atomic_energy",
  "general",
] as const;

export const PRIORITIES = ["low", "normal", "high", "critical"] as const;
export const STATUSES = ["active", "resolved", "expired"] as const;

export const CURRENT_PHASE = {
  label: "PHASE 5 · ENERGY + NOTIFICATIONS",
  title: "Atomic Energy, Coins, and the Notification Center are live.",
  body: "Opt-in end-to-end encryption, in-app OTP email, the Atomic Energy economy, and an in-app Notification Center have shipped. Payments (coin purchases) and this community platform are next.",
};

export const ROADMAP: { phase: string; title: string; state: "done" | "now" | "next" }[] = [
  { phase: "01", title: "Local-first notes, checklists, offline", state: "done" },
  { phase: "02", title: "Per-note realtime sync, multi-device", state: "done" },
  { phase: "03", title: "End-to-end encryption (recovery phrase)", state: "done" },
  { phase: "04", title: "Auth + in-app OTP email & password reset", state: "done" },
  { phase: "05", title: "Atomic Energy + Coins + Notifications", state: "done" },
  { phase: "06", title: "Community Base + Controller (this site)", state: "now" },
  { phase: "07", title: "Payments — coin purchases (Lemon Squeezy / Razorpay)", state: "next" },
];

export const FEATURES = [
  {
    k: "LOCAL-FIRST",
    t: "Your device, first",
    d: "Notes save instantly and work fully offline. The cloud is optional and under your control.",
  },
  {
    k: "END-TO-END",
    t: "Encrypted with a phrase",
    d: "Turn on a vault and your notes are sealed with a 6-word recovery phrase only you hold.",
  },
  {
    k: "NO TRACKING",
    t: "No ads, no analytics",
    d: "Zero trackers, ad SDKs, or telemetry. The business never reads your notes.",
  },
  {
    k: "ATOMIC ENERGY",
    t: "Sync, your way",
    d: "A renewable energy allowance powers cloud sync. Local note-taking is always free.",
  },
];
