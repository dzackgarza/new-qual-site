# Real Analysis subject branch: build proof

Manifest: `publications/real-analysis-guide.yaml`.
Built and inspected at target revision `c374160d` plus the query correction below.

`uv run qualc build` -> 7,208 cards and 323 wiki pages OK.

## Routes

Five routes emitted, one root and four sections, in dependency order:

```
/guide/GUIDE-REAL-ANALYSIS.html
/guide/GUIDE-REAL-ANALYSIS/continuity.html
/guide/GUIDE-REAL-ANALYSIS/differentiation.html
/guide/GUIDE-REAL-ANALYSIS/riemann-stieltjes-integration.html
/guide/GUIDE-REAL-ANALYSIS/uniform-convergence.html
```

## What was inspected

Headless Chrome screenshots at 1440x1100, and full-page captures at 1440x4200 and
1440x5200 so the section foot is in frame. Inspected directly, not merely produced.

**Continuity.** Study-path sidebar showing the four sections with dependency indentation
and the current one marked. Breadcrumb `Real Analysis / Continuity`. Lede. Propositions
3.1 through 3.5 each as a titled theorem block with its card id beside the heading, all
mathematics typeset. `More from the catalog` lists seven `uniform-continuity` problems,
each linked and carrying its card id. Foot navigation reads
`PREVIOUS Real Analysis` / `NEXT Differentiation`.

**Differentiation.** Fermat 4.1, Mean Value 4.2, Taylor 4.3 with the
`M|x-c|^{n+1}/(n+1)!` remainder bound rendered correctly. Foot navigation reads
`PREVIOUS Continuity` / `NEXT Riemann-Stieltjes Integration`.

**Riemann-Stieltjes Integration** and **Uniform Convergence** render their full statement
sets. The Uniform Convergence breadcrumb carries the whole chain,
`Real Analysis / Continuity / Differentiation / Riemann-Stieltjes Integration / Uniform
Convergence`, and its definition card precedes the six theorems that use it.

## What this does not claim

The branch orders the Day 4-7 workshop theorem spine. It is not the whole Real Analysis
wiki tree, so issue #26's reachability criterion -- every Real Analysis source page and
extracted card addressable from the branch -- is not met by this manifest.

Search, the generator, and hint/solution disclosure states were not exercised here.

## Two findings from building it

`run_query` ANDs its topics: it joins one `classifications` row per topic, so a query
naming three topics needs one card carrying all three. A first draft listing
`convergence-of-functions`, `uniform-convergence` and `sequences-of-functions` failed the
build with `publication query has no matches`. The Algebra guide passes a single topic, so
this had not surfaced. The guide now passes one topic per query.

`T-RA-WORKSHOP-D7-6-6` does not exist. The source's own numbering runs 6.1 to 6.5 then
6.7. Recorded on issue #2 rather than filled in.
