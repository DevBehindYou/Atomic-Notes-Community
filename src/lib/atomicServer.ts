// SERVER-ONLY. Replaces src/lib/supabaseAdmin.ts — Community no longer talks
// to a database directly at all; every admin operation goes through the
// Atomic Notes Server's /api/admin/* routes instead, authenticated with a
// static shared key (not a user session — see the Server's
// src/middleware/adminAuth.ts for why this is a deliberately separate trust
// boundary from Community's own /controller login).

export class AtomicServerError extends Error {
  status: number;
  constructor(message: string, status: number) {
    super(message);
    this.status = status;
  }
}

function baseUrl(): string {
  const url = process.env.ATOMIC_SERVER_URL;
  if (!url) throw new Error("ATOMIC_SERVER_URL is not set");
  return url.replace(/\/$/, "");
}

function adminKey(): string {
  const key = process.env.ADMIN_API_KEY;
  if (!key) throw new Error("ADMIN_API_KEY is not set");
  return key;
}

export function isAtomicServerConfigured(): boolean {
  return Boolean(process.env.ATOMIC_SERVER_URL && process.env.ADMIN_API_KEY);
}

async function request<T>(
  path: string,
  init?: { method?: string; body?: unknown }
): Promise<T> {
  const res = await fetch(`${baseUrl()}/api/admin${path}`, {
    method: init?.method ?? "GET",
    headers: {
      "Content-Type": "application/json",
      "x-admin-api-key": adminKey(),
    },
    body: init?.body !== undefined ? JSON.stringify(init.body) : undefined,
    cache: "no-store",
  });
  const body = await res.json().catch(() => ({}));
  if (!res.ok) {
    throw new AtomicServerError(
      (body as { error?: string })?.error ?? `http_${res.status}`,
      res.status
    );
  }
  return body as T;
}

export const atomicAdmin = {
  health: () => request<{ db: boolean; dbError: string | null; time: string }>("/health"),
  stats: () => request<{ stats: Record<string, unknown> }>("/stats"),
  user: (email: string) =>
    request<Record<string, unknown>>(`/user?email=${encodeURIComponent(email)}`),
  adjustEnergy: (body: {
    email?: string;
    user_id?: string;
    coins_delta?: number;
    energy_delta?: number;
    note?: string;
  }) => request<{ ok: true; user_id: string; coins: number; energy: number }>("/energy", { method: "POST", body }),
  listNotifications: () => request<{ rows: unknown[] }>("/notifications"),
  createNotification: (body: Record<string, unknown>) =>
    request<{ row: unknown }>("/notifications", { method: "POST", body }),
  updateNotification: (body: Record<string, unknown>) =>
    request<{ row: unknown }>("/notifications", { method: "PATCH", body }),
  deleteNotification: (id: string) =>
    request<{ ok: true }>(`/notifications?id=${encodeURIComponent(id)}`, { method: "DELETE" }),
};

/** Public (unauthenticated) read, for the homepage and /updates — no admin key needed. */
export async function fetchActiveNotifications() {
  const res = await fetch(`${baseUrl()}/api/public/notifications/active`, { cache: "no-store" });
  if (!res.ok) throw new Error(`http_${res.status}`);
  const body = (await res.json()) as { rows: unknown[] };
  return body.rows;
}
