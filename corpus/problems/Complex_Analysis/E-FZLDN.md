---
schema: qual/card@1
id: E-FZLDN
kind: problem
title: Holomorphic functions of unit modulus on the circle are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Cauchy Integral Formula
relations: []
review: draft
---

::: {.exercise}
Suppose $f$ is continuous and non-zero on $\overline{\DD}$ and holomorphic on $\DD$ such that $\abs{f(z)}=1$ for all $\abs{z}=1$.
Show that $f$ is constant.
:::

::: {.solution}

::: pf

::: {.pf-step #modulus-one}
$\abs{f(z)}=1$ for every $z\in\DD$.

::: pf-proof
Since $f$ has no zeros on $\overline{\DD}$, the function $1/f$ is holomorphic on $\DD$ and continuous on $\overline{\DD}$, and $\abs{f}=\abs{1/f}=1$ on the unit circle.
The maximum modulus principle applied to $f$ gives $\abs{f}\le1$ on $\DD$, and applied to $1/f$ it gives $\abs{f}\ge1$ on $\DD$.
:::

:::

::: pf-step
$f$ is constant.

::: pf-proof
By step [](#modulus-one){.pf-ref}, $f(\DD)$ lies in the unit circle, which has empty interior in $\CC$.
A nonconstant holomorphic function on $\DD$ is an open map, so $f$ is constant.
:::

:::

:::

:::
