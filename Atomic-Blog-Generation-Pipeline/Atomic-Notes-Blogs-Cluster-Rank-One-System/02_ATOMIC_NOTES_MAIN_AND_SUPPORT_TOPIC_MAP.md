# Atomic Notes Main and Support Topic Map

Generated from `keyword-registry.json` by `node scripts/cluster-docs.mjs`. Edit the registry, not this file.

## Structure

• 3 pillars
• 5 Main Blogs per pillar
• 3 Support Blogs per Main Blog
• 15 Main Blogs total
• 45 Support Blogs total

Main Blogs belong on the Atomic Notes website. Support Blogs are unique external articles that link contextually to their assigned Main Blog.

Keyword rules (checked by `node scripts/cluster-check.mjs`):

• Main Blog: 1 primary, 2 secondary, up to 10 LSI
• Support Blog: 1 primary, 4 secondary, up to 10 LSI
• A primary or secondary keyword belongs to exactly one URL in the whole cluster
• An LSI term may repeat across pages, but never as another page's primary or secondary

Research evidence and every change from the original plan are in `05_ATOMIC_NOTES_KEYWORD_MAP.md`.

# PRIVACY

## P1. 9 Privacy Red Flags to Check Before Trusting Any Notes App in 2026

**Role:** Main Blog
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 03/06 - 9 Privacy Red Flags Before Trusting Any Notes App` (work: re-keyword)
**Primary keyword:** `notes app privacy`
**Secondary keywords:** `is notes app private`, `privacy focused notes app`
**LSI keywords:** third party trackers, privacy policy, data safety section, notes app encryption, account deletion, data export options, cloud sync, privacy labels, source code transparency, business model
**Search intent:** informational + commercial investigation
**Atomic Notes URL:** `/blog/notes-app-privacy-red-flags` (current draft slug `9-notes-app-privacy-red-flags`, change it before first publish)
**Angle:** A decision checklist: nine signs a notes app is not as private as it claims, and how to check each one.
**Why this is a Main Blog:** Broad decision-stage privacy checklist with strong internal-link potential across tracking, encryption, AI, permissions, portability, and storage.
**Changed from the original plan:** Primary moved from 'private notes app' (its SERP is app-store listings, a transactional intent) to 'notes app privacy' (mixed educational SERP). 'secure notes app' removed: it was also S5's primary.

### Support Blogs

#### P1-S1. 7 Ways Your Notes App Could Expose More About You Than You Realize

**Primary keyword:** `is the notes app secure`
**Secondary keywords:** `can my notes app be hacked`, `can someone hack into my notes app`, `is the notes app safe`, `can apple read my notes`
**LSI keywords:** cloud backups, analytics SDK, usage tracking, AI processing, shared links, old devices, sync metadata, account security, personal data exposure, phone backups
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 03/07 - 7 Ways Your Notes App Could Expose You` (work: re-keyword)
**Platform:** Medium
**Search intent:** informational
**Purpose:** Exposure paths beyond reading notes: cloud keys, telemetry, SDKs, weak sign-in, backups, AI processing, permissions.
**Required destination link:** `/blog/notes-app-privacy-red-flags`
**Changed from the original plan:** Its old primary 'notes app privacy' now belongs to its Main Blog (P1), so a Medium post can't outrank the site for the head term.

#### P1-S2. What App Permissions Should You Allow a Notes App? 5 to Question on Android

**Original plan title:** 5 Android Permissions a Notes App Should Explain Before You Trust It
**Primary keyword:** `what app permissions should i allow`
**Secondary keywords:** `android app permissions explained`, `android permissions list`, `dangerous permissions android`, `notes app permissions`
**LSI keywords:** runtime permissions, INTERNET permission, storage access, contacts permission, microphone access, location permission, Exodus Privacy, AndroidManifest, permission manager, Google Play data safety
**Source status:** New
**Platform:** Medium
**Search intent:** informational / how-to
**Purpose:** A pre-install permissions checklist for notes apps, with what each permission can expose and how to check it.
**Required destination link:** `/blog/notes-app-privacy-red-flags`
**Changed from the original plan:** 'notes app permissions' shows no autocomplete demand. The question form 'what app permissions should i allow' shows up in all three engines and fits the same article.

#### P1-S3. Is Open Source More Secure? 6 Things Public Source Code Lets You Verify

**Original plan title:** Why Privacy Software Should Be Open Source
**Primary keyword:** `is open source more secure`
**Secondary keywords:** `source available vs open source`, `why open source is more secure`, `open source privacy software`, `source available software`
**LSI keywords:** software transparency, code review, reproducible builds, security through obscurity, Linus's law, license terms, independent audit, supply chain security, verifiable claims, public repository
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 01/Why Privacy Software Should Be Open Source` (work: rewrite)
**Platform:** Substack
**Search intent:** informational / opinion
**Purpose:** What public source code does and doesn't prove, open source vs source-available, and how to verify an app's privacy claims. States plainly that Atomic Notes is source-available.
**Required destination link:** `/blog/notes-app-privacy-red-flags`

### Internal Link Targets

• Link to the Atomic Notes by DevBehindYou hub (`/blog/atomic-notes-by-devbehindyou`) when Atomic Notes is discussed.
• Contextual Main Blog links: P5, S4, P2.
• Link to the official GitHub repository when architecture or source claims need verification.

---

## P2. 7 Best Privacy First Note Taking Apps for Android in 2026

**Role:** Main Blog
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 02/02 - 7 Best Privacy First Note Taking Apps for Android in 2026` (work: re-keyword)
**Primary keyword:** `private notes app android`
**Secondary keywords:** `best private notes app`, `secure notes app android`
**LSI keywords:** privacy first notes app, Notesnook, Standard Notes, Joplin, no ads, F-Droid, data safety section, encrypted sync, offline access, local storage
**Search intent:** commercial investigation
**Atomic Notes URL:** `/blog/best-privacy-first-notes-apps-android`
**Angle:** Android listicle, Atomic Notes first, every app verified against its own store listing and source.
**Why this is a Main Blog:** High-conversion comparison intent. Lets Atomic Notes compete in a category users already search before installing an app.

### Support Blogs

#### P2-S1. Best Open Source Notes Apps for Privacy in 2026

**Original plan title:** Best Private Notes Apps in 2026: 5 Picks Compared
**Primary keyword:** `best open source notes app`
**Secondary keywords:** `open source notes app`, `open source note taking app`, `foss notes app`, `open source notes app android`
**LSI keywords:** GPL license, AGPL, GitHub releases, self hosted sync, end to end encryption, Markdown files, community audits, F-Droid builds, active maintenance, issue tracker
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 01/Best Private Notes Apps in 2026` (work: rewrite)
**Platform:** DEV Community
**Search intent:** commercial investigation
**Purpose:** Open source picks only, with license and audit status. Atomic Notes appears once as a clearly labeled source-available alternative, never in the ranked list. No app may repeat from P2's list.
**Required destination link:** `/blog/best-privacy-first-notes-apps-android`
**Changed from the original plan:** The current draft ('Best Private Notes Apps in 2026') targets the same query and apps as P2. Rewriting it as the open source list the plan intended removes the overlap.

#### P2-S2. 7 Best Google Keep Alternatives for Privacy in 2026

**Primary keyword:** `google keep alternatives`
**Secondary keywords:** `google keep privacy`, `is google keep private`, `google keep alternative open source`, `google keep alternative android`
**LSI keywords:** Google Takeout, Google account, Gemini, labels, checklists, reminders, cross device sync, Notally, data safety section, ad profile
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 02/03 - 7 Best Google Keep Alternatives for Privacy in 2026` (work: re-keyword)
**Platform:** Medium
**Search intent:** commercial investigation
**Purpose:** For people leaving Google Keep over privacy: what Keep collects, then private alternatives.
**Required destination link:** `/blog/best-privacy-first-notes-apps-android`

