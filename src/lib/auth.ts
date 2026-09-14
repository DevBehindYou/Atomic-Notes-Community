import { cookies } from "next/headers";
import crypto from "crypto";

// Minimal signed-cookie session for the secret Atomic-Controller panel. The
// admin proves knowledge of ADMIN_PASSWORD once; we then set an httpOnly,
// HMAC-signed, time-limited cookie. No password or key is ever stored client
// side. This is deliberately simple — it gates a single-operator admin panel,
// not a multi-user auth system.

export const ADMIN_COOKIE = "acb_admin";
const MAX_AGE_MS = 7 * 24 * 60 * 60 * 1000; // 7 days

function secret(): string {
  return process.env.SESSION_SECRET || "insecure-dev-secret-change-me";
}

function sign(value: string): string {
  return crypto.createHmac("sha256", secret()).update(value).digest("hex");
}

export function makeToken(): string {
  const ts = Date.now().toString();
  return `${ts}.${sign(ts)}`;
}

export function tokenValid(token: string | undefined): boolean {
  if (!token) return false;
  const [ts, sig] = token.split(".");
  if (!ts || !sig) return false;
  // Constant-time compare of the signature.
  const expected = sign(ts);
  if (
    sig.length !== expected.length ||
    !crypto.timingSafeEqual(Buffer.from(sig), Buffer.from(expected))
  ) {
    return false;
  }
  return Date.now() - Number(ts) < MAX_AGE_MS;
}

/** Read the admin session from the request cookies (server side). */
export async function isAdmin(): Promise<boolean> {
  return tokenValid((await cookies()).get(ADMIN_COOKIE)?.value);
}

function constEq(input: string | undefined | null, expected: string | undefined): boolean {
  if (!expected || !input) return false;
  const a = Buffer.from(input);
  const b = Buffer.from(expected);
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

export function passwordMatches(input: string | undefined | null): boolean {
  return constEq(input, process.env.ADMIN_PASSWORD);
}

/// Second key — the Controller requires BOTH passwords (two-screen login).
export function password2Matches(input: string | undefined | null): boolean {
  return constEq(input, process.env.ADMIN_PASSWORD_2);
}

export const COOKIE_MAX_AGE_SECONDS = MAX_AGE_MS / 1000;
