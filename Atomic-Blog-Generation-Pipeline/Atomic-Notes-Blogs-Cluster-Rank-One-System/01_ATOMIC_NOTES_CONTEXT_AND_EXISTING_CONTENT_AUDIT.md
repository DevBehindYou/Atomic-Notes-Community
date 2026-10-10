# Atomic Notes Content Context and Existing Asset Audit

## Purpose

This file turns the existing Atomic Notes blog and social assets into a structured 3-pillar content system.

The source files reviewed are:

• Blog List 01  
• Blog List 02  
• Blog List 03  
• Posts List 01

The existing material already contains strong coverage of local-first software, offline use, privacy, encryption, AI-free note taking, data ownership, metadata, Google Drive storage, and Atomic Notes architecture.

The strategy below does **not** discard those assets. It promotes the strongest pieces into Main Blogs, assigns narrower pieces as Support Blogs, and keeps unrelated but useful articles as side clusters.

---

# Atomic Notes Entity Context

Preferred external entity name:

**Atomic Notes by DevBehindYou**

Official site:

https://atomic-notes.devbehindyou.com/

Official repository:

https://github.com/DevBehindYou/Atomic-Notes-App-V0.2

Core positioning:

**Source-available. Local first. Private by design. ⚛️**

> The topic briefs in `../topics/` (Posts List 01 and Blog List 02 in particular) predate the September 28, 2026 license change and still say "open source" about Atomic Notes. Never copy that wording. Atomic Notes is source-available.

Current documented product themes to preserve:

• local-first note taking  
• offline access  
• optional end-to-end encryption  
• user-owned Google Drive storage for synchronized note content  
• server-managed synchronization and metadata, never note content in MongoDB (with the vault off, note text passes through the server in transit)  
• source-available code: public to read and verify, not to reuse  
• no AI features  
• no advertising-led product positioning  
• emphasis on data ownership and portability

Because product architecture changes, all exact implementation claims must be re-verified immediately before publication.

---

# Existing Blog Audit

Every existing draft lives in `../Atomic Notes Blogs/`. As of October 7, 2026 none of them is published anywhere. The keyword sets and the reason for every change are in `keyword-registry.json` and `05_ATOMIC_NOTES_KEYWORD_MAP.md`.