#### P2-S3. 5 F-Droid Notes Apps for Privacy-Conscious Android Users in 2026

**Primary keyword:** `best f droid notes app`
**Secondary keywords:** `notes app f droid`, `f droid apps`, `is f droid safe`, `what is f droid`
**LSI keywords:** reproducible builds, anti-features, IzzyOnDroid, Droid-ify, APK signing, Markor, Material Notes, sideloading, open source repository, app updates
**Source status:** New
**Platform:** DEV Community
**Search intent:** commercial investigation
**Purpose:** What F-Droid is, whether it's safe, and five notes apps worth installing from it. Atomic Notes is not on F-Droid, so it's mentioned only as a GitHub-release alternative.
**Required destination link:** `/blog/best-privacy-first-notes-apps-android`

### Internal Link Targets

• Link to the Atomic Notes by DevBehindYou hub (`/blog/atomic-notes-by-devbehindyou`) when Atomic Notes is discussed.
• Contextual Main Blog links: P1, L2, S2.
• Link to the official GitHub repository when architecture or source claims need verification.

---

## P3. 10 Privacy Mistakes People Make With Notes Apps in 2026

**Role:** Main Blog
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 03/01 - 10 Privacy Mistakes People Make With Notes Apps in 2026` (work: re-keyword)
**Primary keyword:** `notes app security`
**Secondary keywords:** `notes app privacy mistakes`, `note taking privacy`
**LSI keywords:** recovery phrase, screen lock, app lock, cloud backup, shared notes, APK security, password storage risk, end to end encryption, data ownership, cloud notes privacy
**Search intent:** informational / awareness
**Atomic Notes URL:** `/blog/notes-app-privacy-mistakes` (current draft slug `10-notes-app-privacy-mistakes-2026`, change it before first publish)
**Angle:** Problem-first: ten habits that weaken notes app security and privacy, each with a fix.
**Why this is a Main Blog:** Highly shareable problem-first article that can attract broad privacy traffic and feed readers into security and product-selection content.
**Changed from the original plan:** 'notes app privacy mistakes' has no autocomplete demand, so it stays as an exact title-match secondary. 'notes app security' carries the demand. Slug loses the year so the URL stays evergreen.

### Support Blogs

#### P3-S1. What to Look For in a Private Journal App: 6 Privacy Checks Before You Write

**Original plan title:** 5 Sensitive Things You Should Think Twice Before Saving in Ordinary Notes
**Primary keyword:** `private journal app`
**Secondary keywords:** `private journal app for android`, `private diary app`, `private journal app free`, `personal journal app`
**LSI keywords:** journaling privacy, biometric lock, encrypted journal, mood tracking, offline journal, cloud sync, data export, ads, on-device journal, journal backup
**Source status:** New
**Platform:** Medium
**Search intent:** commercial investigation
**Purpose:** Journaling is the most personal thing people type. Six checks: storage, encryption, lock, sync, exports, business model.
**Required destination link:** `/blog/notes-app-privacy-mistakes`
**Changed from the original plan:** The original topic duplicated S3-S2 (secrets you shouldn't keep in notes). Replaced with a journaling angle that has strong demand in all three engines.

#### P3-S2. How to Back Up Notes on Android Without Creating Privacy Risks: 7 Mistakes to Avoid

**Original plan title:** 7 Backup Mistakes That Can Put Private Notes at Risk
**Primary keyword:** `backup notes android`
**Secondary keywords:** `how to backup notes`, `notes backup`, `backup android notes to google drive`, `encrypted vs unencrypted backup`
**LSI keywords:** backup encryption, restore test, Android backup, Google One backup, 3-2-1 backup rule, export file, stale copies, shared folders, recovery material, version history
**Source status:** New
**Platform:** WordPress
**Search intent:** how-to
**Purpose:** Backups done safely: encryption, where copies live, stale copies, restore tests.
**Required destination link:** `/blog/notes-app-privacy-mistakes`

#### P3-S3. Vendor Lock-In for Notes: 6 Ways Convenience Traps Your Data

**Original plan title:** 6 Ways Convenience Can Lock Your Notes Into One Platform
**Primary keyword:** `vendor lock in`
**Secondary keywords:** `proprietary file format`, `data lock in`, `vendor lock in examples`, `non proprietary file formats`
**LSI keywords:** export formats, Markdown, JSON export, switching costs, closed API, account dependency, migration friction, open formats, service shutdown, portability
**Source status:** New
**Platform:** Substack
**Search intent:** informational / opinion
**Purpose:** Proprietary formats, weak exports, account dependency, closed APIs, and how to spot them before years of notes pile up.
**Required destination link:** `/blog/notes-app-privacy-mistakes`

### Internal Link Targets

• Link to the Atomic Notes by DevBehindYou hub (`/blog/atomic-notes-by-devbehindyou`) when Atomic Notes is discussed.
• Contextual Main Blog links: P1, S3, S5.
• Link to the official GitHub repository when architecture or source claims need verification.

---

## P4. 7 Best Note Taking Apps Without AI in 2026

**Role:** Main Blog
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 02/01 - 7 Best Note Taking Apps Without AI in 2026` (work: promote)
**Primary keyword:** `note taking app without ai`
**Secondary keywords:** `notes app without ai`, `notion alternatives without ai`
**LSI keywords:** AI free note taking app, no AI notes app, AI training data, AI features toggle, Apple Intelligence, Gemini, Notion AI, plain notes, distraction free writing, offline writing
**Search intent:** commercial investigation
**Atomic Notes URL:** `/blog/best-note-taking-apps-without-ai`
**Angle:** AI-free notes apps for people who want their thinking left alone. Atomic Notes first.
**Why this is a Main Blog:** The clearest product differentiator Atomic Notes has, with demand in all three engines and a thin SERP (an HN post, a Medium post, a generic ClickUp list). It turns 'no AI' from a slogan into a comparison people already search for.
**Changed from the original plan:** Swapped with P4-S1. The old Main primary 'AI notes app privacy' shows no autocomplete demand, and its SERP is about AI meeting note-takers. 'note taking app without ai' and 'notes app without ai' show demand in all three engines, with a weak SERP (an HN post, a Medium post, ClickUp).

### Support Blogs

#### P4-S1. 6 Questions You Should Ask Before Giving an AI Notes App Your Private Thoughts

