# Real Analysis subject branch: build proof

Manifest: `publications/real-analysis-guide.yaml`, extended from the four-section workshop spine to twelve sections covering the whole Real Analysis area.

Pinned revision `093fe0a4`, built in a clean worktree: `uv run qualc build` -> 8,213 cards and 327 wiki pages OK, thirteen guide routes whose slugs match the committed manifest exactly.

## What changed since the previous proof

The earlier version of this manifest ordered the Day 4-7 workshop theorem spine and said so: its own closing section recorded that issue #26's reachability criterion was **not** met, because the guide named twenty cards out of an area holding sixteen hundred.
That gap is what this revision closes.

Two things had to happen first.
Every Real-Analysis-area card carrying no topic was read and classified, because a guide reaches cards through topic queries and an unclassified card is unreachable by construction.
And `run_query` was changed upstream to OR its topics rather than AND them, which is what makes a section-sized panel expressible at all; the previous proof recorded the AND behaviour as a blocker, and it is now fixed.

## Routes

Thirteen routes, one root and twelve sections:

```
/guide/GUIDE-REAL-ANALYSIS.html
/guide/GUIDE-REAL-ANALYSIS/sequences-and-series-of-numbers.html
/guide/GUIDE-REAL-ANALYSIS/metric-spaces.html
/guide/GUIDE-REAL-ANALYSIS/continuity.html
/guide/GUIDE-REAL-ANALYSIS/differentiation.html
/guide/GUIDE-REAL-ANALYSIS/riemann-stieltjes-integration.html
/guide/GUIDE-REAL-ANALYSIS/sequences-and-series-of-functions.html
/guide/GUIDE-REAL-ANALYSIS/measure-and-measurable-functions.html
/guide/GUIDE-REAL-ANALYSIS/the-lebesgue-integral.html
/guide/GUIDE-REAL-ANALYSIS/lp-spaces.html
/guide/GUIDE-REAL-ANALYSIS/hilbert-spaces-and-duality.html
/guide/GUIDE-REAL-ANALYSIS/fourier-analysis.html
/guide/GUIDE-REAL-ANALYSIS/problems-from-the-joint-exams.html
```

195 items: 99 cards named explicitly by id, and 96 query panels.

## Reachability

The claim is measured, not asserted, and twice by different means that agree.
Against the rendered HTML, every card id appearing anywhere on the thirteen routes was collected and compared with the area's card list.
Against the pinned build, each card was tested directly for a section that names it or a panel whose kind and topic match it, which needs no render.
The table is the pinned-build measurement:

| kind | reached | in area |
| --- | ---: | ---: |
| problem | 510 | 517 |
| proposition | 103 | 103 |
| theorem | 95 | 96 |
| definition | 71 | 71 |
| fact | 39 | 50 |
| exercise | 48 | 49 |
| solution | 36 | 36 |
| example | 14 | 14 |
| proof | 7 | 7 |
| strategy | 5 | 5 |
| corollary | 4 | 4 |
| lemma | 2 | 2 |

934 of the 954 reached at the pinned revision.
Nine of the twenty misses are exactly the nine this lane deferred, listed under nonclaims below.
The other eleven are trigonometric-value flashcards (`FF-ATMHV FF-CIESS FF-CLFAB FF-SF7VN FF-TGHJ5 FF-TGTS7 FF-VT2E7 FF-W2TS2 FF-XEQFR FF-YBIQV FF-ZQFSR`) that entered the area in `1d49862a`, the math-flashcards ingest, after this lane's classification sweep had finished; they carry no topic yet, so no panel can match them.
They are new unclassified cards in the area, not deferrals of this lane, and classifying them belongs to whoever owns that ingest.
The count is a measurement at one revision of a corpus other lanes are still growing, which is why the revision is pinned.

The method that makes this checkable: the twelve sections partition the topic vocabulary.
Every topic carried by any Real-Analysis-area card belongs to exactly one section, and each section carries one panel per card kind present under its topics, with the panel limit set to the exact count.
A card carrying topics from several sections appears in several, which is wanted; a card carrying none would be unreachable, which is why the classification had to come first.

## Source pages and the occurrence layer

Issue #26 asks for every source page and extracted card to be reachable.
Two card kinds are not reachable *from the guide*, and neither is a gap the manifest can close:

**Source cards** are not a query kind, and should not be: a source card records an exam paper and its provenance, not a statement, so no section wants one under a topic.
All 81 Real Analysis source cards render as their own pages under `/exam/`, reachable from the site's Exams index.
This is why the 81 are also the largest block of cards this lane deliberately left unclassified.

**Occurrence cards** are not a query kind either, and unlike source cards they have **no page anywhere in the site** -- a fact of the site, not of this branch, and true for all 691 Real Analysis occurrences and for every other subject's. They are the rows behind the exam pages: an exam page lists the problems of that sitting and links each to its card.
So a sitting is reachable and its problems are reachable; the occurrence card itself is data, not a page.

## What was inspected

Read directly rather than merely produced.
The repository's `build/quarto` is shared with the other subject lanes, whose concurrent builds delete and recreate files mid-render, so the render under inspection was produced into a private root (`qualc --root`) against the same working tree.

**Root**, headless Chrome at 1440x1400 with a virtual time budget so MathJax completes.
Title, the lede with `$L^p$` typeset inline, and the twelve sections as a numbered list in reading order.

