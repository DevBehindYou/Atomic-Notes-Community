import { NextResponse } from "next/server";
import {
  passwordMatches,
  password2Matches,
  makeToken,
  ADMIN_COOKIE,
  COOKIE_MAX_AGE_SECONDS,
} from "@/lib/auth";

export async function POST(req: Request) {
  const body = await req
    .json()
    .catch(() => ({}) as { password?: string; password2?: string });
  // Two-key login: BOTH passwords must match. One generic error either way, so
  // a wrong first vs second key is indistinguishable to an attacker.
  if (!passwordMatches(body?.password) || !password2Matches(body?.password2)) {
    return NextResponse.json({ error: "Invalid credentials" }, { status: 401 });
  }
  const res = NextResponse.json({ ok: true });
  res.cookies.set(ADMIN_COOKIE, makeToken(), {
    httpOnly: true,
    secure: process.env.NODE_ENV === "production",
    sameSite: "lax",
    path: "/",
    maxAge: COOKIE_MAX_AGE_SECONDS,
  });
  return res;
}