**Primary keyword:** `ai note taking privacy`
**Secondary keywords:** `notion ai privacy`, `is notion ai safe`, `does notion ai train on my data`, `ai note taker privacy concerns`
**LSI keywords:** AI data processing, AI data retention, third party AI provider, AI training data opt out, zero data retention, model provider, enterprise AI terms, prompt data, consent, AI privacy settings
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 03/03 - 6 Questions Before Giving an AI Notes App Your Thoughts` (work: demote)
**Platform:** Substack
**Search intent:** informational
**Purpose:** Six questions about AI processing, retention, training, providers, and off switches, for in-app AI and AI note-takers alike.
**Required destination link:** `/blog/best-note-taking-apps-without-ai`
**Changed from the original plan:** Was the Main Blog. Now a support post, and it absorbs the original P4-S3 (an AI-assistant checklist), which duplicated it.

#### P4-S2. Local AI vs Cloud AI for Note Taking: 6 Privacy Differences

**Primary keyword:** `local ai vs cloud ai`
**Secondary keywords:** `on device ai`, `on device ai privacy`, `local ai note taking`, `local ai notes app`
**LSI keywords:** on-device model, Gemini Nano, Private Cloud Compute, Ollama, latency, offline inference, data transfer, retention, model access, NPU
**Source status:** New
**Platform:** Hashnode
**Search intent:** comparison
**Purpose:** Where processing happens, what leaves the device, retention, offline use, model access, control.
**Required destination link:** `/blog/best-note-taking-apps-without-ai`

#### P4-S3. Does Google Use Your Data to Train AI? What It Means for Notes in Google Drive

**Original plan title:** 5 Things to Check Before Allowing an AI Assistant to Read Your Notes
**Primary keyword:** `does google use my data to train ai`
**Secondary keywords:** `does google drive use your data to train ai`, `does google docs use your data to train ai`, `how to opt out of google using my data to train ai`, `google ai training data opt out`
**LSI keywords:** Google Workspace, Gemini, Drive privacy, Web & App Activity, personal account, terms of service, consent, data controls, user owned Google Drive, Google One
**Source status:** New
**Platform:** Medium
**Search intent:** informational
**Purpose:** What Google's current terms say about Drive and Docs content and AI training, and how to check your settings. Atomic Notes stores synced notes in the user's Drive, so this is a real user question. Verify Google's policy on the day of writing.
**Required destination link:** `/blog/best-note-taking-apps-without-ai`
**Changed from the original plan:** Replaced a checklist that duplicated P4-S1. This question has demand in Google autocomplete and directly affects how people judge a Drive-synced notes app.

### Internal Link Targets

• Link to the Atomic Notes by DevBehindYou hub (`/blog/atomic-notes-by-devbehindyou`) when Atomic Notes is discussed.
• Contextual Main Blog links: P5, S4, P2.
• Link to the official GitHub repository when architecture or source claims need verification.

---

## P5. 8 Pieces of Data a Notes App May Know About You Even Without Reading Your Notes

**Role:** Main Blog
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 03/04 - 8 Pieces of Data a Notes App May Know About You` (work: re-keyword)
**Primary keyword:** `notes app metadata`
**Secondary keywords:** `notes app data collection`, `apps that don't collect data`
**LSI keywords:** IP address, device model, login timestamps, sync activity, usage analytics, account email, device fingerprinting, server logs, retention period, privacy policy
**Search intent:** informational
**Atomic Notes URL:** `/blog/notes-app-data-collection` (current draft slug `8-types-of-data-notes-apps-may-collect`, change it before first publish)
**Angle:** Operational data versus note content: what a provider can learn without opening a single note.
**Why this is a Main Blog:** Builds topical authority around metadata, data minimization, telemetry, and the difference between note content and operational data.
**Changed from the original plan:** 'notes app data collection' shows no autocomplete demand, so it stays as the title-match secondary. 'notes app metadata' carries the demand. Dropped 'notes app tracking' (its autocomplete is about change tracking). Slug loses the count so the URL survives edits.

### Support Blogs

#### P5-S1. Zero Telemetry: Why Your Notes App Should Know Less About You

**Primary keyword:** `zero telemetry`
**Secondary keywords:** `what is telemetry`, `telemetry data`, `app telemetry`, `telemetry privacy`
**LSI keywords:** analytics SDK, crash reporting, Firebase Analytics, opt-in analytics, anonymous data, usage events, Exodus Privacy, network traffic, tracker SDKs, privacy friendly analytics
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 01/Zero Telemetry - Why Your Notes App Should Know Less About You` (work: re-keyword)
**Platform:** Medium
**Search intent:** informational
**Purpose:** What telemetry is, why notes apps add it, and how to check an app for it.
**Required destination link:** `/blog/notes-app-data-collection`

#### P5-S2. What Does Metadata Reveal? 6 Examples From Apps You Use Every Day

**Original plan title:** Metadata vs Note Content: 7 Things Encryption May Not Hide
**Primary keyword:** `what does metadata reveal`
**Secondary keywords:** `metadata examples`, `what can metadata reveal`, `is metadata personal data`, `what is personal metadata`
**LSI keywords:** EFF, call records, timestamps, location data, EXIF, communication patterns, GDPR personal data, data aggregation, inference, social graph
**Source status:** New
**Platform:** Medium
**Search intent:** informational
**Purpose:** General metadata education with everyday examples (photos, calls, notes). Leaves the encryption angle to S4-S2.
**Required destination link:** `/blog/notes-app-data-collection`
**Changed from the original plan:** The original topic duplicated S4-S2 (seven things E2EE can't hide). Re-angled to everyday metadata, which has its own demand.

#### P5-S3. Data Minimization Examples: 5 Signs a Notes App Collects Less

**Original plan title:** Data Minimization for Notes Apps: 5 Signs a Product Collects Less
**Primary keyword:** `data minimization examples`
**Secondary keywords:** `what is data minimization`, `data minimization principle`, `data minimization techniques`, `data minimization`
**LSI keywords:** GDPR Article 5, purpose limitation, storage limitation, retention schedule, pseudonymization, collection limits, privacy notice, consent, local processing, deletion
**Source status:** New
**Platform:** WordPress
**Search intent:** informational
**Purpose:** The legal principle turned into a user-facing checklist, with notes-app examples.
**Required destination link:** `/blog/notes-app-data-collection`

### Internal Link Targets

• Link to the Atomic Notes by DevBehindYou hub (`/blog/atomic-notes-by-devbehindyou`) when Atomic Notes is discussed.
• Contextual Main Blog links: P1, S4, P4.
• Link to the official GitHub repository when architecture or source claims need verification.

---

# LOCAL FIRST

## L1. What Is a Local First Notes App and Why Does It Matter?

**Role:** Main Blog
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 01/What Is a Local-First Notes App` (work: re-keyword)
**Primary keyword:** `local first notes app`
**Secondary keywords:** `local-first software`, `local first meaning`
**LSI keywords:** Ink & Switch, Martin Kleppmann, source of truth, on-device storage, sync engine, cloud dependency, CRDT, offline capability, user control, longevity
**Search intent:** informational / definition
**Atomic Notes URL:** `/blog/what-is-a-local-first-notes-app`
**Angle:** The category definition Atomic Notes wants to own, with the Ink & Switch ideals and honest limits.
**Why this is a Main Blog:** Foundational pillar defining the category Atomic Notes wants to be associated with across SERPs and AI answer engines.
**Changed from the original plan:** 'offline notes app' removed: it is now L4's secondary, and L3 targets the offline problem.

### Support Blogs

#### L1-S1. Local Storage vs Cloud Storage for Notes: 3 Places Your Notes Can Live

