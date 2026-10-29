---
schema: qual/card@1
id: P-PA2XA
kind: problem
title: $\int_T f=0$ when $f$ is holomorphic and bounded near an interior puncture
  of $T$
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Morera
  - Contour Integration
relations: []
review: draft
---

::: {.problem}
Suppose that $f$ is holomorphic on a punctured open set $\Omega\setminus\theset{w_0}$ and let $T\subset \Omega$ be a triangle containing $w_0$.
Prove that if $f$ is bounded near $w_0$, then $\int_T f(z) \,dz = 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #extend}

$f$ extends to a holomorphic function $\widetilde f$ on $\Omega$.

::: pf-proof

$f$ is holomorphic on a punctured neighborhood of $w_0$ and bounded there, so Riemann's removable-singularity theorem applies.

:::

:::

::: pf-step

$\int_T f(z)\,dz=0$.

::: pf-proof

The functions $f$ and $\widetilde f$ agree on $\partial T$, so by step [](#extend){.pf-ref} and Cauchy's theorem for a triangle,
$$
\int_T f(z)\,dz=\int_{\partial T}\widetilde f(z)\,dz=0.
$$

:::

:::

:::

:::
