# NetConfiger GitHub Pages — v2

## Deployment

Upload `index.html`, `zh.html`, and the entire `assets` folder to the **root** of the GitHub repository `netconfiger/netconfiger`, on the `main` branch. Keep the directory structure unchanged. GitHub Pages should be configured for deployment from `main` / root.

English: https://netconfiger.github.io/netconfiger/index.html
Chinese: https://netconfiger.github.io/netconfiger/zh.html

## Brand and product consistency

- Uses the official site's favicon URL: `https://netconfiger.com/favicon.ico`. The icon is **referenced**, not copied or redesigned. Verify that this URL actually serves the official icon; if the site uses another icon URL, replace both references in each HTML file.
- Mirrors the official site's Windows network distribution / HTTP-SOCKS5 product scope, not future transparent gateway capabilities.
- Navigation and conversion links return to `netconfiger.com`.
- `canonical` points to the official homepage to avoid a competing duplicate index page.
- CSS is bundled locally; no build step, external JS, or third-party UI framework is required.

## Important

The official site's precise CSS tokens and icon asset could not be fetched in this build environment. This is a carefully aligned companion page based on the public site's verified content and structure, **not** an exact copy of its production CSS. Review the favicon URL and visual details after deploying.
