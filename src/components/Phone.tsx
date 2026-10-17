// A screenshot in a phone frame: ink body, thin bezel and the design system's solid offset shadow.
export function Phone({
  src,
  alt,
  shadow = "signal",
  className = "",
  eager = false,
  height = 2460,
}: {
  src: string;
  alt: string;
  shadow?: "signal" | "ink";
  className?: string;
  eager?: boolean;
  /** Pixel height of the screenshot at 1080 px wide. Release 2.03.5 screens are 2199. */
  height?: number;
}) {
  return (
    <div className={`phone phone-${shadow} ${className}`}>
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img src={src} alt={alt} width={1080} height={height} loading={eager ? "eager" : "lazy"} />
    </div>
  );
}
