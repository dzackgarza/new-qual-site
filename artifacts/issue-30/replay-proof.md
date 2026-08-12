# Full-site publication: browser replay proof

This records the interactive browser replay that issue #30 asks for and that
`deploy-proof.md` explicitly disclaims. It is a read-only verification. No source file
was changed.

## What was replayed, and against what

| | |
| --- | --- |
| Local artifact | `/home/dzack/gitclones/new-qual-site/build/quarto/_site`, served by `python3 -m http.server 8731 --bind 127.0.0.1` |
| Deployed host | <https://dzackgarza.github.io/new-qual-site/> |
| Repository HEAD when the replay started | `7572c98f` |
| Deployed revision when the replay started | `bba5c28a` (GitHub deployment `5874746934`) |
| Driver | Playwright 1.x (Python) driving the system `/bin/google-chrome-stable`, version `151.0.7922.71` |
| Viewports | 375x812, 768x1024, 1024x768, 1440x900 CSS pixels |

The repository moved during the replay. HEAD advanced to `90052fc9` and the deployment
record advanced to `7e4ac34a`, and the run for `90052fc9` failed. At the end of the
replay the Pages host still served bytes identical to the local build for
`/guide/GUIDE-TOPOLOGY.html`, `/guide/GUIDE-COMPLEX-ANALYSIS/residues.html`,
`/problems.html` and `/generate.html`, and the deployed `index.html` was still the same
file fetched at the start. The replay therefore describes the artifact both hosts were
serving throughout; it does not describe `90052fc9`.

### Local and deployed are the same artifact

Every route was captured twice, once per host, with the same driver and settings. **56 of
the 60 screenshot pairs are byte-identical.** The four that differ are `index.html` at all
four widths, and the whole difference is two cells of the summary table: the deployed
build says Propositions 304 / Theorems 302 where the local build says 306 / 304. Every
defect below reproduces on both hosts.

## Route matrix

15 routes x 4 viewports x 2 hosts = 120 page loads, each with a screenshot.

Five guide roots: `GUIDE-ALGEBRA`, `GUIDE-REAL-ANALYSIS`, `GUIDE-COMPLEX-ANALYSIS`,
`GUIDE-TOPOLOGY`, `GUIDE-WORKSHOPS`.
Six terminal sections: `GUIDE-ALGEBRA/sylow-theory`, `GUIDE-REAL-ANALYSIS/uniform-convergence`,
`GUIDE-COMPLEX-ANALYSIS/residues`, `GUIDE-TOPOLOGY/compactness`, `GUIDE-WORKSHOPS/topology`,
`GUIDE-WORKSHOPS/complex-analysis` (the last carries 40 figures and was added to cover
diagrams).
Four tool surfaces: `/`, `/exams.html`, `/problems.html`, `/generate.html`.

Exercised outside the viewport matrix: `/tag/P-25AFH.html`, `/tag/P-P2UAH.html`,
`/tag/P-VGN3T.html`, `/exam/SRC-JHU-RA-FALL-2017.html`, and
`/wiki/10_Algebra/100_Linear_Algebra/120_RCF.html` (reached by clicking a search result).
`/guides.html` and `/wiki/index.html` were checked for status only.

## Screenshot inventory

172 PNGs, 39.1 MB, in the session scratchpad at
`/tmp/claude-1000/-home-dzack-gitclones-qual-review-and-solutions-broken-pack-preserved/f74b57aa-8084-4694-8f97-57ab482186d7/scratchpad/`:

| directory | files | contents |
| --- | ---: | --- |
| `shots-local/` | 60 | 15 routes x 4 viewports, local |
| `shots-deployed/` | 60 | the same 15 x 4, deployed |
| `shots-interact/` | 22 | search, filter, disclosure, sitting, generation at 1440 and 375, local |
| `shots-interact-deployed/` | 22 | the same interaction set, deployed |
| `shots-gen/` | 4 | generation with a fixed problem set, all four widths |
| `shots-mobile/` | 4 | touch-emulated 375 device: search, disclosure, generation |

These files are in a session scratchpad and are not preserved in the repository. The
observations below are the durable record.

### Which images were inspected by eye

