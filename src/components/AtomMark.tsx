// Animated atom mark (CSS-driven spin; no JS needed).
export function AtomMark() {
  return (
    <div className="atom-stage">
      <svg className="atom" viewBox="0 0 300 300" role="img" aria-label="Atom mark">
        <g className="spin">
          <ellipse cx="150" cy="150" rx="120" ry="44" fill="none" stroke="#3A2FF0" strokeWidth="4" />
          <ellipse cx="150" cy="150" rx="120" ry="44" fill="none" stroke="#15171B" strokeWidth="4" transform="rotate(60 150 150)" />
          <ellipse cx="150" cy="150" rx="120" ry="44" fill="none" stroke="#3A2FF0" strokeWidth="4" transform="rotate(120 150 150)" />
          <circle cx="270" cy="150" r="10" fill="#3A2FF0" />
          <circle cx="90" cy="253.9" r="10" fill="#15171B" />
          <circle cx="90" cy="46.1" r="10" fill="#3A2FF0" />
        </g>
        <circle cx="150" cy="150" r="24" fill="#15171B" />
        <circle cx="150" cy="150" r="9" fill="#F4F5F1" />
      </svg>
    </div>
  );
}
