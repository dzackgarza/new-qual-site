# Design Issues: Wiki

Reviewed the wiki as rendered: 12 pages across every page type, in the browser at 540px and re-rendered at 1440px and 375px (your window manager pins the Chromium window at 540, so the three-column desktop layout had to be captured separately). Frequency counts come from the built HTML in `build/quarto/_site/wiki` (398 pages).

## Broken, visible on almost every page

**1. Sidebar disclosure triangle sits above its label.** Every collapsible entry takes two lines: `▶` on one, the name on the next. Cause is `.subject-sidebar a { display: block }` (`site/styles.css:194`) applied to the `<a>` inside `<summary>`. I isolated it: same markup with `display:inline` puts the caret and label on one line and halves the sidebar height. Right now one expanded subject makes the rail 1400px tall.

**2. Clicking a section name navigates instead of expanding.** The markup is `<summary><a>Prelims</a></summary>`. I clicked "Prelims" in the mobile nav; it left the page and the panel closed. The only expand target is the ~10px triangle — far below the 44px touch minimum, and on mobile the panel is capped at `50vh` with its own scrollbar.

**3. 163 blocks print a literal `?` as their title,** on 63 pages. Source is `:::{.proof title="?"}` (e.g. `wiki/10_Algebra/01_Groups/12_Sylow_Theorems.md:28`). The emitter writes the authored title as body text (`.qual-section-title`), so the placeholder renders under the PROOF label.

**4. Adjacent links merge into one underlined run.** 151 paragraphs on 78 pages hold 2+ wikilinks separated only by a space. On `00_Prelims/Worked_Exams/2016 Fall.html` nine links form a single block of underlined text; at 540px you cannot see where one ends. Source: bare `[[P-XXXXX]] [[P-VPCLD]] …` lines.

**5. All 12 environment kinds look identical.** 859 blocks render with the same 3px grey left border and grey small-caps label (`site/styles.css:530`). A Warning, a Proof, a Definition and an Example are indistinguishable. `.theorem` and `.concept` get no treatment at all — the stylesheet comment already admits this.

## The dominant page shape is a link list, not a page

**6. 108 of 398 pages (27%) are more than 60% link text.** `40_Topology/02_Point_set/001_Definitions.html` is a "Definitions" page containing no definitions: 198 links, one per paragraph, ~42px apart. Root cause is that a bare `[[card-id]]` renders as a link and never transcludes the card. There are 3,968 such lines across 245 pages. The wiki source has exactly **one** `.definition` environment — the definitions live in `corpus/` and are only pointed at.

**7. Same-title links sit next to each other.** That page links 22 titles twice ("Locally Compact", "Dense subspace", "Hausdorff space", "Boundary of a subset"…) — distinct cards sharing a title, visually identical, no way to choose.

**8. Link text is sometimes a whole sentence with math in it.** "Closed Sets: A set $U \subseteq X$ is closed in $X$ iff…" as link text: the underline cuts through subscripts, and MathJax spacing blows gaps around operators (`SO(2) ⊲ SL₂(R)` on `992 Extra_Questions.html`).

**9. `992 Extra_Questions.html` spends ~107px per item** on an `<h3>Question 1.n</h3>` above a single link, 285 times. The TOC then lists 285 entries reading "Question 1.1 … Question 1.37", carrying no information. Some headings keep a stray period ("Question 1.6.").

## Typography and layout

**10. Measure is too wide.** Content column is `52rem` ≈ 832px (`site/styles.css:140`) at 16px body — roughly 100 characters per line. 65–75ch is the readable band.

**11. Three type families compete:** Inter for body, Charter for headings, MathJax TeX serif for math. Inline math reads visibly larger than the sans around it. There is no `chtml: { scale, matchFontHeight }` in the MathJax config.

**12. List rhythm is inconsistent** — loose lists ~42px between items (Algebra index), tight lists ~26px (Archives/Topics), on pages a click apart. Markdown loose/tight leaks straight through; the CSS never normalises it.

**13. Pages with no headings keep the empty TOC rail.** `10_Algebra/11_Resources/index.html` shows three lines of body next to a 1200px sidebar and ~280px of reserved dead space.

**14. Figures have no component.** Images are bare inline `<img>`. On `031_Conformal_Standard.html` the word "Generally," strands at the right edge of a figure; on `202_Examples.html` an image-grid caption sits left-aligned under the wrong column, a display equation runs two definitions together on one line, and a lone `.` drops onto its own line.

**15. Nested grey-on-grey.** A blockquote inside an EXAMPLE gives a grey left border inside a grey left border. Three different meanings share one container style: "Wiki navigation", "Solution", and "What links to this" are all the same grey box.

**16. Naked URLs as link text** (the Keith Conrad PDF on the Sylow page) — overflows the column on mobile.

**17. Card pages show "None." cards.** On `tag/P-A4JGH.html`, DEPENDENCIES and BACKLINKS render as empty cards, and the fourth card ("What links to this") breaks the 3-column grid. Metadata labels are `0.7rem` (11px) uppercase; `status: draft` is exposed raw.

## Responsive, theme, accessibility

**18. The TOC disappears below 1024px with no replacement** (`site/styles.css:718`). Long pages get no in-page navigation on any phone or tablet.

**19. No dark mode and no print styles.** `color-scheme: light` only, zero `prefers-color-scheme` or `@media print` rules — for a site people read at night and print before exams.

**20. Focus styles exist for one element** (`.wiki-sidebar summary`). Everything else falls back to the UA ring.

**21. Small text below 14px:** sidebar 13.8px, TOC 13.4px, metadata labels 11.2px, environment labels 13.6px at 65% opacity. Sidebar leaf links use `--muted` and inherit it, so links look like disabled labels; only the current page has contrast.

**22. Sticky header ghosting.** `backdrop-filter: blur(12px)` over 94% white lets scrolled content smudge through behind the brand at narrow widths.

**23. URLs carry spaces and mixed case** — `992 Extra_Questions.html`, `2016 Fall.html` — and hrefs embed the raw spaces.

## Search

**24. There is no ranking.** `site/app.js:38` filters and takes the first 30 in index order. Searching "sylow" returns "Basics", "Classification", "Galois Theory" and two rows both named "Algebra" above and around the actual "Sylow Theorems" page. The index holds 4,921 Problems and 4,272 Cards; none surfaced for that query.

**25. Every result row says "Page" and nothing else.** `.search-result-detail` is `display:none` below 38rem, so the only discriminator is hidden exactly where rows are most ambiguous. No path, no snippet.

The preview server is still running on port 8412 (`build/quarto/_site`) if you want to walk any of these yourself. Tell me which cluster to fix first — items 1, 2, 3 and 24 are each a few lines and land immediately; item 6 is the one that changes what the wiki *is*, and needs a decision from you about transclusion before I touch anything.