I opened and read 20 images: `index-375`, `problems-375`, `problems-1440`, `exams-375`,
`generate-375`, `generate-768`, `root-algebra-375`, `root-topology-375`,
`term-real-uniform-375`, `term-complex-residues-375` (plus a magnified crop),
`term-topology-compactness-1440`, `term-workshops-topology-375`,
`term-workshops-complex-375`, deployed `term-workshops-complex-768`, `search-Problem`,
`filter-zzzznomatch`, `P-P2UAH-collapsed`, `P-P2UAH-open`, `generate-sheet-1440`,
`genfixed-375`, `mobile-generate`, `sitting`.

The other 150 were measured but not read by eye. For the deployed set this is not a gap:
56 of its 60 files are byte-identical to local files, so inspecting the local file is
inspecting the deployed pixel. For the remaining local files the evidence is
instrumental only, and I say so rather than claim inspection I did not do.

## Console, network and MathJax measurement

Every one of the 120 loads recorded `pageerror` events, console messages of type `error`
and `warning`, failed requests, and responses with status >= 400.

**Across the 120 route-viewport loads I performed, there were zero uncaught page errors,
zero console errors, zero console warnings and zero failed requests.** One response was a
transient HTTP 503 from the Pages CDN for
`assets/figures/Pasted%20image%2020210527172954.png` during
`term-workshops-complex@768`; three immediate retries returned 200, and the local copy is
present. I treat it as CDN load shedding under my parallel capture, not a site defect.

This is a claim about the 120 loads I performed. It is not a claim that the site has no
console errors: 5,786 HTML pages exist and I loaded 20 distinct ones.

### The `mjx-merror` metric used in `deploy-proof.md` undercounts MathJax failures

`mjx-merror` was 0 on all 120 loads, including in the document head. The "every page
carries exactly one from MathJax's own stylesheet" caveat did not reproduce; a clean page
reports 0, so any nonzero count is a real failure.

But `tex-chtml-full` loads the `noundefined` extension, which renders an **undefined
control sequence as red text and emits no `mjx-merror` at all**. Counting `mjx-merror` is
therefore blind to the entire undefined-macro class. Measuring red-rendered tokens
instead, the 15 routes carry 5:

- `/guide/GUIDE-COMPLEX-ANALYSIS/residues.html` — `\elts` twice, in the statement of the
  residue theorem. The set of poles renders as a red literal `{\eltszN}` instead of
  `{z_1, ..., z_N}`. Visible at all four widths.
- `/problems.html` — 3 tokens, `\oldexp` and a stray `\(`.

`\oldexp` is a self-inflicted break in the macro dictionary itself: the config defines
`"exp": ["\\oldexp\\qty{#1}", 1]` but never defines `\oldexp`. Every `\exp{...}` on the
site fails. Counting uses inside `span.math` across the built site: `\exp` 30 uses on 11
pages, and eight further undefined names — `\Deck` 9, `\SS` 9, `\TT` 12, `\matt` 11,
`\correspond` 15, `\Ind` 9, `\CRing` 8, `\elts` 1 — for about 104 uses on at most 40
pages. I checked these nine names specifically; I did not diff every macro used on the
site against MathJax's full command table, so this is a lower bound.

Where the generator injects content after page load, real `mjx-merror` elements do appear.
See defect 1.

## What was exercised, and what it did

### Typed search — works

`/` search dialog, opened with the button and driven by typing. One query per type:

| query | intended type | result |
| --- | --- | --- |
| `card archives` | Page | 2 results, both `Page` / "authored wiki page" |
| `cantor set nowhere dense` | Card | 3 results; first is `Card` `C-44LL4` "The Cantor set is nowhere dense.", plus 2 `Problem` |
| `companion matrix` | Problem | 13 results spanning `Page`, `Card` and `Problem` (`E-2JG2B`) |
| `sylow` | mixed | 30 results |

A one-character query returns nothing (by design, the code requires two). A nonsense
query returns an empty list. Clicking the first `companion matrix` result navigated to
`/wiki/10_Algebra/100_Linear_Algebra/120_RCF.html` and the page rendered. Identical
behaviour on the deployed host. The search index is one 3.8 MB `search.json` holding 5,781
records: 3,047 Problem, 2,376 Card, 358 Page.

### Problem filter — works

`/problems.html` renders all 3,047 problem rows. Typing into the filter hides
non-matching rows live: `sylow` 22 visible, `uga 2017` 81, `complex-analysis` 466,
`zzzznomatch` 0, and clearing restores 3,047. Identical on the deployed host.

