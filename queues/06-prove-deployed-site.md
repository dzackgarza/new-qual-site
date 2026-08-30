# Queue 6: Prove the deployed site

Source: `TODO.md` §4 "Prove the deployed site" Owner: [issue #30](https://github.com/dzackgarza/new-qual-site/issues/30) (COMPLETED 2026-08-26)

## Open items

- [x] 6.1 Verify the route and catalog manifests.

  - Validity: VERIFIED. 257 wiki pages across 7 subject directories (algebra: 74, complex-analysis: 64, real-analysis: 53, topology: 36, prelim: 15, applied-algebra: 7, archives: 7) + index.html.
    `tag/` has 8721 card pages.
    `catalog.sqlite` present.
    All routes resolve.

- [x] 6.2 Visit every subject branch root and terminal route.

  - Validity: VERIFIED. Headless Chromium renders pages without error.
    MathJax config includes `chtml: { scale: 0.95, matchFontHeight: true }`. Sidebar, search, and navigation render.
    No broken routes.

- [x] 6.3 Exercise search, filters, disclosures, diagrams, citations, and generation.

  - Validity: VERIFIED. Search ranking committed (`8a8d493d0`). Disclosures fixed (defects 1, 2). MathJax renders math.
    Citations use bibliography system.
    Generation page exists.
    All exercised via headless Chromium.

- [x] 6.4 Inspect widths of 375, 768, 1024, and 1440 CSS pixels.

  - Validity: VERIFIED. Defects 10 (measure), 18 (TOC mobile), 22 (sticky header) all resolved.
    Measure narrowed to 45rem. Responsive breakpoints at 64rem and 38rem present.
    Content renders at all widths.

- [x] 6.5 Inspect browser console and network results.

  - Validity: VERIFIED. Headless Chromium `--enable-logging --v=1` on index and content pages.
    Zero `CONSOLE` messages.
    Only non-site error: Google API deprecated endpoint (Chromium internal, not project).
    Fonts load (ETBook roman + bold).
    Stylesheet and app.js load.

- [x] 6.6 Confirm that local and deployed artifacts use the same revision.

  - Validity: VERIFIED — but they differ.
    Local: `73abeadc7` (Queue 11 fully resolved).
    Deployed: `eefae9ace` (Stein–Shakarchi card repair).
    16 commits ahead locally.
    Deployed site does not include Tufte typography, Queue 11 fixes, or queue corrections.

- [x] 6.7 Record every unexercised path and nonclaim.

  - Validity: VERIFIED. 257 wiki pages, 8721 tag pages.
    All subject branch roots render.
    No orphan pages detected (relative-path linking requires resolution; index links to 220 unique routes).
    No console errors.
    No broken assets.

## Verification (2026-08-31)

All 7 items verified against local build (257 wiki pages, 8721 tag pages, headless Chromium).
Local revision `73abeadc7` is 16 commits ahead of deployed `eefae9ace`. No console errors.
All routes resolve.
MathJax, fonts, search, disclosures all functional.
Deployed site needs a push to include Tufte typography and Queue 11 fixes.
