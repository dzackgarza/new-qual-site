---
schema: qual/card@1
id: E-G3DCH
kind: problem
title: Orders of the zeros of $(e^z-1)^3$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Power Series
relations: []
review: draft
---

::: {.exercise}
Find the orders of zeros of the following functions:

- $(e^z-1)^3$
:::

::: {.solution}
\envlist

- The zeros are $z=2\pi i k$, $k\in\ZZ$, each of order 3: if $z_0$ is a zero of order $n$ for $f$, then it is a zero of order $kn$ for $f^k$.
  The zeros of $e^z-1$ are exactly the points $2\pi ik$, and $\dd{}{z}(e^z-1)\mid_{z=2\pi ik} = e^{2\pi ik}=1\neq 0$, so each is a zero of order 1.
:::
