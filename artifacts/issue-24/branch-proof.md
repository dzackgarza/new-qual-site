# Prelim subject branch: build proof

Manifest: `publications/prelims-guide.yaml`. Built and inspected at `22377eac`, in a
worktree pinned to that commit rather than in the shared checkout.

`uv run qualc build` -> 8,213 cards and 327 wiki pages OK.

## What the branch is

UGA's preliminary exam is one paper over calculus, linear algebra and algebra, and the
corpus holds it as 419 cards: 198 problems, 189 occurrences, 29 exam sittings, 3
solutions, and **no definitions, theorems or propositions at all**. So this branch is a
reading order over problems, not a theory spine with problems hanging off it. Every one of
the 198 problems is referenced by exactly one section; nothing is published twice.

| section | problems |
| --- | ---: |
| Logic and Proof | 28 |
| Limits and Continuity | 7 |
| Integration Techniques | 61 |
| Sequences and Series | 10 |
| Multivariable Calculus | 20 |
| Linear Algebra | 18 |
| Groups | 17 |
| Rings and Modules | 23 |
| Fields and Galois Theory | 10 |
| Complex Numbers | 4 |
| Counterexamples | catalog panel, 16 |

Counterexamples is the one section published as a query rather than as references. All
sixteen of those problems appear above in the subject section they also belong to, so it
is a cross-cutting revision index rather than a first appearance, which is what a catalog
panel is for.

## Routes

Twelve emitted, one root and eleven sections:

```
/guide/GUIDE-PRELIM.html
/guide/GUIDE-PRELIM/logic-and-proof.html
/guide/GUIDE-PRELIM/limits-and-continuity.html
/guide/GUIDE-PRELIM/integration-techniques.html
/guide/GUIDE-PRELIM/sequences-and-series.html
/guide/GUIDE-PRELIM/multivariable-calculus.html
/guide/GUIDE-PRELIM/linear-algebra.html
/guide/GUIDE-PRELIM/groups.html
/guide/GUIDE-PRELIM/rings-and-modules.html
/guide/GUIDE-PRELIM/fields-and-galois.html
/guide/GUIDE-PRELIM/complex-numbers.html
/guide/GUIDE-PRELIM/counterexamples.html
```

The id is `GUIDE-PRELIM`, not `GUIDE-PRELIMS`: `PublicationManifest.area` derives the query
scope by stripping `GUIDE-` from the id, so `prelims` would scope every query to an area no
card carries.

## What was inspected

Headless Chrome at 1440x1100, full-page screenshots of all twelve routes, read directly
rather than merely produced.

**Every route:** zero `mjx-merror`, zero `pre > code` blocks, no horizontal overflow at
375, zero uncaught page errors.

**Root.** Title `Prelim`, the lede, all eleven sections listed in reading order, `NEXT
Logic and Proof`. The study-path sidebar shows the dependency tree with every section name
legible: Logic and Proof at depth one carrying Limits and Continuity, which carries
Integration Techniques and Sequences and Series; Linear Algebra and Counterexamples back at
depth one.

**Limits and Continuity**, read closely. Breadcrumb `Prelim / Logic and Proof / Limits and
Continuity`, an on-this-page contents list, and seven items each as a titled block carrying
its card id and its statement with the mathematics typeset. `P-TBXVH`, `P-FPWV6` and
`P-UE5L6` render inside the bordered problem frame with their statements. Foot navigation
reads `PREVIOUS Logic and Proof` / `NEXT Integration Techniques`.

**Previous/next** chains the whole reading order across all twelve routes, root to
Counterexamples, and each section's breadcrumb carries its own prerequisite path rather
than the whole guide: `Prelim / Counterexamples` at depth one, `Prelim / Logic and Proof /
Groups / Rings and Modules / Fields and Galois Theory / Complex Numbers` at depth five.

## Two defects the rendered pages make visible

Both are corpus defects that predate this branch, recorded here and reported to issue #2
rather than corrected.

**Four of the seven items in Limits and Continuity are answers, not questions.** `P-3OH6H`
publishes "Claim: take `δ < min(1, √(ε/5))`. Then…", `P-L3LHW` publishes "We need to
show", `P-LF4NL` publishes "Let `δ = min{1/2, √(ε/2)}`", `P-TEVPO` publishes "Parts
Suppose `∃M_g`…". These are solution write-ups carrying `kind: problem`, so they render
without the problem frame and their derived titles are the first line of a solution.
Twenty-five such cards were found across the area.

**The problem frame prints a literal `?`.** Every genuine problem card in this area carries
`title="?"` in its div, and the frame renders that question mark as the block's title above
the statement.

## What this does not claim

The topics on these cards were assigned by reading each of the 198 problems. The 189
occurrences and 3 solutions took their problem's topics through `instance-of` and `solves`
and were not read individually; an occurrence is that problem at one sitting.

Hint and solution disclosure order is **not** proven here. The Prelim area holds three
solution cards and no hint cards, so the disclosure machinery is barely exercised by this
branch; the Workshops branch is where that behaviour was shown.

Reachability of every prelim card is not this manifest's doing and is not claimed for it.
All 419 were already reachable from the `wiki/00_Prelims` pages before the guide existed —
`audit.py --only orphans` listed none of them — so the guide adds a reading order, not
addressability.

Search, the exam generator, and the other four subject guides were not exercised. The
twelve routes above were inspected at one viewport width for content and at 375 for
overflow only.
