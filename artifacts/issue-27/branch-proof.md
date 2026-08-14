# Complex Analysis subject branch: build proof

Manifest: `publications/complex-analysis-guide.yaml`. Built and inspected at `4be4426a`.

`uv run qualc build` -> 8,207 cards and 327 wiki pages OK, 5,791 HTML pages, 13 Complex Analysis guide routes.

The build was run against a copy of the tree, not against the working tree.
See the last section for why, and for what that does and does not leave proved.

## What the branch covers

1,527 cards carry `complex-analysis`. 1,479 of them now carry topics; before this work 161 did.
The classification is what makes the branch traversable at all: a guide panel selects on topic, so before it only `meromorphic-functions` and `residues` could be asked for, and the manifest was a theory spine of 64 references with two panels.
It is now twelve sections, 112 references and 30 panels.

The 48 cards left unclassified are named, not rounded off.
42 are `source` cards, which record a sitting or a homework set and state no mathematics; a study-guide section has nothing to put them under, and a reader reaches them through the exam route instead.
The remaining six have bodies consisting only of image references with no statement in text: `P-642LC`, `P-FWVKJ`, `E-FZLDN`, `E-IYBZP`, `E-G4N4D`, `E-USHMH`.

## Routes

Thirteen routes, one root and twelve sections:

```
/guide/GUIDE-COMPLEX-ANALYSIS.html
/guide/GUIDE-COMPLEX-ANALYSIS/complex-arithmetic-and-elementary-functions.html
/guide/GUIDE-COMPLEX-ANALYSIS/series-and-convergence.html
/guide/GUIDE-COMPLEX-ANALYSIS/holomorphy-and-analyticity.html
/guide/GUIDE-COMPLEX-ANALYSIS/harmonic-functions.html
/guide/GUIDE-COMPLEX-ANALYSIS/cauchy-theory.html
/guide/GUIDE-COMPLEX-ANALYSIS/zeros-and-singularities.html
/guide/GUIDE-COMPLEX-ANALYSIS/argument-principle.html
/guide/GUIDE-COMPLEX-ANALYSIS/residues.html
/guide/GUIDE-COMPLEX-ANALYSIS/conformal-maps-and-the-disc.html
/guide/GUIDE-COMPLEX-ANALYSIS/normal-families-and-omitted-values.html
/guide/GUIDE-COMPLEX-ANALYSIS/special-functions-and-factorization.html
/guide/GUIDE-COMPLEX-ANALYSIS/problems-from-the-qual-sittings.html
```

## What was inspected

All thirteen rendered in headless Chromium at 1440 wide, screenshotted full-page at 1440x3000, and read directly.
Measurements below are taken from the post-MathJax DOM of the same renders, not from the source.

**MathJax.** `<mjx-merror>` count is zero on all thirteen routes, against 44 to 133 typeset containers per section page, so the zero is not the vacuous zero of a page that never typeset anything.

**Root.** Study path listing all twelve sections, the lede naming the three arcs, the ordered list 1 to 12, and `NEXT Complex Arithmetic and the Elementary Functions`. Every section label renders in full; that is a change made because the first render did not (below).

**Harmonic Functions**, one of the five new sections.
Breadcrumb carries the whole chain, `Complex Analysis / Complex Arithmetic and the Elementary Functions / Series and Convergence / Holomorphy and Analyticity / Harmonic Functions`. Six titled blocks, each with its card id beside the heading: `D-CFBSA`, `PR-UWGI6`, `PR-6WOTK`, `PR-QW3ZK`, `C-KOFDQ`, `D-XR64P`. The Laplacian, the mean value integral and both strict maximum principles typeset correctly.
Two panels return 8 problems and 6 exercises, each linked and carrying its id.
Foot navigation reads `PREVIOUS Holomorphy and Analyticity` / `NEXT Cauchy Theory`.

**Residues and Contour Integration.** Breadcrumb shows the second arc, `Complex Analysis / Cauchy Theory / Zeros and Singularities / The Argument Principle / Residues and Contour Integration`. The residue theorem, the order-n formula, the rational quotient rule, the ML bound and Jordan's lemma all typeset, and Jordan's lemma renders its contour as a drawn figure with axes and a labelled arc rather than a missing image.

**Complex Arithmetic and the Elementary Functions.** Fourteen blocks, all typeset.
Four headings render wrong, which is a corpus defect rather than a routing one; see findings.

