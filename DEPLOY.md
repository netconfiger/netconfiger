# Deployment notes

1. Upload the contents of this folder to the root of your existing repository.
2. Keep `index.html` at the repository root.
3. In repository Settings → Pages, choose **Deploy from a branch**, your main branch, and `/(root)`.
4. Open the GitHub Pages URL after deployment completes.
5. Do not change DNS for `netconfiger.com` for this test; the page links to the existing official site.

Before publishing, confirm the wording matches the current release. Add real screenshots only when verified UI captures are available. Dynamic GitHub Stars / contributors badges can be added once the actual repository URL is known.


## Repository-specific notes

- Repository: https://github.com/netconfiger/netconfiger
- The README contains dynamic GitHub Stars and Issues badges.
- The license badge only resolves correctly if the repository has a `LICENSE` file. If it does not, remove that badge or add the actual license before publishing.
- Do not add a source-code license badge or claim the application is open source unless the repository's license and published contents support that claim.

- The bilingual static pages are `index.html` (English) and `zh.html` (Simplified Chinese). Both files must be uploaded to the repository root, along with `styles.css` and `assets/`.
- GitHub Pages is serving this repository under a GitHub-hosted URL; relative links are used for the language switch so it works under a project path.
- Before using this as a standalone SEO landing site, configure canonical and hreflang URLs to the actual published GitHub Pages URLs. They should not point at the main product homepage unless that is intentionally the canonical destination.
