"use client";

import { useEffect, useState } from "react";
import Link from "next/link";

const LINKS = [
  { id: "why", label: "Why" },
  { id: "energy", label: "Energy" },
  { id: "interface", label: "Interface" },
  { id: "roadmap", label: "Roadmap" },
  { id: "get", label: "Get it" },
];

const APK =
  process.env.NEXT_PUBLIC_APK_URL ||
  "https://github.com/DevBehindYou/Project-Atomic-Notes-New/releases/tag/ci-latest";

export function SiteNav() {
  const [active, setActive] = useState("");
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) setActive(e.target.id);
        });
      },
      { rootMargin: "-45% 0px -50% 0px" }
    );
    LINKS.forEach(({ id }) => {
      const el = document.getElementById(id);
      if (el) io.observe(el);
    });
    return () => io.disconnect();
  }, []);

  return (
    <header className="nav">
      <div className="wrap nav-inner">
        <a href="#top" className="brand">
          ATOMIC NOTES
        </a>
        <nav className={`nav-links ${open ? "open" : ""}`} onClick={() => setOpen(false)}>
          {LINKS.map((x) => (
            <a key={x.id} href={`#${x.id}`} className={active === x.id ? "active" : ""}>
              {x.label}
            </a>
          ))}
          <Link href="/blog">Blog</Link>
          <Link href="/updates">Updates</Link>
          <a href={APK} className="btn-signal" style={{ padding: "9px 16px" }}>
            Download
          </a>
        </nav>
        <button className="burger" onClick={() => setOpen((o) => !o)} aria-label="Menu">
          ☰
        </button>
      </div>
    </header>
  );
}
