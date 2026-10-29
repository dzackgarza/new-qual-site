---
schema: qual/card@1
id: E-X4MBB
kind: problem
title: The fourth roots of $i$
classification:
  areas:
  - complex-analysis
  topics:
  - Trigonometry
  - Polynomials
relations: []
review: draft
---

::: {.exercise}
Solve $z^4=i$.
:::

::: {.solution}
::: pf

::: {.pf-step #one-root}
$z_0 = e^{i\pi/8}$ satisfies $z_0^4 = i$.

::: pf-proof
$z_0^4 = e^{i\pi/2} = i$.
:::

:::

::: pf-step
The solutions of $z^4 = i$ are $\boxed{e^{i\pi/8},\ e^{5i\pi/8},\ e^{9i\pi/8},\ e^{13i\pi/8}}$.

::: pf-proof
$z^4 = i$ if and only if $(z/z_0)^4 = 1$ by step [](#one-root){.pf-ref}, so the solutions are $z_0\,i^k = e^{i\pi(1+4k)/8}$ for $k = 0,1,2,3$, and a degree-$4$ polynomial has no others.
:::

:::

:::

:::