**Problems from the Qual Sittings.** Four panels, 29 distinct problems, titles typeset including the ones carrying displayed mathematics.
Breadcrumb is the short `Complex Analysis / Problems from the Qual Sittings`, correct for a section hanging off the root, and it carries `PREVIOUS` with no `NEXT`, correct for the last section.

**Special Functions and Factorization** renders, and reading it is what confirmed the section is thin: five of its eleven cards render as raster images of textbook pages rather than authored mathematics.
Six `<img>` elements on that one route, against zero on seven of the other twelve.

## Findings from building it

**The study path rail clips its labels, and this branch was provoking it.** The rail indents one level per section with no cap.
The manifest had been written with `parent` meaning "comes after", making one chain twelve deep, and by Special Functions the label had roughly a 40 pixel column and broke into four fragments.
The manifest now uses `parent` to mean "hangs under" and says the subject is three arcs, which is both true and readable.
The rail defect is untouched and still live: Topology chains all thirteen of its sections and renders "Su" for Surfaces with Manifolds and Duality pushed out of the column entirely.
Real Analysis was already arc-split and already renders cleanly.
This belongs to whoever owns the sidebar, not to a manifest.

**Nineteen card titles open a math span with a space, and lose their operators.** Pandoc does not treat `$ x$` as math when a space follows the opening delimiter, so the backslash commands are dropped and only the surrounding punctuation survives.
Four are Complex Analysis and all four are in this branch's first section: `FF-AGEQ4` and `FF-MV5X6` render as "Relating hyperbolic functions to usual ones: (z) = (?)", `FF-VFWB6` and `FF-VR4UT` as "Angle addition formulas: (x+iy) =.". The other fifteen are Topology 9, Real Analysis 4, Algebra 2. This is the same family as the title defect fixed in `a1c85d4e` and belongs in the same `degenerate-titles` check, which currently does not catch it.

**A panel cannot be titled.** `PublicationQuery` has no heading field, so every panel emits the identical "More from the catalog".
On the four-panel closing section the "On this page" rail lists that phrase four times and a reader cannot tell the panels apart.
This also made the closing section's original lede false, since it promised problems that cut across sections and a topic query cannot express that; the lede now describes what the panels do.

## What this does not claim

**The build was not run against the working tree.** `qualc check` does not pass on `main` at `4be4426a`: six wiki block anchors referenced from the two "Qual Progress" dashboard pages no longer exist on their target pages, which fails reference resolution and stops the build before it emits.
Those files are not this lane's to edit.
The build proved here was run with `--root` against a copy of the tree with those six referencing bullets removed in the copy only.
The removed lines are on Real Analysis and Complex Analysis dashboard pages and are not reachable from any guide route, so no route inspected above depends on the patch, but the claim is "these routes render from this corpus", not "main builds".
Main does not currently build, and that is reported separately.

**Reachability is not proved.** Issue #27 asks that every Complex Analysis source page and extracted card be reachable from the branch.
`tools/audit.py --only orphans` cannot run, because it validates the corpus first and hits the same six references.
The manifest names 112 cards where it named 64, and panels reach several hundred more, but the orphan set for this subject is unmeasured and this proof does not assert it is empty.

**Only the guide routes were inspected.** The wiki pages, the exam routes, search, the generator, and hint and solution disclosure were not exercised.

**The panels were not checked for mathematical correctness of what they return**, only that they return the right kind of card, scoped to the subject, in the numbers recorded.
Reading the cards for the classification did surface mathematics that is wrong or missing; those are recorded on issue #2, not here.

* * *

## Addendum, 2026-08-14: reachability measured, build re-proved on main

Appended after the publisher fixes landed.
The sections above are unchanged; this adds what they left unclaimed.

Pinned revision: `57085cfa9c2089baa8a3bdd811b08f32575585c5`, built in a fresh worktree with no local patching and no `--root` redirection.

**Main builds.
The "main does not build" caveat above is superseded.** `uv run qualc build` exits 0: 8,213 cards and 327 wiki pages OK, 5,822 HTML pages.
The six dead wiki anchors that stopped the build now degrade and warn instead of failing, so the copy-of-the-tree workaround the proof describes is no longer needed.
All thirteen Complex Analysis guide routes emit, at the paths listed above.

**Reachability, the criterion the proof recorded as unmeasured.** `uv run python tools/audit.py --only orphans` runs now.
It reports 15 orphan cards corpus-wide.
Scoped to this subject the set is one card:

```
P-Y37R6   problem   areas=['complex-analysis']   corpus/qrs
```