| Draft folder | Planned title | Decision | Campaign ID | Primary keyword | Work |
|---|---|---|---|---|---|
| `Blog List 01/Atomic Notes - Local-First and Private by Design` | Atomic Notes by DevBehindYou: Source-Available, Local First and Private by Design (draft: Atomic Notes: Local-First and Private by Design) | BRAND HUB | HUB | `atomic notes app` | Update H1, facts and entity links |
| `Blog List 01/Best Private Notes Apps in 2026` | Best Open Source Notes Apps for Privacy in 2026 (draft: Best Private Notes Apps in 2026: 5 Picks Compared) | SUPPORT | P2-S1 | `best open source notes app` | Rewrite to the new angle |
| `Blog List 01/Encrypted Notes Explained - T2T vs End-to-End` | Encrypted Notes Explained: T2T vs End to End Encryption | MAIN | S1 | `encrypted notes` | Keep the article, re-keyword to the registry |
| `Blog List 01/Encryption Alone Does Not Make a Notes App Private` | Privacy by Design for Notes Apps: 6 Layers Beyond Encryption (draft: Encryption Alone Does Not Make a Notes App Private) | SUPPORT | S4-S1 | `privacy by design` | Rewrite to the new angle |
| `Blog List 01/Offline Notes Apps - Why Notes Should Work Offline` | Offline Notes Apps: Why Your Notes Should Work Without Internet | MAIN | L3 | `notes app without internet` | Keep the article, re-keyword to the registry |
| `Blog List 01/What Happens to Your Notes When the Cloud Goes Down` | What Happens to Your Notes When the Cloud Goes Down? | SUPPORT | L3-S1 | `cloud outage` | Keep the article, re-keyword to the registry |
| `Blog List 01/What Is a Local-First Notes App` | What Is a Local First Notes App and Why Does It Matter? | MAIN | L1 | `local first notes app` | Keep the article, re-keyword to the registry |
| `Blog List 01/Why Atomic Notes Uses Energy Instead of a Subscription` | Why Atomic Notes Uses Energy Instead of a Subscription | SIDE CLUSTER | ECON | `notes app without subscription` | Keep the article, re-keyword to the registry |
| `Blog List 01/Why Privacy Software Should Be Open Source` | Is Open Source More Secure? 6 Things Public Source Code Lets You Verify (draft: Why Privacy Software Should Be Open Source) | SUPPORT | P1-S3 | `is open source more secure` | Rewrite to the new angle |
| `Blog List 01/Zero Telemetry - Why Your Notes App Should Know Less About You` | Zero Telemetry: Why Your Notes App Should Know Less About You | SUPPORT | P5-S1 | `zero telemetry` | Keep the article, re-keyword to the registry |
| `Blog List 02/01 - 7 Best Note Taking Apps Without AI in 2026` | 7 Best Note Taking Apps Without AI in 2026 | MAIN | P4 | `note taking app without ai` | Promoted from Support to Main |
| `Blog List 02/02 - 7 Best Privacy First Note Taking Apps for Android in 2026` | 7 Best Privacy First Note Taking Apps for Android in 2026 | MAIN | P2 | `private notes app android` | Keep the article, re-keyword to the registry |
| `Blog List 02/03 - 7 Best Google Keep Alternatives for Privacy in 2026` | 7 Best Google Keep Alternatives for Privacy in 2026 | SUPPORT | P2-S2 | `google keep alternatives` | Keep the article, re-keyword to the registry |
| `Blog List 02/04 - 6 Best Local First Note Taking Apps in 2026` | 6 Best Local First Note Taking Apps in 2026 That Keep Your Data Yours | MAIN | L2 | `local first note taking apps` | Keep the article, re-keyword to the registry |
| `Blog List 02/05 - 5 Best End to End Encrypted Notes Apps in 2026` | 5 Best End to End Encrypted Notes Apps in 2026 for Private Notes | MAIN | S2 | `best encrypted notes app` | Keep the article, re-keyword to the registry |
| `Blog List 02/06 - 8 Best Offline Notes Apps for Android in 2026` | 8 Best Offline Notes Apps for Android in 2026 | MAIN | L4 | `best offline notes app android` | Keep the article, re-keyword to the registry |
| `Blog List 02/07 - 3 Best Private Notion Alternatives in 2026` | 3 Best Private Notion Alternatives for Local First Notes in 2026 | SUPPORT | L2-S1 | `local notion alternative` | Keep the article, re-keyword to the registry |
| `Blog List 03/01 - 10 Privacy Mistakes People Make With Notes Apps in 2026` | 10 Privacy Mistakes People Make With Notes Apps in 2026 | MAIN | P3 | `notes app security` | Keep the article, re-keyword to the registry |
| `Blog List 03/02 - 5 Dangers of Storing Passwords in a Notes App` | 5 Dangerous Consequences of Storing Passwords in an Insecure Notes App | MAIN | S3 | `storing passwords in notes app` | Keep the article, re-keyword to the registry |
| `Blog List 03/03 - 6 Questions Before Giving an AI Notes App Your Thoughts` | 6 Questions You Should Ask Before Giving an AI Notes App Your Private Thoughts | SUPPORT | P4-S1 | `ai note taking privacy` | Moved from Main to Support |
| `Blog List 03/04 - 8 Pieces of Data a Notes App May Know About You` | 8 Pieces of Data a Notes App May Know About You Even Without Reading Your Notes | MAIN | P5 | `notes app metadata` | Keep the article, re-keyword to the registry |
| `Blog List 03/05 - 4 Layers Behind Atomic Notes` | 4 Layers Behind Atomic Notes: How a Local First Notes App Actually Works | MAIN | L5 | `local first architecture` | Keep the article, re-keyword to the registry |
| `Blog List 03/06 - 9 Privacy Red Flags Before Trusting Any Notes App` | 9 Privacy Red Flags to Check Before Trusting Any Notes App in 2026 | MAIN | P1 | `notes app privacy` | Keep the article, re-keyword to the registry |
| `Blog List 03/07 - 7 Ways Your Notes App Could Expose You` | 7 Ways Your Notes App Could Expose More About You Than You Realize | SUPPORT | P1-S1 | `is the notes app secure` | Keep the article, re-keyword to the registry |
| `Blog List 03/08 - 5 Reasons Encrypted Is Not Private` | 5 Reasons "Your Data Is Encrypted" Does Not Automatically Mean Your Notes Are Private | MAIN | S4 | `how does encryption protect privacy` | Keep the article, re-keyword to the registry |
| `Blog List 03/09 - 3 Places Your Notes Can Live` | Local Storage vs Cloud Storage for Notes: 3 Places Your Notes Can Live (draft: 3 Places Your Notes Can Live and Why the Difference Matters for Privacy) | SUPPORT | L1-S1 | `local storage vs cloud storage` | Keep the article, re-keyword to the registry |
| `Blog List 03/10 - 7 Things to Check Before Moving Your Notes` | 7 Things to Check Before Moving Your Private Notes to a New App | MAIN | S5 | `switch notes app` | Keep the article, re-keyword to the registry |

