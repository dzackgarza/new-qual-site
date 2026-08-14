# Publisher foundation: the four proofs issue #23 defers

Issue #23 lists four proofs and records that none of them had been run. This is the
record of running all four. **One passes and three fail.** The failures are recorded, not
repaired: every defect below is a measurement, and no source file was changed to make a
number better.

## What was measured, and against what

| | |
| --- | --- |
| Revision | `798748df03c456d2afaa83358eb4ea7fe25a1b66` |
| Working copy | a detached `git worktree` at that revision, under the session scratchpad |
| Build | `uv run qualc build` -> `8208 cards and 327 wiki pages OK`, exit 0, wall 81.4 s, max RSS 628 MiB |
| Served from | `build/quarto/_site` on `127.0.0.1:8742` via `python3 -m http.server` |
| Browser | system Chromium 151.0.7922.137, driven by Playwright |
| Widths | 375x812 and 1440x900 CSS pixels |

The worktree is why the revision is nameable. Other agents were editing `corpus/`,
`vocabularies/` and `wiki/` in the main checkout throughout, and a concurrent
`qualc build` deleted `_site` underneath a first run of these measurements. Every number
below comes from the isolated tree, and every one of them was reproduced there from a
cold build.

**Issue #23's "current 403-page inventory" is stale.** The authored inventory is **327**
pages at this revision. `fd37c3d1` merged the two parallel subject trees and took the
count from 403 to 291; later commits, `fcf76b67` in particular, brought it to 327. The
set-equality proof below is against 327, which is what "current inventory" means now.

## Verdict

| issue #23's proof | result |
| --- | --- |
| Source-page and route manifests are set-equal for the current inventory | **passes**, 327 = 327 = 327 = 327 |
| Semantic comparison rejects dropped authored prose and duplicate/missing routes | **fails** — 1,393 of 58,683 prose words never reach a reader (defects 1 and 2); the route half is proof 1 and passes |
| Static validation reports zero unresolved references, assets, fragments, or macros | **fails** — 116 unresolved fragments (defect 3); references and assets are clean |
| A representative browser replay covers cards, hints/solutions, figures, citations, nested navigation, and desktop/narrow widths | **runs**; every named feature works, and it finds defects 4, 5 and 6 |

Six defects, none repaired here. Defects 1, 2, 3 and 6 belong to the publisher and so to
this issue. Defect 5 originates in authored source and belongs to issue #5, though the
publisher passes it through silently. Defect 4 is a macro-dictionary entry MathJax cannot
render, the family issue #42 closed.

The scripts are preserved beside this file and each is named for the measurement it
takes: `route-set-equality`, `prose-retention`, `missing-fragments`, `div-labelling`,
`replay-wiki-pages`, `narrow-width-overflow`. The static validator is issue #17's
`artifacts/issue-17/validate-site`, reused unchanged.

* * *

## Proof 1 — Route and source set-equality — **passes**

```text
python3 artifacts/issue-23/route-set-equality <worktree>

source_pages: 327
manifest_entries: 327
distinct_routes: 327
emitted_wiki_html: 327
sources_not_in_manifest: 0
manifest_not_in_sources: 0
routes_repeated: 0
routes_not_emitted: 0
emitted_not_in_manifest: 0
routes_not_source_derived: 0
```

Four sets are compared, not two: the `wiki/**/*.md` files on disk, the `source` field of
every `wiki-manifest.json` entry, the `route` field of the same entries, and the
`_site/wiki/**/*.html` files that exist. All four agree, no route is emitted twice, and
every route is its own source path with the suffix changed. Nothing is dropped and
nothing is invented.

**This proof does not establish** that any page's *content* survived. It compares
filenames. Proof 2 is where content is measured, and it fails.

## Proof 2 — Prose retention against the authored source — **fails**

```text
python3 artifacts/issue-23/prose-retention <worktree>

pages_compared: 327
source_prose_words: 58683
words_not_retained: 1393
words_not_retained_excluding_div_titles: 198
pages_with_any_deficit: 117
```

The comparison takes, for each page, the multiset of prose words in the source and the
multiset of prose words a reader can see in the emitted `<main>`, and reports the words
the source carries more often than the page shows. Mathematics is removed from both sides
because the two sides spell one formula differently; so are code, link targets, raw TeX
commands, and the fenced-div class and attribute *names*. Attribute **values** are kept
on the source side, because an authored title is authored prose.