The other fourteen belong to other subjects: seven problems and one solution (`P-2GD4H`, `P-4T7W2`, `P-BPL7E`, `P-E5NRO`, `P-LCEHH`, `P-LFIZY`, `S-NSNXV`), one strategy card (`ST-DKYXZ`), and the six textbook source cards added for issue #7 (`SRC-TEXT-DF04`, `SRC-TEXT-HAT02`, `SRC-TEXT-HK71`, `SRC-TEXT-HUN74`, `SRC-TEXT-MUN00`, `SRC-TEXT-SMI`), which are unreferenced because the citation link emission that will target them has not landed yet.

`P-Y37R6` is reported, not adjudicated.
Whether it should be reachable, and from where, is a reading decision and is not made here.

**Spot-renders against the descriptions above.** Three routes re-rendered headless at 1440 wide from this build:

| route | `mjx-merror` | `mjx-container` | `img` |
| --- | --- | --- | --- |
| Harmonic Functions | 0 | 53 | 0 |
| Residues and Contour Integration | 0 | 86 | 2 |
| Problems from the Qual Sittings | 0 | 44 | 0 |

All six card ids the proof names on Harmonic Functions are present (`D-CFBSA`, `PR-UWGI6`, `PR-6WOTK`, `PR-QW3ZK`, `C-KOFDQ`, `D-XR64P`). Foot navigation renders on all three.
Residues carries the two drawn contour figures the proof describes.
Nothing regressed against what the sections above state.

## What this addendum still does not claim

**The wiki half of the reachability criterion is not measured.** Issue #27 asks that every Complex Analysis source page *and* extracted card be reachable.
`orphan_ids` returns card ids only, so the orphan measurement above covers cards.
No check here establishes that every Complex Analysis wiki page is reachable from the branch.

**Only three of the thirteen routes were re-rendered**, chosen to match sections the proof describes in detail.
The other ten emit, and were not re-inspected.

**The findings above are untouched.** The clipped study-path rail, the nineteen space-opened math titles, and the untitleable panel are all still live; this addendum measures reachability and re-proves the build, and fixes nothing.

## Addendum part two, 2026-08-14: page reachability, and why the one card orphan stands

Same pinned revision and same build as part one.

**Page-side reachability is complete: 105 of 105.**
Breadth-first traversal of the rendered site starting at
`/guide/GUIDE-COMPLEX-ANALYSIS.html`, following local `href` and `src` links only.
Link extraction and target resolution are lifted from
`artifacts/issue-17/validate-site` rather than written fresh, so both measurements
agree on what counts as a local link. 5,804 pages are reachable from the branch
root; every one of the 105 `wiki/30_Complex_Analysis` pages is among them, and the
unreached set is empty. The per-branch wiki navigation added in `cb9e21dd` is
what closes it.

This is the half the first addendum recorded as unmeasured. Both halves of #27's
reachability criterion now have a number: 105 of 105 pages, and one card.

**`P-Y37R6` is deferred, and the reason is not classification.**
The card states mathematics — a three-part fixed-point problem on the disc with a
Blaschke-factor hint — and it is *already* classified, carrying `fixed-points`,
`schwarz-lemma` and `blaschke-factors`, all three registered. It has its own route
at `/tag/P-Y37R6.html`, appears in the problems index, the generator and the search
index, and is linked from `P-4PTIX`.

What it is missing is a path from *this branch*. It matches the Conformal Maps and
the Disc panel on `schwarz-lemma, blaschke-factors, biholomorphisms`, which has 57
matching problems and `limit: 8`. The card is one of the 49 the limit truncates.
No classification change reaches it: it is already tagged with the topics that
panel selects on. Reaching it needs a manifest change — a larger cap, a narrower
panel, or an explicit `ref` — and that is a decision about what the section should
show, not a tagging gap. Recorded here, not made here.

**Panel limits carry no exact-count tripwire.**
All 30 panels in `publications/complex-analysis-guide.yaml` were checked against
their current match counts in the built catalog. None has a limit equal to its
match count, so none silently truncates the next card classified into its topics.
The two narrowest margins are Normal Families problems at 6 against 7 matches and
Special Functions exercises at 8 against 9; both are one card from becoming exact.
The counts ignore each panel's `review` filter and are therefore upper bounds,
which does not change the verdict for any panel but those two.

The truncation that hides `P-Y37R6` is the same mechanism seen from the other end:
not a limit that has caught up with its matches, but a limit far below them.
