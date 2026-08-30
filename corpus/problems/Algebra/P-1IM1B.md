---
schema: qual/card@1
id: P-1IM1B
kind: problem
title: The sum of (skew-)symmetric matrices is (skew-)symmetric
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Bilinear Forms
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
If $A,B$ are (skew)-symmetric, then $A^t = \pm A$ and $B^t = \pm B$ respectively.
But then
$$
(A+B)^t = A^t + B^t = \pm A + \pm B = \pm(A + B),
$$

which shows that $A+B$ is (skew)-symmetric.
:::

::: {.solution}
<1>1. $G$ group.
Proof: Sylow.

<1>2. Q.E.D.
Proof: <1>1.
:::
