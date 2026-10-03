// The Atomic Coin from public/icons/atomic-coin.svg, redrawn without its background square and with
// heavier strokes, so it stays legible from 18px (nav) up to 72px (home page callout).
export function CoinMark({ size = 18, className }: { size?: number; className?: string }) {
  return (
    <svg viewBox="-120 -120 244 244" width={size} height={size} className={className} aria-hidden="true">
      <circle cx="12" cy="12" r="100" fill="#1D14A0" />
      <circle r="100" fill="#F4F5F1" stroke="#3A2FF0" strokeWidth="14" />
      <g fill="none" stroke="#15171B" strokeWidth="10">
        <ellipse rx="54" ry="20" />
        <ellipse rx="54" ry="20" transform="rotate(60)" />
        <ellipse rx="54" ry="20" transform="rotate(120)" />
      </g>
      <circle r="17" fill="#15171B" />
    </svg>
  );
}
