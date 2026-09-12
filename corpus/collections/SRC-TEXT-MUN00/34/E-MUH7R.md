---
schema: qual/card@1
id: E-MUH7R
kind: problem
title: Compact Hausdorff spaces are metrizable exactly when second countable
classification:
  areas:
  - topology
  topics:
  - Metrizability
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Let $X$ be a compact Hausdorff space.
Show that $X$ is metrizable if and only if $X$ has a countable basis.
:::

::: {.solution}
If \(X\) has a countable basis, then compact Hausdorffness implies regularity, and the Urysohn metrization theorem gives a compatible metric.

Conversely, suppose \(X\) is compact and metrizable with metric \(d\). For each \(n\ge1\), compactness gives finitely many points
\[
x_{n,1},\dots,x_{n,k_n}
\]
such that the balls \(B(x_{n,j},1/n)\) cover \(X\). Let
\[
D=\{x_{n,j}:n\ge1,1\le j\le k_n\}.
\]
Then \(D\) is countable and dense. The family of balls
\[
B(d,q),\qquad d\in D,\ q\in\mathbb Q_{>0},
\]
is countable and forms a basis for the metric topology. Thus \(X\) has a countable basis.

Hence a compact Hausdorff space is metrizable exactly when it is second countable.
:::
