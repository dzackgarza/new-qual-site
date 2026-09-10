---
schema: qual/card@1
id: P-TOP-WORKSHOP-D4-W3
kind: problem
title: Spaces in which open sets are compact (workshop warm-up)
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Counterexamples
  - Point-Set Topology
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
Provide an example of a topological space where open sets are compact.
Then find an infinite set with a Hausdorff topology where open sets are compact.
:::

::: {.solution}
For the first request, any finite topological space works. For example, on
\[
X=\{0,1\}
\]
take the Sierpiński topology
\[
\tau=\{\varnothing,\{1\},X\}.
\]
Every open subset is finite, hence compact.

For the second request, no infinite Hausdorff example exists. Suppose \(X\) is Hausdorff and every open subset of \(X\) is compact. In a Hausdorff space every compact subset is closed, so every open subset of \(X\) is also closed. Therefore complements of open sets are open as well, and arbitrary intersections of open sets are open: if \(U_i\) are open, then
\[
\bigcap_i U_i=X\setminus\bigcup_i(X\setminus U_i)
\]
is open.

Because Hausdorff implies \(T_1\), for each \(x\in X\),
\[
\{x\}=\bigcap_{y\ne x}(X\setminus\{y\})
\]
is an arbitrary intersection of open sets, hence is open. Thus \(X\) is discrete.

But then the open cover by singletons
\[
\{\{x\}:x\in X\}
\]
has no finite subcover when \(X\) is infinite, so the open set \(X\) itself is not compact. This contradicts the hypothesis that every open set is compact.

Hence the second requested example cannot exist: a Hausdorff space in which every open set is compact must be finite.
:::