---

# Why These 15 Became Main Blogs

The Main Blogs were selected because together they cover three complementary intent layers:

## Privacy

• evaluation and red flags  
• product comparison  
• common mistakes  
• AI privacy  
• metadata/data collection

## Local First

• category definition  
• product comparison  
• offline behavior  
• Android offline comparison  
• Atomic Notes architecture

## Security

• encryption fundamentals  
• encrypted app comparison  
• password-storage risk  
• limits of vague encryption claims  
• secure migration

This gives the site a mix of:

• informational queries  
• commercial investigation queries  
• comparison queries  
• branded architecture queries  
• problem-aware security queries  
• decision-stage migration queries

---

# Existing Social Asset Audit

`Posts List 01` already contains 40 platform-specific posts across X, Reddit, Patreon, and Ko-fi.

Do not discard them.

Map them into the new campaigns as follows:

| Existing Social Theme | Best Cluster Use |
|---|---|
| Your Notes Should Work Without Permission | L3 / L1 |
| No AI Reading Your Notes | P4 / P4-S1 |
| Your Own Google Drive | L5 / L1 |
| Optional E2E | S1 / S4 |
| What Local First Means | L1 |
| Atomic Energy | Economics side cluster |
| Why Public Code Matters (X 07) | P1-S3 |
| Metadata Matters Too | P5 |
| The Goal Is Simpler Software | P4 / brand hub |
| Build In Public | Brand / architecture |
| Google Drive ownership Reddit discussion | L5 |
| Local-first definition Reddit discussion | L1 |
| "Encrypted" is misleading Reddit discussion | S1 / S4 |
| Privacy red flags Reddit discussion | P1 |
| Metadata retention Reddit discussion | P5 |
| Why Atomic Notes Saves Locally First | L1 / L3 |
| Why Your Own Google Drive Is Part of Atomic Notes | L5 |
| Encryption Is Not One Checkbox | S1 |
| Invisible Work Behind One Sync Button | L5 |
| Why Atomic Notes Does Not Need AI to Read Your Notes | P4 |
| Private by Design | P1 / brand hub |
| Why Public Code Is Part of the Privacy Model (Patreon 09) | P1-S3 |
| Cloud Should Be a Tool, Not Owner | L1 / L5 |
| Best Privacy Feature Might Be Collecting Less | P5 |

When reusing an existing post:

• change the CTA so it points to the correct Support Blog  
• update facts and links  
• do not repost identical text across multiple networks  
• preserve the original idea but adapt the hook to the current campaign

---

# Important Cannibalization Rules

Do not create two Atomic Notes website pages targeting the same dominant query and intent. `node scripts/cluster-check.mjs` enforces this across all 62 URLs.

Examples:

• `notes app privacy` (P1, a checklist) and `private notes app android` (P2, an Android comparison) coexist because each page serves its own intent. The bare `private notes app` has an app-store SERP, so no blog page targets it.

• `notes app without internet` (L3, why offline matters) and `best offline notes app android` (L4, a listicle) coexist. L4 also owns `offline notes app`, because that SERP is commercial.

• `encrypted notes` (S1, educational) and `best encrypted notes app` (S2, commercial) coexist. This is one of the reviewed overlaps listed in `keyword-registry.json`.

If the live SERP suggests two planned Main Blogs answer the same intent, consolidate or re-angle before publishing.

---

# Existing URLs

When an existing article is already published on the Atomic Notes site:

• keep the existing URL where practical  
• update the article rather than publishing a duplicate  
• preserve internal/external links through redirects if a slug absolutely must change

When an existing article is already published externally:

• keep it as a Support Blog if it fits  
• do not duplicate it on the Atomic Notes site word-for-word  
• create a distinct Main Blog with stronger scope, or migrate deliberately with canonical/redirect handling

---

# Side Clusters to Keep

These are valuable but are not counted among the 15 Main Blogs:

## Atomic Notes Entity Hub

**Atomic Notes by DevBehindYou: Source-Available, Local First and Private by Design**

Purpose:

• brand/entity disambiguation  
• product overview  
• core architecture summary  
• official links  
• conversion/download/support path  
• internal link target from all three topical pillars

## Economics / Sustainability

**Why Atomic Notes Uses Energy Instead of a Subscription**

Purpose:

• explain Atomic Energy  
• explain why local note taking and hosted sync are economically different  
• explain sustainability without framing local note ownership as a recurring permission

These side clusters can receive links from relevant articles without stealing the primary query of the 15 Main Blogs.