**The Lebesgue Integral**, in the repository render at 1465x812. Full breadcrumb chain back to the root, lede, and the ten explicitly referenced cards as titled blocks each carrying its card id: the definition of `$L^+$` and of the integral, monotone convergence, Fatou, dominated convergence, Markov/Chebyshev with its hand-drawn figure intact, small tails, Tonelli, Fubini, and Fubini-Tonelli.
The supremum-over-simple-functions definition and Chebyshev's `$\alpha^{-p}\|f\|_p^p$` form typeset correctly.
The 151-problem panel renders every problem as a linked title carrying its card id, mathematics typeset in the titles.

**Measure and Measurable Functions**, headless at 1440x2600. Lede, then outer measure, Lebesgue measurable sets, the approximation theorem, existence of a non-measurable set, continuity of measure, measurable functions, simple functions, Borel-Cantelli, Egorov and Lusin, in that order, each with its id.

**Fourier Analysis** and **Problems from the Joint Analysis Exams**, headless at 1440x1100 and 1440x1000, chosen because they are the deepest node of the second chain and the appendix.
The study path renders every one of the twelve section names in full, wrapping rather than clipping, with the two chains visible as two returns to the first indent level and the current node highlighted; there is no horizontal overflow.
The Fourier breadcrumb carries its whole chain, `Real Analysis / Measure and Measurable Functions / The Lebesgue Integral / Lp Spaces and Convolution / Hilbert Spaces and Duality / Fourier Analysis`, and the joint-exams breadcrumb is correspondingly short.
The Fourier lede typesets `$L^1$`, `$L^2$` and `$\hat f$` inline; the transform's definition and the six transform identities render correctly; the thirty joint-exam problems list with their ids and typeset statements.

A third, smaller artifact is visible in the Fourier on-this-page index: the Plancherel card's title contains display mathematics, and the index strips the markup rather than typesetting it, so the entry reads `Plancherel: ‖f‖L22=‖f^‖L2∫Rd|f|2=∫Rd|f^|2`. The title is upstream of this manifest.

## Two defects the rendered pages show

**`\coloneqq` renders as red error text.** `vocabularies/macros.json` defines `\da` and `\definedas` as `\coloneqq`, and MathJax does not define `\coloneqq` -- it is a mathtools command, not core TeX. Every use therefore renders as a literal red `\coloneqq`. Three are visible in the Measure page capture alone: in the outer measure definition, in the Lebesgue measurable set definition, and twice in the continuity-of-measure mnemonic.
141 of the 1,726 Real Analysis cards use one of the two macros, so the defect is corpus-wide rather than particular to this subject.
The macro file is mirrored from the author's pandoc preamble by `sync_macros.py`, so neither the file nor the fix belongs to this lane.

This one is stated from the screenshots rather than from a count.
MathJax on this site runs in the browser, so the error markup is absent from the served HTML, and `--dump-dom` returns inconsistent counts across routes because it samples while MathJax is still working.
A route-level `mjx-merror` census would need a real wait on MathJax's completion promise, which this proof does not claim to have done.

**Every query panel renders under the same heading, `More from the catalog`.** With one panel per section that read fine, and it is what the previous four-section version of this guide showed.
With ten panels in a section the on-this-page index lists `More from the catalog` ten times in a row and a reader cannot tell the definition panel from the problem panel.
The heading is emitted by shared site code rather than by the manifest, so this lane did not change it.

## What this does not claim

The nine cards below are unclassified and therefore unreachable from the guide.
Seven hold only screenshot links where a problem statement should be, one is a bare cross-reference to another card, and one asks the reader to prove three theorems that do not exist in the corpus:

```
P-4FH62  P-FYFEC  P-HKQHN  P-NLNZ3  P-VLG4M     screenshot-only problem cards
E-IAQ6D  T-TRW6N                                 screenshot-only exercise and theorem
P-XKFPD                                          body is only "See \cref{hilbert_space_exam_question}"
P-RA-WORKSHOP-D3-SEQ-15                          "Prove Theorems 2.1, 2.2, and 2.3"
```

Eight occurrence cards are likewise unclassified: six mirror the deferred problems above, and three instantiate problems whose own area is complex-analysis or topology and so belong to another lane's adjudication.

The study path is two chains rather than one.
Sections one through six form the single-variable core in dependency order, sections seven through eleven the measure-theoretic half, and each chain hangs from the root.
A single twelve-deep chain is the honest dependency statement and was built and rendered first, but the sidebar indents by depth: at twelve levels it clipped every section name to a few characters and pushed a horizontal scrollbar into the panel, which the capture of that version shows.
At six it does not, which the Fourier capture shows.
The dependence of the second half on the first is therefore stated in the measure section's lede instead of in the tree.
The numbered list on the root and the foot navigation still carry the full linear reading order.

The twelfth section is not mathematics this guide is claiming.
Thirty problems in the real-analysis area state complex analysis -- entire functions, conformal maps, normal families, residues, Rouche, Hurwitz, Schwarz -- because they come from combined analysis prelims where one paper covers both subjects and the area label followed the paper.
They are collected in a section that says so, to keep them reachable and to make the misfiling visible.
Adjudicating that label is not this branch's to do.

Search, the exam generator, and hint/solution disclosure states were not exercised here.