**Original plan title:** 3 Places Your Notes Can Live and Why the Difference Matters for Privacy
**Primary keyword:** `local storage vs cloud storage`
**Secondary keywords:** `where are notes stored on android`, `where are google keep notes stored`, `cloud storage vs local storage for personal use`, `local storage and cloud storage difference`
**LSI keywords:** device storage, company cloud, own cloud, Google Drive, iCloud, encryption keys, backups, account lock, shutdown risk, sync
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 03/09 - 3 Places Your Notes Can Live` (work: re-keyword)
**Platform:** Medium
**Search intent:** comparison
**Purpose:** Device only vs company cloud vs your own cloud, compared on control, backups, shutdown risk, and keys.
**Required destination link:** `/blog/what-is-a-local-first-notes-app`
**Changed from the original plan:** The old primary 'where are notes stored' has a device-specific SERP ('…on mac', '…on android'). The conceptual comparison matches 'local storage vs cloud storage' (demand in all three engines). The Android location question becomes a secondary.

#### L1-S2. Local First vs Offline First vs Cloud First: 7 Differences That Matter

**Primary keyword:** `local first vs offline first`
**Secondary keywords:** `offline first database`, `local first vs cloud first`, `offline first app`, `offline first architecture`
**LSI keywords:** source of truth, server authority, sync queue, conflict resolution, CRDTs, latency, cache, RxDB, eventual consistency, seven ideals
**Source status:** New
**Platform:** DEV Community
**Search intent:** comparison
**Purpose:** Where the source of truth lives in each model, and why 'works offline' is not the same as 'local first'.
**Required destination link:** `/blog/what-is-a-local-first-notes-app`

#### L1-S3. Who Owns Your Data? 5 Questions About Notes, Portability, and Storage

**Original plan title:** Who Owns Your Notes? 5 Questions About Portability, Export, and Storage
**Primary keyword:** `who owns your data`
**Secondary keywords:** `data portability`, `user owned data`, `own your data`, `data portability gdpr`
**LSI keywords:** GDPR Article 20, export formats, terms of service, account deletion, service shutdown, file ownership, cloud control, interoperability, lock-in, takeout
**Source status:** New
**Platform:** Substack
**Search intent:** informational / opinion
**Purpose:** Ownership in practice: file location, export rights, account dependency, terms of service, service exit.
**Required destination link:** `/blog/what-is-a-local-first-notes-app`

### Internal Link Targets

• Link to the Atomic Notes by DevBehindYou hub (`/blog/atomic-notes-by-devbehindyou`) when Atomic Notes is discussed.
• Contextual Main Blog links: L3, L5, P5.
• Link to the official GitHub repository when architecture or source claims need verification.

---

## L2. 6 Best Local First Note Taking Apps in 2026 That Keep Your Data Yours

**Role:** Main Blog
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 02/04 - 6 Best Local First Note Taking Apps in 2026` (work: re-keyword)
**Primary keyword:** `local first note taking apps`
**Secondary keywords:** `local first note taking`, `apps like obsidian`
**LSI keywords:** Logseq, Anytype, Joplin, Markdown files, plain text, sync options, encryption, offline access, data ownership, vault
**Search intent:** commercial investigation
**Atomic Notes URL:** `/blog/best-local-first-note-taking-apps`
**Angle:** Listicle, Atomic Notes first, compared on storage model, sync, encryption, and file format.
**Why this is a Main Blog:** Comparison query with strong discovery potential and natural coverage of storage models, offline behavior, synchronization, and portability.
**Changed from the original plan:** The plan gave L2 the secondaries 'local first notes app' and 'local first note taking', which were L1's primary and secondary. L2 now targets 'local first note taking apps' (the form Google autocompletes) and 'apps like obsidian' (demand in all three engines). Use 'best' in the title, not in the keyword.

### Support Blogs

#### L2-S1. 3 Best Private Notion Alternatives for Local First Notes in 2026

**Primary keyword:** `local notion alternative`
**Secondary keywords:** `private notion alternative`, `local first notion alternative`, `open source notion alternative`, `notion alternative local storage`
**LSI keywords:** AppFlowy, AFFiNE, offline workspace, databases, self hosting, encrypted workspace, Markdown export, block editor, data ownership, templates
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 02/07 - 3 Best Private Notion Alternatives in 2026` (work: re-keyword)
**Platform:** Medium
**Search intent:** commercial investigation
**Purpose:** Workspace users who want Notion's structure without a vendor holding their data.
**Required destination link:** `/blog/best-local-first-note-taking-apps`

#### L2-S2. 5 Notes Apps That Sync Through Your Own Cloud Storage

**Original plan title:** 5 Local First Notes Apps That Use Plain Files or User-Owned Storage
**Primary keyword:** `notes app that syncs with google drive`
**Secondary keywords:** `google drive notes app`, `save notes to google drive`, `self hosted notes app`, `self hosted notes app with sync`
**LSI keywords:** Dropbox sync, WebDAV, Nextcloud, OneDrive, Syncthing, folder sync, user owned cloud storage, sync targets, file based notes, file sync apps
**Source status:** New
**Platform:** Medium
**Search intent:** commercial investigation
**Purpose:** Apps that sync through Google Drive, Dropbox, WebDAV, Nextcloud, or a folder you control. Atomic Notes is one honest entry (Google Drive, drive.file scope).
**Required destination link:** `/blog/best-local-first-note-taking-apps`

#### L2-S3. Obsidian vs Logseq vs Anytype vs Atomic Notes: 8 Local First Differences

**Primary keyword:** `obsidian vs logseq vs anytype`
**Secondary keywords:** `obsidian vs logseq`, `obsidian vs anytype`, `logseq vs anytype`, `local first comparison`
**LSI keywords:** Markdown vault, outliner, block references, any-sync, E2EE sync, plugins, mobile apps, Google Drive sync, Logseq DB version, file formats
**Source status:** New
**Platform:** Hashnode
**Search intent:** comparison
**Purpose:** Four local-first apps with very different data, sync, and complexity models.
**Required destination link:** `/blog/best-local-first-note-taking-apps`

### Internal Link Targets

• Link to the Atomic Notes by DevBehindYou hub (`/blog/atomic-notes-by-devbehindyou`) when Atomic Notes is discussed.
• Contextual Main Blog links: L1, L4, P2.
• Link to the official GitHub repository when architecture or source claims need verification.

---

## L3. Offline Notes Apps: Why Your Notes Should Work Without Internet

**Role:** Main Blog
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 01/Offline Notes Apps - Why Notes Should Work Offline` (work: re-keyword)
**Primary keyword:** `notes app without internet`
**Secondary keywords:** `notes app no internet`, `does notes app work without internet`
**LSI keywords:** airplane mode, local storage, sync later, cloud dependency, latency, dead zones, travel, outages, Hive storage, source of truth
**Search intent:** informational / problem-solution
**Atomic Notes URL:** `/blog/why-notes-should-work-offline` (current draft slug `offline-notes-apps`, change it before first publish)
**Angle:** Why offline should be the default, what breaks without it, and how to test an app yourself.
**Why this is a Main Blog:** Explains the user benefit of local-first architecture in a simple real-world way and supports resilience/outage queries.
**Changed from the original plan:** 'offline notes app' moved to L4 (its SERP is commercial). L3 takes the problem phrasing. The draft slug 'offline-notes-apps' would also have competed with L4, so the slug changes before first publish.

### Support Blogs

#### L3-S1. What Happens to Your Notes When the Cloud Goes Down?

