# Atomic Notes Keyword Map, Research, and Cannibalization Guard

Generated from `keyword-registry.json` by `node scripts/cluster-docs.mjs` on 2026-10-07. Edit the registry, then rerun the generator and `node scripts/cluster-check.mjs`.

## How the research was done

• **Demand.** Autocomplete presence, not search volume. On October 7, 2026 every keyword was sent to Google (suggestqueries, en-US), Bing (osjson) and DuckDuckGo (ac), and each engine was marked when it suggested the exact phrase for any probe. Engines only autocomplete queries people actually type, so a mark means real demand. No mark means low or no demand, not proof of zero. 390 queries were probed.
• **Intent.** Live search results were reviewed for the head terms and for every keyword whose intent was in doubt. Findings are in the "Changes" section below.
• **What the marks mean.** `G B D` means Google, Bing and DuckDuckGo all suggested the exact phrase. A dot means that engine didn't. `· · ·` means no autocomplete signal: kept only as a title-match or brand term, never as the reason a page exists.
• **What this is not.** These are not search volumes. No volume, difficulty or traffic numbers were invented. For volumes, export this keyword list into Google Search Console (after launch) or Keyword Planner.

## Rules this map enforces

• Main Blog: 1 primary, 2 secondary, up to 10 LSI. Support Blog: 1 primary, 4 secondary, up to 10 LSI.
• Each primary and secondary keyword has exactly one owner URL in the whole cluster (see the ownership index).
• LSI terms are supporting vocabulary. They may repeat across pages, never as another page's target.
• Matching ignores case, plurals, word order, and small words (a, the, for, your). Question words count, because "is the notes app encrypted" and "encrypted notes app" are different searches.
• Overlaps a person reviewed and accepted are listed below with the reason. Anything else that overlaps fails `cluster-check.mjs`.

## Duplicate content (plagiarism) guard

• `node scripts/cluster-check.mjs --overlap` compares every article in `Atomic Notes Blogs/` and `content/blog/` using 8-word shingles. A pair fails at 10% shared text or any shared run of 25+ words.
• `node scripts/cluster-check.mjs --draft <file.md>` checks one new draft against the corpus and confirms its first keyword matches the registry primary.
• Baseline on 2026-10-07: 28 articles, highest overlap 1.7%, no failures. The repeated listicle disclosure line ("Atomic Notes is my app, so it goes first") should be reworded per article before the listicles go live on the same site.
• External check: before publishing, search two or three distinctive sentences in quotes. A spot check of three existing drafts on 2026-10-07 found no copies online. Support Blogs must be written fresh, not reworded from their Main Blog.
• Never publish the same article on the site and on Medium. A Main Blog republished elsewhere must carry a canonical link to the site.

## Overview

| ID | Role | Title | Primary keyword | Signal |
|---|---|---|---|---|
| P1 | main | 9 Privacy Red Flags to Check Before Trusting Any Notes App in 2026 | `notes app privacy` | G · · |
| P1-S1 | support | 7 Ways Your Notes App Could Expose More About You Than You Realize | `is the notes app secure` | G B D |
| P1-S2 | support | What App Permissions Should You Allow a Notes App? 5 to Question on Android | `what app permissions should i allow` | G B D |
| P1-S3 | support | Is Open Source More Secure? 6 Things Public Source Code Lets You Verify | `is open source more secure` | G B D |
| P2 | main | 7 Best Privacy First Note Taking Apps for Android in 2026 | `private notes app android` | G · · |
| P2-S1 | support | Best Open Source Notes Apps for Privacy in 2026 | `best open source notes app` | G B D |
| P2-S2 | support | 7 Best Google Keep Alternatives for Privacy in 2026 | `google keep alternatives` | G B D |
| P2-S3 | support | 5 F-Droid Notes Apps for Privacy-Conscious Android Users in 2026 | `best f droid notes app` | G · · |
| P3 | main | 10 Privacy Mistakes People Make With Notes Apps in 2026 | `notes app security` | G · · |
| P3-S1 | support | What to Look For in a Private Journal App: 6 Privacy Checks Before You Write | `private journal app` | G B D |
| P3-S2 | support | How to Back Up Notes on Android Without Creating Privacy Risks: 7 Mistakes to Avoid | `backup notes android` | G · · |
| P3-S3 | support | Vendor Lock-In for Notes: 6 Ways Convenience Traps Your Data | `vendor lock in` | G B D |
| P4 | main | 7 Best Note Taking Apps Without AI in 2026 | `note taking app without ai` | G B D |
| P4-S1 | support | 6 Questions You Should Ask Before Giving an AI Notes App Your Private Thoughts | `ai note taking privacy` | G · · |
| P4-S2 | support | Local AI vs Cloud AI for Note Taking: 6 Privacy Differences | `local ai vs cloud ai` | G B D |
| P4-S3 | support | Does Google Use Your Data to Train AI? What It Means for Notes in Google Drive | `does google use my data to train ai` | G · · |
| P5 | main | 8 Pieces of Data a Notes App May Know About You Even Without Reading Your Notes | `notes app metadata` | G · · |
| P5-S1 | support | Zero Telemetry: Why Your Notes App Should Know Less About You | `zero telemetry` | G B D |
| P5-S2 | support | What Does Metadata Reveal? 6 Examples From Apps You Use Every Day | `what does metadata reveal` | G · · |
| P5-S3 | support | Data Minimization Examples: 5 Signs a Notes App Collects Less | `data minimization examples` | G B D |
| L1 | main | What Is a Local First Notes App and Why Does It Matter? | `local first notes app` | G · · |
| L1-S1 | support | Local Storage vs Cloud Storage for Notes: 3 Places Your Notes Can Live | `local storage vs cloud storage` | G B D |
| L1-S2 | support | Local First vs Offline First vs Cloud First: 7 Differences That Matter | `local first vs offline first` | G · · |
| L1-S3 | support | Who Owns Your Data? 5 Questions About Notes, Portability, and Storage | `who owns your data` | G B D |
| L2 | main | 6 Best Local First Note Taking Apps in 2026 That Keep Your Data Yours | `local first note taking apps` | G · · |
| L2-S1 | support | 3 Best Private Notion Alternatives for Local First Notes in 2026 | `local notion alternative` | G B D |
| L2-S2 | support | 5 Notes Apps That Sync Through Your Own Cloud Storage | `notes app that syncs with google drive` | G · · |
| L2-S3 | support | Obsidian vs Logseq vs Anytype vs Atomic Notes: 8 Local First Differences | `obsidian vs logseq vs anytype` | G · · |
| L3 | main | Offline Notes Apps: Why Your Notes Should Work Without Internet | `notes app without internet` | G · · |
| L3-S1 | support | What Happens to Your Notes When the Cloud Goes Down? | `cloud outage` | G B D |
| L3-S2 | support | Offline Sync Explained: 6 Things a Notes App Should Do Without Internet | `offline sync` | G B D |
| L3-S3 | support | Offline Cache vs Local Storage: 5 Differences Users Should Know | `cache vs local storage` | G · · |
| L4 | main | 8 Best Offline Notes Apps for Android in 2026 | `best offline notes app android` | G · · |
| L4-S1 | support | 5 Offline Notes Apps That Do Not Require an Account | `notes app without account` | G · · |
| L4-S2 | support | Does Google Keep Work Offline? 6 Popular Notes Apps Tested Without Internet | `does google keep work offline` | G B D |
| L4-S3 | support | 5 Plain Text and Markdown Notes Apps for Android That Work Fully Offline | `markdown notes app android` | G · · |
| L5 | main | 4 Layers Behind Atomic Notes: How a Local First Notes App Actually Works | `local first architecture` | G B D |
| L5-S1 | support | How Atomic Notes Sync Works in 6 Steps: From Local Hive to Your Google Drive | `local first sync` | G · · |
| L5-S2 | support | Why Atomic Notes Uses Your Google Drive Instead of a Database for Note Content | `google drive as database` | G B D |
| L5-S3 | support | How Atomic Notes Handles Offline Edits, Retries, and Sync Conflicts | `sync conflict` | G · · |
| S1 | main | Encrypted Notes Explained: T2T vs End to End Encryption | `encrypted notes` | G B D |
| S1-S1 | support | HTTPS vs Encryption at Rest vs E2EE: 5 Differences You Should Know | `encryption in transit vs at rest` | G · · |
| S1-S2 | support | Who Holds the Encryption Key? Zero Knowledge Encryption Explained in 6 Questions | `zero knowledge encryption` | G B D |
| S1-S3 | support | Client-Side Encryption Explained: What Happens Before a Note Reaches the Cloud | `client side encryption` | G B D |
| S2 | main | 5 Best End to End Encrypted Notes Apps in 2026 for Private Notes | `best encrypted notes app` | G · · |
| S2-S1 | support | Standard Notes vs Notesnook vs Joplin: How Their Encryption Models Differ | `notesnook vs standard notes` | G B D |
| S2-S2 | support | Is Your Notes App Encrypted? Apple Notes, Google Keep, Samsung Notes, and Obsidian Checked | `is the notes app encrypted` | G · · |
| S2-S3 | support | Notes App With Lock vs Encrypted Notes: 5 Differences Android Users Should Know | `notes app with lock` | G B D |
| S3 | main | 5 Dangerous Consequences of Storing Passwords in an Insecure Notes App | `storing passwords in notes app` | G · · |
| S3-S1 | support | Password Manager vs Notes App vs Paper: Where Should Your Passwords Live? | `is it safe to write passwords down` | G · · |
| S3-S2 | support | Where to Store 2FA Backup Codes, Recovery Phrases, and Other Secrets | `where to store 2fa backup codes` | G · · |
| S3-S3 | support | What Happens After One Password Is Leaked? 6 Steps in a Credential Chain | `what happens if your password is leaked` | G · · |
| S4 | main | 5 Reasons "Your Data Is Encrypted" Does Not Automatically Mean Your Notes Are Private | `how does encryption protect privacy` | G · · |
| S4-S1 | support | Privacy by Design for Notes Apps: 6 Layers Beyond Encryption | `privacy by design` | G B D |
| S4-S2 | support | Metadata Privacy: 7 Things End-to-End Encryption Can and Cannot Hide | `metadata privacy` | G · · |
| S4-S3 | support | Account Recovery vs Zero Knowledge: 5 Security Tradeoffs | `zero knowledge account recovery` | G · · |
| S5 | main | 7 Things to Check Before Moving Your Private Notes to a New App | `switch notes app` | G · · |
| S5-S1 | support | 7 Steps to Export and Verify Your Notes Before Switching Apps | `export notes to markdown` | G · · |
| S5-S2 | support | How to Export Encrypted Notes From Standard Notes, Notesnook, and Joplin Without Losing Access | `standard notes export` | G B D |
| S5-S3 | support | Pocket, Omnivore, Evernote: What Happens to Your Notes When an App Shuts Down | `pocket shutting down` | G B D |
| HUB | hub | Atomic Notes by DevBehindYou: Source-Available, Local First and Private by Design | `atomic notes app` | G · · |
| ECON | side | Why Atomic Notes Uses Energy Instead of a Subscription | `notes app without subscription` | G · · |

