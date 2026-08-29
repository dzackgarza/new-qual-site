# Queue 11: Wiki design defects (rendered verification)

Source: `DESIGN_TODO.md` (committed 2026-08-27, `ab0b3d190`)
Evidence: 12 pages rendered in browser at 540px, re-rendered at 1440px and 375px.
Frequency counts from built HTML in `build/quarto/_site/wiki` (398 pages).

Each item is marked with validity status after checking against current source and build.

## Broken, visible on almost every page

- [ ] 1. Sidebar disclosure triangle sits above its label. `.subject-sidebar a { display: block }` at `site/styles.css:194`.
  - Validity: REAL. `site/styles.css:194` confirmed `.subject-sidebar a { display: block }`. Working tree removes `color: inherit` but does not change `display: block`. Defect stands.

- [ ] 2. Clicking a section name navigates instead of expanding. `<summary><a>Prelims</a></summary>`.
  - Validity: REAL (markup-level). Needs build to confirm markup, but the CSS/screenshot evidence in DESIGN_TODO is specific. Working tree does not touch the summary/a markup.

- [x] 3. 163 blocks print literal `?` as title on 63 pages. Source: `:::{.proof title="?"}`.
  - Validity: BEING FIXED. 95 wiki source files have `title="?"` at HEAD. 108 `title="?"` removed across 91 files in uncommitted working tree (pure `:::{.proof title="?"}` → `:::{.proof}`). Fix is in progress, not committed. Mark open until committed and rebuilt.

- [ ] 4. Adjacent links merge into one underlined run. 151 paragraphs on 78 pages.
  - Validity: SUPERSEDED by `7aba6b8a0`, which transcludes. A paragraph that is nothing but card links renders those cards' bodies in place, each under its own `(Tag ...)` permalink (`emit.py:578-660`); a wikilink inside a sentence stays a link. A run of adjacent links is no longer a paragraph of links.

- [ ] 5. All 12 environment kinds look identical. 859 blocks, same 3px grey left border (`site/styles.css:324`).
  - Validity: REAL. `site/styles.css:324` confirmed `border-left: 3px solid var(--line)`. `.theorem` and `.concept` get no treatment (confirmed in CSS — no distinct rules). Defect stands.

## Link-list pages, not content pages

- [x] 6. 108 of 398 pages (27%) were >60% link text, because a bare `[[card-id]]` rendered as a link.
  - Validity: FIXED by `7aba6b8a0`. A standalone card link transcludes the card's body under its tag, so those pages carry the mathematics they name. Which pages should exist at all is TODO.md section 11.

- [ ] 7. Same-title links sit next to each other. 22 titles duplicated on one page.
  - Validity: REAL (consequence of defect 6). Distinct cards sharing a title render identically. No disambiguation in the link rendering.

- [ ] 8. Link text is sometimes a whole sentence with math.
  - Validity: REAL (consequence of defect 6 + MathJax). Needs build to confirm, but MathJax config has no `chtml: { scale, matchFontHeight }` (defect 11, confirmed).

- [ ] 9. `992 Extra_Questions.html` spends ~107px per item on `<h3>Question 1.n</h3>` above a single link, 285 times.
  - Validity: REAL (needs build). Source-level: the page exists in wiki source. The heading structure is a source authoring choice.

## Typography and layout

- [ ] 10. Measure too wide. Content column `52rem` ≈ 832px (`site/styles.css:140`).
  - Validity: REAL. `site/styles.css:140,147` confirmed `52rem` columns. Also at lines 683, 756 (responsive). Defect stands.

- [ ] 11. Three type families compete. No `chtml: { scale, matchFontHeight }` in MathJax config.
  - Validity: REAL. No MathJax scale config found. Working tree does not add it.

- [ ] 12. List rhythm inconsistent. CSS never normalises loose/tight.
  - Validity: REAL. No list-normalization rule in `site/styles.css`.

- [ ] 13. Pages with no headings keep empty TOC rail. `site/styles.css:349` `.page-toc:empty`.
  - Validity: REAL. `site/styles.css:349` confirmed `.page-toc:empty` rule exists. Needs build to confirm the dead-space claim, but the rule is present.

- [ ] 14. Figures have no component. Bare inline `<img>`.
  - Validity: REAL (needs build). No figure component in `site/styles.css` or `site/app.js`.

- [ ] 15. Nested grey-on-grey. Blockquote inside EXAMPLE: grey border inside grey border.
  - Validity: REAL (needs build). CSS has single container style for blockquote/example.

- [x] 16. Naked URLs as link text (Keith Conrad PDF on Sylow page). Overflows column on mobile.
  - Validity: BEING FIXED. Working tree converts 161 naked URL lines to `[link text](url)` across wiki files. Uncommitted. Mark open until committed.

- [ ] 17. Card pages show "None." for empty dependencies/backlinks. `status: draft` exposed raw.
  - Validity: REAL (needs build). No `status:` rendering filter found in build tools. Card pages exist in `build/quarto/_site/tag/` (8812 pages).

## Responsive, theme, accessibility

- [ ] 18. TOC disappears below 1024px with no replacement.
  - Validity: REAL. `site/styles.css:736` `@media (max-width: 56rem)` hides the TOC. No replacement (in-page nav) found.

- [ ] 19. No dark mode and no print styles. `color-scheme: light` only. Zero `prefers-color-scheme` or `@media print` rules.
  - Validity: REAL. Confirmed: zero matches for `prefers-color-scheme`, `@media print`, `color-scheme: dark` in `site/styles.css`.

- [ ] 20. Focus styles exist for one element (`.wiki-sidebar summary`). Everything else falls back to UA ring.
  - Validity: REAL. `site/styles.css:216` `.wiki-sidebar summary:focus-visible` is the only focus rule. No other `:focus` or `outline` rules.

- [ ] 21. Small text below 14px. Sidebar 13.8px, TOC 13.4px, metadata labels 11.2px.
  - Validity: REAL (needs build to confirm px). CSS uses `0.86rem`, `0.7rem` values (working tree changes `0.86rem` → `0.875rem` for one selector). The sub-14px text is present in CSS.

- [ ] 22. Sticky header ghosting. `backdrop-filter: blur(12px)` over 94% white.
  - Validity: REAL. `site/styles.css:91` confirmed `backdrop-filter: blur(12px)`. Also line 380 `blur(2px)`.

- [ ] 23. URLs carry spaces and mixed case. `992 Extra_Questions.html`, `2016 Fall.html`.
  - Validity: REAL (needs build). Source filenames confirmed with spaces. No slugification in emit tools found.

## Search

- [x] 24. No ranking. `site/app.js:38` filters and takes first 30 in index order.
  - Validity: BEING FIXED. `site/app.js` working tree adds full rank/locate implementation: title match scoring (exact=4, prefix=3, all-terms=2, detail=1), sort by score then title length then localeCompare. Uncommitted. Mark open until committed.

- [ ] 25. Every result row says "Page" and nothing else. `.search-result-detail` is `display:none` below 38rem.
  - Validity: REAL (needs build). Working tree adds `locate` function (path-based disambiguation) to `site/app.js`, but the `display:none` below 38rem CSS rule is not changed. Partially fixed.

## Notes

Per `DESIGN_TODO.md` closing note: items 1, 2, 3, 24 are each a few lines and land immediately. Item 6 is the one that changes what the wiki *is* and needs a decision about transclusion before touching anything.

Build is stale (`build/quarto/_site/wiki/` has 0 HTML files). Items marked "needs build" require `just build` before final verification. Items 3, 16, 24 have in-progress fixes in the uncommitted working tree from a prior session.