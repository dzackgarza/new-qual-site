---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2A-HW4
kind: problem
title: Relate paths to connected components (warm-up)
classification:
  areas:
  - topology
  topics:
  - Connectedness
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
Show that if there is a path between two points, they lie in the same connected component.
Why does this show that a path connected space is connected?
:::

::: {.solution}
Suppose \(x,y\in X\) are joined by a path \(\gamma:[0,1]\to X\). The interval \([0,1]\) is connected, so its continuous image
\[
\gamma([0,1])
\]
is connected. This connected subset contains both \(x\) and \(y\). Therefore \(x\) and \(y\) lie in the same connected component of \(X\), since a connected component is the maximal connected subset containing either point.

If \(X\) is path connected, fix \(x_0\in X\). Every \(x\in X\) is connected to \(x_0\) by a path, hence lies in the same connected component as \(x_0\). Thus that component is all of \(X\), so \(X\) is connected.
:::
