"use client";

import { usePathname } from "next/navigation";
import { Analytics, type BeforeSendEvent } from "@vercel/analytics/next";

// Vercel Web Analytics for the public pages. The secret Controller is never reported: its address
// stays out of the analytics dashboard, the same way robots.ts keeps it out of robots.txt.
function isController(pathname: string): boolean {
  return pathname === "/controller" || pathname.startsWith("/controller/");
}

// A script loaded on a public page keeps running after client-side navigation, so events are
// filtered as well as the component being left off the Controller.
function dropController(event: BeforeSendEvent): BeforeSendEvent | null {
  return isController(new URL(event.url).pathname) ? null : event;
}

export function SiteAnalytics() {
  if (isController(usePathname() ?? "")) return null;
  return <Analytics beforeSend={dropController} />;
}
