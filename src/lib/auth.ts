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
  const value = process.env.SESSION_SECRET;
  if (!value || Buffer.byteLength(value) < 32) throw new Error("SESSION_SECRET must contain at least 32 bytes");
  return value;
}

function sign(value: string): string {
  return crypto.createHmac("sha256", secret()).update(value).digest("hex");
}

export function makeToken(): string {
  const ts = Date.now().toString();
  return `${ts}.${sign(ts)}`;
}

export function tokenValid(token: string | undefined): boolean {
  if (!token || !process.env.SESSION_SECRET || Buffer.byteLength(process.env.SESSION_SECRET) < 32) return false;
  const match = /^(\d{13})\.([a-f0-9]{64})$/.exec(token);
  if (!match) return false;
  const [, ts, sig] = match;
  const age = Date.now() - Number(ts);
  if (age < 0 || age >= MAX_AGE_MS) return false;
  return crypto.timingSafeEqual(Buffer.from(sig, "hex"), Buffer.from(sign(ts), "hex"));
}

/** Read the admin session from the request cookies (server side). */
export async function isAdmin(): Promise<boolean> {
  return tokenValid((await cookies()).get(ADMIN_COOKIE)?.value);
}

function constEq(input: string | undefined | null, expected: string | undefined): boolean {
  if (!expected || typeof input !== "string" || !input) return false;
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

export function adminLoginConfigured(): boolean {
  return Boolean(process.env.ADMIN_PASSWORD && process.env.ADMIN_PASSWORD_2 && process.env.SESSION_SECRET && Buffer.byteLength(process.env.SESSION_SECRET) >= 32);
}
