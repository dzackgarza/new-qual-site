---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-06
kind: problem
title: A compact set meets each fiber of a cover in finitely many points
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Compactness
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
(Purdue Jan ’08) Let $p:E\to B$ be a covering map.
Suppose that points are closed in $B$.
Let $A\subset E$ be compact.
Prove that for every $b\in B$, the set $A\cap p^{-1}(b)$ is finite.
:::

::: {.solution}
Fix \(b\in B\). Since points are closed in \(B\) and \(p\) is continuous, the fiber
\[
p^{-1}(b)
\]
is closed in \(E\). Hence
\[
A\cap p^{-1}(b)
\]
is closed in the compact space \(A\), so it is compact.

The fiber is also a discrete subspace of \(E\). Indeed, if \(e\in p^{-1}(b)\), choose an evenly covered neighborhood \(U\ni b\), and let \(V\) be the sheet containing \(e\). Since \(p|_V:V\to U\) is a homeomorphism,
\[
V\cap p^{-1}(b)=\{e\}.
\]
Thus each point of the fiber is isolated in the fiber, and the same is true of its subspace \(A\cap p^{-1}(b)\).

A compact discrete space is finite: its cover by singletons has a finite subcover. Therefore
\[
A\cap p^{-1}(b)
\]
is finite for every \(b\in B\).
:::