**Primary keyword:** `cloud outage`
**Secondary keywords:** `notion outage`, `aws outage`, `evernote outage`, `google keep down`
**LSI keywords:** status page, outage timeline, cached notes, sync failure, single point of failure, resilience, local copy, read-only mode, incident report, downtime
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 01/What Happens to Your Notes When the Cloud Goes Down` (work: re-keyword)
**Platform:** Medium
**Search intent:** informational / news-driven
**Purpose:** Dated, sourced outage examples as the real-world test of local-first behavior.
**Required destination link:** `/blog/why-notes-should-work-offline`

#### L3-S2. Offline Sync Explained: 6 Things a Notes App Should Do Without Internet

**Original plan title:** 6 Things a Notes App Should Let You Do Without Internet
**Primary keyword:** `offline sync`
**Secondary keywords:** `offline synchronization`, `offline mode app`, `how to know if an app works offline`, `offline sync google drive`
**LSI keywords:** sync queue, reconnect, airplane mode test, pending changes, retry, local database, search offline, media files, conflict, background sync
**Source status:** New
**Platform:** Medium
**Search intent:** informational / how-to
**Purpose:** Six offline capabilities (create, edit, search, delete, queue, recover), how sync catches up, and how to test each one.
**Required destination link:** `/blog/why-notes-should-work-offline`
**Changed from the original plan:** The original primary 'notes app without internet' now belongs to L3. 'offline sync' shows demand in all three engines.

#### L3-S3. Offline Cache vs Local Storage: 5 Differences Users Should Know

**Primary keyword:** `cache vs local storage`
**Secondary keywords:** `offline cache`, `cache vs storage`, `cache storage vs indexeddb`, `browser local storage vs cache`
**LSI keywords:** IndexedDB, Service Worker, Cache API, eviction, persistence, authoritative copy, Hive box, SQLite, quota, progressive web app
**Source status:** New
**Platform:** DEV Community
**Search intent:** comparison / technical
**Purpose:** Why cached access is not local-first ownership: eviction, persistence, authority, sync.
**Required destination link:** `/blog/why-notes-should-work-offline`

### Internal Link Targets

• Link to the Atomic Notes by DevBehindYou hub (`/blog/atomic-notes-by-devbehindyou`) when Atomic Notes is discussed.
• Contextual Main Blog links: L1, L4, L5.
• Link to the official GitHub repository when architecture or source claims need verification.

---

## L4. 8 Best Offline Notes Apps for Android in 2026

**Role:** Main Blog
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 02/06 - 8 Best Offline Notes Apps for Android in 2026` (work: re-keyword)
**Primary keyword:** `best offline notes app android`
**Secondary keywords:** `offline notes app`, `offline note taking app`
**LSI keywords:** offline notes app android, airplane mode, no account, local storage, Notally, Markor, Joplin, F-Droid, sync later, battery
**Search intent:** commercial investigation
**Atomic Notes URL:** `/blog/best-offline-notes-apps-android`
**Angle:** Android listicle, Atomic Notes first, each app tested in airplane mode.
**Why this is a Main Blog:** Captures Android users with practical install intent while reinforcing Atomic Notes' offline/local-first positioning.

### Support Blogs

#### L4-S1. 5 Offline Notes Apps That Do Not Require an Account

**Primary keyword:** `notes app without account`
**Secondary keywords:** `notes app without login`, `notes app no sign in`, `free notes app without login`, `notes app no sign up`
**LSI keywords:** no email required, local only, guest mode, optional sign in, Google account, device only storage, data export, backups, privacy, offline first
**Source status:** New
**Platform:** Medium
**Search intent:** commercial investigation
**Purpose:** Account-free apps for privacy-conscious users. Be honest that Atomic Notes needs a Google account, so it isn't on this list.
**Required destination link:** `/blog/best-offline-notes-apps-android`

#### L4-S2. Does Google Keep Work Offline? 6 Popular Notes Apps Tested Without Internet

**Original plan title:** 7 F-Droid Offline Notes Apps Worth Trying in 2026
**Primary keyword:** `does google keep work offline`
**Secondary keywords:** `does notion work offline`, `does obsidian work offline`, `does notion work without internet`, `does obsidian work without internet`
**LSI keywords:** offline mode, cached notes, sync on reconnect, Notion offline pages, Obsidian vault, Apple Notes offline, OneNote offline, airplane mode, conflict, local first
**Source status:** New
**Platform:** Medium
**Search intent:** informational / comparison
**Purpose:** Hands-on airplane-mode tests of Google Keep, Notion, Obsidian, Apple Notes, OneNote, and Atomic Notes, with dates.
**Required destination link:** `/blog/best-offline-notes-apps-android`
**Changed from the original plan:** The original was a second F-Droid listicle that duplicated P2-S3. Replaced with three 'does X work offline' questions that each show demand in all three engines.

#### L4-S3. 5 Plain Text and Markdown Notes Apps for Android That Work Fully Offline

**Original plan title:** How to Test Whether a Notes App Really Works Offline: 8 Checks
**Primary keyword:** `markdown notes app android`
**Secondary keywords:** `plain text notes app`, `markdown notes app`, `plain text note taking`, `android plain text notes app`
**LSI keywords:** Markor, Obsidian mobile, txt files, folder sync, Syncthing, portability, offline editing, file manager, open formats, front matter
**Source status:** New
**Platform:** DEV Community
**Search intent:** commercial investigation
**Purpose:** File-based Android editors that never need a server. The offline-test checklist moves into L3 and L3-S2.
**Required destination link:** `/blog/best-offline-notes-apps-android`
**Changed from the original plan:** 'test offline notes app' shows no demand in any engine. The test checklist now lives in L3 and L3-S2.

### Internal Link Targets

• Link to the Atomic Notes by DevBehindYou hub (`/blog/atomic-notes-by-devbehindyou`) when Atomic Notes is discussed.
• Contextual Main Blog links: L3, L2, P2.
• Link to the official GitHub repository when architecture or source claims need verification.

---

## L5. 4 Layers Behind Atomic Notes: How a Local First Notes App Actually Works

**Role:** Main Blog
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 03/05 - 4 Layers Behind Atomic Notes` (work: re-keyword)
**Primary keyword:** `local first architecture`
**Secondary keywords:** `local first app architecture`, `atomic notes architecture`
**LSI keywords:** Flutter, Hive CE, Hono, MongoDB metadata, Google Drive API, AES-256-GCM, Argon2id, sync engine, request id replay, user owned cloud storage
**Search intent:** technical informational + branded
**Atomic Notes URL:** `/blog/atomic-notes-architecture` (current draft slug `4-layers-atomic-notes-architecture`, change it before first publish)
**Angle:** The device, sync server, user's Drive, and optional vault, with what each layer can and can't see.
**Why this is a Main Blog:** Strong entity-building and trust article. Explains local Hive storage, optional client-side encryption, server/metadata responsibilities, and user-owned Google Drive storage.
**Changed from the original plan:** 'local first notes architecture' shows no demand. 'local first architecture' shows demand in all three engines.

### Support Blogs

#### L5-S1. How Atomic Notes Sync Works in 6 Steps: From Local Hive to Your Google Drive

**Primary keyword:** `local first sync`
**Secondary keywords:** `local first sync engine`, `how does sync work`, `hive database flutter`, `flutter hive`
**LSI keywords:** dirty flag, push queue, retry backoff, idempotency, transaction, Drive write, pull pagination, per-user lock, base version, conflict copy
**Source status:** New
**Platform:** DEV Community
**Search intent:** technical informational
**Purpose:** The sync path in plain language, with a diagram and failure-state caveats.
**Required destination link:** `/blog/atomic-notes-architecture`

#### L5-S2. Why Atomic Notes Uses Your Google Drive Instead of a Database for Note Content

**Original plan title:** Why Atomic Notes Stores Note Content in Your Google Drive, Not Its Database
**Primary keyword:** `google drive as database`
**Secondary keywords:** `use google drive as database`, `drive.file scope`, `google drive file scope`, `google drive database app`
**LSI keywords:** Google Drive API, OAuth scopes, appDataFolder, .atomic files, My-Atomic-Notes folder, metadata server, MongoDB Atlas, rate limits, file revisions, user ownership
**Source status:** New
**Platform:** Hashnode
**Search intent:** technical informational
**Purpose:** Drive as the content store, MongoDB for metadata only, the drive.file scope, and the tradeoffs (rate limits, latency).
**Required destination link:** `/blog/atomic-notes-architecture`

#### L5-S3. How Atomic Notes Handles Offline Edits, Retries, and Sync Conflicts

**Primary keyword:** `sync conflict`
**Secondary keywords:** `sync conflict resolution`, `what is a conflicted copy`, `conflicted copy meaning`, `crdt local first`
**LSI keywords:** base version, note_conflict, last write wins, three-way merge, CRDT, vector clocks, tombstones, stale deletes, idempotency key, conflict copy UX
**Source status:** New
**Platform:** DEV Community
**Search intent:** technical informational
**Purpose:** Base versions, refused stale edits, conflict copies, replay-safe retries.
**Required destination link:** `/blog/atomic-notes-architecture`

### Internal Link Targets

• Link to the Atomic Notes by DevBehindYou hub (`/blog/atomic-notes-by-devbehindyou`) when Atomic Notes is discussed.
• Contextual Main Blog links: L1, S1, P5.
• Link to the official GitHub repository when architecture or source claims need verification.

---

# SECURITY

## S1. Encrypted Notes Explained: T2T vs End to End Encryption

**Role:** Main Blog
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 01/Encrypted Notes Explained - T2T vs End-to-End` (work: re-keyword)
**Primary keyword:** `encrypted notes`
**Secondary keywords:** `end to end encryption explained`, `what is end to end encryption`
**LSI keywords:** transport encryption vs end to end encryption, T2T, TLS, AES-256-GCM, Argon2id, recovery phrase, key derivation, ciphertext, optional vault, threat model
**Search intent:** informational / definition
**Atomic Notes URL:** `/blog/encrypted-notes-explained` (current draft slug `encrypted-notes-t2t-vs-end-to-end`, change it before first publish)
**Angle:** What 'encrypted' means for a note, the T2T vs E2E split, and Atomic Notes' optional vault, labeled optional.
**Why this is a Main Blog:** Core security pillar that can define terminology clearly and establish Atomic Notes' precise use of optional E2E.
**Changed from the original plan:** The plan gave 'end to end encrypted notes' to S1, S2, and S4, and 'encrypted notes app' to S1 and S4. Each now has one owner: S2 owns the commercial 'app' forms.