## PRIVACY

### P1 · 9 Privacy Red Flags to Check Before Trusting Any Notes App in 2026

• **Role:** Main Blog on https://atomic-notes.devbehindyou.com/blog/notes-app-privacy-red-flags
• **Status:** existing draft, re-keyword
• **Intent:** informational + commercial investigation
• **Primary:** `notes app privacy` (G · ·)
• **Secondary:** `is notes app private` (G · ·), `privacy focused notes app` (G · ·)
• **LSI (10):** third party trackers, privacy policy, data safety section, notes app encryption, account deletion, data export options, cloud sync, privacy labels, source code transparency, business model
• **Changed:** Primary moved from 'private notes app' (its SERP is app-store listings, a transactional intent) to 'notes app privacy' (mixed educational SERP). 'secure notes app' removed: it was also S5's primary.

### P1-S1 · 7 Ways Your Notes App Could Expose More About You Than You Realize

• **Role:** Support Blog on Medium, links to P1
• **Status:** existing draft, re-keyword
• **Intent:** informational
• **Primary:** `is the notes app secure` (G B D)
• **Secondary:** `can my notes app be hacked` (G · ·), `can someone hack into my notes app` (G · ·), `is the notes app safe` (G · ·), `can apple read my notes` (G · ·)
• **LSI (10):** cloud backups, analytics SDK, usage tracking, AI processing, shared links, old devices, sync metadata, account security, personal data exposure, phone backups
• **Changed:** Its old primary 'notes app privacy' now belongs to its Main Blog (P1), so a Medium post can't outrank the site for the head term.

### P1-S2 · What App Permissions Should You Allow a Notes App? 5 to Question on Android

• **Role:** Support Blog on Medium, links to P1
• **Status:** new article
• **Intent:** informational / how-to
• **Primary:** `what app permissions should i allow` (G B D)
• **Secondary:** `android app permissions explained` (G B D), `android permissions list` (G B D), `dangerous permissions android` (G · ·), `notes app permissions` (· · ·)
• **LSI (10):** runtime permissions, INTERNET permission, storage access, contacts permission, microphone access, location permission, Exodus Privacy, AndroidManifest, permission manager, Google Play data safety
• **Changed:** 'notes app permissions' shows no autocomplete demand. The question form 'what app permissions should i allow' shows up in all three engines and fits the same article.

### P1-S3 · Is Open Source More Secure? 6 Things Public Source Code Lets You Verify

• **Role:** Support Blog on Substack, links to P1
• **Status:** existing draft, rewrite
• **Intent:** informational / opinion
• **Primary:** `is open source more secure` (G B D)
• **Secondary:** `source available vs open source` (G B D), `why open source is more secure` (G · ·), `open source privacy software` (G · ·), `source available software` (G B D)
• **LSI (10):** software transparency, code review, reproducible builds, security through obscurity, Linus's law, license terms, independent audit, supply chain security, verifiable claims, public repository

### P2 · 7 Best Privacy First Note Taking Apps for Android in 2026

• **Role:** Main Blog on https://atomic-notes.devbehindyou.com/blog/best-privacy-first-notes-apps-android
• **Status:** existing draft, re-keyword
• **Intent:** commercial investigation
• **Primary:** `private notes app android` (G · ·)
• **Secondary:** `best private notes app` (G · ·), `secure notes app android` (G · ·)
• **LSI (10):** privacy first notes app, Notesnook, Standard Notes, Joplin, no ads, F-Droid, data safety section, encrypted sync, offline access, local storage

### P2-S1 · Best Open Source Notes Apps for Privacy in 2026

• **Role:** Support Blog on DEV Community, links to P2
• **Status:** existing draft, rewrite
• **Intent:** commercial investigation
• **Primary:** `best open source notes app` (G B D)
• **Secondary:** `open source notes app` (G B D), `open source note taking app` (G B D), `foss notes app` (G B D), `open source notes app android` (G · ·)
• **LSI (10):** GPL license, AGPL, GitHub releases, self hosted sync, end to end encryption, Markdown files, community audits, F-Droid builds, active maintenance, issue tracker
• **Changed:** The current draft ('Best Private Notes Apps in 2026') targets the same query and apps as P2. Rewriting it as the open source list the plan intended removes the overlap.

### P2-S2 · 7 Best Google Keep Alternatives for Privacy in 2026

• **Role:** Support Blog on Medium, links to P2
• **Status:** existing draft, re-keyword
• **Intent:** commercial investigation
• **Primary:** `google keep alternatives` (G B D)
• **Secondary:** `google keep privacy` (G B D), `is google keep private` (G B D), `google keep alternative open source` (G · ·), `google keep alternative android` (G · ·)
• **LSI (10):** Google Takeout, Google account, Gemini, labels, checklists, reminders, cross device sync, Notally, data safety section, ad profile

### P2-S3 · 5 F-Droid Notes Apps for Privacy-Conscious Android Users in 2026

• **Role:** Support Blog on DEV Community, links to P2
• **Status:** new article
• **Intent:** commercial investigation
• **Primary:** `best f droid notes app` (G · ·)
• **Secondary:** `notes app f droid` (G · ·), `f droid apps` (G B D), `is f droid safe` (G B D), `what is f droid` (G B D)
• **LSI (10):** reproducible builds, anti-features, IzzyOnDroid, Droid-ify, APK signing, Markor, Material Notes, sideloading, open source repository, app updates

### P3 · 10 Privacy Mistakes People Make With Notes Apps in 2026

• **Role:** Main Blog on https://atomic-notes.devbehindyou.com/blog/notes-app-privacy-mistakes
• **Status:** existing draft, re-keyword
• **Intent:** informational / awareness
• **Primary:** `notes app security` (G · ·)
• **Secondary:** `notes app privacy mistakes` (· · ·), `note taking privacy` (· · ·)
• **LSI (10):** recovery phrase, screen lock, app lock, cloud backup, shared notes, APK security, password storage risk, end to end encryption, data ownership, cloud notes privacy
• **Changed:** 'notes app privacy mistakes' has no autocomplete demand, so it stays as an exact title-match secondary. 'notes app security' carries the demand. Slug loses the year so the URL stays evergreen.

### P3-S1 · What to Look For in a Private Journal App: 6 Privacy Checks Before You Write

