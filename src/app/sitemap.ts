import type { MetadataRoute } from "next";
import { getAllPosts } from "@/lib/blog";

const BASE = "https://atomic-notes.vercel.app";

export default function sitemap(): MetadataRoute.Sitemap {
  const posts = getAllPosts().map((p) => ({
    url: `${BASE}/blog/${p.slug}`,
    lastModified: p.updatedAt || p.publishedAt || undefined,
    changeFrequency: "monthly" as const,
    priority: 0.7,
  }));

  return [
    { url: BASE, changeFrequency: "weekly", priority: 1 },
    { url: `${BASE}/blog`, changeFrequency: "weekly", priority: 0.8 },
    { url: `${BASE}/updates`, changeFrequency: "daily", priority: 0.6 },
    ...posts,
  ];
}
