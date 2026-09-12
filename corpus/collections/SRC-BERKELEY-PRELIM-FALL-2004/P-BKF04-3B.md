---
schema: qual/card@1
id: P-BKF04-3B
kind: problem
title: UC Berkeley Fall 2004 prelim 3B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
For which positive integers n does there exist an $n \times n$ matrix A with rational entries such that $A ^ { 3 } + \bar { A } + I = 0 ?$
:::

::: {.solution}
The polynomial $f ( x ) = x ^ { 3 } + x + 1$ is irreducible over $\mathbb { Q }$ (because it is irreducible modulo 2, or because of the rational root test, for instance). Since all eigenvalues of A are roots of $f ( x )$ , the characteristic polynomial of A divides a power of $f ( x )$ , and hence is equal to a power of $f ( x )$ by irreducibility. Therefore n must be a multiple of 3.

Conversely, if $n = 3$ , we may let $V = \mathbb { Q } [ x ] / ( x ^ { 3 } + x + 1 )$ , and let A be the matrix (with respect to some basis) of the Q-linear transformation $V  V$ given by multiplication by the image of x. And for n any larger multiple of 3, we can take A to be block-diagonal with each $3 \times 3$ diagonal block equal to the solution for $n = 3$
:::
