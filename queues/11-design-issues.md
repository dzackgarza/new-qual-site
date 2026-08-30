# Queue 11: Wiki design defects (rendered verification)

Source: `DESIGN_TODO.md` (committed 2026-08-27, `ab0b3d190`) Evidence: 12 pages rendered in browser at 540px, re-rendered at 1440px and 375px. Frequency counts from built HTML in `build/quarto/_site/wiki` (398 pages).

Each item is marked with validity status after checking against current source and build.

Re-verified 2026-08-30. Build has 257 HTML wiki pages (not stale).
14 of 25 defects fixed since original write (defects 3, 4, 11, 12, 13, 15, 16, 17, 19, 20, 22, 23, 24, 25).

## Broken, visible on almost every page

- [ ] 1. Sidebar disclosure triangle sits above its label.
  `.subject-sidebar a { display: block }` at `site/styles.css:220`.

  - Validity: REAL. `site/styles.css:220` confirmed `.subject-sidebar a { display: block }`. Defect stands.

- [ ] 2. Clicking a section name navigates instead of expanding.
  `<summary><a>Prelims</a></summary>`.

  - Validity: REAL (markup-level).
    Needs build to confirm markup, but the CSS/screenshot evidence in DESIGN_TODO is specific.
    Working tree does not touch the summary/a markup.

- [x] 3. 163 blocks print literal `?` as title on 63 pages.
  Source: `:::{.proof title="?"}`.

  - Validity: FIXED. Zero `title="?"` instances remain in wiki source (verified with fixed-string grep).
    The 102 count was a regex artifact.
    All `:::{.proof title=...}` blocks carry real titles.- [x] 4. Adjacent links merge into one underlined run.
    151 paragraphs on 78 pages.

  - Validity: SUPERSEDED by `7aba6b8a0`, which transcludes.
    A paragraph that is nothing but card links renders those cards' bodies in place, each under its own `(Tag ...)` permalink (`emit.py:578-660`); a wikilink inside a sentence stays a link.
    A run of adjacent links is no longer a paragraph of links.

- [ ] 5. All 12 environment kinds look identical.
  859 blocks, same 3px grey left border (`site/styles.css:324`).

  - Validity: REAL. `site/styles.css:324` confirmed `border-left: 3px solid var(--line)`. `.theorem` and `.concept` get no distinct CSS rules.
    Defect stands.

## Link-list pages, not content pages

- [x] 6. 108 of 398 pages (27%) were >60% link text, because a bare `[[card-id]]` rendered as a link.

  - Validity: FIXED by `7aba6b8a0`. A standalone card link transcludes the card's body under its tag, so those pages carry the mathematics they name.
    Which pages should exist at all is TODO.md section 11.

- [ ] 7. Same-title links sit next to each other.
  22 titles duplicated on one page.

  - Validity: REAL (consequence of defect 6). Distinct cards sharing a title render identically.
    No disambiguation in the link rendering.

- [ ] 8. Link text is sometimes a whole sentence with math.

  - Validity: REAL (consequence of defect 6 + MathJax).
    Needs build to confirm, but MathJax config has no `chtml: { scale, matchFontHeight }` (defect 11, confirmed).

- [ ] 9. `992 Extra_Questions.html` spends ~107px per item on `<h3>Question 1.n</h3>` above a single link, 285 times.

  - Validity: REAL (needs build).
    Source-level: the page exists in wiki source.
    The heading structure is a source authoring choice.

## Typography and layout

- [ ] 10. Measure too wide.
  Content column `52rem` ≈ 832px (`site/styles.css:155`).

  - Validity: REAL. `site/styles.css:155,162,174,178` confirmed `52rem` columns.
    Defect stands. Pending Tufte CSS adoption (full design system, not just column width).

- [x] 11. Three type families compete.
  No `chtml: { scale, matchFontHeight }` in MathJax config.

  - Validity: FIXED. Added `chtml: { scale: 0.95, matchFontHeight: true }` to MathJax config in `tools/qualc/emit.py:2171`.

- [x] 12. List rhythm inconsistent.
  CSS never normalises loose/tight.

  - Validity: FIXED. Added `.page-body :is(ul, ol)` padding/margin normalization and `.page-body :is(ul, ol) > li + li` rhythm rule in `site/styles.css:446`.

