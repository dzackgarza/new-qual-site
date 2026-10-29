---
schema: qual/card@1
id: E-RKPAV
kind: problem
title: Holomorphic functions satisfying $f^{2}=\overline{f}$ are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Open Mapping Theorem
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

::: {.exercise}
Prove that if $f$ is holomorphic on a connected open set $\Omega$ and $f^2(z) = \bar{f(z)}$ then $f$ is constant.
:::

::: {.solution}

::: pf

::: {.pf-step #cube-constant}
$f^3$ is constant on $\Omega$.

::: pf-proof
Put $F \coloneqq f^3$, which is holomorphic on $\Omega$. For $z\in\Omega$,
$$
F(z) = f^2(z) f(z) = \bar{f(z)}f(z) = \abs{f(z)}^2,
$$
so $F(\Omega) \subseteq [0,\infty)$. This set has empty interior in $\CC$, so $F(\Omega)$ is not open, and by the open mapping theorem the holomorphic function $F$ on the connected set $\Omega$ is constant.
:::

:::

::: pf-step
$f$ is constant on $\Omega$.

::: pf-proof
By step [](#cube-constant){.pf-ref}, $f^3 = c$ for a constant $c$. Then $f$ takes values in the finite set of cube roots of $c$. A continuous function on the connected set $\Omega$ with values in a finite set is constant.
:::

:::

:::

:::
