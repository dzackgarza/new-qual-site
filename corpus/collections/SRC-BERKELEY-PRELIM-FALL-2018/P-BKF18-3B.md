---
schema: qual/card@1
id: P-BKF18-3B
kind: problem
title: Continuous open maps $\mathbb R\to\mathbb R$ are monotone
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Prove that a continuous function from $\mathbb R$ to $\mathbb R$ which maps open sets to open sets must be monotone.
:::

::: {.solution}
We prove the contrapositive.
Assume f is not monotone, i.e., there exist $a < b < c$ with $f ( a ) < f ( b )$ and $f ( b ) > f ( c )$ or with $f ( a ) > f ( b )$ and $f ( b ) < f ( c )$ . In the first case, let m be the point at which $f ( x )$ is maximized in $[ a , c ] ;$ such a point exists since f is continuous.
Moreover we must have m $\neq a , c$ by the hypothesis.
But now the image of $( a , c )$ under f contains $m _ { : }$ , but does not contain a neighborhood of $m$ , so $f$ cannot map open sets to open sets.

The second case is completely analogous.
:::
