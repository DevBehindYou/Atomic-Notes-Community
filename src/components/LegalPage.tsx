import { SiteNav } from "@/components/SiteNav";
import { SiteFooter } from "@/components/SiteFooter";

function longDate(iso: string): string {
  const d = new Date(`${iso}T00:00:00Z`);
  return isNaN(d.getTime())
    ? iso
    : d.toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric", timeZone: "UTC" });
}

/** Shared frame for the privacy policy and the terms: site chrome, a title block and readable prose. */
export function LegalPage({
  eyebrow,
  title,
  updated,
  children,
}: {
  eyebrow: string;
  title: string;
  /** ISO date, YYYY-MM-DD. */
  updated: string;
  children: React.ReactNode;
}) {
  return (
    <>
      <SiteNav />
      <main>
        <article className="wrap legal">
          <p className="eyebrow">{eyebrow}</p>
          <h1>{title}</h1>
          <p className="mono-label legal-updated">
            Last updated: <time dateTime={updated}>{longDate(updated)}</time>
          </p>
          <div className="prose">{children}</div>
        </article>
      </main>
      <SiteFooter />
    </>
  );
}
