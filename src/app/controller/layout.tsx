import type { Metadata } from "next";

// Belt-and-suspenders with the X-Robots-Tag header in next.config: emit a
// <meta name="robots" content="noindex,nofollow"> for the whole /controller
// subtree so the secret panel never lands in a search index.
export const metadata: Metadata = {
  robots: { index: false, follow: false, nocache: true },
};

export default function ControllerLayout({ children }: { children: React.ReactNode }) {
  return <>{children}</>;
}
