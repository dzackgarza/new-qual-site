---
schema: qual/card@1
id: PR-5WUAP
kind: proposition
title: The $p$-test
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Series of Numbers
relations: []
review: draft
---

::: {.proposition}
For $p\in\RR$, the series $\sum_{n\ge1} n^{-p}$ converges if and only if $p>1$.
:::

::: {.proof}
If $p\le0$, then $n^{-p}\ge1$ for all $n$, so the terms do not tend to $0$ and the series diverges.
If $p>0$, the function $x\mapsto x^{-p}$ is positive and decreasing on $[1,\infty)$, so by the integral test the series converges if and only if $\int_1^\infty x^{-p}\dx$ is finite, which holds if and only if $p>1$.
:::
