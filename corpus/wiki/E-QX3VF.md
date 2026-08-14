---
schema: qual/card@1
id: E-QX3VF
kind: exercise
title: "Entire functions with poles at infinity"
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
---
:::{.exercise title="Entire functions with poles at infinity"}
Characterize all entire functions with a pole of order $m$ at $\infty$.

:::

:::{.solution}
Since $f$ is entire, $f(z) = \sum_{k\geq 0 } c_k z^k$.
Expanding about $z_0=\infty$, we have $f(1/z) = \sum_{k\geq 0} c_k z^{-k} = c_0 + {c_1\over z} + \cdots$.
If $z_0=\infty$ is a pole of order $m$, then $c_m\neq 0$ but $c_{>m} = 0$, which forces $f(z) = \sum_{0\leq k \leq m} c_k z^k$ to be a polynomial of degree $m$.
:::
