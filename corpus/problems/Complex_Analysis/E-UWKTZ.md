---
schema: qual/card@1
id: E-UWKTZ
kind: problem
title: Entire functions for which $f(1/z)$ has a pole at $0$ are polynomials
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Polynomials
  - Poles
  - Singularities
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ is entire and $f(1/z)$ has a pole at $z=0$, then $f$ is a polynomial.
:::

::: {.solution}
Write $f(z) = \sum_{k\geq 0}c_k z^k$, which converges on all of $\CC$, and let $m$ be the order of the pole of $g(z) \coloneqq f(1/z)$ at $0$.

::: pf

::: {.pf-step #laurent}
The Laurent series of $g$ on $\CC\setminus\theset{0}$ is $\sum_{k\geq 0} c_k z^{-k}$.

::: pf-proof
Substitute $1/z$ into the power series of $f$; the series converges for every $z\neq0$, and a Laurent series on an annulus is unique.
:::

:::

::: pf-step
$f(z) = \sum_{k=0}^{m}c_k z^k$ is a polynomial of degree at most $m$.

::: pf-proof
A pole of order $m$ at $0$ means the Laurent coefficients of $z^{-k}$ vanish for $k>m$.
By step [](#laurent){.pf-ref} these coefficients are $c_k$, so $c_k=0$ for $k>m$.
:::

:::

:::

:::
