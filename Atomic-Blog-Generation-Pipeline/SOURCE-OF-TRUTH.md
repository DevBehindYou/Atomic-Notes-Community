# Source of Truth — writing accurately about Atomic Notes

When an article states anything about Atomic Notes itself, trust in this order. If two
sources disagree, the higher one wins and the lower is stale.

```
1. Current source code: Atomic-Notes-App-V0.2 (lib/), and the private Server (ask the owner)
2. The App README and TRANSPARENCY.md (Atomic-Notes-App-V0.2), and the live website
3. docs/ai-handover/ in the workspace (CURRENT_STATE, ARCHITECTURE, DECISIONS)
4. Older documentation (may describe superseded architecture; do not resurrect)
```

If older content conflicts with the current implementation, the current implementation
wins. Never reintroduce a superseded system just because an old doc mentions it: the
Supabase backend, email + password auth with OTP, the 20-note allowance, last-write-wins
sync, the single-blob notebook storage, and the random-wrapped-key vault are all gone.

## Shipped vs planned (verify against code before every article)

Every claim must be labeled honestly. As of version 2.03.5 (28 September 2026):

**SHIPPED**
- Android app (Flutter), Android 9+, signed split-ABI APKs on GitHub Releases.
- Local-first notes + checklists saved to on-device Hive storage as you type; fully offline.
- Sync to the user's own Google Drive: one `.atomic` file per note in a `My-Atomic-Notes`
  folder, Google `drive.file` scope only (the app sees only files it created).
- Server (Hono on Vercel, Mumbai region, MongoDB Atlas) stores metadata only: ids, kind,
  pinned/deleted flags, timestamps, Drive file ids. Never note titles or text.
- Sync engine: request-id replay (no double charge, no duplicates), per-user lock, one
  transaction per push, 8 Drive writes in flight with retry, pulls of 10 files per page,
  network retries after 5/15/45 s, auto sync a few seconds after typing stops, on resume
  and on reconnect.
- Conflicts keep both versions: each push carries a base version; a stale edit is refused
  (`note_conflict`) and the phone saves it as "(conflict copy)". Stale deletes are refused.
- Opt-in end-to-end vault: 6-word phrase (1,024-word list, 60 bits), Argon2id (64 MiB,
  3 passes, parallelism 1), salt = SHA-256("atomic-notes-vault-v1|<user id>"), AES-256-GCM
  (12-byte nonce, 16-byte tag), server stores only a verifier. Off by default (T2T: plain
  text in the user's Drive, passing through the server in transit).
- Sign-in: Google only.
- Atomic Energy + Atomic Coins: +20 energy per day at a fixed daily time, missed days paid,
  cap 120; standard sync 5 (at most once an hour), instant 10, nothing-to-upload free,
  refund when no note gets through; 1 coin = 40 energy; 5-coin welcome gift.
- Capacity tiers: Tachyon 30 notes (free), Antimatter 40 (10 coins), Monopole 50
  (20 more), Strangelet 100 (30 more).
- Notification center with web-link buttons; three welcome messages for new accounts.
- Biometric lock, TOTP two-step verification, FLAG_SECURE (no screenshots), Android
  secure storage. No ads, no analytics, no trackers, no crash SDK, no AI.

**PLANNED / NOT YET SHIPPED (never say these are live)**
- Coins sold in the app. Today supporters get coins early by hand (see the website's
  support page). Do not name a payment platform in app copy or notifications.
- Email + password sign-in, a web version, iOS, background sync while the app is closed,
  a full export feature, store listings.

## Verified constants (do not drift)

- Version 2.03.5 (build 8), released 2026-09-28. Certificate SHA-256
  cc24ae5ce1dca50fcd5e5c4c252d69e4965c55a975bd0e4739e8938fad9bebeb.
- Free note allowance: 30 per account (server-enforced).
- Energy cap 120; daily grant +20 at a fixed daily time; missed days paid up to the cap.
- 1 Atomic Coin = 40 energy. Sync cost: standard 5, instant 10, nothing to upload 0.
- Measured (27 Sep 2026, production, server time): 9-note push 3.2 s, 22-note push 6.8 s,
  Google Drive about 1.5 s per file write, cold start 0.5 to 0.9 s.
- Stack: Flutter (Dart) app with bloc + Hive CE; Server Hono (TypeScript) on Vercel +
  MongoDB Atlas + Google Drive API; website Next.js 15.
- Design: ink #15171B, paper #F4F5F1, signal #3A2FF0; Bebas Neue / Hanken Grotesk / JetBrains Mono.

## Security-claim rules

- Do not overstate encryption. It is opt-in. T2T notes are plain text in the user's Drive
  and pass through the server in transit until the vault is on. Say so plainly.
- A lost recovery phrase means unrecoverable vault notes, by design. Never imply recovery.
- Do not invent audits, certifications, penetration tests, or CVE numbers.

## Licensing (since 28 September 2026)

- The App (`Atomic-Notes-App-V0.2`) and this website are **source-available**: the code is public to read and verify, under the proprietary Atomic Notes Source-Available License. All rights reserved.
- Never call Atomic Notes "open source" or "MIT licensed". Versions before 28 September 2026 were MIT, and only those old copies keep that grant.
- The Server and the legacy App (v1) are proprietary and private. Do not link to them.
