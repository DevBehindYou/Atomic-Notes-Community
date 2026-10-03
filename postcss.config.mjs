/** @type {import('postcss-load-config').Config} */
export default {
  plugins: {
    // Tailwind v4 handles imports and vendor prefixes itself, so autoprefixer is gone.
    "@tailwindcss/postcss": {},
  },
};
