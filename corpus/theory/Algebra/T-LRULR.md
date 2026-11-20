---
schema: qual/card@1
id: T-LRULR
kind: theorem
title: The Littlewood--Richardson rule
slogan: '$c^{\lambda}_{\mu\nu}$ counts the semistandard tableaux of shape $\lambda/\mu$ and content $\nu$ with lattice word'
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
  - Representation Theory
relations: []
review: draft
---

::: {.theorem}
Let $\mu$ and $\nu$ be [[D-YTABL|partitions]], let $\abs\mu=d$ and $\abs\nu=m$, and let $s_\lambda$ be the [[D-SCHUR|Schur function]].
Then
$$
s_\mu s_\nu=\sum_{\lambda}c^{\lambda}_{\mu\nu}s_\lambda,
$$
the sum over the partitions $\lambda$ of $d+m$, where $c^{\lambda}_{\mu\nu}$ is the number of [[D-YTABL|semistandard tableaux]] of skew shape $\lambda/\mu$ and content $\nu$ whose [[D-YTABL|word]] is a lattice word.

This is [@FH91, (A.8)], where such a tableau is called a strict $\nu$-expansion of the diagram of $\mu$.
:::
