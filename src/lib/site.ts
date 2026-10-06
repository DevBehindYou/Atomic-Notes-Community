// Public, non-secret site settings. Only NEXT_PUBLIC_* variables belong here:
// this module is also bundled into client components.
const DEFAULT_SITE_URL = "https://atomic-notes.devbehindyou.com";
// The App is built from Atomic-Notes-App-V0.2 (the older Atomic-Notes-App repository has no releases).
const DEFAULT_APK_URL = "https://github.com/DevBehindYou/Atomic-Notes-App-V0.2/releases/latest";

/** Hosts the site used to live on. They redirect to SITE_URL and never appear as canonical. */
export const LEGACY_HOSTS = ["atomic-notes-community.vercel.app"];

/**
 * The origin of a configured site URL, or the fallback. NEXT_PUBLIC_* values are baked in at
 * build time, so a stale value (the retired address, or a *.vercel.app deployment URL) would
 * ship in every canonical, sitemap and feed link until the next build. Those are never a valid
 * canonical origin, so they fall back to the production domain instead.
 */
function siteOrigin(value: string | undefined, fallback: string): string {
  try {
    const url = new URL((value || fallback).trim());
    const host = url.host.toLowerCase();
    if (LEGACY_HOSTS.includes(host) || host.endsWith(".vercel.app")) return fallback;
    return url.origin;
  } catch {
    return fallback;
  }
}

/** Canonical origin for metadata, sitemap and feed links. No trailing slash. */
export const SITE_URL = siteOrigin(process.env.NEXT_PUBLIC_SITE_URL, DEFAULT_SITE_URL);

/** The developer's own site, used for author links and structured data. */
export const DEVELOPER_URL = "https://devbehindyou.com";

/** Where the download buttons point. */
export const APK_URL = process.env.NEXT_PUBLIC_APK_URL || DEFAULT_APK_URL;

/** Invite to the Atomic Notes Community Discord server. */
export const DISCORD_URL = "https://discord.gg/T4Vs7P3Qs";
