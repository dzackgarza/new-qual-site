---
schema: qual/card@1
id: PR-6C3GQ
kind: proposition
title: Geometric series
slogan: 'Inside the unit disk, the geometric series sums to $1/(1-x)$; outside it does not converge.'
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
relations: []
review: draft
---

::: {.proposition}
Let $x\in\CC$.
The series $\sum_{k=0}^\infty x^k$ converges if and only if $\abs{x} < 1$, and in that case
$$
\sum_{k=0}^\infty x^k = \frac 1 {1-x} .
$$
:::