### Support Blogs

#### S1-S1. HTTPS vs Encryption at Rest vs E2EE: 5 Differences You Should Know

**Primary keyword:** `encryption in transit vs at rest`
**Secondary keywords:** `https vs end to end encryption`, `tls vs end to end encryption`, `encryption at rest`, `encryption at rest vs end to end`
**LSI keywords:** TLS certificates, disk encryption, provider keys, server access, data in use, key management, ciphertext, plaintext exposure, threat model, compliance
**Source status:** New
**Platform:** DEV Community
**Search intent:** comparison
**Purpose:** Transport, storage, and client-side encryption separated, with who can read the data at each point.
**Required destination link:** `/blog/encrypted-notes-explained`

#### S1-S2. Who Holds the Encryption Key? Zero Knowledge Encryption Explained in 6 Questions

**Original plan title:** Who Holds the Encryption Key? 6 Questions Before Trusting an Encrypted Notes App
**Primary keyword:** `zero knowledge encryption`
**Secondary keywords:** `zero knowledge vs end to end encryption`, `zero knowledge encryption meaning`, `zero knowledge encryption cloud storage`, `encryption key management`
**LSI keywords:** key custody, master password, key derivation function, recovery key, provider access, server verifier, password manager model, security audit, client side keys, key escrow
**Source status:** New
**Platform:** Medium
**Search intent:** informational
**Purpose:** Key custody as the center of every encryption claim, and when 'zero knowledge' is accurate.
**Required destination link:** `/blog/encrypted-notes-explained`
**Changed from the original plan:** 'encryption key ownership notes' shows no demand. 'zero knowledge encryption' shows demand in all three engines and asks the same question.

#### S1-S3. Client-Side Encryption Explained: What Happens Before a Note Reaches the Cloud

**Primary keyword:** `client side encryption`
**Secondary keywords:** `what is client side encryption`, `client side vs server side encryption`, `client side encryption example`, `what is server side encryption`
**LSI keywords:** Web Crypto API, AES-GCM, nonce, key derivation, envelope encryption, ciphertext upload, Google Workspace CSE, S3 client side encryption, plaintext boundary, salt
**Source status:** New
**Platform:** DEV Community
**Search intent:** technical informational
**Purpose:** The encryption and decryption boundary in plain language, with the Atomic Notes vault as a worked example.
**Required destination link:** `/blog/encrypted-notes-explained`

### Internal Link Targets

• Link to the Atomic Notes by DevBehindYou hub (`/blog/atomic-notes-by-devbehindyou`) when Atomic Notes is discussed.
• Contextual Main Blog links: S4, S2, L5.
• Link to the official GitHub repository when architecture or source claims need verification.

---

## S2. 5 Best End to End Encrypted Notes Apps in 2026 for Private Notes

**Role:** Main Blog
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 02/05 - 5 Best End to End Encrypted Notes Apps in 2026` (work: re-keyword)
**Primary keyword:** `best encrypted notes app`
**Secondary keywords:** `end to end encrypted notes app`, `most secure notes app`
**LSI keywords:** encrypted notes app, best secure notes app, E2EE notes app, Standard Notes, Notesnook, audited encryption, key ownership, recovery options, metadata, default encryption
**Search intent:** commercial investigation
**Atomic Notes URL:** `/blog/best-end-to-end-encrypted-notes-apps`
**Angle:** Listicle, Atomic Notes first with its vault labeled optional, compared on keys, recovery, metadata, and audits.
**Why this is a Main Blog:** High-intent comparison cluster where technical accuracy, key ownership, recovery, and metadata can differentiate Atomic Notes.

### Support Blogs

#### S2-S1. Standard Notes vs Notesnook vs Joplin: How Their Encryption Models Differ

**Original plan title:** 5 Open Source Encrypted Notes Apps and How Their Security Models Differ
**Primary keyword:** `notesnook vs standard notes`
**Secondary keywords:** `standard notes vs joplin`, `notesnook vs joplin`, `open source encrypted notes app`, `is joplin end to end encrypted`
**LSI keywords:** XChaCha20-Poly1305, AES-256, Argon2, security audit, self hosting, sync server, free tier, web clipper, Markdown, export
**Source status:** New
**Platform:** DEV Community
**Search intent:** comparison
**Purpose:** A threat-model comparison of three open source encrypted apps. Turning it into a 'vs' piece keeps it apart from P2-S1's open source list.
**Required destination link:** `/blog/best-end-to-end-encrypted-notes-apps`

#### S2-S2. Is Your Notes App Encrypted? Apple Notes, Google Keep, Samsung Notes, and Obsidian Checked

**Original plan title:** 7 Features to Compare Before Choosing an Encrypted Notes App
**Primary keyword:** `is the notes app encrypted`
**Secondary keywords:** `is obsidian encrypted`, `is google keep encrypted`, `are samsung notes encrypted`, `is apple notes end to end encrypted`
**LSI keywords:** Advanced Data Protection, locked notes, Samsung Cloud, Google account encryption, Obsidian Sync, OneNote password sections, device encryption, iCloud, storage encryption, default settings
**Source status:** New
**Platform:** Medium
**Search intent:** informational
**Purpose:** Plain, sourced answers on default encryption for the apps people already use.
**Required destination link:** `/blog/best-end-to-end-encrypted-notes-apps`
**Changed from the original plan:** The original checklist duplicated S1-S2 (questions before trusting an encrypted app). Replaced with brand questions that each show demand.

#### S2-S3. Notes App With Lock vs Encrypted Notes: 5 Differences Android Users Should Know

**Original plan title:** Encrypted Notes on Android: 6 Questions to Ask Before You Sync
**Primary keyword:** `notes app with lock`
**Secondary keywords:** `notes app with lock android`, `best note taking app with lock`, `can you lock the notes app`, `notes app with lock feature`
**LSI keywords:** biometric lock, PIN lock, app lock vs encryption, FLAG_SECURE, screenshot blocking, encrypted vault, device encryption, Android Keystore, shoulder surfing, lock screen
**Source status:** New
**Platform:** Medium
**Search intent:** comparison
**Purpose:** Many users think a PIN lock is encryption. What each protects against, with Atomic Notes' biometric lock and optional vault as honest examples.
**Required destination link:** `/blog/best-end-to-end-encrypted-notes-apps`
**Changed from the original plan:** 'encrypted notes Android' has a commercial SERP that overlaps P2 and S2. 'notes app with lock' shows demand in all three engines and covers a common misunderstanding.

### Internal Link Targets

• Link to the Atomic Notes by DevBehindYou hub (`/blog/atomic-notes-by-devbehindyou`) when Atomic Notes is discussed.
• Contextual Main Blog links: S1, P2, S4.
• Link to the official GitHub repository when architecture or source claims need verification.

---

## S3. 5 Dangerous Consequences of Storing Passwords in an Insecure Notes App

**Role:** Main Blog
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 03/02 - 5 Dangers of Storing Passwords in a Notes App` (work: re-keyword)
**Primary keyword:** `storing passwords in notes app`
**Secondary keywords:** `is it safe to store passwords in notes`, `should i keep passwords in notes`
**LSI keywords:** password manager, credential theft, account takeover, identity theft, reused passwords, plaintext passwords, is it safe to store passwords in google keep, is samsung notes safe for passwords, recovery email compromise, financial account security
**Search intent:** informational / problem-solution
**Atomic Notes URL:** `/blog/storing-passwords-in-notes-app` (current draft slug `5-risks-storing-passwords-in-notes-app`, change it before first publish)
**Angle:** Why a notes app is not a password manager. Atomic Notes is never presented as one.
**Why this is a Main Blog:** Clear high-stakes user problem with strong educational value. It can also distinguish notes apps from dedicated password managers without pretending Atomic Notes is one.
**Changed from the original plan:** 'secure password storage' was dropped. Its SERP is OWASP's developer cheat sheet on password hashing, a different intent.