**97.6% of authored prose words reach the page. The 2.4% that do not have two causes,
and both are defects.**

### Defect 1 — 488 authored environment titles are invisible

An authored page writes `:::{.remark title="Shifting"}`. That becomes
`<div class="remark" title="Shifting">`, and an HTML `title` attribute is a tooltip, not
text. The title is in the DOM and not on the page.

```text
python3 artifacts/issue-23/div-labelling <site>

environment_divs: 802
divs_carrying_an_authored_title: 488
pages_carrying_a_titled_div: 94
divs_reaching_the_visible_label_rule: 0
```

1,195 of the 1,393 unretained words are these titles. The same measurement shows the
second half of the defect: **none of the 802 divs is labelled at all.** `styles.css`
gives `div.qual-section` a visible `::before` label from `data-label`, and the emitter
writes that pair for corpus cards — the card page in the replay below shows PROBLEM and
REMARK in small caps. Wiki pages get neither the class nor the attribute, so on a wiki
page a proof, a remark, an example, a fact, a warning, a slogan, a corollary and a
proposition all render as undistinguished prose:

| class | count | | class | count |
| --- | ---: | --- | --- | ---: |
| `proof` | 233 | | `slogan` | 20 |
| `remark` | 206 | | `corollary` | 10 |
| `example` | 168 | | `proposition` | 5 |
| `fact` | 111 | | `solution` | 2 |
| `warnings` | 23 | | `definition`, `claim`, `problem`, `concept` | 1 each |

The `styles.css` comment says this rule exists because `.theorem` and `.concept` once
"came to render as plain prose". On the authored wiki that is still the case for every
class.

### Defect 2 — `\cref` cross-references are dropped, leaving empty list items

`wiki/30_Complex_Analysis/010_Basics/000_Tips_Techs.md` writes its Greatest Hits list as
ten raw-TeX cross-references:

```markdown
- \cref[CauchyTheorem]{Cauchy's Theorem}
- \cref[CauchyIntegral]{Cauchy's Integral Formula}
```

Neither the reference nor its text reaches the page. The emitted list is one real bullet
followed by **ten empty ones**:

```html
<li><p>Estimates for derivatives, mean value theorem</p></li>
<li><p></p></li>
<li><p></p></li>
```

The browser replay counts `empty_list_items: 10` on that route at both widths, and
`shots/crop-greatest-hits.png` shows the ten bare bullets. This accounts for 36 of the
198 words outside defect 1. The build does not warn.

### The remaining 162 words are declared transformations

They fall in four classes, each confirmed by reading the source:

- **Image `alt` text** — `![Squaring](.../2021-12-10_20-25-14.png)` keeps `alt="Squaring"`
  and displays nothing. `model.drop_path_captions` says so in its own docstring: the alt
  "is not displayed, and it is the last pointer from the rendered page back to the file in
  the vault".
- **Citation keys** — `[@DF04]` renders as `[DuFo04]` through citeproc, so the key itself
  is not on the page. Verified on `10_Algebra/10_Basics/00_Syllabus.md`.
- **Footnote labels** — `[^kunneth]`, `[^pullbacks]`, `[^df_p80_identical_disjoint]`
  become numbered marks.
- **Heading attributes** — `## Bounded Variation {#bounded-variation .unnumbered}`.

These are markup, and their loss is correct. I classified them by reading the twelve
largest residue pages plus a sample of the smaller ones; the 28 pages carrying four words
or fewer were classified from their word lists, not by opening each source file.

## Proof 3 — Static validation — **fails**

```text
uv run --with html5lib python artifacts/issue-17/validate-site <site>

html_pages: 5773
html_parse_errors: 0
local_references: 63429
missing_local_targets: 0
missing_fragments: 116
qmd_links: 0
exit 1, wall 18.2 s
```

Issue #23 requires "zero unresolved references, assets, fragments, or macros". Pages,
parses, link targets and asset targets are clean across 63,429 local references. **116
fragments are not.**

### Defect 3 — Obsidian block and heading anchors are not adapted

```text
uv run --with html5lib python artifacts/issue-23/missing-fragments <site>

unresolved_fragments: 116
source_pages: 3
target_pages: 27
shape obsidian block id (^hex): 104
shape other: 12
```

