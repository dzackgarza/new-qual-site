---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS3B-HW1
kind: problem
title: Universal covers of $S^1$ and $S^1\vee S^1$ (warm-up)
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
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
Find the universal covers of these spaces:

(a) $X=S^1$.

(b) $Y=S^1\vee S^1$ (two circles glued together along a point).
:::

::: {.solution}
(a) The universal cover of \(S^1\) is
\[
p:\mathbb R\to S^1,
\qquad p(t)=e^{2\pi i t}.
\]
The space \(\mathbb R\) is simply connected, and every point of \(S^1\) has a small arc whose inverse image is a disjoint union of intervals mapped homeomorphically onto that arc.

(b) The universal cover of \(S^1\vee S^1\) is the \(4\)-regular tree that is the Cayley graph of the free group
\[
F(a,b)=\pi_1(S^1\vee S^1).
\]
Its vertices are group elements \(g\in F(a,b)\), with an \(a\)-edge from \(g\) to \(ga\) and a \(b\)-edge from \(g\) to \(gb\). Map every \(a\)-edge homeomorphically to the first circle and every \(b\)-edge to the second. The resulting graph is a tree, hence simply connected, and the map is a covering map.
:::
