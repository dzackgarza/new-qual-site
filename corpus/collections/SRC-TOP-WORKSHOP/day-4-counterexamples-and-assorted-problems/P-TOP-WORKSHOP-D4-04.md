---
schema: qual/card@1
id: P-TOP-WORKSHOP-D4-04
kind: problem
title: A compact union of two Hausdorff subspaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $X$ be a compact space.
If $X=A\cup B$ with both $A$ and $B$ Hausdorff, must $X$ be Hausdorff?
:::

::: {.solution}
No. Let \(X=\{0,1\}\) with the Sierpiński topology
\[
\tau=\{\varnothing,\{1\},X\}.
\]
The space \(X\) is finite, hence compact, but it is not Hausdorff because every neighborhood of \(0\) is all of \(X\), so \(0\) and \(1\) cannot be separated by disjoint open sets.

Set \(A=\{0\}\) and \(B=\{1\}\). Each singleton, with its subspace topology, is Hausdorff, and
\[
X=A\cup B.
\]
Thus a compact space can be the union of two Hausdorff subspaces without itself being Hausdorff.
:::