### Support Blogs

#### S3-S1. Password Manager vs Notes App vs Paper: Where Should Your Passwords Live?

**Original plan title:** Password Manager vs Notes App: 7 Security Differences
**Primary keyword:** `is it safe to write passwords down`
**Secondary keywords:** `password manager vs notes app`, `safest way to store passwords`, `is it ok to write down passwords`, `is writing down passwords bad`
**LSI keywords:** NIST guidance, physical security, password notebook, passkeys, master password, autofill, breach monitoring, encrypted vault, phishing resistance, family sharing
**Source status:** New
**Platform:** Medium
**Search intent:** comparison
**Purpose:** Three storage methods compared on theft, loss, phishing, sharing, and recovery.
**Required destination link:** `/blog/storing-passwords-in-notes-app`
**Changed from the original plan:** 'password manager vs notes app' shows no autocomplete demand, so it stays as a secondary. The paper question shows demand and widens the comparison.

#### S3-S2. Where to Store 2FA Backup Codes, Recovery Phrases, and Other Secrets

**Original plan title:** 5 Types of Secrets You Should Not Store in Ordinary Plaintext Notes
**Primary keyword:** `where to store 2fa backup codes`
**Secondary keywords:** `2fa backup codes`, `where to store seed phrase`, `where to store recovery phrase`, `where to store backup codes`
**LSI keywords:** API keys, recovery codes, crypto wallet, metal backup, password manager secure notes, offline storage, encrypted vault, identity documents, financial details, plaintext notes
**Source status:** New
**Platform:** Medium
**Search intent:** how-to
**Purpose:** Five kinds of secrets (2FA codes, recovery phrases, API keys, IDs, financial details), where each belongs, and why plaintext notes aren't it.
**Required destination link:** `/blog/storing-passwords-in-notes-app`

#### S3-S3. What Happens After One Password Is Leaked? 6 Steps in a Credential Chain

**Original plan title:** What Happens After One Password Is Exposed? 6 Steps in a Credential Chain
**Primary keyword:** `what happens if your password is leaked`
**Secondary keywords:** `what to do if password is compromised`, `credential stuffing`, `password reuse`, `what to do if your password is in a data breach`
**LSI keywords:** Have I Been Pwned, account takeover chain, recovery email, SIM swap, two factor authentication, session revoke, breach notification, OWASP, lateral access, password manager
**Source status:** New
**Platform:** WordPress
**Search intent:** informational / how-to
**Purpose:** Reuse, stuffing, recovery takeover, financial exposure, and the response steps that break the chain.
**Required destination link:** `/blog/storing-passwords-in-notes-app`

### Internal Link Targets

• Link to the Atomic Notes by DevBehindYou hub (`/blog/atomic-notes-by-devbehindyou`) when Atomic Notes is discussed.
• Contextual Main Blog links: P3, S5, S1.
• Link to the official GitHub repository when architecture or source claims need verification.

---

## S4. 5 Reasons "Your Data Is Encrypted" Does Not Automatically Mean Your Notes Are Private

**Role:** Main Blog
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 03/08 - 5 Reasons Encrypted Is Not Private` (work: re-keyword)
**Primary keyword:** `how does encryption protect privacy`
**Secondary keywords:** `encryption and privacy`, `encrypted notes privacy`
**LSI keywords:** transport encryption, provider held keys, metadata, analytics, account recovery, key custody, Advanced Data Protection, encryption marketing, server side keys, threat model
**Search intent:** informational
**Atomic Notes URL:** `/blog/encrypted-notes-privacy` (current draft slug `5-reasons-encryption-does-not-guarantee-notes-privacy`, change it before first publish)
**Angle:** Decoding vague encryption marketing: transit only, provider keys, metadata, tracking, recovery.
**Why this is a Main Blog:** Corrects vague encryption marketing and creates strong internal links to E2EE, metadata, analytics, and recovery-model content.
**Changed from the original plan:** 'encrypted notes privacy' shows no demand, so it stays as the title-match secondary. The question form carries the demand. 'encrypted notes app' and 'end to end encrypted notes' now belong to S2. Remove the FAQ 'Is an encrypted notes app automatically private?', which also appears in S4-S1.

### Support Blogs

#### S4-S1. Privacy by Design for Notes Apps: 6 Layers Beyond Encryption

**Original plan title:** Encryption Alone Does Not Make a Notes App Private
**Primary keyword:** `privacy by design`
**Secondary keywords:** `privacy by design principles`, `privacy by design meaning`, `privacy by design and by default`, `privacy by design framework`
**LSI keywords:** Ann Cavoukian, GDPR Article 25, storage location, telemetry, AI training, business model, defaults, collect less, transparency, full lifecycle protection
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 01/Encryption Alone Does Not Make a Notes App Private` (work: rewrite)
**Platform:** Medium
**Search intent:** informational / framework
**Purpose:** Keeps the existing six-layer framework (storage, E2E, metadata, telemetry, AI, business model) and reframes it as privacy by design so it stops competing with S4's thesis.
**Required destination link:** `/blog/encrypted-notes-privacy`
**Changed from the original plan:** As planned, this support post argued the same thesis as its Main Blog and shared an FAQ with it, which is a duplicate-content risk. The privacy-by-design framing has demand in all three engines and a distinct intent.

#### S4-S2. Metadata Privacy: 7 Things End-to-End Encryption Can and Cannot Hide

**Original plan title:** Metadata Privacy: 7 Things E2EE Can and Cannot Hide
**Primary keyword:** `metadata privacy`
**Secondary keywords:** `metadata leakage`, `e2ee metadata`, `traffic analysis`, `end to end encryption metadata`
**LSI keywords:** sealed sender, file sizes, timestamps, IP address, sync events, padding, access patterns, server logs, minimal metadata, encrypted filenames
**Source status:** New
**Platform:** DEV Community
**Search intent:** informational / technical
**Purpose:** The boundary between content confidentiality and what servers still observe.
**Required destination link:** `/blog/encrypted-notes-privacy`

