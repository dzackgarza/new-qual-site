---
schema: qual/card@1
id: P-PPWDW
kind: problem
title: A conformal map from the strip $\{0<\Im z<1\}$ onto $\HH$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Find a conformal map from the strip $\theset{z\in \CC \suchthat 0 < \Im(z) < 1}$ to $\HH$.
:::

::: {.solution}
Write $S \coloneqq \theset{z \suchthat 0 < \Im z < 1}$ and $T(z)\coloneqq e^{\pi z}$.

::: pf

::: {.pf-step #onto}

$T$ maps $S$ onto $\HH$.

::: pf-proof

For $z = x + iy \in S$, $T(z) = e^{\pi x} e^{i\pi y}$. As $x$ ranges over $\RR$ and $y$ over $(0,1)$, the modulus $e^{\pi x}$ takes every positive value and the argument $\pi y$ takes every value in $(0,\pi)$, so $T(S)$ is the set of nonzero complex numbers with argument in $(0,\pi)$, which is $\HH$.

:::

:::

::: {.pf-step #injective}

$T$ is injective on $S$.

::: pf-proof

If $e^{\pi z_1} = e^{\pi z_2}$, then $z_1 - z_2 \in 2i\ZZ$. For $z_1, z_2 \in S$ we have $\Im(z_1 - z_2) \in (-1, 1)$, so $z_1 = z_2$.

:::

:::

::: pf-step

$T(z)=\boxed{e^{\pi z}}$ is a conformal map from $S$ onto $\HH$.

::: pf-proof

$T$ is entire, and by steps [](#onto){.pf-ref} and [](#injective){.pf-ref} it is a holomorphic bijection $S\to\HH$, hence a biholomorphism.

:::

:::

:::

:::