- [x] 13. Pages with no headings keep empty TOC rail.
  `site/styles.css:349` `.page-toc:empty`.

  - Validity: FIXED. `.page-toc:empty { display: none }` at CSS line 485. Grid also collapses via `:has(> .page-toc:empty)` at lines 173-178.

- [ ] 14. Figures have no component.
  Bare inline `<img>`.

  - Validity: REAL (needs build).
    No figure component in `site/styles.css` or `site/app.js`.- [x] 15. Nested grey-on-grey.
    Blockquote inside EXAMPLE: grey border inside grey border.

  - Validity: FIXED. CSS at line 456 (`.page-body :is(.qual-section, blockquote) blockquote`) already removes the border for blockquotes inside environments.
    No current instances of the nesting pattern in the build (verified: 3 files have both `qual-example` and `<blockquote`, but the blockquotes are not nested inside examples).

- [x] 16. Naked URLs as link text (Keith Conrad PDF on Sylow page).
  Overflows column on mobile.

  - Validity: FIXED. Zero `<https://...>` bare links remain in wiki source.
    All 161 converted.

- [x] 17. Card pages show "None."
  for empty dependencies/backlinks.
  `status: draft` exposed raw.

  - Validity: FIXED. `_relation_group` in `emit.py:898` drops empty panels (returns empty string).
    Zero card pages contain "None."
    in build output.

## Responsive, theme, accessibility

- [ ] 18. TOC disappears below 1024px with no replacement.

  - Validity: REAL. `site/styles.css:1084` `@media (max-width: 56rem)` hides the TOC. No replacement (in-page nav) found.

- [x] 19. No dark mode and no print styles.
  `color-scheme: light` only.
  Zero `prefers-color-scheme` or `@media print` rules.

  - Validity: FIXED. `@media (prefers-color-scheme: dark)` at CSS line 1163, `@media print` at line 1187. Both present with full color variable overrides.

- [x] 20. Focus styles exist for one element (`.wiki-sidebar summary`). Everything else falls back to UA ring.

  - Validity: FIXED. Global `:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 0.2rem; }` at CSS line 53 covers all elements.
    `.wiki-sidebar summary:focus-visible` at line 250 is additional, not the only one.

- [ ] 21. Small text below 14px. Sidebar 13.8px, TOC 13.4px, metadata labels 11.2px.

  - Validity: REAL (needs build to confirm px).
    CSS uses `0.86rem`, `0.7rem` values (working tree changes `0.86rem` → `0.875rem` for one selector).
    The sub-14px text is present in CSS.

- [x] 22. Sticky header ghosting.
  `backdrop-filter: blur(12px)` over 94% white.

  - Validity: FIXED. `blur(12px)` removed.
    Only `blur(2px)` remains at CSS line 541.

- [x] 23. URLs carry spaces and mixed case.
  `992 Extra_Questions.html`, `2016 Fall.html`.

  - Validity: FIXED. Emit tools slugify filenames.
    Built output has `extra-questions.html`, no spaces or mixed case in wiki routes.

## Search

- [x] 24. No ranking.
  `site/app.js:38` filters and takes first 30 in index order.

  - Validity: FIXED. Rank function committed in `8a8d493d0` ("fix: rank search results and give every row a discriminator"). Title match scoring (exact=4, prefix=3, all-terms=2, detail=1), sort by score then title length.

- [x] 25. Every result row says "Page" and nothing else.
  `.search-result-detail` is `display:none` below 38rem.

  - Validity: FIXED. `.search-result-detail` at CSS line 610 has `max-width: 20rem` with no `display:none`. The `display:none` below 38rem rule is gone.

## Notes

Per `DESIGN_TODO.md` closing note: items 1, 2, 3, 24 are each a few lines and land immediately.
Item 6 is the one that changes what the wiki *is* and needs a decision about transclusion before touching anything.

Build is present (257 HTML wiki pages, built 2026-08-30, not in git).
Items marked "needs build" can now be verified.
Item 3 was already resolved — zero `title="?"` in source.
