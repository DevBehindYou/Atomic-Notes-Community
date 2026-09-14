/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  async headers() {
    // Keep the secret admin surface out of search engines even if a URL leaks.
    return [
      {
        source: "/controller",
        headers: [{ key: "X-Robots-Tag", value: "noindex, nofollow, noarchive, nosnippet" }],
      },
      {
        source: "/api/controller/:path*",
        headers: [{ key: "X-Robots-Tag", value: "noindex, nofollow, noarchive, nosnippet" }],
      },
    ];
  },
};

export default nextConfig;
