import type { Metadata } from "next";
import { Bebas_Neue, Hanken_Grotesk, JetBrains_Mono } from "next/font/google";
import "./globals.css";

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

export const metadata: Metadata = {
  metadataBase: new URL("https://atomic-notes.vercel.app"),
  title: "Atomic Community Base",
  description:
    "Atomic Notes — local-first, privacy-first notes. Development updates, features, the Atomic Energy economy, and downloads.",
  icons: { icon: "/icon.png" },
  openGraph: {
    title: "Atomic Notes — Community Base",
    description:
      "Local-first, privacy-first notes. No ads, no trackers. Optional encrypted cloud sync.",
    images: ["/og-banner.png"],
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    images: ["/og-banner.png"],
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${bebas.variable} ${hanken.variable} ${mono.variable}`}>
      <body className="font-body antialiased">{children}</body>
    </html>
  );
}
