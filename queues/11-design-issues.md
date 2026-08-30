# Queue 11: Wiki design defects (rendered verification)

Source: `DESIGN_TODO.md` (committed 2026-08-27, `ab0b3d190`) Evidence: 12 pages rendered in browser at 540px, re-rendered at 1440px and 375px. Frequency counts from built HTML in `build/quarto/_site/wiki` (398 pages).

Each item is marked with validity status after checking against current source and build.

Re-verified 2026-08-30. Build has 257 HTML wiki pages (not stale).
25 of 25 defects resolved.
17 fixed (code changes), 8 design-accepted.

## Broken, visible on almost every page

- [x] 1. Sidebar disclosure triangle sits above its label.
  `.subject-sidebar a { display: block }` at `site/styles.css:220`.

  - Validity: FIXED. Removed `<a>` from `<summary>` in sidebar generation (`static_site.py:408`). Plain text title keeps triangle beside label.

- [x] 2. Clicking a section name navigates instead of expanding.
  `<summary><a>Prelims</a></summary>`.

  - Validity: FIXED. Same fix as defect 1. Plain text summary toggles disclosure; no link intercepts the click.

- [x] 3. 163 blocks print literal `?` as title on 63 pages.
  Source: `:::{.proof title="?"}`.

  - Validity: FIXED. Zero `title="?"` instances remain in wiki source (verified with fixed-string grep).
    The 102 count was a regex artifact.
    All `:::{.proof title=...}` blocks carry real titles.- [x] 4. Adjacent links merge into one underlined run.
    151 paragraphs on 78 pages.

  - Validity: SUPERSEDED by `7aba6b8a0`, which transcludes.
    A paragraph that is nothing but card links renders those cards' bodies in place, each under its own `(Tag ...)` permalink (`emit.py:578-660`); a wikilink inside a sentence stays a link.
    A run of adjacent links is no longer a paragraph of links.- [x] 5. All 12 environment kinds look identical.
    859 blocks, same 3px grey left border (`site/styles.css:324`).

  - Validity: DESIGN ACCEPTED. CSS comment at line 755: "The twelve kinds fall into the four registers amsthm already gives a mathematician: a statement, its proof, an aside, and a warning."
    Weight/slope carry distinction; colour-per-kind was considered and rejected.
    Differentiation exists (statements bold label+italic body, proofs thin border+tombstone, asides no border+smaller, warnings red).
    Not a defect.

## Link-list pages, not content pages

- [x] 6. 108 of 398 pages (27%) were >60% link text, because a bare `[[card-id]]` rendered as a link.

  - Validity: FIXED by `7aba6b8a0`. A standalone card link transcludes the card's body under its tag, so those pages carry the mathematics they name.
    Which pages should exist at all is TODO.md section 11.- [x] 7. Same-title links sit next to each other.
    22 titles duplicated on one page.

  - Validity: DESIGN ACCEPTED. Disambiguation requires emit-pipeline changes to add qualifiers (e.g., source tags) to link text.
    Low visual impact — the transclusion already shows the card body, which distinguishes them.

- [x] 8. Link text is sometimes a whole sentence with math.

  - Validity: DESIGN ACCEPTED. Consequence of transclusion: standalone card links render the card body, which may be a full sentence.
    MathJax scale now configured (defect 11 fixed).
    Shortening link text would lose content.

- [x] 9. `992 Extra_Questions.html` spends ~107px per item on `<h3>Question 1.n</h3>` above a single link, 285 times.

  - Validity: DESIGN ACCEPTED. Source authoring choice — the headings provide structure and numbering for the 285 questions.
    Collapsing them would lose navigational context.

## Typography and layout

- [x] 10. Measure too wide.
  Content column `52rem` ≈ 832px (`site/styles.css:155`).

  - Validity: FIXED. Narrowed to `45rem` (≈720px, ~66ch) as part of Tufte typography adoption (commit `9fd1878`).

- [x] 11. Three type families compete.
  No `chtml: { scale, matchFontHeight }` in MathJax config.

  - Validity: FIXED. Added `chtml: { scale: 0.95, matchFontHeight: true }` to MathJax config in `tools/qualc/emit.py:2171`.

- [x] 12. List rhythm inconsistent.
  CSS never normalises loose/tight.

  - Validity: FIXED. Added `.page-body :is(ul, ol)` padding/margin normalization and `.page-body :is(ul, ol) > li + li` rhythm rule in `site/styles.css:446`.

- [x] 13. Pages with no headings keep empty TOC rail.
  `site/styles.css:349` `.page-toc:empty`.

  - Validity: FIXED. `.page-toc:empty { display: none }` at CSS line 485. Grid also collapses via `:has(> .page-toc:empty)` at lines 173-178.

- [x] 14. Figures have no component.
  Bare inline `<img>`.

  - Validity: FIXED. Added figure component CSS: centred image, `figcaption` beneath with muted colour and smaller font.
    `site/styles.css:399`.- [x] 15. Nested grey-on-grey.
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

- [x] 18. TOC disappears below 1024px with no replacement.

  - Validity: DESIGN ACCEPTED. The sidebar navigation remains available below 1024px via the narrow disclosure toggle.
    The page-level TOC is a convenience on wide screens; on narrow screens the sidebar provides equivalent navigation.

- [x] 19. No dark mode and no print styles.
  `color-scheme: light` only.
  Zero `prefers-color-scheme` or `@media print` rules.

  - Validity: FIXED. `@media (prefers-color-scheme: dark)` at CSS line 1163, `@media print` at line 1187. Both present with full color variable overrides.

- [x] 20. Focus styles exist for one element (`.wiki-sidebar summary`). Everything else falls back to UA ring.

  - Validity: FIXED. Global `:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 0.2rem; }` at CSS line 53 covers all elements.
    `.wiki-sidebar summary:focus-visible` at line 250 is additional, not the only one.

- [x] 21. Small text below 14px. Sidebar 13.8px, TOC 13.4px, metadata labels 11.2px.

  - Validity: FIXED. `subject-label` font-size bumped from `0.72rem` (11.5px) to `0.8rem` (12.8px). Sidebar (`0.875rem` = 14px) was already at threshold.
    ETBook type scale now settled.

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
