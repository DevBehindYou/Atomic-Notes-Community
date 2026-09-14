# Atomic Community Base

The community platform for **Atomic Notes** — development updates, features, and
app downloads — plus the secret **Atomic-Controller** admin panel for managing
notifications and user Energy/Coins.

Built with **Next.js 14 (App Router)**, **TypeScript**, **Tailwind CSS**, and
the **Atomic Notes Server** (Node.js/MongoDB) as its backend, deployed on
**Vercel**. Brand-matched to the app's Technical Editorial system (ink
`#15171B`, paper `#F4F5F1`, signal `#3A2FF0`).

## Structure

- `/` — public community home: hero, current dev phase, features, roadmap, download.
- `/updates` — public Notification Center feed (active announcements).
- `/controller` — **secret** admin panel (password-gated). CRUD notifications and
  adjust a user's Atomic Coins / Energy.
- `/api/controller/*` — server route handlers. All admin routes check an
  HMAC-signed httpOnly session cookie, then call the Atomic Notes Server's
  `/api/admin/*` endpoints (server-only) to read or write.

## Security model

- Community holds **no database credentials at all** — it calls the Atomic
  Notes Server's admin API instead, authenticated with a static
  `ADMIN_API_KEY` shared between the two projects (`src/lib/atomicServer.ts`,
  route handlers only). Never `NEXT_PUBLIC_`, never sent to the browser.
- The public site reads notifications **server-side** (server components),
  via the Server's separate, unauthenticated `/api/public/notifications/active`
  endpoint — so no privileged key reaches the client, and the public read path
  is a different, lower-trust endpoint from the admin one.
- The Controller is gated by `ADMIN_PASSWORD`; a successful login sets a
  time-limited, HMAC-signed httpOnly cookie (`SESSION_SECRET`). Every admin API
  re-checks it, then relies on `ADMIN_API_KEY` to authorize the call to the
  Server — two separate, deliberately unrelated trust boundaries (see the
  Server's `src/middleware/adminAuth.ts`).
- Notification writes and Energy/Coin adjustments are logged to `energy_ledger`
  (adjustments) on the Server, and are only reachable via the admin API — the
  app itself has no path to them with a user session.

## Local development

Use Node.js 22. GitHub Actions runs `npm ci`, `npm audit --audit-level=high`,
`npx tsc --noEmit`, `npm run build`, and `npm run test:smoke`.
The smoke test starts its own localhost production server with test credentials
and no backend connection; it checks admin authentication, blog pages, and RSS.
Run it after building. Real Server/MongoDB/Google integration needs separate checks.

The security update uses Next.js 15.5.24 and React 19. Next's nested PostCSS
is overridden to the patched root PostCSS version because Next still pins an
affected version. Keep the override until the upstream dependency is patched.

```bash
npm install
cp .env.example .env.local   # fill in real values (never commit .env.local)
npm run dev                  # http://localhost:3000
```

Environment variables (see `.env.example`):

| Var | Where | Purpose |
|---|---|---|
| `ATOMIC_SERVER_URL` | server | base URL of the Atomic Notes Server |
| `ADMIN_API_KEY` | server | must match the Server's own `ADMIN_API_KEY` |
| `ADMIN_PASSWORD` | server | Controller gate |
| `SESSION_SECRET` | server | signs the admin session cookie |
| `NEXT_PUBLIC_APK_URL` | public | download link on the home page |

## Deploy on Vercel

1. Import this repo in Vercel (framework auto-detected as Next.js).
2. Add the environment variables above in Project Settings → Environment
   Variables (mark the admin key + admin secrets for Production/Preview only).
3. Deploy. The public site is static/dynamic as needed; the Controller and its
   APIs run as serverless functions.

## Prerequisite

The Atomic Notes Server must be deployed and reachable at `ATOMIC_SERVER_URL`,
with a matching `ADMIN_API_KEY` on both projects — that server owns the
`notifications`, `atomic_users`, and `energy_ledger` MongoDB collections this
panel reads and writes.
