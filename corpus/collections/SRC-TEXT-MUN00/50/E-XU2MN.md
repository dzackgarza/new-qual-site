---
schema: qual/card@1
id: E-XU2MN
kind: problem
title: Hausdorff equals completely regular for locally euclidean spaces
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Separation Axioms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Let $X$ be a space that is locally $m$-euclidean.
Show that $X$ is Hausdorff if and only if $X$ is completely regular.
:::

::: {.solution}
If \(X\) is completely regular, then by definition it is \(T_1\), and complete regularity separates points from closed sets; in particular distinct points have disjoint neighborhoods. Thus \(X\) is Hausdorff.

Conversely, suppose \(X\) is Hausdorff and locally \(m\)-euclidean. Every point has a neighborhood homeomorphic to an open subset of \(\mathbb R^m\); shrinking inside such a chart gives a neighborhood whose closure in the chart is compact. Hence \(X\) is locally compact. Every locally compact Hausdorff space is completely regular (the theorem proved in §33). Therefore
\[
X\text{ is Hausdorff}\quad\Longleftrightarrow\quad X\text{ is completely regular}.
\]
:::
