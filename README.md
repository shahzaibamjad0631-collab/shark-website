# SHARK — Fire & Safety Equipment Website

A custom-built, static website for **SHARK Equipment Safety and Fire Trading — L.L.C — S.P.C**.

## What's in this package

- `dist/` — the finished, ready-to-deploy website (HTML, CSS, JS, SVG icon system). This is the folder you upload to hosting.
- `src/` — the Python source that generates `dist/`. All content lives in `src/data.py`, separated from markup (`src/templates.py`) and the SVG icon system (`src/icons.py`), so products, industries, FAQs, articles, etc. can be edited without touching design code.

The site is plain HTML/CSS/JS with no build framework and no runtime dependencies — it will run on any static host (Netlify, Vercel, GitHub Pages, cPanel, S3, etc.) with zero configuration.

## Previewing locally

Because pages reference assets with root-relative paths (`/assets/...`), open the site through a local server rather than double-clicking the HTML files:

```
cd dist
python3 -m http.server 8000
```

Then visit `http://localhost:8000/index.html`.

## IMPORTANT — placeholders to replace before going live

Nothing on this site was invented. Every detail that wasn't supplied is marked as a clear, bracketed placeholder. Before publishing, open **`src/data.py`** and update the `CONFIG` dictionary at the top:

| Placeholder | Where it appears |
|---|---|
| `[PHONE NUMBER]` | Header, footer, Contact page |
| `[WHATSAPP NUMBER]` (currently `00000000000`) | Floating WhatsApp button, header, footer, mobile bar — update `whatsapp_digits` in `CONFIG` |
| `[EMAIL ADDRESS]` | Footer, Contact page |
| `[BUSINESS ADDRESS]`, `[EMIRATE]` | Footer, Contact page |
| `[BUSINESS HOURS]` | Contact page |
| `www.sharksafety-uae.com` (placeholder domain) | `base_url` in `CONFIG` — used for canonical URLs, sitemap.xml, Open Graph tags |

After editing `src/data.py`, regenerate the site:

```
cd src
python3 build.py
```

This rewrites every HTML file in `dist/` from the updated data — you never need to hand-edit the HTML.

## Logo

Your real SHARKFIRE logo (from `shark_fire_final.pdf`) is now integrated site-wide — header, mobile menu, footer, and the browser-tab favicon. Since all three of those spots sit on a dark background, the logo's dark-charcoal shapes were recolored to white (keeping the red flame) so it reads clearly; the original dark-on-transparent version is also included for any future light-background placement. All variants live in `dist/assets/img/`:

| File | What it is |
|---|---|
| `shark-mark-white.png` / `shark-mark-dark.png` | Icon only (shield + fin + flame) |
| `shark-wordmark-white.png` / `shark-wordmark-dark.png` | "SHARKFIRE" wordmark |
| `shark-subtitle-white.png` / `shark-subtitle-dark.png` | "AND SAFETY EQUIPMENT" subtitle line |
| `favicon.png` | Icon on a small dark square, used as the browser tab icon |

A backup copy of all of these, plus the originally-uploaded PDF-derived crops, is also kept in `src/brand-assets/`. If you ever get a refreshed logo file, send it over and these can be regenerated the same way.

## Adding or editing products

All products live in the `PRODUCTS` list in `src/data.py`. Each entry has `slug`, `name`, `cat` (category key), `short` description, `overview`, `features`, `specs`, `applications`, and `variants`. Add a new product by copying an existing entry — a new page at `/products/{slug}.html` is generated automatically, along with its catalogue card and inclusion in related-product lists.

**No technical specification, certification, or claim was invented.** Where a spec wasn't provided, the site says "Specification available on request" rather than guessing — update these in `data.py` as real specs are confirmed.

## Content notes

- **Services/Solutions page** intentionally covers equipment *supply* only (matching your registered trading activity) — no installation, maintenance, AMC, testing or commissioning claims. Add those sections in `build_solutions()` in `src/build.py` once/if those services are confirmed.
- **Projects page** is built as "Applications" (generic, non-fabricated use cases) rather than real case studies, since no project data was supplied. Swap in real projects later by editing `APPLICATIONS` in `data.py` or extending `build_applications()`.
- **Privacy Policy & Terms & Conditions** are professional placeholder documents — please have them reviewed by a qualified legal advisor before publishing, and fill in the `[DATE]` placeholders.
- Social links in the footer point to `#` (no real accounts were supplied) — update the `href` values in `templates.py`'s `footer()` function once you have real profiles.

## SEO

Each page has a unique title tag, meta description, canonical URL, Open Graph tags, and (where relevant) JSON-LD schema (Organization, Product, FAQPage). `sitemap.xml` and `robots.txt` are generated automatically and reference the placeholder domain above — they'll be correct as soon as you update `base_url`.