### Problem hint and solution disclosure — works

`/tag/P-P2UAH.html` collapsed shows three closed `<details>`: an occurrence, `Hint`,
`Solution`. Opened, the hint reads "Normality of P buys you a subgroup PS, not merely a
subset. Compute its order." and the solution renders the full Sylow argument with
typeset display math and no MathJax error. `/tag/P-25AFH.html` and `/tag/P-VGN3T.html`
behave the same for their solutions. Verified again on a touch-emulated 375px device:
tapping each summary opens it, no horizontal overflow, `mjx-merror` 0.

Corpus scale of the feature: 802 `qual-solution` and **2 `qual-hint`** disclosures site
wide; `index.html` reports 1 hint card. Hint disclosure is proved on the single instance
that exists.

### Exam sittings render and link forward

`/exam/SRC-JHU-RA-FALL-2017.html` renders, typesets, and links to its problem. Across all
273 sitting pages there are 2,798 forward links to `tag/*`, matching the occurrence count
on the home page. No sitting page has zero links.

### Diagrams render

Figures are raster images, not SVG or TikZ. 621 `<img>` references across the built site,
**0 of them missing on disk**. The Tube Lemma diagram on
`/guide/GUIDE-TOPOLOGY/compactness.html` and the 40 pasted figures on
`/guide/GUIDE-WORKSHOPS/complex-analysis.html` all loaded, at every width, on both hosts.
No broken image was observed except the one transient CDN 503 above.

### Citations do not render

See defect 7.

---

## Defects

### 1. `/generate.html` prints worked solutions inside the exam — the make-me-a-qual surface is not statements-only

This is the headline failure. Issue #30 requires "statements-only exam generation".

The generator embeds its own copy of the catalog as `const QDATA` inside `generate.html`.
The catalog identity is correct: 3,047 ids, matching the 3,047 `Problem` records in
`search.json` and the 3,047 rows of `/problems.html` exactly, with no id on either side
missing from the other. So it does consume the same canonical problem catalog.

What it does not share is the body extraction. The canonical page at `tag/<id>.html`
splits the card: the statement is the article body, and solution, proof, strategy,
concept and warning material sits inside `<details>` disclosures. `QDATA[i].q` takes the
**whole card body including those blocks**.

Counting the blocks inside `QDATA` bodies:

| block | problems affected |
| --- | ---: |
| `<div class="solution">` | 385 |
| `<div class="concept">` | 162 |
| `<div class="proof">` | 85 |
| `<strong>Solution:</strong>` | 61 |
| `<div class="strategy">` | 25 |
| `<div class="warnings">` | 10 |
| `<strong>Hint</strong>` | 4 |
| `(DZG)` author asides | 8 |
| **distinct problems carrying at least one** | **464 of 3047 (15.2%)** |

For all 464, the canonical `tag/<id>.html` body hides the block and `generate.html`
inlines it. This is not a corpus problem; it is a divergence between two extractions of
the same corpus.

At the page's default of 8 problems, the chance a sheet prints at least one worked
solution is **1 - (1 - 0.152)^8 = 73%**.

Observed, not merely computed. In `shots-interact/generate-sheet-1440.png`, a 6-problem
Algebra set at 1440:

- Item 1 (`P-OQCJR`) is not a problem at all. It reads "We want to show that Ax = 0 has a
  nontrivial solution <=> rank(A) < m. =>: Suppose Av = 0 for some v != 0. Then dim ker A
  >= 1, and by rank nullity ..." — a complete proof, numbered as question 1.
- Item 2 (`P-EI5VA`) prints the three-part statement, then a concept sheet listing
  orbit, stabiliser, orbit-stabiliser and Burnside's lemma, then the full worked solution.
- Item 3 (`P-23M4O`) prints "Lemma: ... Proof: ..." and ends with a red `\qed`.

Route: `/generate.html`. Viewports: all four, and on the deployed host. Reproduced with a
fixed problem set (`shots-gen/`) so it is not an artefact of one random draw.

Two smaller things fall out of the same extraction. Items 4 and 5 of that sheet were
"State the structure theorem for semisimple Artinian rings." and "Do you know about
singular value decomposition?" — flashcard prompts, not qual problems, drawn from a
catalog that labels them `Problem`. And two `QDATA` bodies are empty; the generator's
`q.q.length > 10` guard silently drops them.

