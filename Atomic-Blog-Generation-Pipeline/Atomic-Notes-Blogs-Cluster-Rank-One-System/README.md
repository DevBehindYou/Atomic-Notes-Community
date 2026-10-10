# Atomic Notes Blogs Cluster Rank One System

This folder contains the complete planning package for an AI Agent.

## Files

1. `00_ATOMIC_NOTES_AI_AGENT_MASTER_PROMPT.md`
   Full execution prompt and quality rules.

2. `01_ATOMIC_NOTES_CONTEXT_AND_EXISTING_CONTENT_AUDIT.md`
   Existing blog/post audit and decisions on Main vs Support vs side-cluster use.

3. `02_ATOMIC_NOTES_MAIN_AND_SUPPORT_TOPIC_MAP.md`
   15 Main Blogs and 45 Support Blogs across Privacy, Local First, and Security.

4. `03_ATOMIC_NOTES_SOCIAL_SUPPORT_POSTS_MATRIX.md`
   360 platform-specific social post briefs, 8 for each Support Blog.

5. `04_ATOMIC_NOTES_PROMOTION_PLAN.md`
   Publication order, linking architecture, SEO/GEO workflow, indexing, distribution, and refresh plan.

6. `05_ATOMIC_NOTES_KEYWORD_MAP.md`
   Keyword research evidence, the keyword set for all 62 URLs, the ownership index, and every change from the original plan.

7. `keyword-registry.json`
   The single source of truth for titles, keywords, platforms, and slugs. Files 02, 03, and 05 are generated from it.

8. `research/autocomplete-evidence.json`
   Raw demand evidence: Google, Bing, and DuckDuckGo autocomplete results for 390 probes (October 7, 2026).

## Tools (run from `Atomic-Blog-Generation-Pipeline/`)

• `npm run cluster:check`: keyword counts, one owner per keyword, no LSI term stealing another page's target. Must pass.
• `npm run cluster:overlap`: duplicate-text scan across every article in `Atomic Notes Blogs/` and `content/blog/`.
• `node scripts/cluster-check.mjs --draft <file.md>`: one draft against the registry and the corpus. Run before publishing.
• `npm run cluster:docs`: rebuilds files 02, 03, and 05 after a registry change.

## Core Campaign Totals

• 15 Main Blogs  
• 45 Support Blogs  
• 360 social support posts  
• 420 core campaign assets  
• plus the Atomic Notes brand/entity hub and the Atomic Energy side cluster

## Important

Atomic Notes is **source-available**, never "open source". New Google sign-ins are limited to test users until the OAuth consent screen is published, so see the launch gate in file 04 before sending traffic.

The plan is a strategy, not a ranking guarantee.

Every changing product, competitor, privacy, security, AI, pricing, or platform claim must be freshly verified before publication.
