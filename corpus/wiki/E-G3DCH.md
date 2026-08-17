---
schema: qual/card@1
id: E-G3DCH
kind: exercise
title: "Orders of zeros"
classification:
  areas:
  - complex-analysis
  topics:
  - zeros
  - power-series
relations: []
review: draft
solved: true
---

::: {.exercise title="Orders of zeros"}
Find the orders of zeros of the following functions:

- $(e^z-1)^3$
:::

::: {.solution}
\envlist

- $z=0$ of order 3: if $z_0$ is order $n$ for $f$, then it's order $kn$ for $f^k$.
  So check that $e^z-1$ has a root $z=0$ and $\dd{}{z}e^z-1\mid_{z=0} = e^z\mid_{z=0}\neq 0$, making it order 1.
:::
