// Static site content + shared types. Notifications come from the Atomic
// Notes Server (src/lib/atomicServer.ts). The rest is editorial content for the
// website. Keep it true to the App: every number is checked against the App and
// Server code, and the FAQ answers are also published as FAQPage structured data.

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

/** The release the website describes. Update together with the App's pubspec.yaml. */
export const RELEASE = {
  version: "2.03.5",
  build: 8,
  date: "2026-09-28",
  minAndroid: "Android 9 (API 28)",
  certSha256: "cc24ae5ce1dca50fcd5e5c4c252d69e4965c55a975bd0e4739e8938fad9bebeb",
  certSha1: "20:08:8F:BF:45:D7:D1:5A:4C:26:69:D6:47:84:16:E2:7F:32:85:45",
};

/** When the legal pages last changed (ISO dates). Shown on the pages and used as sitemap lastmod. */
export const LEGAL_UPDATED = { privacy: "2026-09-30", terms: "2026-09-29" };

export const REPO_URL = "https://github.com/DevBehindYou/Atomic-Notes-App-V0.2";

/** Where supporters go. Early supporters get Atomic Coins by hand (see /support-atomic-notes). */
export const PATREON_URL = "https://www.patreon.com/cw/DevBehindYou";
/** Patreon's membership page, where a supporter picks a tier. */
export const PATREON_JOIN_URL = "https://www.patreon.com/16654968/join";
export const KOFI_URL = "https://ko-fi.com/devbehindyou";

/** The answer-first definition, used in the page and in structured data. */
export const DEFINITION =
  "The Atomic Notes app is a free, source-available notes app for Android that keeps your notes on your phone first and syncs them to a private folder in your own Google Drive. It's a notes app without ads, AI, or analytics. Turn on the optional vault and it becomes an encrypted note taking app: AES-256-GCM seals every note on the device, so the sync server and Google only ever store ciphertext.";

export const FACTS: { k: string; v: string }[] = [
  { k: "Platform", v: "Android 9 or newer" },
  { k: "Latest version", v: `${RELEASE.version}, released Sep 28, 2026` },
  { k: "Where notes live", v: "Your phone, then your own Google Drive" },
  { k: "Encryption", v: "Optional vault: Argon2id + AES-256-GCM" },
  { k: "Price", v: "Free. 30 notes and daily sync energy" },
  { k: "Tracking", v: "None. No analytics, crash, or ad SDKs" },
  { k: "Source", v: "Public to read and verify. All rights reserved" },
  { k: "Made by", v: "DevBehindYou (Ashutosh Sharma)" },
];

export const COMPARISON: { them: string; us: string }[] = [
  { them: "Banner ads, pop-ups, and features locked behind a paywall", us: "A notes app without ads. Every feature is on the free plan, and coins only add space and energy." },
  { them: "Content used to \"improve services\" and train AI", us: "No AI in the Atomic Notes app. Your notes are never used for training." },
  { them: "Analytics and crash SDKs profiling behavior", us: "Zero telemetry. No analytics, no crash reporters." },
  { them: "Cloud-first, so a weak signal means a spinner", us: "Local-first. Your phone holds the main copy, and the app works offline." },
  { them: "Notes stuck inside the app, exported one at a time", us: "Google Drive notes sync: every note is a file in your own Drive." },
  { them: "A password screen that hides notes but doesn't encrypt them", us: "An optional vault seals notes with AES-256-GCM before they leave the phone." },
];

/** What each party can see, with the vault off and on. */
export const VISIBILITY: { who: string; off: string; on: string }[] = [
  { who: "Your phone", off: "Everything", on: "Everything, after unlock" },
  { who: "Your Google Drive", off: "Note titles and text", on: "Ciphertext only" },
  { who: "Atomic Notes server", off: "Note text in transit to Drive. Stores metadata only", on: "Ciphertext in transit. Stores metadata only" },
  { who: "Atomic Notes team", off: "No access to your Drive files", on: "No access, and no key" },
];

export const ENERGY_RULES: { k: string; v: string }[] = [
  { k: "Free energy", v: "+20 every 24 hours" },
  { k: "Energy cap", v: "120" },
  { k: "Standard sync", v: "5 energy, at most once an hour" },
  { k: "Instant sync", v: "10 energy, any time" },
  { k: "Nothing to upload", v: "Free" },
  { k: "1 Atomic Coin", v: "40 energy" },
];