### 2. `/generate.html` overflows horizontally at every viewport once a set is generated

With six fixed problems in the sheet, `document.documentElement.scrollWidth` measures:

| viewport | scrollWidth | overflow |
| ---: | ---: | ---: |
| 375 | 2577 | 6.9x the viewport |
| 768 | 2583 | 3.4x |
| 1024 | 2591 | 2.5x |
| 1440 | 2695 | 1.9x |

At 375 the page is unusable: the control column keeps its full width and the sheet is
pushed off-screen, so each line of each problem shows about five characters
(`shots-gen/genfixed-375.png`). Re-checked with real touch emulation
(`shots-mobile/mobile-generate.png`): same result, and `window.innerWidth` reported 510
instead of 375 as the browser shrank to fit. Horizontal scrolling at 375px is the defect
the task names; here it is present at all four widths.

At 1440 (`shots-interact/generate-sheet-1440.png`) the prose and the display equations are
visibly clipped at the right edge — for example `H <= N_G(` and `1 = |X/G| = (1/|G|) sum`
are cut mid-formula.

The print button (`window.print()`) inherits this layout.

### 3. `/generate.html` produces MathJax errors that the same content does not produce on its own page

The fixed six-problem sheet yields **8 `mjx-merror` elements inside `#gen-sheet`**, at
each of the four viewports. The failing constructs are `&`-aligned blocks with `\\` that
are not wrapped in an environment, plus `\qed`:

```
h \in \Stab(x) &\iff h\cdot x = x && \text{by being in the stabilizer} \\ ...
\abs{\Union_{g\in G}gHg\inv} &< (\text{Number of Conjugates of } H) \cdot ...
\lambda(E) \definedas \int_E f ~d\mu &= \lim_{n\to\infty} \theset{...
BA^k \vector v &= A^k B\vector v \\ &= A^k p(A) \vector v ...
\qed   (twice)
```

Root cause, and it is precise. The MathJax config installs a `startup.pageReady` hook that
finds `.math.display` blocks containing a bare `&` and rewraps them in
`\begin{aligned}...\end{aligned}`. That hook runs **once, at page ready**. The generated
sheet is injected afterwards and calls `MathJax.typesetPromise([sheet])` directly, so it
never gets the rewrap. The same `\lambda(E) \definedas ...` block renders cleanly on
`/tag/P-25AFH.html`, where the hook did run — that page measures `mjx-merror` 0. So this
is a repair that exists but is not applied on the dynamic path.

Route: `/generate.html` after pressing "Generate set". Viewports: 375, 768, 1024, 1440.
Both hosts.

### 4. Occurrence disclosures do not link to the sitting

Issue #30 asks for "occurrence links from a problem to the sitting it appeared in". They
do not exist. **No page under `tag/` contains a single link to `exam/SRC-*.html`.** The
only pages that link to sittings are `/exams.html` and the five wiki source archives.

What the occurrence disclosure actually contains, in the two shapes I found:

- `/tag/P-25AFH.html`, `/tag/P-VGN3T.html`: summary "UGA real-analysis Spring 2017,
  problem 2"; opened body "P-25AFH appeared at UGA real-analysis Spring 2017, problem 2",
  where `P-25AFH` is a link **back to the page you are already on**. I followed it: it
  reloads the same URL.
- `/tag/P-P2UAH.html`: summary "UGA algebra Fall 2018, problem 1"; opened body is a
  verbatim second copy of the statement printed immediately above it, with no link at all.

The reverse direction works (2,798 sitting-to-problem links), so the data exists and only
the problem-side link is missing. Route: every problem page. Viewports: all. Both hosts.

### 5. `/problems.html` overflows at 375, and its catalog is visibly degenerate

`problems@375` measures `scrollWidth` 396 against a 375 viewport. The offenders are a
`.problem-row`, an `<a>`, an `<img>` and a `<code>`, all reaching x = 382-396.

Looking at the page rather than the numbers, the first screen of the canonical problem
browser at 1440 is mostly broken entries:

- Two rows use an entire embedded exam scan as the row title (`P-FWKVJ`, `P-IC2GD`), one
  of which shows the author's red-flag annotation.
- Titles that are raw unrendered TeX: `$(x) + (y) = 2 () (\frac {x - y}{...` (`P-PC2H7`),
  `$|f|(, s)J = {z D_s(z_0)}|f(z)...` (`P-S5FOO`).
