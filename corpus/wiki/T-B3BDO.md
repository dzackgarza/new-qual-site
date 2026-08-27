---
schema: qual/card@1
id: T-B3BDO
kind: theorem
title: Goursat
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Theorem
  - Contour Integration
  - Holomorphic Functions
relations: []
review: draft
---

::: {.theorem}
If $\Omega \subseteq \CC$ is open and $T\subseteq \Omega$ is a triangle whose interior is also contained in $\Omega$, then
\[
\int_T f(z) \dz = 0
\]
whenever $f$ is holomorphic in $\Omega$.
:::

::: {.remark}
Stein and Shakarchi, *Complex Analysis*, Ch. 2 Theorem 1.1. This is the base case everything else in Cauchy theory is deduced from: it produces primitives on discs, hence Cauchy's theorem for toy contours, hence the integral formula, hence the power series expansion.
Only differentiability of $f$ is assumed, not continuity of $f'$, which is what makes the bisection proof necessary.
:::