export const TIERS: { name: string; icon: string; notes: number; cost: string }[] = [
  { name: "Tachyon", icon: "/icons/tachyon.svg", notes: 30, cost: "Free" },
  { name: "Antimatter", icon: "/icons/antimatter.svg", notes: 40, cost: "10 coins" },
  { name: "Monopole", icon: "/icons/monopole.svg", notes: 50, cost: "20 coins" },
  { name: "Strangelet", icon: "/icons/strangelet.svg", notes: 100, cost: "30 coins" },
];

/** Measured on a real phone against production on 2026-09-27 (server time, single samples). */
export const PERFORMANCE: { k: string; v: string }[] = [
  { k: "Push 9 notes to Drive", v: "3.2 s" },
  { k: "Push 22 notes to Drive", v: "6.8 s" },
  { k: "Cold start after a force stop", v: "0.5 to 0.9 s" },
];

export const ROADMAP: { phase: string; title: string; state: "done" | "now" | "next" }[] = [
  { phase: "01", title: "Local-first notes and checklists, offline by default", state: "done" },
  { phase: "02", title: "Sync to your own Google Drive, replay-safe", state: "done" },
  { phase: "03", title: "End-to-end vault with a 6-word recovery phrase", state: "done" },
  { phase: "04", title: "Atomic Energy, Atomic Coins, and capacity tiers", state: "done" },
  { phase: "05", title: "Notification center, biometric lock, and two-step codes", state: "done" },
  { phase: "06", title: "Open Google sign-in to everyone", state: "now" },
  { phase: "07", title: "Coin packs you can buy", state: "next" },
  { phase: "08", title: "Background sync while the app is closed", state: "next" },
  { phase: "09", title: "iOS build", state: "next" },
];

export const FAQ: { q: string; a: string }[] = [
  {
    q: "Is the Atomic Notes app free?",
    a: "Yes. Writing and keeping notes on your phone is free, and every account holds 30 notes at no cost. Cloud sync uses Atomic Energy, which refills by 20 every 24 hours. That covers four standard syncs a day. Atomic Coins add more energy or note capacity. There are no subscriptions.",
  },
  {
    q: "Is this the same as the atomic notes method or other apps called Atomic Notes?",
    a: "No. The Atomic Notes app on this site is an Android notes app made by DevBehindYou. It isn't related to the atomic notes method, where you keep one idea per note, or to other apps with a similar name. You can still use it for one-idea notes if you like that style.",
  },
  {
    q: "Is there a notes app for Android that syncs with Google Drive?",
    a: "Yes. The Atomic Notes app syncs each note as its own .atomic file in a My-Atomic-Notes folder in your Google Drive. That Google Drive notes sync uses the narrow drive.file permission, so the app sees only the files it created. The Atomic Notes server stores only metadata such as note IDs, timestamps, and flags, never your note titles or text.",
  },
  {
    q: "Does the Atomic Notes app work offline?",
    a: "Yes. The app opens and saves notes the same way with or without a connection, because the phone holds the main copy. Changes made offline sync on their own when the network comes back. You need a connection only for the first Google sign-in and for syncing to Drive.",
  },
  {
    q: "Can I password protect my notes on Android?",
    a: "Yes. Turn on the biometric app lock, and the app asks for your fingerprint or face before it opens, with your phone's own PIN, pattern, or password as the backup. For real encryption, turn on the vault too. A lock hides the screen, and the vault scrambles the stored notes.",
  },
  {
    q: "Is Atomic Notes an encrypted note taking app?",
    a: "It is once you turn on the vault, which is optional and off by default. The vault derives a key from a six-word recovery phrase with Argon2id and seals each note with AES-256-GCM on your phone, so your Drive and the server hold only ciphertext. With the vault off, notes are plain text in your own Drive, and they pass through the server on the way there.",
  },
  {
    q: "Does Atomic Notes have ads, AI, or analytics?",
    a: "No. It's a notes app without ads, AI features, or analytics. Your notes are never sent to a model or used as training data, and the app ships no crash-reporting or advertising SDKs. You can check this in the public source code, where pubspec.yaml lists every library the app uses.",
  },
  {
    q: "What happens if I lose my six-word recovery phrase?",
    a: "Any phone where the vault is already open keeps showing your notes. A new phone is different: it needs the six words to rebuild the key, and that key only ever exists on your devices. So nobody, including the developer, can open your vault notes without them. Keep the phrase on paper, somewhere safe and away from the phone.",
  },
  {
    q: "Is the Atomic Notes app on Google Play or iOS?",
    a: "Not yet. Atomic Notes for Android ships as signed APKs on GitHub Releases, and you can check each file's certificate and SHA-256 before you install it. An iOS build is on the roadmap.",
  },
];
