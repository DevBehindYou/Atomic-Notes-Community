import type { Metadata } from "next";
import { LEGACY_HOSTS, SITE_URL } from "@/lib/site";

export const SITE_NAME = "Atomic Notes";
export const TWITTER_HANDLE = "@devbehindyou";
export const OG_IMAGE = {
  url: "/og-banner.png",
  width: 1200,
  height: 630,
  alt: "Atomic Notes, local-first notes for Android",
};

/** RSS discovery link. Pages that set `alternates` replace the root one, so each includes this. */
export const FEED_ALTERNATE = { "application/rss+xml": [{ url: "/feed.xml", title: "Atomic Notes Blog" }] };

/** Absolute URL on the canonical origin. Absolute inputs are returned unchanged. */
export function absoluteUrl(pathOrUrl: string): string {
  if (/^https?:\/\//i.test(pathOrUrl)) return pathOrUrl;
  return `${SITE_URL}${pathOrUrl.startsWith("/") ? "" : "/"}${pathOrUrl}`;
}

/**
 * A canonical taken from content (blog front matter) is kept as written unless it is on a
 * retired host; those are moved onto the current origin so a stale draft can never point
 * search engines back at the old address.
 */
export function canonicalUrl(candidate: string | undefined, fallback: string): string {
  if (!candidate) return fallback;
  try {
    const u = new URL(candidate);
    return LEGACY_HOSTS.includes(u.host.toLowerCase()) ? absoluteUrl(u.pathname + u.search) : candidate;
  } catch {
    return fallback;
  }
}

/**
 * Metadata for a standalone page. Next.js replaces (not merges) the root `openGraph` and
 * `twitter` objects when a page sets its own, so every page sets the full card here instead
 * of inheriting the home page's title and URL.
 */
export function pageMetadata({
  title,
  description,
  path,
  socialTitle,
}: {
  title: string;
  description: string;
  path: string;
  socialTitle?: string;
}): Metadata {
  const card = socialTitle ?? `${title} | ${SITE_NAME}`;
  return {
    title,
    description,
    alternates: { canonical: path, types: FEED_ALTERNATE },
    openGraph: {
      type: "website",
      siteName: SITE_NAME,
      locale: "en_US",
      url: path,
      title: card,
      description,
      images: [OG_IMAGE],
    },
    twitter: {
      card: "summary_large_image",
      site: TWITTER_HANDLE,
      creator: TWITTER_HANDLE,
      title: card,
      description,
      images: [OG_IMAGE.url],
    },
  };
}