Two distinct failures:

**104 block references.** A source page writes `^9d4269` on its own line to anchor the
block above, and another page links to `...#^9d4269`. The publisher emits no anchor for
the marker — it renders the marker as literal body text, `<p>^9d4269</p>` — so the link
dangles and the reader sees a stray hex token. Site-wide the literal markers are **97
paragraphs on 22 wiki pages**. The replay counts 16 of them on
`0010_Measure Theory.html`, and `shots/crop-cards-2.png` shows them in the rendered page.

**12 heading references.** `[[005_Calculus_Preliminaries#Implicit Function Theorem]]`
resolves its page half and keeps the fragment verbatim, but Pandoc gave that heading the
id `implicit-function-theorem`. The target exists under a slug the link does not use.

All 116 come from three source pages: `20_Real_Analysis/Real Analysis Qual Progress`
(64), `30_Complex_Analysis/Complex Qual Progress` (41), and
`30_Complex_Analysis/000_Resources/00_Study Schedule and Topics` (11). They reach 27
target pages.

Issue #23 says "Stop on an ambiguous reference or an asset collision; do not omit the
page." A fragment that names nothing is neither missing nor ambiguous by the resolver's
test, so the build does not stop, and the reader gets a link to the top of the right page
instead of to the block that was cited.

## Proof 4 — Browser replay — **runs, and finds three more defects**

Nine routes x two widths = 18 loads, plus two disclosure interactions at each width.
Every route was chosen for a feature issue #23 names.

```text
loads: 20            page_errors: 0
non_200: 0           console_errors_or_warnings: 0
                     failed_requests: 0
mathjax_did_not_settle: 0
mjx_merror_total: 4
images_not_decoded: 0
loads_with_horizontal_overflow: 3
```

### What works

**Extracted cards.** Card references are real links: 22 on the Measure Theory page, 64 on
the Real Analysis progress page, 28 on Tips/Techniques, 20 on the wiki root. Following
one reaches its `tag/` page, which renders the statement, the area/institution/year
facets, and its relation groups.

**Hints and solutions.** `tag/P-P2UAH.html` carries three `<details>`; clicking every
summary opens all three, labelled `UGA algebra Fall 2018, problem 1`, `Hint` and
`Solution`, with typeset mathematics inside. Identical at 375 and 1440. This is the only
card on the site carrying both a hint and a solution, so the feature is proved on its
single instance and no more.

**Figures.** Every image that a replayed page requests decodes: 5 of 5 on the Cauchy
Integral Formula page, 14 of 14 on Galois Theory Computations, 19 of 19 overall.

**Citations.** The Algebra syllabus renders `[DuFo04]`, `[Hung74]`, `[Smit]` in place of
its `[@...]` keys and emits four `.csl-entry` bibliography entries.

**Mathematics.** All 20 loads settle, and no `span.math` is left untypeset — 1,382
typeset containers across the replayed routes.

**Navigation.** Every page carries a source-path subtitle and an on-this-page table of
contents (8 to 32 entries on the replayed routes), and the wiki root links to each subject.

### Defect 4 — `\notdivides` renders as a red MathJax error

`mjx-merror` is 0 on every replayed load except Galois Theory Computations, which has 2
at both widths. Both are `\notdivides`. The vocabulary defines it with `\ooalign`,
`\hidewidth` and `\cr` — plain-TeX alignment primitives MathJax does not implement — so
every use renders as a red error box. Six uses on five pages:
`10_Algebra/040_Rings/20_Rings`, `10_Algebra/020_Groups/13_Groups_Classification`,
`10_Algebra/060_Galois/36_Galois_Theory_Computations`, `tag/PR-SLWTB`, `tag/P-QWEAV`.

This is the family issue #42 closed — a macro carried out of a LaTeX preamble that
MathJax cannot render — with one member still live.

### Defect 5 — literal `:::` fence text on eight pages

Eight wiki pages render a fenced-div fence as body text, e.g.
`<p>::: :::{.fact} To count zeros:</p>` on Tips/Techniques. The cause is in the source
line, which puts two fences and a title on one line; the publisher renders it faithfully
and does not warn. Affected: `010_Cauchy_Theorem`, `110_Complex_Preliminaries`,
`020_Residues`, `000_Tips_Techs`, `001_Definitions`, `13_Groups_Classification`,
`091_Appendix Unsorted`, `230_Homology`.

