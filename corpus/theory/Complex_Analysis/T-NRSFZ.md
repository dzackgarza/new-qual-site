---
schema: qual/card@1
id: T-NRSFZ
kind: theorem
title: Holomorphic logarithm when $f'/f$ has zero periods
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Logarithm
  - Holomorphic Functions
relations: []
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be a connected open set and let $f$ be [[D-E7A5W|holomorphic]] and nonvanishing on $\Omega$.
Suppose that $\int_\gamma\frac{f'(z)}{f(z)}\dz=0$ for every piecewise smooth closed curve $\gamma$ in $\Omega$.
Fix $z_0\in\Omega$ and $c\in\CC$ with $e^c=f(z_0)$, and define
$$
g(z)\coloneqq c+\int_{z_0}^z\frac{f'(\xi)}{f(\xi)}\dxi,
$$
the integral taken along any piecewise smooth path in $\Omega$ from $z_0$ to $z$.
Then $g$ is well defined and holomorphic on $\Omega$, $g'=f'/f$, and $e^{g}=f$ on $\Omega$.
:::