- Titles that are fragments of a proof rather than a statement: `<= : Suppose that
  Ax = b has a solution $...` (`P-DB3EP`), and `=> :` alone (`P-HGQ8T`).
- Titles that are a bare formula: `|G| < oo` (`P-AMD-EKBYIW4X`), `S_m v S_n`
  (`P-AMD-IJD6LW4S`).
- Titles missing their first word: "R be a commutative ring with identity and let n be a
  positive inte..." (`P-SD043`).
- Enumeration debris kept in the title: `(1) Y is metric space...`, `(a) f(z) = ...`,
  `(June 2014 1)Define alpha: [-1,1] -> R by`.
- One title is literally `(Images)`.

Because rows sort by title string, `$`, `(` and the arrows sort first, so the degenerate
entries occupy the opening screen.

Measured over the 3,047 problem records:

| condition | records |
| --- | ---: |
| title contains raw `$` | 1,873 |
| title is 12 characters or fewer | 124 (29 titled exactly `Let`, 20 exactly `Show that`) |
| title begins with punctuation or enumeration | 316 |
| duplicate titles | 216 distinct titles covering 541 records |
| **at least one of the above** | **2,072 of 3,047 (68%)** |

`deploy-proof.md` records the residual as "one degenerate title". By any reader-facing
measure that is a large undercount.

The raw `$` matters twice over: `/problems.html` typesets row titles, but the search
dialog sets `link.textContent = record.title` and never typesets, so all 1,873 appear as
literal dollar-delimited source in search results. Visible in
`shots-interact/search-Problem.png`.

### 6. `/guide/GUIDE-WORKSHOPS/topology.html` overflows at 375, 768 and 1024

Measured `scrollWidth` 773 at both 375 and 768, and 1073 at 1024; only 1440 fits. The
overflowing elements are all `<code>`.

The cause is visible in the screenshot: several cards publish their raw markdown source.
`P-MFWBK` is titled `Q` with body `- $\QQ$`. `P-HPN6K` is titled `Z` with body
`- $\ZZ$ - $\ts{1}$ - $\ts{p \in \ZZ^{\geq 0} \st p\text{...` running off the right edge.
`P-N7RR5` is a one-line code block "Is it true that the interior of a..." that does the
same. Single-character card titles and unprocessed TeX in `<code>` are both present on a
published branch terminal.

### 7. Citations are not processed; the raw `[@key]` source shows to the reader

Two pages carry citations: `/wiki/40_Topology/000_Basics/000_Preface.html` and
`/wiki/10_Algebra/10_Basics/00_Syllabus.html`. Pandoc recognised them — the markup is
`<span class="citation" data-cites="dummit_foote_2004">` — but no CSL processing ran, so
the span's text is the literal `[@dummit_foote_2004]`. 21 such tokens across 6 keys
(`dummit_foote_2004`, `hoffman_kunze_1981`, `hungerford_2008`, `smith`, `munkres_2018`,
`hatcher_2002`).

**No page in the built site contains a `csl-entry`**, so no bibliography is rendered
anywhere and none of the six keys resolves to a reference.

These two routes are outside my 15-route viewport matrix; the finding is from the built
HTML, not from a rendered inspection.

### 8. Figure captions are raw vault attachment paths

Every pasted figure carries its source path as both `alt` and `<figcaption>`, so the
caption a reader sees is `_attachments/Pasted image 20210517025125.png`. 93 such
figcaptions on 22 pages. Two of the routes in the matrix are affected:
`/guide/GUIDE-WORKSHOPS/complex-analysis.html` (71 occurrences of the string; visible at
all four widths on both hosts) and `/guide/GUIDE-TOPOLOGY/compactness.html`, whose Tube
Lemma diagram is captioned `figures/image_2021-05-21-00-28-13.png`.

On that workshops page the figures are also scaled to a small fraction of the column, so
at 375 each pasted exam scan is an illegible thumbnail followed by a filesystem path.

### 9. `/problems.html` claims the URL is the query; it is not

The page's own lede reads "Every problem in the corpus. Filter by any facet; the URL is
the query." Measured:

- typing `sylow` into the filter leaves the URL at `/problems.html` — no history entry, no
  query string, no fragment;
