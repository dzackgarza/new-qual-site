---
schema: qual/card@1
id: E-BPEP3
kind: exercise
title: Entire functions with a pole at infinity are polynomials
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - polynomials
  - singularities
  - poles
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Find all entire functions with have poles at $\infty$.
:::

:::{.solution}
If $f$ is entire, write $f(z) = \sum_{k\geq 0}c_k z^k$ and $g(z) \da f(1/z) = \sum_{k\geq 0}c_k z^{-k}$.
If $z=\infty$ is a pole of order $m$ of $f$, $z=0$ is a pole of order $m$ of $g$, so 
\[
g(z) = \sum_{0\leq k \leq m}c_k z^{-k} \implies f(z) = \sum_{0\leq k \leq m}c_k z^k
,\]
making $f$ a polynomial of degree at most $m$.
:::

