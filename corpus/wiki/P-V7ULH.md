---
schema: qual/card@1
id: P-V7ULH
kind: problem
title: "Let $f$ be a power series centered at the origin. Prove that $f$\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - power-series
  - cauchy-integral-formula
relations: []
review: draft
---
:::{.problem title="?"}
Let $f$ be a power series centered at the origin.
Prove that $f$ has a power series expansion about any point in its disc of convergence.
:::

:::{.concept}
\envlist

- Cauchy's integral formula:
\[
f(z) = \int {f(\xi) \over \xi - z}\dxi
.\]

:::

:::{.solution}
Idea: use Cauchy's integral formula to get a series in $(z-z_0)$.
\[
f(z) 
&= \int {f(\xi) \over \xi -z} \dxi\\
&= \int f(\xi) \qty{ 1\over \xi - (z - z_0) - z_0 } \dxi\\
&= \int { f(\xi) \over\xi - z_0}  \qty{ 1\over 1-w  } \dxi && w\da {z-z_0 \over \xi - z_0} \\
&= \int { f(\xi) \over\xi - z_0}  \sum_{k\geq 0} w^k \dxi \\
&= \sum_{k\geq 0} \qty{\int {f(\xi) \over \xi - z_0} \dxi } w^k\\
&= \sum_{k\geq 0} \qty{\int {f(\xi) \over \xi - z_0} \dxi } w^k\\
&= \sum_{k\geq 0} \qty{\int {f(\xi) \over (\xi - z_0)^{k+1} } \dxi } (z-z_0)^k
,\]
where we've integrated over a curve contained in $D$ the disc of convergence, and that the power series for $f$ converges uniformly on $D$ to commute the sum and integral.

:::