• **Role:** Support Blog on Medium, links to P3
• **Status:** new article
• **Intent:** commercial investigation
• **Primary:** `private journal app` (G B D)
• **Secondary:** `private journal app for android` (G · ·), `private diary app` (G · ·), `private journal app free` (G · ·), `personal journal app` (G · ·)
• **LSI (10):** journaling privacy, biometric lock, encrypted journal, mood tracking, offline journal, cloud sync, data export, ads, on-device journal, journal backup
• **Changed:** The original topic duplicated S3-S2 (secrets you shouldn't keep in notes). Replaced with a journaling angle that has strong demand in all three engines.

### P3-S2 · How to Back Up Notes on Android Without Creating Privacy Risks: 7 Mistakes to Avoid

• **Role:** Support Blog on WordPress, links to P3
• **Status:** new article
• **Intent:** how-to
• **Primary:** `backup notes android` (G · ·)
• **Secondary:** `how to backup notes` (G B D), `notes backup` (G B D), `backup android notes to google drive` (G · ·), `encrypted vs unencrypted backup` (G · ·)
• **LSI (10):** backup encryption, restore test, Android backup, Google One backup, 3-2-1 backup rule, export file, stale copies, shared folders, recovery material, version history

### P3-S3 · Vendor Lock-In for Notes: 6 Ways Convenience Traps Your Data

• **Role:** Support Blog on Substack, links to P3
• **Status:** new article
• **Intent:** informational / opinion
• **Primary:** `vendor lock in` (G B D)
• **Secondary:** `proprietary file format` (G B D), `data lock in` (G · ·), `vendor lock in examples` (G B D), `non proprietary file formats` (G · ·)
• **LSI (10):** export formats, Markdown, JSON export, switching costs, closed API, account dependency, migration friction, open formats, service shutdown, portability

### P4 · 7 Best Note Taking Apps Without AI in 2026

• **Role:** Main Blog on https://atomic-notes.devbehindyou.com/blog/best-note-taking-apps-without-ai
• **Status:** existing draft, promote
• **Intent:** commercial investigation
• **Primary:** `note taking app without ai` (G B D)
• **Secondary:** `notes app without ai` (G B D), `notion alternatives without ai` (G · ·)
• **LSI (10):** AI free note taking app, no AI notes app, AI training data, AI features toggle, Apple Intelligence, Gemini, Notion AI, plain notes, distraction free writing, offline writing
• **Changed:** Swapped with P4-S1. The old Main primary 'AI notes app privacy' shows no autocomplete demand, and its SERP is about AI meeting note-takers. 'note taking app without ai' and 'notes app without ai' show demand in all three engines, with a weak SERP (an HN post, a Medium post, ClickUp).

### P4-S1 · 6 Questions You Should Ask Before Giving an AI Notes App Your Private Thoughts

• **Role:** Support Blog on Substack, links to P4
• **Status:** existing draft, demote
• **Intent:** informational
• **Primary:** `ai note taking privacy` (G · ·)
• **Secondary:** `notion ai privacy` (G B D), `is notion ai safe` (G B D), `does notion ai train on my data` (G · ·), `ai note taker privacy concerns` (G · ·)
• **LSI (10):** AI data processing, AI data retention, third party AI provider, AI training data opt out, zero data retention, model provider, enterprise AI terms, prompt data, consent, AI privacy settings
• **Changed:** Was the Main Blog. Now a support post, and it absorbs the original P4-S3 (an AI-assistant checklist), which duplicated it.

### P4-S2 · Local AI vs Cloud AI for Note Taking: 6 Privacy Differences

• **Role:** Support Blog on Hashnode, links to P4
• **Status:** new article
• **Intent:** comparison
• **Primary:** `local ai vs cloud ai` (G B D)
• **Secondary:** `on device ai` (G B D), `on device ai privacy` (G · ·), `local ai note taking` (G · ·), `local ai notes app` (G · ·)
• **LSI (10):** on-device model, Gemini Nano, Private Cloud Compute, Ollama, latency, offline inference, data transfer, retention, model access, NPU

### P4-S3 · Does Google Use Your Data to Train AI? What It Means for Notes in Google Drive

• **Role:** Support Blog on Medium, links to P4
• **Status:** new article
• **Intent:** informational
• **Primary:** `does google use my data to train ai` (G · ·)
• **Secondary:** `does google drive use your data to train ai` (G · ·), `does google docs use your data to train ai` (G · ·), `how to opt out of google using my data to train ai` (G · ·), `google ai training data opt out` (G · ·)
• **LSI (10):** Google Workspace, Gemini, Drive privacy, Web & App Activity, personal account, terms of service, consent, data controls, user owned Google Drive, Google One
• **Changed:** Replaced a checklist that duplicated P4-S1. This question has demand in Google autocomplete and directly affects how people judge a Drive-synced notes app.

### P5 · 8 Pieces of Data a Notes App May Know About You Even Without Reading Your Notes

• **Role:** Main Blog on https://atomic-notes.devbehindyou.com/blog/notes-app-data-collection
• **Status:** existing draft, re-keyword
• **Intent:** informational
• **Primary:** `notes app metadata` (G · ·)
• **Secondary:** `notes app data collection` (· · ·), `apps that don't collect data` (G · ·)
• **LSI (10):** IP address, device model, login timestamps, sync activity, usage analytics, account email, device fingerprinting, server logs, retention period, privacy policy
• **Changed:** 'notes app data collection' shows no autocomplete demand, so it stays as the title-match secondary. 'notes app metadata' carries the demand. Dropped 'notes app tracking' (its autocomplete is about change tracking). Slug loses the count so the URL survives edits.

### P5-S1 · Zero Telemetry: Why Your Notes App Should Know Less About You

• **Role:** Support Blog on Medium, links to P5
• **Status:** existing draft, re-keyword
• **Intent:** informational
• **Primary:** `zero telemetry` (G B D)
• **Secondary:** `what is telemetry` (G B D), `telemetry data` (G B D), `app telemetry` (G B D), `telemetry privacy` (G · ·)
• **LSI (10):** analytics SDK, crash reporting, Firebase Analytics, opt-in analytics, anonymous data, usage events, Exodus Privacy, network traffic, tracker SDKs, privacy friendly analytics

### P5-S2 · What Does Metadata Reveal? 6 Examples From Apps You Use Every Day

• **Role:** Support Blog on Medium, links to P5
• **Status:** new article
• **Intent:** informational
• **Primary:** `what does metadata reveal` (G · ·)
• **Secondary:** `metadata examples` (G B D), `what can metadata reveal` (G B D), `is metadata personal data` (G B D), `what is personal metadata` (G · ·)
• **LSI (10):** EFF, call records, timestamps, location data, EXIF, communication patterns, GDPR personal data, data aggregation, inference, social graph
• **Changed:** The original topic duplicated S4-S2 (seven things E2EE can't hide). Re-angled to everyday metadata, which has its own demand.

### P5-S3 · Data Minimization Examples: 5 Signs a Notes App Collects Less

• **Role:** Support Blog on WordPress, links to P5
• **Status:** new article
• **Intent:** informational
• **Primary:** `data minimization examples` (G B D)
• **Secondary:** `what is data minimization` (G B D), `data minimization principle` (G B D), `data minimization techniques` (G B D), `data minimization` (G B D)
• **LSI (10):** GDPR Article 5, purpose limitation, storage limitation, retention schedule, pseudonymization, collection limits, privacy notice, consent, local processing, deletion

## LOCAL FIRST

### L1 · What Is a Local First Notes App and Why Does It Matter?

• **Role:** Main Blog on https://atomic-notes.devbehindyou.com/blog/what-is-a-local-first-notes-app
• **Status:** existing draft, re-keyword
• **Intent:** informational / definition
• **Primary:** `local first notes app` (G · ·)
• **Secondary:** `local-first software` (G B D), `local first meaning` (G B D)
• **LSI (10):** Ink & Switch, Martin Kleppmann, source of truth, on-device storage, sync engine, cloud dependency, CRDT, offline capability, user control, longevity
• **Changed:** 'offline notes app' removed: it is now L4's secondary, and L3 targets the offline problem.

### L1-S1 · Local Storage vs Cloud Storage for Notes: 3 Places Your Notes Can Live

• **Role:** Support Blog on Medium, links to L1
• **Status:** existing draft, re-keyword
• **Intent:** comparison
• **Primary:** `local storage vs cloud storage` (G B D)
• **Secondary:** `where are notes stored on android` (G B D), `where are google keep notes stored` (G B D), `cloud storage vs local storage for personal use` (G · ·), `local storage and cloud storage difference` (G · ·)
• **LSI (10):** device storage, company cloud, own cloud, Google Drive, iCloud, encryption keys, backups, account lock, shutdown risk, sync
• **Changed:** The old primary 'where are notes stored' has a device-specific SERP ('…on mac', '…on android'). The conceptual comparison matches 'local storage vs cloud storage' (demand in all three engines). The Android location question becomes a secondary.

### L1-S2 · Local First vs Offline First vs Cloud First: 7 Differences That Matter

• **Role:** Support Blog on DEV Community, links to L1
• **Status:** new article
• **Intent:** comparison
• **Primary:** `local first vs offline first` (G · ·)
• **Secondary:** `offline first database` (G · ·), `local first vs cloud first` (G · ·), `offline first app` (G B D), `offline first architecture` (G B D)
• **LSI (10):** source of truth, server authority, sync queue, conflict resolution, CRDTs, latency, cache, RxDB, eventual consistency, seven ideals

### L1-S3 · Who Owns Your Data? 5 Questions About Notes, Portability, and Storage

• **Role:** Support Blog on Substack, links to L1
• **Status:** new article
• **Intent:** informational / opinion
• **Primary:** `who owns your data` (G B D)
• **Secondary:** `data portability` (G B D), `user owned data` (G · ·), `own your data` (G B D), `data portability gdpr` (G B D)
• **LSI (10):** GDPR Article 20, export formats, terms of service, account deletion, service shutdown, file ownership, cloud control, interoperability, lock-in, takeout

### L2 · 6 Best Local First Note Taking Apps in 2026 That Keep Your Data Yours

• **Role:** Main Blog on https://atomic-notes.devbehindyou.com/blog/best-local-first-note-taking-apps
• **Status:** existing draft, re-keyword
• **Intent:** commercial investigation
• **Primary:** `local first note taking apps` (G · ·)
• **Secondary:** `local first note taking` (G · ·), `apps like obsidian` (G B D)
• **LSI (10):** Logseq, Anytype, Joplin, Markdown files, plain text, sync options, encryption, offline access, data ownership, vault
• **Changed:** The plan gave L2 the secondaries 'local first notes app' and 'local first note taking', which were L1's primary and secondary. L2 now targets 'local first note taking apps' (the form Google autocompletes) and 'apps like obsidian' (demand in all three engines). Use 'best' in the title, not in the keyword.

### L2-S1 · 3 Best Private Notion Alternatives for Local First Notes in 2026

• **Role:** Support Blog on Medium, links to L2
• **Status:** existing draft, re-keyword
• **Intent:** commercial investigation
• **Primary:** `local notion alternative` (G B D)
• **Secondary:** `private notion alternative` (G · ·), `local first notion alternative` (G · ·), `open source notion alternative` (G B D), `notion alternative local storage` (G · ·)
• **LSI (10):** AppFlowy, AFFiNE, offline workspace, databases, self hosting, encrypted workspace, Markdown export, block editor, data ownership, templates

### L2-S2 · 5 Notes Apps That Sync Through Your Own Cloud Storage

• **Role:** Support Blog on Medium, links to L2
• **Status:** new article
• **Intent:** commercial investigation
• **Primary:** `notes app that syncs with google drive` (G · ·)
• **Secondary:** `google drive notes app` (G · ·), `save notes to google drive` (G · ·), `self hosted notes app` (G B D), `self hosted notes app with sync` (G · ·)
• **LSI (10):** Dropbox sync, WebDAV, Nextcloud, OneDrive, Syncthing, folder sync, user owned cloud storage, sync targets, file based notes, file sync apps

### L2-S3 · Obsidian vs Logseq vs Anytype vs Atomic Notes: 8 Local First Differences

• **Role:** Support Blog on Hashnode, links to L2
• **Status:** new article
• **Intent:** comparison
• **Primary:** `obsidian vs logseq vs anytype` (G · ·)
• **Secondary:** `obsidian vs logseq` (G B D), `obsidian vs anytype` (G B D), `logseq vs anytype` (G B D), `local first comparison` (G · ·)
• **LSI (10):** Markdown vault, outliner, block references, any-sync, E2EE sync, plugins, mobile apps, Google Drive sync, Logseq DB version, file formats

### L3 · Offline Notes Apps: Why Your Notes Should Work Without Internet

• **Role:** Main Blog on https://atomic-notes.devbehindyou.com/blog/why-notes-should-work-offline
• **Status:** existing draft, re-keyword
• **Intent:** informational / problem-solution
• **Primary:** `notes app without internet` (G · ·)
• **Secondary:** `notes app no internet` (G · ·), `does notes app work without internet` (G · ·)
• **LSI (10):** airplane mode, local storage, sync later, cloud dependency, latency, dead zones, travel, outages, Hive storage, source of truth
• **Changed:** 'offline notes app' moved to L4 (its SERP is commercial). L3 takes the problem phrasing. The draft slug 'offline-notes-apps' would also have competed with L4, so the slug changes before first publish.

### L3-S1 · What Happens to Your Notes When the Cloud Goes Down?

• **Role:** Support Blog on Medium, links to L3
• **Status:** existing draft, re-keyword
• **Intent:** informational / news-driven
• **Primary:** `cloud outage` (G B D)
• **Secondary:** `notion outage` (G B D), `aws outage` (G B D), `evernote outage` (G B D), `google keep down` (G B D)
• **LSI (10):** status page, outage timeline, cached notes, sync failure, single point of failure, resilience, local copy, read-only mode, incident report, downtime

### L3-S2 · Offline Sync Explained: 6 Things a Notes App Should Do Without Internet

• **Role:** Support Blog on Medium, links to L3
• **Status:** new article
• **Intent:** informational / how-to
• **Primary:** `offline sync` (G B D)
• **Secondary:** `offline synchronization` (G B D), `offline mode app` (G · ·), `how to know if an app works offline` (G · ·), `offline sync google drive` (G · ·)
• **LSI (10):** sync queue, reconnect, airplane mode test, pending changes, retry, local database, search offline, media files, conflict, background sync
• **Changed:** The original primary 'notes app without internet' now belongs to L3. 'offline sync' shows demand in all three engines.

### L3-S3 · Offline Cache vs Local Storage: 5 Differences Users Should Know

• **Role:** Support Blog on DEV Community, links to L3
• **Status:** new article
• **Intent:** comparison / technical
• **Primary:** `cache vs local storage` (G · ·)
• **Secondary:** `offline cache` (G B D), `cache vs storage` (G B D), `cache storage vs indexeddb` (G · ·), `browser local storage vs cache` (G · ·)
• **LSI (10):** IndexedDB, Service Worker, Cache API, eviction, persistence, authoritative copy, Hive box, SQLite, quota, progressive web app

### L4 · 8 Best Offline Notes Apps for Android in 2026

• **Role:** Main Blog on https://atomic-notes.devbehindyou.com/blog/best-offline-notes-apps-android
• **Status:** existing draft, re-keyword
• **Intent:** commercial investigation
• **Primary:** `best offline notes app android` (G · ·)
• **Secondary:** `offline notes app` (G B D), `offline note taking app` (G B D)
• **LSI (10):** offline notes app android, airplane mode, no account, local storage, Notally, Markor, Joplin, F-Droid, sync later, battery

### L4-S1 · 5 Offline Notes Apps That Do Not Require an Account

• **Role:** Support Blog on Medium, links to L4
• **Status:** new article
• **Intent:** commercial investigation
• **Primary:** `notes app without account` (G · ·)
• **Secondary:** `notes app without login` (G · ·), `notes app no sign in` (G B D), `free notes app without login` (G · ·), `notes app no sign up` (G B D)
• **LSI (10):** no email required, local only, guest mode, optional sign in, Google account, device only storage, data export, backups, privacy, offline first

### L4-S2 · Does Google Keep Work Offline? 6 Popular Notes Apps Tested Without Internet

• **Role:** Support Blog on Medium, links to L4
• **Status:** new article
• **Intent:** informational / comparison
• **Primary:** `does google keep work offline` (G B D)
• **Secondary:** `does notion work offline` (G B D), `does obsidian work offline` (G B D), `does notion work without internet` (G · ·), `does obsidian work without internet` (G · ·)
• **LSI (10):** offline mode, cached notes, sync on reconnect, Notion offline pages, Obsidian vault, Apple Notes offline, OneNote offline, airplane mode, conflict, local first
• **Changed:** The original was a second F-Droid listicle that duplicated P2-S3. Replaced with three 'does X work offline' questions that each show demand in all three engines.

### L4-S3 · 5 Plain Text and Markdown Notes Apps for Android That Work Fully Offline

• **Role:** Support Blog on DEV Community, links to L4
• **Status:** new article
• **Intent:** commercial investigation
• **Primary:** `markdown notes app android` (G · ·)
• **Secondary:** `plain text notes app` (G · ·), `markdown notes app` (G B D), `plain text note taking` (G · ·), `android plain text notes app` (G · ·)
• **LSI (10):** Markor, Obsidian mobile, txt files, folder sync, Syncthing, portability, offline editing, file manager, open formats, front matter
• **Changed:** 'test offline notes app' shows no demand in any engine. The test checklist now lives in L3 and L3-S2.

### L5 · 4 Layers Behind Atomic Notes: How a Local First Notes App Actually Works

• **Role:** Main Blog on https://atomic-notes.devbehindyou.com/blog/atomic-notes-architecture
• **Status:** existing draft, re-keyword
• **Intent:** technical informational + branded
• **Primary:** `local first architecture` (G B D)
• **Secondary:** `local first app architecture` (G · ·), `atomic notes architecture` (· · ·)
• **LSI (10):** Flutter, Hive CE, Hono, MongoDB metadata, Google Drive API, AES-256-GCM, Argon2id, sync engine, request id replay, user owned cloud storage
• **Changed:** 'local first notes architecture' shows no demand. 'local first architecture' shows demand in all three engines.

### L5-S1 · How Atomic Notes Sync Works in 6 Steps: From Local Hive to Your Google Drive

• **Role:** Support Blog on DEV Community, links to L5
• **Status:** new article
• **Intent:** technical informational
• **Primary:** `local first sync` (G · ·)
• **Secondary:** `local first sync engine` (G · ·), `how does sync work` (G B D), `hive database flutter` (G B D), `flutter hive` (G B D)
• **LSI (10):** dirty flag, push queue, retry backoff, idempotency, transaction, Drive write, pull pagination, per-user lock, base version, conflict copy

### L5-S2 · Why Atomic Notes Uses Your Google Drive Instead of a Database for Note Content

• **Role:** Support Blog on Hashnode, links to L5
• **Status:** new article
• **Intent:** technical informational
• **Primary:** `google drive as database` (G B D)
• **Secondary:** `use google drive as database` (G · ·), `drive.file scope` (G B D), `google drive file scope` (G · ·), `google drive database app` (G · ·)
• **LSI (10):** Google Drive API, OAuth scopes, appDataFolder, .atomic files, My-Atomic-Notes folder, metadata server, MongoDB Atlas, rate limits, file revisions, user ownership

### L5-S3 · How Atomic Notes Handles Offline Edits, Retries, and Sync Conflicts

• **Role:** Support Blog on DEV Community, links to L5
• **Status:** new article
• **Intent:** technical informational
• **Primary:** `sync conflict` (G · ·)
• **Secondary:** `sync conflict resolution` (· · ·), `what is a conflicted copy` (G B D), `conflicted copy meaning` (G B D), `crdt local first` (G · ·)
• **LSI (10):** base version, note_conflict, last write wins, three-way merge, CRDT, vector clocks, tombstones, stale deletes, idempotency key, conflict copy UX

## SECURITY

### S1 · Encrypted Notes Explained: T2T vs End to End Encryption

• **Role:** Main Blog on https://atomic-notes.devbehindyou.com/blog/encrypted-notes-explained
• **Status:** existing draft, re-keyword
• **Intent:** informational / definition
• **Primary:** `encrypted notes` (G B D)
• **Secondary:** `end to end encryption explained` (G B D), `what is end to end encryption` (G B D)
• **LSI (10):** transport encryption vs end to end encryption, T2T, TLS, AES-256-GCM, Argon2id, recovery phrase, key derivation, ciphertext, optional vault, threat model
• **Changed:** The plan gave 'end to end encrypted notes' to S1, S2, and S4, and 'encrypted notes app' to S1 and S4. Each now has one owner: S2 owns the commercial 'app' forms.

### S1-S1 · HTTPS vs Encryption at Rest vs E2EE: 5 Differences You Should Know

• **Role:** Support Blog on DEV Community, links to S1
• **Status:** new article
• **Intent:** comparison
• **Primary:** `encryption in transit vs at rest` (G · ·)
• **Secondary:** `https vs end to end encryption` (G · ·), `tls vs end to end encryption` (G B D), `encryption at rest` (G B D), `encryption at rest vs end to end` (G · ·)
• **LSI (10):** TLS certificates, disk encryption, provider keys, server access, data in use, key management, ciphertext, plaintext exposure, threat model, compliance

### S1-S2 · Who Holds the Encryption Key? Zero Knowledge Encryption Explained in 6 Questions

• **Role:** Support Blog on Medium, links to S1
• **Status:** new article
• **Intent:** informational
• **Primary:** `zero knowledge encryption` (G B D)
• **Secondary:** `zero knowledge vs end to end encryption` (G · ·), `zero knowledge encryption meaning` (G · ·), `zero knowledge encryption cloud storage` (G B D), `encryption key management` (G B D)
• **LSI (10):** key custody, master password, key derivation function, recovery key, provider access, server verifier, password manager model, security audit, client side keys, key escrow
• **Changed:** 'encryption key ownership notes' shows no demand. 'zero knowledge encryption' shows demand in all three engines and asks the same question.

### S1-S3 · Client-Side Encryption Explained: What Happens Before a Note Reaches the Cloud

• **Role:** Support Blog on DEV Community, links to S1
• **Status:** new article
• **Intent:** technical informational
• **Primary:** `client side encryption` (G B D)
• **Secondary:** `what is client side encryption` (G B D), `client side vs server side encryption` (G B D), `client side encryption example` (G · ·), `what is server side encryption` (G B D)
• **LSI (10):** Web Crypto API, AES-GCM, nonce, key derivation, envelope encryption, ciphertext upload, Google Workspace CSE, S3 client side encryption, plaintext boundary, salt

### S2 · 5 Best End to End Encrypted Notes Apps in 2026 for Private Notes

• **Role:** Main Blog on https://atomic-notes.devbehindyou.com/blog/best-end-to-end-encrypted-notes-apps
• **Status:** existing draft, re-keyword
• **Intent:** commercial investigation
• **Primary:** `best encrypted notes app` (G · ·)
• **Secondary:** `end to end encrypted notes app` (G B D), `most secure notes app` (G B D)
• **LSI (10):** encrypted notes app, best secure notes app, E2EE notes app, Standard Notes, Notesnook, audited encryption, key ownership, recovery options, metadata, default encryption

### S2-S1 · Standard Notes vs Notesnook vs Joplin: How Their Encryption Models Differ

• **Role:** Support Blog on DEV Community, links to S2
• **Status:** new article
• **Intent:** comparison
• **Primary:** `notesnook vs standard notes` (G B D)
• **Secondary:** `standard notes vs joplin` (G B D), `notesnook vs joplin` (G · ·), `open source encrypted notes app` (G · ·), `is joplin end to end encrypted` (G · ·)
• **LSI (10):** XChaCha20-Poly1305, AES-256, Argon2, security audit, self hosting, sync server, free tier, web clipper, Markdown, export

### S2-S2 · Is Your Notes App Encrypted? Apple Notes, Google Keep, Samsung Notes, and Obsidian Checked

• **Role:** Support Blog on Medium, links to S2
• **Status:** new article
• **Intent:** informational
• **Primary:** `is the notes app encrypted` (G · ·)
• **Secondary:** `is obsidian encrypted` (G B D), `is google keep encrypted` (G B D), `are samsung notes encrypted` (G · ·), `is apple notes end to end encrypted` (G · ·)
• **LSI (10):** Advanced Data Protection, locked notes, Samsung Cloud, Google account encryption, Obsidian Sync, OneNote password sections, device encryption, iCloud, storage encryption, default settings
• **Changed:** The original checklist duplicated S1-S2 (questions before trusting an encrypted app). Replaced with brand questions that each show demand.

### S2-S3 · Notes App With Lock vs Encrypted Notes: 5 Differences Android Users Should Know

• **Role:** Support Blog on Medium, links to S2
• **Status:** new article
• **Intent:** comparison
• **Primary:** `notes app with lock` (G B D)
• **Secondary:** `notes app with lock android` (G · ·), `best note taking app with lock` (G · ·), `can you lock the notes app` (G · ·), `notes app with lock feature` (G · ·)
• **LSI (10):** biometric lock, PIN lock, app lock vs encryption, FLAG_SECURE, screenshot blocking, encrypted vault, device encryption, Android Keystore, shoulder surfing, lock screen
• **Changed:** 'encrypted notes Android' has a commercial SERP that overlaps P2 and S2. 'notes app with lock' shows demand in all three engines and covers a common misunderstanding.

### S3 · 5 Dangerous Consequences of Storing Passwords in an Insecure Notes App

• **Role:** Main Blog on https://atomic-notes.devbehindyou.com/blog/storing-passwords-in-notes-app
• **Status:** existing draft, re-keyword
• **Intent:** informational / problem-solution
• **Primary:** `storing passwords in notes app` (G · ·)
• **Secondary:** `is it safe to store passwords in notes` (G · ·), `should i keep passwords in notes` (G · ·)
• **LSI (10):** password manager, credential theft, account takeover, identity theft, reused passwords, plaintext passwords, is it safe to store passwords in google keep, is samsung notes safe for passwords, recovery email compromise, financial account security
• **Changed:** 'secure password storage' was dropped. Its SERP is OWASP's developer cheat sheet on password hashing, a different intent.

### S3-S1 · Password Manager vs Notes App vs Paper: Where Should Your Passwords Live?

• **Role:** Support Blog on Medium, links to S3
• **Status:** new article
• **Intent:** comparison
• **Primary:** `is it safe to write passwords down` (G · ·)
• **Secondary:** `password manager vs notes app` (· · ·), `safest way to store passwords` (G B D), `is it ok to write down passwords` (G · ·), `is writing down passwords bad` (G · ·)
• **LSI (10):** NIST guidance, physical security, password notebook, passkeys, master password, autofill, breach monitoring, encrypted vault, phishing resistance, family sharing
• **Changed:** 'password manager vs notes app' shows no autocomplete demand, so it stays as a secondary. The paper question shows demand and widens the comparison.

### S3-S2 · Where to Store 2FA Backup Codes, Recovery Phrases, and Other Secrets

• **Role:** Support Blog on Medium, links to S3
• **Status:** new article
• **Intent:** how-to
• **Primary:** `where to store 2fa backup codes` (G · ·)
• **Secondary:** `2fa backup codes` (G B D), `where to store seed phrase` (G B D), `where to store recovery phrase` (G · ·), `where to store backup codes` (G · ·)
• **LSI (10):** API keys, recovery codes, crypto wallet, metal backup, password manager secure notes, offline storage, encrypted vault, identity documents, financial details, plaintext notes

### S3-S3 · What Happens After One Password Is Leaked? 6 Steps in a Credential Chain

• **Role:** Support Blog on WordPress, links to S3
• **Status:** new article
• **Intent:** informational / how-to
• **Primary:** `what happens if your password is leaked` (G · ·)
• **Secondary:** `what to do if password is compromised` (G B D), `credential stuffing` (G B D), `password reuse` (G B D), `what to do if your password is in a data breach` (G · ·)
• **LSI (10):** Have I Been Pwned, account takeover chain, recovery email, SIM swap, two factor authentication, session revoke, breach notification, OWASP, lateral access, password manager

### S4 · 5 Reasons "Your Data Is Encrypted" Does Not Automatically Mean Your Notes Are Private

• **Role:** Main Blog on https://atomic-notes.devbehindyou.com/blog/encrypted-notes-privacy
• **Status:** existing draft, re-keyword
• **Intent:** informational
• **Primary:** `how does encryption protect privacy` (G · ·)
• **Secondary:** `encryption and privacy` (G · ·), `encrypted notes privacy` (· · ·)
• **LSI (10):** transport encryption, provider held keys, metadata, analytics, account recovery, key custody, Advanced Data Protection, encryption marketing, server side keys, threat model
• **Changed:** 'encrypted notes privacy' shows no demand, so it stays as the title-match secondary. The question form carries the demand. 'encrypted notes app' and 'end to end encrypted notes' now belong to S2. Remove the FAQ 'Is an encrypted notes app automatically private?', which also appears in S4-S1.

### S4-S1 · Privacy by Design for Notes Apps: 6 Layers Beyond Encryption

• **Role:** Support Blog on Medium, links to S4
• **Status:** existing draft, rewrite
• **Intent:** informational / framework
• **Primary:** `privacy by design` (G B D)
• **Secondary:** `privacy by design principles` (G B D), `privacy by design meaning` (G B D), `privacy by design and by default` (G B D), `privacy by design framework` (G B D)
• **LSI (10):** Ann Cavoukian, GDPR Article 25, storage location, telemetry, AI training, business model, defaults, collect less, transparency, full lifecycle protection
• **Changed:** As planned, this support post argued the same thesis as its Main Blog and shared an FAQ with it, which is a duplicate-content risk. The privacy-by-design framing has demand in all three engines and a distinct intent.

### S4-S2 · Metadata Privacy: 7 Things End-to-End Encryption Can and Cannot Hide

• **Role:** Support Blog on DEV Community, links to S4
• **Status:** new article
• **Intent:** informational / technical
• **Primary:** `metadata privacy` (G · ·)
• **Secondary:** `metadata leakage` (G B D), `e2ee metadata` (G · ·), `traffic analysis` (G B D), `end to end encryption metadata` (· · ·)
• **LSI (10):** sealed sender, file sizes, timestamps, IP address, sync events, padding, access patterns, server logs, minimal metadata, encrypted filenames

### S4-S3 · Account Recovery vs Zero Knowledge: 5 Security Tradeoffs

• **Role:** Support Blog on Substack, links to S4
• **Status:** new article
• **Intent:** informational / opinion
• **Primary:** `zero knowledge account recovery` (G · ·)
• **Secondary:** `lost recovery key` (G B D), `reset end to end encryption` (G B D), `recover end to end encryption` (G · ·), `zero knowledge recovery` (· · ·)
• **LSI (10):** recovery phrase, Advanced Data Protection, recovery contact, key escrow, support reset, data loss, 6-word phrase, trusted device, account takeover, social recovery

### S5 · 7 Things to Check Before Moving Your Private Notes to a New App

• **Role:** Main Blog on https://atomic-notes.devbehindyou.com/blog/switch-notes-app
• **Status:** existing draft, re-keyword
• **Intent:** migration / decision-stage
• **Primary:** `switch notes app` (G · ·)
• **Secondary:** `migrate notes to a new app` (· · ·), `move notes to another app` (· · ·)
• **LSI (10):** notes migration, data export, export format, attachments, note counts, rollback copy, account recovery, offline notes, cloud storage provider, secure data migration
• **Changed:** The old primary 'secure notes app' has an app-store SERP, the wrong intent for a migration guide, and it was also P1's secondary. Autocomplete for migration phrases is weak, so expect low but well-matched traffic.

### S5-S1 · 7 Steps to Export and Verify Your Notes Before Switching Apps

• **Role:** Support Blog on Medium, links to S5
• **Status:** new article
• **Intent:** how-to
• **Primary:** `export notes to markdown` (G · ·)
• **Secondary:** `export google keep notes` (G B D), `export apple notes to markdown` (G B D), `convert notes to markdown` (G · ·), `export google keep notes to markdown` (G · ·)
• **LSI (10):** Google Takeout, ENEX, JSON export, attachments, front matter, file names, note counts, internal links, Obsidian importer, checksum

### S5-S2 · How to Export Encrypted Notes From Standard Notes, Notesnook, and Joplin Without Losing Access

• **Role:** Support Blog on Medium, links to S5
• **Status:** new article
• **Intent:** how-to
• **Primary:** `standard notes export` (G B D)
• **Secondary:** `joplin export` (G B D), `notesnook export` (G · ·), `joplin export to markdown` (G · ·), `standard notes export markdown` (G · ·)
• **LSI (10):** decrypted export, encrypted backup, recovery key, attachments, JEX format, re-encryption, import, verification, rollback copy, plaintext exposure
• **Changed:** 'migrate encrypted notes' shows no demand in any engine. The app-specific export questions show demand and cover the same task.

### S5-S3 · Pocket, Omnivore, Evernote: What Happens to Your Notes When an App Shuts Down

• **Role:** Support Blog on Substack, links to S5
• **Status:** new article
• **Intent:** informational / news-driven
• **Primary:** `pocket shutting down` (G B D)
• **Secondary:** `omnivore shutting down` (G · ·), `is evernote shutting down` (G · ·), `pocket shutting down alternative` (G · ·), `evernote shutting down` (G · ·)
• **LSI (10):** export window, shutdown notice, data deletion date, account dependency, offline copy, open formats, service exit, acquisition, read-it-later, portability
• **Changed:** 'notes app shutdown data' shows no demand. Real shutdown events show demand and make the risk concrete.

## Brand hub and side cluster

### HUB · Atomic Notes by DevBehindYou: Source-Available, Local First and Private by Design

• **Primary:** `atomic notes app` (G · ·)
• **Secondary:** `atomic notes by devbehindyou` (· · ·), `atomic notes android` (· · ·)
• **LSI:** local first notes app for Android, user owned Google Drive, optional end to end vault, source-available license, no AI features, no ads or trackers, Atomic Energy, GitHub releases, SHA-256 checksums, DevBehindYou
• **Note:** The plan's H1 said 'Open Source'. Atomic Notes has been source-available since September 28, 2026, so the H1 now says Source-Available. 'atomic notes' alone is owned by the Zettelkasten concept and by Atomic Blend's unrelated Atomic Notes app, so the hub targets the branded forms.

### ECON · Why Atomic Notes Uses Energy Instead of a Subscription

• **Primary:** `notes app without subscription` (G · ·)
• **Secondary:** `no subscription notes app` (G · ·), `free notes app no subscription` (G · ·)
• **LSI:** Atomic Energy, Atomic Coins, sync cost, daily energy, free tier, server costs, Google Drive API, sustainable software, no ads, pay per sync

## Accepted overlaps

These pairs share words, but a person reviewed each one and the intents differ.

| Pages | Why it's allowed |
|---|---|
| P1 and P3 | P1 owns the head term 'notes app privacy'. P3 keeps only the longer 'notes app privacy mistakes' as a title match. Don't use the bare head term in P3's title, H1 or meta description. |
| L1 and L2 | Definition vs listicle. L1 answers 'what is it' and L2 answers 'which apps'. L2 uses the plural 'apps' and 'best' in its title, L1 never does. |
| S1 and S2 | S1 is the 'encrypted notes' explainer. S2 owns the commercial 'best … app' and '… notes app' forms. S1 links to S2 for app picks instead of listing apps. |
| S1 and S2-S1 | S2-S1 targets a named 'vs' comparison, a different intent from S1's definition. |
| S1 and S2-S2 | S2-S2 answers yes/no questions about specific apps, a different intent from S1's definition. |
| S1 and S4 | S4 is about the limits of encryption claims, S1 defines encryption types. S4 links to S1 for definitions instead of re-explaining them. |
| S5-S1 and S5-S2 | False match. 'Standard Notes' is a brand name, and its word 'notes' overlaps S5-S1's generic keyword. |

## Keywords without autocomplete signal

Kept on purpose, never as a page's only reason to exist:

• `atomic notes android` (HUB secondary)
• `atomic notes architecture` (L5 secondary)
• `atomic notes by devbehindyou` (HUB secondary)
• `encrypted notes privacy` (S4 secondary)
• `end to end encryption metadata` (S4-S2 secondary)
• `migrate notes to a new app` (S5 secondary)
• `move notes to another app` (S5 secondary)
• `note taking privacy` (P3 secondary)
• `notes app data collection` (P5 secondary)
• `notes app permissions` (P1-S2 secondary)
• `notes app privacy mistakes` (P3 secondary)
• `password manager vs notes app` (S3-S1 secondary)
• `sync conflict resolution` (L5-S3 secondary)
• `zero knowledge recovery` (S4-S3 secondary)

## Keyword ownership index

Before using any of these as the focus of a new article, check who owns it.

| Keyword | Owner | As |
|---|---|---|
| 2fa backup codes | S3-S2 | secondary |
| ai note taker privacy concerns | P4-S1 | secondary |
| ai note taking privacy | P4-S1 | primary |
| android app permissions explained | P1-S2 | secondary |
| android permissions list | P1-S2 | secondary |
| android plain text notes app | L4-S3 | secondary |
| app telemetry | P5-S1 | secondary |
| apps like obsidian | L2 | secondary |
| apps that don't collect data | P5 | secondary |
| are samsung notes encrypted | S2-S2 | secondary |
| atomic notes android | HUB | secondary |
| atomic notes app | HUB | primary |
| atomic notes architecture | L5 | secondary |
| atomic notes by devbehindyou | HUB | secondary |
| aws outage | L3-S1 | secondary |
| backup android notes to google drive | P3-S2 | secondary |
| backup notes android | P3-S2 | primary |
| best encrypted notes app | S2 | primary |
| best f droid notes app | P2-S3 | primary |
| best note taking app with lock | S2-S3 | secondary |
| best offline notes app android | L4 | primary |
| best open source notes app | P2-S1 | primary |
| best private notes app | P2 | secondary |
| browser local storage vs cache | L3-S3 | secondary |
| cache storage vs indexeddb | L3-S3 | secondary |
| cache vs local storage | L3-S3 | primary |
| cache vs storage | L3-S3 | secondary |
| can apple read my notes | P1-S1 | secondary |
| can my notes app be hacked | P1-S1 | secondary |
| can someone hack into my notes app | P1-S1 | secondary |
| can you lock the notes app | S2-S3 | secondary |
| client side encryption | S1-S3 | primary |
| client side encryption example | S1-S3 | secondary |
| client side vs server side encryption | S1-S3 | secondary |
| cloud outage | L3-S1 | primary |
| cloud storage vs local storage for personal use | L1-S1 | secondary |
| conflicted copy meaning | L5-S3 | secondary |
| convert notes to markdown | S5-S1 | secondary |
| crdt local first | L5-S3 | secondary |
| credential stuffing | S3-S3 | secondary |
| dangerous permissions android | P1-S2 | secondary |
| data lock in | P3-S3 | secondary |
| data minimization | P5-S3 | secondary |
| data minimization examples | P5-S3 | primary |
| data minimization principle | P5-S3 | secondary |
| data minimization techniques | P5-S3 | secondary |
| data portability | L1-S3 | secondary |
| data portability gdpr | L1-S3 | secondary |
| does google docs use your data to train ai | P4-S3 | secondary |
| does google drive use your data to train ai | P4-S3 | secondary |
| does google keep work offline | L4-S2 | primary |
| does google use my data to train ai | P4-S3 | primary |
| does notes app work without internet | L3 | secondary |
| does notion ai train on my data | P4-S1 | secondary |
| does notion work offline | L4-S2 | secondary |
| does notion work without internet | L4-S2 | secondary |
| does obsidian work offline | L4-S2 | secondary |
| does obsidian work without internet | L4-S2 | secondary |
| drive.file scope | L5-S2 | secondary |
| e2ee metadata | S4-S2 | secondary |
| encrypted notes | S1 | primary |
| encrypted notes privacy | S4 | secondary |
| encrypted vs unencrypted backup | P3-S2 | secondary |
| encryption and privacy | S4 | secondary |
| encryption at rest | S1-S1 | secondary |
| encryption at rest vs end to end | S1-S1 | secondary |
| encryption in transit vs at rest | S1-S1 | primary |
| encryption key management | S1-S2 | secondary |
| end to end encrypted notes app | S2 | secondary |
| end to end encryption explained | S1 | secondary |
| end to end encryption metadata | S4-S2 | secondary |
| evernote outage | L3-S1 | secondary |
| evernote shutting down | S5-S3 | secondary |
| export apple notes to markdown | S5-S1 | secondary |
| export google keep notes | S5-S1 | secondary |
| export google keep notes to markdown | S5-S1 | secondary |
| export notes to markdown | S5-S1 | primary |
| f droid apps | P2-S3 | secondary |
| flutter hive | L5-S1 | secondary |
| foss notes app | P2-S1 | secondary |
| free notes app no subscription | ECON | secondary |
| free notes app without login | L4-S1 | secondary |
| google ai training data opt out | P4-S3 | secondary |
| google drive as database | L5-S2 | primary |
| google drive database app | L5-S2 | secondary |
| google drive file scope | L5-S2 | secondary |
| google drive notes app | L2-S2 | secondary |
| google keep alternative android | P2-S2 | secondary |
| google keep alternative open source | P2-S2 | secondary |
| google keep alternatives | P2-S2 | primary |
| google keep down | L3-S1 | secondary |
| google keep privacy | P2-S2 | secondary |
| hive database flutter | L5-S1 | secondary |
| how does encryption protect privacy | S4 | primary |
| how does sync work | L5-S1 | secondary |
| how to backup notes | P3-S2 | secondary |
| how to know if an app works offline | L3-S2 | secondary |
| how to opt out of google using my data to train ai | P4-S3 | secondary |
| https vs end to end encryption | S1-S1 | secondary |
| is apple notes end to end encrypted | S2-S2 | secondary |
| is evernote shutting down | S5-S3 | secondary |
| is f droid safe | P2-S3 | secondary |
| is google keep encrypted | S2-S2 | secondary |
| is google keep private | P2-S2 | secondary |
| is it ok to write down passwords | S3-S1 | secondary |
| is it safe to store passwords in notes | S3 | secondary |
| is it safe to write passwords down | S3-S1 | primary |
| is joplin end to end encrypted | S2-S1 | secondary |
| is metadata personal data | P5-S2 | secondary |
| is notes app private | P1 | secondary |
| is notion ai safe | P4-S1 | secondary |
| is obsidian encrypted | S2-S2 | secondary |
| is open source more secure | P1-S3 | primary |
| is the notes app encrypted | S2-S2 | primary |
| is the notes app safe | P1-S1 | secondary |
| is the notes app secure | P1-S1 | primary |
| is writing down passwords bad | S3-S1 | secondary |
| joplin export | S5-S2 | secondary |
| joplin export to markdown | S5-S2 | secondary |
| local ai note taking | P4-S2 | secondary |
| local ai notes app | P4-S2 | secondary |
| local ai vs cloud ai | P4-S2 | primary |
| local first app architecture | L5 | secondary |
| local first architecture | L5 | primary |
| local first comparison | L2-S3 | secondary |
| local first meaning | L1 | secondary |
| local first note taking | L2 | secondary |
| local first note taking apps | L2 | primary |
| local first notes app | L1 | primary |
| local first notion alternative | L2-S1 | secondary |
| local first sync | L5-S1 | primary |
| local first sync engine | L5-S1 | secondary |
| local first vs cloud first | L1-S2 | secondary |
| local first vs offline first | L1-S2 | primary |
| local notion alternative | L2-S1 | primary |
| local storage and cloud storage difference | L1-S1 | secondary |
| local storage vs cloud storage | L1-S1 | primary |
| local-first software | L1 | secondary |
| logseq vs anytype | L2-S3 | secondary |
| lost recovery key | S4-S3 | secondary |
| markdown notes app | L4-S3 | secondary |
| markdown notes app android | L4-S3 | primary |
| metadata examples | P5-S2 | secondary |
| metadata leakage | S4-S2 | secondary |
| metadata privacy | S4-S2 | primary |
| migrate notes to a new app | S5 | secondary |
| most secure notes app | S2 | secondary |
| move notes to another app | S5 | secondary |
| no subscription notes app | ECON | secondary |
| non proprietary file formats | P3-S3 | secondary |
| note taking app without ai | P4 | primary |
| note taking privacy | P3 | secondary |
| notes app data collection | P5 | secondary |
| notes app f droid | P2-S3 | secondary |
| notes app metadata | P5 | primary |
| notes app no internet | L3 | secondary |
| notes app no sign in | L4-S1 | secondary |
| notes app no sign up | L4-S1 | secondary |
| notes app permissions | P1-S2 | secondary |
| notes app privacy | P1 | primary |
| notes app privacy mistakes | P3 | secondary |
| notes app security | P3 | primary |
| notes app that syncs with google drive | L2-S2 | primary |
| notes app with lock | S2-S3 | primary |
| notes app with lock android | S2-S3 | secondary |
| notes app with lock feature | S2-S3 | secondary |
| notes app without account | L4-S1 | primary |
| notes app without ai | P4 | secondary |
| notes app without internet | L3 | primary |
| notes app without login | L4-S1 | secondary |
| notes app without subscription | ECON | primary |
| notes backup | P3-S2 | secondary |
| notesnook export | S5-S2 | secondary |
| notesnook vs joplin | S2-S1 | secondary |
| notesnook vs standard notes | S2-S1 | primary |
| notion ai privacy | P4-S1 | secondary |
| notion alternative local storage | L2-S1 | secondary |
| notion alternatives without ai | P4 | secondary |
| notion outage | L3-S1 | secondary |
| obsidian vs anytype | L2-S3 | secondary |
| obsidian vs logseq | L2-S3 | secondary |
| obsidian vs logseq vs anytype | L2-S3 | primary |
| offline cache | L3-S3 | secondary |
| offline first app | L1-S2 | secondary |
| offline first architecture | L1-S2 | secondary |
| offline first database | L1-S2 | secondary |
| offline mode app | L3-S2 | secondary |
| offline note taking app | L4 | secondary |
| offline notes app | L4 | secondary |
| offline sync | L3-S2 | primary |
| offline sync google drive | L3-S2 | secondary |
| offline synchronization | L3-S2 | secondary |
| omnivore shutting down | S5-S3 | secondary |
| on device ai | P4-S2 | secondary |
| on device ai privacy | P4-S2 | secondary |
| open source encrypted notes app | S2-S1 | secondary |
| open source note taking app | P2-S1 | secondary |
| open source notes app | P2-S1 | secondary |
| open source notes app android | P2-S1 | secondary |
| open source notion alternative | L2-S1 | secondary |
| open source privacy software | P1-S3 | secondary |
| own your data | L1-S3 | secondary |
| password manager vs notes app | S3-S1 | secondary |
| password reuse | S3-S3 | secondary |
| personal journal app | P3-S1 | secondary |
| plain text note taking | L4-S3 | secondary |
| plain text notes app | L4-S3 | secondary |
| pocket shutting down | S5-S3 | primary |
| pocket shutting down alternative | S5-S3 | secondary |
| privacy by design | S4-S1 | primary |
| privacy by design and by default | S4-S1 | secondary |
| privacy by design framework | S4-S1 | secondary |
| privacy by design meaning | S4-S1 | secondary |
| privacy by design principles | S4-S1 | secondary |
| privacy focused notes app | P1 | secondary |
| private diary app | P3-S1 | secondary |
| private journal app | P3-S1 | primary |
| private journal app for android | P3-S1 | secondary |
| private journal app free | P3-S1 | secondary |
| private notes app android | P2 | primary |
| private notion alternative | L2-S1 | secondary |
| proprietary file format | P3-S3 | secondary |
| recover end to end encryption | S4-S3 | secondary |
| reset end to end encryption | S4-S3 | secondary |
| safest way to store passwords | S3-S1 | secondary |
| save notes to google drive | L2-S2 | secondary |
| secure notes app android | P2 | secondary |
| self hosted notes app | L2-S2 | secondary |
| self hosted notes app with sync | L2-S2 | secondary |
| should i keep passwords in notes | S3 | secondary |
| source available software | P1-S3 | secondary |
| source available vs open source | P1-S3 | secondary |
| standard notes export | S5-S2 | primary |
| standard notes export markdown | S5-S2 | secondary |
| standard notes vs joplin | S2-S1 | secondary |
| storing passwords in notes app | S3 | primary |
| switch notes app | S5 | primary |
| sync conflict | L5-S3 | primary |
| sync conflict resolution | L5-S3 | secondary |
| telemetry data | P5-S1 | secondary |
| telemetry privacy | P5-S1 | secondary |
| tls vs end to end encryption | S1-S1 | secondary |
| traffic analysis | S4-S2 | secondary |
| use google drive as database | L5-S2 | secondary |
| user owned data | L1-S3 | secondary |
| vendor lock in | P3-S3 | primary |
| vendor lock in examples | P3-S3 | secondary |
| what app permissions should i allow | P1-S2 | primary |
| what can metadata reveal | P5-S2 | secondary |
| what does metadata reveal | P5-S2 | primary |
| what happens if your password is leaked | S3-S3 | primary |
| what is a conflicted copy | L5-S3 | secondary |
| what is client side encryption | S1-S3 | secondary |
| what is data minimization | P5-S3 | secondary |
| what is end to end encryption | S1 | secondary |
| what is f droid | P2-S3 | secondary |
| what is personal metadata | P5-S2 | secondary |
| what is server side encryption | S1-S3 | secondary |
| what is telemetry | P5-S1 | secondary |
| what to do if password is compromised | S3-S3 | secondary |
| what to do if your password is in a data breach | S3-S3 | secondary |
| where are google keep notes stored | L1-S1 | secondary |
| where are notes stored on android | L1-S1 | secondary |
| where to store 2fa backup codes | S3-S2 | primary |
| where to store backup codes | S3-S2 | secondary |
| where to store recovery phrase | S3-S2 | secondary |
| where to store seed phrase | S3-S2 | secondary |
| who owns your data | L1-S3 | primary |
| why open source is more secure | P1-S3 | secondary |
| zero knowledge account recovery | S4-S3 | primary |
| zero knowledge encryption | S1-S2 | primary |
| zero knowledge encryption cloud storage | S1-S2 | secondary |
| zero knowledge encryption meaning | S1-S2 | secondary |
| zero knowledge recovery | S4-S3 | secondary |
| zero knowledge vs end to end encryption | S1-S2 | secondary |
| zero telemetry | P5-S1 | primary |

## Changes from the original plan (31)

• **P1**: Primary moved from 'private notes app' (its SERP is app-store listings, a transactional intent) to 'notes app privacy' (mixed educational SERP). 'secure notes app' removed: it was also S5's primary.
• **P1-S1**: Its old primary 'notes app privacy' now belongs to its Main Blog (P1), so a Medium post can't outrank the site for the head term.
• **P1-S2** (was "5 Android Permissions a Notes App Should Explain Before You Trust It"): 'notes app permissions' shows no autocomplete demand. The question form 'what app permissions should i allow' shows up in all three engines and fits the same article.
• **P2-S1** (was "Best Private Notes Apps in 2026: 5 Picks Compared"): The current draft ('Best Private Notes Apps in 2026') targets the same query and apps as P2. Rewriting it as the open source list the plan intended removes the overlap.
• **P3**: 'notes app privacy mistakes' has no autocomplete demand, so it stays as an exact title-match secondary. 'notes app security' carries the demand. Slug loses the year so the URL stays evergreen.
• **P3-S1** (was "5 Sensitive Things You Should Think Twice Before Saving in Ordinary Notes"): The original topic duplicated S3-S2 (secrets you shouldn't keep in notes). Replaced with a journaling angle that has strong demand in all three engines.
• **P4**: Swapped with P4-S1. The old Main primary 'AI notes app privacy' shows no autocomplete demand, and its SERP is about AI meeting note-takers. 'note taking app without ai' and 'notes app without ai' show demand in all three engines, with a weak SERP (an HN post, a Medium post, ClickUp).
• **P4-S1**: Was the Main Blog. Now a support post, and it absorbs the original P4-S3 (an AI-assistant checklist), which duplicated it.
• **P4-S3** (was "5 Things to Check Before Allowing an AI Assistant to Read Your Notes"): Replaced a checklist that duplicated P4-S1. This question has demand in Google autocomplete and directly affects how people judge a Drive-synced notes app.
• **P5**: 'notes app data collection' shows no autocomplete demand, so it stays as the title-match secondary. 'notes app metadata' carries the demand. Dropped 'notes app tracking' (its autocomplete is about change tracking). Slug loses the count so the URL survives edits.
• **P5-S2** (was "Metadata vs Note Content: 7 Things Encryption May Not Hide"): The original topic duplicated S4-S2 (seven things E2EE can't hide). Re-angled to everyday metadata, which has its own demand.
• **L1**: 'offline notes app' removed: it is now L4's secondary, and L3 targets the offline problem.
• **L1-S1** (was "3 Places Your Notes Can Live and Why the Difference Matters for Privacy"): The old primary 'where are notes stored' has a device-specific SERP ('…on mac', '…on android'). The conceptual comparison matches 'local storage vs cloud storage' (demand in all three engines). The Android location question becomes a secondary.
• **L2**: The plan gave L2 the secondaries 'local first notes app' and 'local first note taking', which were L1's primary and secondary. L2 now targets 'local first note taking apps' (the form Google autocompletes) and 'apps like obsidian' (demand in all three engines). Use 'best' in the title, not in the keyword.
• **L3**: 'offline notes app' moved to L4 (its SERP is commercial). L3 takes the problem phrasing. The draft slug 'offline-notes-apps' would also have competed with L4, so the slug changes before first publish.
• **L3-S2** (was "6 Things a Notes App Should Let You Do Without Internet"): The original primary 'notes app without internet' now belongs to L3. 'offline sync' shows demand in all three engines.
• **L4-S2** (was "7 F-Droid Offline Notes Apps Worth Trying in 2026"): The original was a second F-Droid listicle that duplicated P2-S3. Replaced with three 'does X work offline' questions that each show demand in all three engines.
• **L4-S3** (was "How to Test Whether a Notes App Really Works Offline: 8 Checks"): 'test offline notes app' shows no demand in any engine. The test checklist now lives in L3 and L3-S2.
• **L5**: 'local first notes architecture' shows no demand. 'local first architecture' shows demand in all three engines.
• **S1**: The plan gave 'end to end encrypted notes' to S1, S2, and S4, and 'encrypted notes app' to S1 and S4. Each now has one owner: S2 owns the commercial 'app' forms.
• **S1-S2** (was "Who Holds the Encryption Key? 6 Questions Before Trusting an Encrypted Notes App"): 'encryption key ownership notes' shows no demand. 'zero knowledge encryption' shows demand in all three engines and asks the same question.
• **S2-S2** (was "7 Features to Compare Before Choosing an Encrypted Notes App"): The original checklist duplicated S1-S2 (questions before trusting an encrypted app). Replaced with brand questions that each show demand.
• **S2-S3** (was "Encrypted Notes on Android: 6 Questions to Ask Before You Sync"): 'encrypted notes Android' has a commercial SERP that overlaps P2 and S2. 'notes app with lock' shows demand in all three engines and covers a common misunderstanding.
• **S3**: 'secure password storage' was dropped. Its SERP is OWASP's developer cheat sheet on password hashing, a different intent.
• **S3-S1** (was "Password Manager vs Notes App: 7 Security Differences"): 'password manager vs notes app' shows no autocomplete demand, so it stays as a secondary. The paper question shows demand and widens the comparison.
• **S4**: 'encrypted notes privacy' shows no demand, so it stays as the title-match secondary. The question form carries the demand. 'encrypted notes app' and 'end to end encrypted notes' now belong to S2. Remove the FAQ 'Is an encrypted notes app automatically private?', which also appears in S4-S1.
• **S4-S1** (was "Encryption Alone Does Not Make a Notes App Private"): As planned, this support post argued the same thesis as its Main Blog and shared an FAQ with it, which is a duplicate-content risk. The privacy-by-design framing has demand in all three engines and a distinct intent.
• **S5**: The old primary 'secure notes app' has an app-store SERP, the wrong intent for a migration guide, and it was also P1's secondary. Autocomplete for migration phrases is weak, so expect low but well-matched traffic.
• **S5-S2** (was "How to Migrate Encrypted Notes Without Losing Access: 6 Checks"): 'migrate encrypted notes' shows no demand in any engine. The app-specific export questions show demand and cover the same task.
• **S5-S3** (was "What Happens to Your Notes If an App Shuts Down? 6 Questions to Ask First"): 'notes app shutdown data' shows no demand. Real shutdown events show demand and make the risk concrete.
• **HUB** (was "Atomic Notes: Local-First and Private by Design"): The plan's H1 said 'Open Source'. Atomic Notes has been source-available since September 28, 2026, so the H1 now says Source-Available. 'atomic notes' alone is owned by the Zettelkasten concept and by Atomic Blend's unrelated Atomic Notes app, so the hub targets the branded forms.
