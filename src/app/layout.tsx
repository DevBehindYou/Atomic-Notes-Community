import type { Metadata, Viewport } from "next";
import { Bebas_Neue, Hanken_Grotesk, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import { DEVELOPER_URL, SITE_URL } from "@/lib/site";
import { FEED_ALTERNATE } from "@/lib/seo";
import { SiteAnalytics } from "@/components/SiteAnalytics";
import { CommunityPopup } from "@/components/CommunityPopup";

const bebas = Bebas_Neue({
  weight: "400",
  subsets: ["latin"],
  variable: "--font-bebas",
});
const hanken = Hanken_Grotesk({
  subsets: ["latin"],
  variable: "--font-hanken",
});
const mono = JetBrains_Mono({
  subsets: ["latin"],
  variable: "--font-mono",
});

const DESCRIPTION =
  "Atomic Notes is a free offline notes app for Android. Notes sync to your own Google Drive, with an optional end-to-end encrypted vault. No AI, no ads.";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: "Atomic Notes: Offline, E2E Vault & Google Drive Sync",
    template: "%s | Atomic Notes",
  },
  description: DESCRIPTION,
  applicationName: "Atomic Notes",
  authors: [{ name: "Ashutosh Sharma (DevBehindYou)", url: DEVELOPER_URL }],
  creator: "DevBehindYou",
  keywords: [
    "Atomic Notes",
    "local-first notes app",
    "private notes app Android",
    "Google Drive notes app",
    "end-to-end encrypted notes",
    "notes app without AI",
    "offline notes app",
    "privacy-first notes app",
  ],
  alternates: {
    canonical: "/",
    types: FEED_ALTERNATE,
  },
  icons: { icon: "/icon.png", apple: "/icon.png" },
  openGraph: {
    type: "website",
    siteName: "Atomic Notes",
    url: "/",
    title: "Atomic Notes: Your Notes, Your Drive, Always Yours.",
    description: DESCRIPTION,
    images: [{ url: "/og-banner.png", width: 1200, height: 630, alt: "Atomic Notes, local-first notes for Android" }],
    locale: "en_US",
  },
  twitter: {
    card: "summary_large_image",
    site: "@devbehindyou",
    creator: "@devbehindyou",
    title: "Atomic Notes: Your Notes, Your Drive, Always Yours.",
    description: DESCRIPTION,
    images: ["/og-banner.png"],
  },
};

export const viewport: Viewport = {
  themeColor: "#F4F5F1",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en-US" className={`${bebas.variable} ${hanken.variable} ${mono.variable}`}>
      <body className="font-body antialiased">
        {children}
        <CommunityPopup />
        <SiteAnalytics />
      </body>
    </html>
  );
}
