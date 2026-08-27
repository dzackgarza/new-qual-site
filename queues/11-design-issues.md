# Queue 11: Wiki design defects (rendered verification)

Source: `DESIGN_TODO.md` (committed 2026-08-27, `ab0b3d190`)
Evidence: 12 pages rendered in browser at 540px, re-rendered at 1440px and 375px.
Frequency counts from built HTML in `build/quarto/_site/wiki` (398 pages).

These are the concrete rendered-page defects that queues 2, 3, 5, and 6 reference. Each is verified against the current build.

## Broken, visible on almost every page

- [ ] 1. Sidebar disclosure triangle sits above its label. `.subject-sidebar a { display: block }` at `site/styles.css:194` applied to `<a>` inside `<summary>`. Two lines per entry; one expanded subject makes rail 1400px tall. Fix: `display:inline`.
- [ ] 2. Clicking a section name navigates instead of expanding. `<summary><a>Prelims</a></summary>` — only ~10px triangle is expand target, below 44px touch minimum. Mobile panel capped at `50vh`.
- [ ] 3. 163 blocks print literal `?` as title on 63 pages. Source: `:::{.proof title="?"}`. Emitter writes authored title as body text. Confirmed in `12_Sylow_Theorems.html`.
- [ ] 4. Adjacent links merge into one underlined run. 151 paragraphs on 78 pages hold 2+ wikilinks separated by space. Bare `[[P-XXXXX]] [[P-VPCLD]]` lines.
- [ ] 5. All 12 environment kinds look identical. 859 blocks, same 3px grey left border (`site/styles.css:324`) and grey small-caps label. `.theorem` and `.concept` get no treatment.

## Link-list pages, not content pages

- [ ] 6. 108 of 398 pages (27%) are >60% link text. Bare `[[card-id]]` renders as link, never transcludes. 3,968 such lines across 245 pages. Wiki source has one `.definition` environment — definitions live in `corpus/`.
- [ ] 7. Same-title links sit next to each other. 22 titles duplicated on one page. Distinct cards sharing a title, visually identical.
- [ ] 8. Link text is sometimes a whole sentence with math. Underline cuts through subscripts; MathJax spacing blows gaps around operators.
- [ ] 9. `992 Extra_Questions.html` spends ~107px per item on `<h3>Question 1.n</h3>` above a single link, 285 times. TOC lists 285 entries with no information. Stray periods on some headings.

## Typography and layout

- [ ] 10. Measure too wide. Content column `52rem` ≈ 832px (`site/styles.css:140`). Readable band is 65–75ch.
- [ ] 11. Three type families compete. Inter body, Charter headings, MathJax TeX serif. Inline math reads larger than surrounding sans. No `chtml: { scale, matchFontHeight }` in MathJax config.
- [ ] 12. List rhythm inconsistent. Loose lists ~42px, tight lists ~26px, pages a click apart. CSS never normalises loose/tight.
- [ ] 13. Pages with no headings keep empty TOC rail. `10_Algebra/11_Resources/index.html`: three body lines next to 1200px sidebar and ~280px dead space.
- [ ] 14. Figures have no component. Bare inline `<img>`. Word strands at figure edge; captions misalign; display equations run definitions together.
- [ ] 15. Nested grey-on-grey. Blockquote inside EXAMPLE: grey border inside grey border. Three meanings share one container style.
- [ ] 16. Naked URLs as link text (Keith Conrad PDF on Sylow page). Overflows column on mobile.
- [ ] 17. Card pages show "None." for empty dependencies/backlinks. `tag/P-A4JGH.html`: fourth card breaks 3-column grid. Metadata labels 11px uppercase; `status: draft` exposed raw.

## Responsive, theme, accessibility

- [ ] 18. TOC disappears below 1024px with no replacement. Long pages get no in-page navigation on phone or tablet.
- [ ] 19. No dark mode and no print styles. `color-scheme: light` only. Zero `prefers-color-scheme` or `@media print` rules.
- [ ] 20. Focus styles exist for one element (`.wiki-sidebar summary`). Everything else falls back to UA ring.
- [ ] 21. Small text below 14px. Sidebar 13.8px, TOC 13.4px, metadata labels 11.2px, environment labels 13.6px at 65% opacity. Sidebar leaf links inherit `--muted`, look like disabled labels.
- [ ] 22. Sticky header ghosting. `backdrop-filter: blur(12px)` over 94% white lets scrolled content smudge through.
- [ ] 23. URLs carry spaces and mixed case. `992 Extra_Questions.html`, `2016 Fall.html`. Hrefs embed raw spaces.

## Search

- [ ] 24. No ranking. `site/app.js:38` filters and takes first 30 in index order. "sylow" returns "Basics", "Classification", "Galois Theory" above "Sylow Theorems". 4,921 Problems and 4,272 Cards in index; none surfaced for that query.
- [ ] 25. Every result row says "Page" and nothing else. `.search-result-detail` is `display:none` below 38rem — the only discriminator hidden where rows are most ambiguous. No path, no snippet.

## Notes

Per `DESIGN_TODO.md` closing note: items 1, 2, 3, 24 are each a few lines and land immediately. Item 6 is the one that changes what the wiki *is* and needs a decision about transclusion before touching anything.