# Ignitia website

Complete 13-page static website with responsive layouts, custom orange/chrome artwork, three services, work, about, insights and an email enquiry flow.

## GitHub Pages setup

1. Create a GitHub repository named `ignitia-website`, with a README and `main` as the default branch. Public repositories support GitHub Pages on GitHub Free; private repositories require an eligible paid plan.
2. Upload this folder's contents, including `.github/workflows/pages.yml`, into the repository root. Do not upload only the ZIP.
3. Open **Settings → Pages → Build and deployment → Source**, and select **GitHub Actions**.
4. Open **Actions → Deploy Ignitia to GitHub Pages → Run workflow** if the initial push occurred before Pages was enabled.
5. Wait for the workflow to finish. Its deployment output provides the live website URL.

The workflow automatically adjusts links and asset paths for the repository path or a configured custom domain. It deploys `dist/` via `_site/` and runs on pushes to `main`.

## Edit and preview

- `generate.py`: page content and shared HTML. Run `python3 generate.py` after editing.
- `dist/style.css`: responsive styles, theme and motion.
- `dist/app.js`: mobile navigation, FAQs via native details, project filters and email draft generation.
- `dist/assets/signal.webp`: custom hero image, already included.
- `scripts/prepare_pages.py`: adjusts root-relative links for GitHub Pages.

To preview locally: `python3 -m http.server 8000 --directory dist`, then open `http://localhost:8000`.
Python 3 is required to regenerate or prepare pages. No third-party Python packages or Node dependencies are required. Google Fonts are loaded externally with local font fallbacks.

## Current launch limitations

The enquiry form opens the visitor's email app and provides a copyable fallback; it does not submit to a backend. Client case studies, results, prices, social links and legal policies need approved content before a full business launch. The included work is explicitly an in-house design concept. No analytics or tracking scripts are installed.

No domain or DNS changes are made by this repository. GitHub Pages deployment and the existing private Sites version are independent.