#### S4-S3. Account Recovery vs Zero Knowledge: 5 Security Tradeoffs

**Primary keyword:** `zero knowledge account recovery`
**Secondary keywords:** `lost recovery key`, `reset end to end encryption`, `recover end to end encryption`, `zero knowledge recovery`
**LSI keywords:** recovery phrase, Advanced Data Protection, recovery contact, key escrow, support reset, data loss, 6-word phrase, trusted device, account takeover, social recovery
**Source status:** New
**Platform:** Substack
**Search intent:** informational / opinion
**Purpose:** Why recovery convenience changes who can read your data, and what a lost recovery key really costs.
**Required destination link:** `/blog/encrypted-notes-privacy`

### Internal Link Targets

• Link to the Atomic Notes by DevBehindYou hub (`/blog/atomic-notes-by-devbehindyou`) when Atomic Notes is discussed.
• Contextual Main Blog links: S1, P5, P1.
• Link to the official GitHub repository when architecture or source claims need verification.

---

## S5. 7 Things to Check Before Moving Your Private Notes to a New App

**Role:** Main Blog
**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 03/10 - 7 Things to Check Before Moving Your Notes` (work: re-keyword)
**Primary keyword:** `switch notes app`
**Secondary keywords:** `migrate notes to a new app`, `move notes to another app`
**LSI keywords:** notes migration, data export, export format, attachments, note counts, rollback copy, account recovery, offline notes, cloud storage provider, secure data migration
**Search intent:** migration / decision-stage
**Atomic Notes URL:** `/blog/switch-notes-app` (current draft slug `7-things-check-before-switching-notes-app`, change it before first publish)
**Angle:** Exports, backups, encryption, storage, offline access, recovery, and shutdown risk, checked before you move.
**Why this is a Main Blog:** Captures users at the moment of switching tools and combines backups, exports, encryption, cloud storage, recovery, offline access, and service-exit risk.
**Changed from the original plan:** The old primary 'secure notes app' has an app-store SERP, the wrong intent for a migration guide, and it was also P1's secondary. Autocomplete for migration phrases is weak, so expect low but well-matched traffic.

### Support Blogs

#### S5-S1. 7 Steps to Export and Verify Your Notes Before Switching Apps

**Primary keyword:** `export notes to markdown`
**Secondary keywords:** `export google keep notes`, `export apple notes to markdown`, `convert notes to markdown`, `export google keep notes to markdown`
**LSI keywords:** Google Takeout, ENEX, JSON export, attachments, front matter, file names, note counts, internal links, Obsidian importer, checksum
**Source status:** New
**Platform:** Medium
**Search intent:** how-to
**Purpose:** Export to open formats, then verify counts, attachments, and links before anything is deleted.
**Required destination link:** `/blog/switch-notes-app`

#### S5-S2. How to Export Encrypted Notes From Standard Notes, Notesnook, and Joplin Without Losing Access

**Original plan title:** How to Migrate Encrypted Notes Without Losing Access: 6 Checks
**Primary keyword:** `standard notes export`
**Secondary keywords:** `joplin export`, `notesnook export`, `joplin export to markdown`, `standard notes export markdown`
**LSI keywords:** decrypted export, encrypted backup, recovery key, attachments, JEX format, re-encryption, import, verification, rollback copy, plaintext exposure
**Source status:** New
**Platform:** Medium
**Search intent:** how-to
**Purpose:** Decrypted vs encrypted exports, recovery material, attachments, and rollback copies, using real export menus.
**Required destination link:** `/blog/switch-notes-app`
**Changed from the original plan:** 'migrate encrypted notes' shows no demand in any engine. The app-specific export questions show demand and cover the same task.

#### S5-S3. Pocket, Omnivore, Evernote: What Happens to Your Notes When an App Shuts Down

**Original plan title:** What Happens to Your Notes If an App Shuts Down? 6 Questions to Ask First
**Primary keyword:** `pocket shutting down`
**Secondary keywords:** `omnivore shutting down`, `is evernote shutting down`, `pocket shutting down alternative`, `evernote shutting down`
**LSI keywords:** export window, shutdown notice, data deletion date, account dependency, offline copy, open formats, service exit, acquisition, read-it-later, portability
**Source status:** New
**Platform:** Substack
**Search intent:** informational / news-driven
**Purpose:** Real shutdowns as case studies (verify dates and export windows at writing time), then six questions to ask any app today.
**Required destination link:** `/blog/switch-notes-app`
**Changed from the original plan:** 'notes app shutdown data' shows no demand. Real shutdown events show demand and make the risk concrete.

### Internal Link Targets

• Link to the Atomic Notes by DevBehindYou hub (`/blog/atomic-notes-by-devbehindyou`) when Atomic Notes is discussed.
• Contextual Main Blog links: S3, P1, L1.
• Link to the official GitHub repository when architecture or source claims need verification.

---

# Brand Hub and Side Cluster

## HUB. Atomic Notes by DevBehindYou: Source-Available, Local First and Private by Design

**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 01/Atomic Notes - Local-First and Private by Design` (work: update)
**Primary keyword:** `atomic notes app`
**Secondary keywords:** `atomic notes by devbehindyou`, `atomic notes android`
**LSI keywords:** local first notes app for Android, user owned Google Drive, optional end to end vault, source-available license, no AI features, no ads or trackers, Atomic Energy, GitHub releases, SHA-256 checksums, DevBehindYou
**URL:** `/blog/atomic-notes-by-devbehindyou`
**Note:** The plan's H1 said 'Open Source'. Atomic Notes has been source-available since September 28, 2026, so the H1 now says Source-Available. 'atomic notes' alone is owned by the Zettelkasten concept and by Atomic Blend's unrelated Atomic Notes app, so the hub targets the branded forms.

## ECON. Why Atomic Notes Uses Energy Instead of a Subscription

**Source status:** Existing draft: `Atomic Notes Blogs/Blog List 01/Why Atomic Notes Uses Energy Instead of a Subscription` (work: re-keyword)
**Primary keyword:** `notes app without subscription`
**Secondary keywords:** `no subscription notes app`, `free notes app no subscription`
**LSI keywords:** Atomic Energy, Atomic Coins, sync cost, daily energy, free tier, server costs, Google Drive API, sustainable software, no ads, pay per sync
**URL:** `/blog/why-atomic-notes-uses-energy`

# Recommended Main-Blog Cross-Link Graph

| Main | Contextual Main-Blog Links |
|---|---|
| P1 | P5, S4, P2 |
| P2 | P1, L2, S2 |
| P3 | P1, S3, S5 |
| P4 | P5, S4, P2 |
| P5 | P1, S4, P4 |
| L1 | L3, L5, P5 |
| L2 | L1, L4, P2 |
| L3 | L1, L4, L5 |
| L4 | L3, L2, P2 |
| L5 | L1, S1, P5 |
| S1 | S4, S2, L5 |
| S2 | S1, P2, S4 |
| S3 | P3, S5, S1 |
| S4 | S1, P5, P1 |
| S5 | S3, P1, L1 |

Use these as suggestions, not exact-match link rules. Link only where the section genuinely helps the reader.

# Support Blog Publication Guidance

Choose platforms by topic fit rather than rotating mechanically.

• Medium: editorial privacy, consumer education, comparisons
• WordPress: evergreen search-focused support articles
• DEV Community: architecture, encryption, sync, engineering comparisons
• Hashnode: technical local-first and security architecture
• Substack: opinion and analysis pieces such as open source, lock-in, data ownership, and recovery tradeoffs

Do not use low-quality publishing sites solely because they allow a backlink.