- loading `/problems.html?q=sylow` leaves the filter empty and all 3,047 rows visible;
- loading `/problems.html#sylow` does the same.

Filter state is neither shareable nor bookmarkable, and the page states the opposite.

### 10. Zero-result states are silent

A filter query matching nothing hides all 3,047 rows and shows nothing else — no count,
no "no matches", just the input above empty space (`shots-interact/filter-zzzznomatch.png`).
There is no result count at any time, matching or not. The search dialog has the same
shape: it caps results at 30 with no total and no way to see more, so `sylow` and `the`
both report exactly 30.

### 11. Author TODOs are published

`/guide/GUIDE-WORKSHOPS/complex-analysis.html` publishes "Part 2: ???? Todo get help" as
body text, at all four widths on both hosts. Four further `todo:` markers exist in the
built HTML.

### 12. Minor

- Search results have no relevance ranking. `companion matrix` returns four wiki Pages
  before the `Companion Matrix` definition cards and the matching Problem, because
  results are taken in catalog order and truncated at 30.
- `/exam/*.html` prints "1 problems, in the order they appeared." — no pluralisation. 38 of
  the 273 sittings hold exactly one problem, so this is the common case, and an
  unnumbered occurrence renders its position marker as a bare `?`.
- Guide roots print the branch name as a breadcrumb directly above the identical `h1`.
- Occurrence disclosure on `/tag/P-P2UAH.html` duplicates the statement verbatim.
- Touch targets: on the 375 viewport, 191 of the 199 interactive elements on
  `/exams.html` and 8 of 12 on `/` are under 32px tall. Most are inline text links, which
  the WCAG target-size rule exempts, but `/exams.html` is a 273-item list whose entire
  purpose is tapping.

---

## What I could not exercise, and why

- **Route coverage.** The build holds 5,786 HTML pages. I loaded 20 distinct routes. No
  statement here covers the 5,766 I did not open — in particular the 5,151 `tag/` pages,
  the 273 `exam/` pages and the 327 wiki pages are represented by 3, 1 and 1 samples.
- **Image inspection.** 20 of 172 screenshots were read by eye. The rest were measured
  (scrollWidth, `mjx-merror`, broken images, target sizes, console, network) but not
  looked at. For the deployed set this gap is closed by byte-identity with local files;
  for the remaining local files it is not.
- **The revision under test is not current.** HEAD is now `90052fc9`, whose deploy run
  failed, and which includes `183b72c6 "restore the author's macro set and wrap alignment
  inside environments"` — plausibly a fix for defects 3 and the `\oldexp` half of the
  MathJax finding. Nothing here says whether that commit fixes them. This replay covers
  the artifact both hosts served during the capture window, which still carries `\oldexp`
  in its deployed macro block.
- **Printing.** I did not render `/generate.html` through a real print pipeline; the
  "Print / PDF" button was clicked only as far as confirming it calls `window.print()`.
- **Undefined macros are a lower bound.** I confirmed nine undefined names by construction
  and measured 5 red tokens on the 15 routes. I did not diff every macro used across the
  site against MathJax's full command table, so more may exist.
- **Screenshots are not preserved.** They live in a session scratchpad, not in the
  repository. Reproduce with `shots2.py`, `interact.py`, `genprobe.py` and `mobile.py`
  from that scratchpad, or re-derive from the description above.
- **No accessibility, performance or cross-browser audit** was run. One browser engine,
  one Chrome version, no assistive technology, no throttling.

## Bottom line against issue #30's acceptance text

| #30 requires | status |
| --- | --- |
| search | exercised, all three types, works |
| filters | exercised, works; but the page's URL claim is false and the empty state is silent |
| occurrence links to the sitting | **absent** — no problem page links to any sitting |
| problem disclosure, collapsed and opened | exercised, works; hint disclosure exists on 1 card |
| diagrams | render; captions are raw file paths |
| citations | **do not render** — literal `[@key]` text, no bibliography anywhere |
| statements-only generation | **fails** — 15.2% of the catalog carries solutions into the sheet; ~73% of default sheets contain one |
| screenshots at 375/768/1024/1440, manually inspected | captured on both hosts; 20 inspected by eye, the rest measured |
| deployed host receives the same replay | done; 56 of 60 screenshots byte-identical to local |

Three of the seven named interactions do not do what the issue requires. The claim is not
supportable as written.
