---
schema: qual/card@1
id: T-ERNLN
kind: theorem
title: Uniform limit theorem
slogan: 'Uniform convergence preserves continuity.'
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Continuity
relations: []
review: draft
---

::: {.theorem}
Let $X$ be a topological space, and let $f_n\colon X\to\CC$ for $n\geq1$ and $f\colon X\to\CC$ be functions.
If each $f_n$ is [[D-AEAAD|continuous]] and $f_n\to f$ [[D-YZC3C|uniformly]] on $X$, then $f$ is continuous. This is [@Rud76, ch. 7, Theorem 7.12].
:::

::: {.corollary}
If each $f_n$ is continuous and the partial sums $S_N\coloneqq\sum_{n=1}^N f_n$ converge uniformly on $X$ to $f$, then $f$ is continuous.
:::
