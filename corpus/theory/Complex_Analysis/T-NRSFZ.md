---
schema: qual/card@1
id: T-NRSFZ
kind: theorem
title: Holomorphic logarithm when $f'/f$ has zero periods
slogan: 'A nonvanishing holomorphic function has a holomorphic logarithm exactly when its logarithmic derivative has no periods.'
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
Let $\Omega\subseteq\CC$ be a simply connected region and let $f$ be [[D-E7A5W|holomorphic]] and nonvanishing on $\Omega$.
Fix $z_0\in\Omega$ and $c\in\CC$ with $e^c=f(z_0)$, and define
$$
g(z)\coloneqq c+\int_{z_0}^z\frac{f'(\xi)}{f(\xi)}\dxi,
$$
the integral taken along any piecewise smooth path in $\Omega$ from $z_0$ to $z$, which is independent of the path because $\Omega$ is simply connected.
Then $g$ is well defined and holomorphic on $\Omega$, $g'=f'/f$, and $e^{g}=f$ on $\Omega$.

This is [@SS03, ch. 3, §6, Theorem 6.2], which asserts on a simply connected region the existence of a holomorphic $g$ with $e^g=f$; the displayed integral is the construction its proof gives.
:::