Fourteen further paragraphs across the wiki render a literal `## ` heading marker, from
the same class of source defect: a `[[TAG]]` line immediately followed by a `## Heading`
line with no blank between, which Pandoc reads as one lazy paragraph.

### Defect 6 — 119 of 327 wiki pages scroll sideways at 375px

Three of the nine replayed routes overflow at 375 and none at 1440, so the whole
inventory was swept at that width rather than extrapolated from three pages:

```text
python3 artifacts/issue-23/narrow-width-overflow <base-url> <manifest> <out.json>

pages_loaded: 327
mathjax_did_not_settle: 1
pages_overflowing_375px: 119
overflow_px_min_median_max: 2 51 659
```

Reporting the deepest element carrying the largest excess, the causes split in two:

| widest overflowing element | pages |
| --- | ---: |
| `p.page-subtitle` | 77 |
| MathJax display math (`MJX-CONTAINER`, `MJX-EXT`, `math`) | 37 |
| `article.page-body`, `figure`, `div.remark`, `div.fact` | 5 |

**The 77 are one rule away from fixed.** `p.page-subtitle` holds the source path in a
monospace face with no wrapping rule, so a path like
`20_Real_Analysis/600_Qual_Questions_UGA/0010_Measure Theory.md` pushes the document to
424px inside a 355px column. It is decoration — the reader already has the title — and it
widens the page for every path longer than the column.

**The 37 are real content.** Wide display equations have no horizontal scroll container of
their own, so the page scrolls instead of the equation. `40_Topology/010_Examples/202_Examples`
is the worst at 659px, nearly triple the viewport.

One page did not finish typesetting inside the 15-second budget; its row is marked and its
overflow figure is from an unsettled page.

### What the replay did not exercise

Search, the problem browser, the exam generator, and the guide routes are not in it —
they belong to issues #10 and #30. No deployed host was touched: this is the local
artifact only. Nine of 327 wiki pages were replayed closely; that gap is closed for
layout width only, by the sweep in defect 6.

### Screenshots

Twenty-two full-page PNGs (nine routes x two widths, plus four disclosure-open
captures) in the session scratchpad at
`.../83186ef5-b2d2-4c67-87e9-90920e6fd250/scratchpad/shots/`, with `replay.json` beside
them. They are not preserved in the repository; this document is the durable record.

I opened and read eight of them by eye: `desktop-1440-wiki-root`,
`desktop-1440-cref-tips-and-techniques` and two crops of it,
`desktop-1440-cards-measure-theory` and a crop lower down it,
`desktop-1440-citations-algebra-syllabus` (crop), `desktop-1440-figures-cauchy-integral`
(crop), `desktop-1440-card-target-occurrences` (crop),
`desktop-1440-card-target-hint-and-solution-open` (crop), and
`mobile-375-cards-measure-theory` (crop). The other fourteen were measured but not read,
and I say so rather than claim inspection I did not do.

* * *

## What these four proofs do not establish

- **Not that the site is correct.** 5,773 HTML pages exist. Twenty were loaded in a
  browser and nine of them are wiki pages. The zero page errors, zero console errors and
  zero failed requests are claims about those 20 loads, not about the site.
- **Not that the mathematics is right.** Every measurement here is about bytes, elements,
  words and pixels. Whether a statement is true, correctly attributed, or in the right
  section is not measured and cannot be, per `AGENTS.md`.
- **Not prose equality.** Proof 2 compares word multisets. A page whose every word
  survives may still have been reordered, and the proof would not see it.
- **Not that the declared transformations are the right ones.** It records that alt text,
  citation keys, footnote labels and heading attributes do not reach the page, and that
  the code says so deliberately. It does not adjudicate those choices.
- **Not a claim about macros beyond the ones counted.** Issue #23 asks for zero
  unresolved macros. `mjx-merror` was counted on 20 loads and `\notdivides` was traced
  site-wide; the whole macro dictionary was not diffed against what MathJax implements, so
  defect 4 is a lower bound.
- **Not the deployed site.** Nothing here was measured against
  `dzackgarza.github.io/new-qual-site`.
- **Not a revision other than `798748df`.** `main` moved twice while these ran.
