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

::: problem
Find a conformal map from the strip $\theset{z\in \CC \suchthat 0 < \Im(z) < 1}$ to $\HH$.
:::

::: {.solution}
**Goal:** Find a conformal (biholomorphic) map from the strip $S = \theset{z \suchthat 0 < \Im z < 1}$ onto the upper half-plane $\HH$.

<1>1. $e^{\pi z}$ maps $S$ onto $\HH$.
::: {.proof}
For $z = x + iy \in S$, $e^{\pi z} = e^{\pi x} e^{i\pi y}$; since $y \in (0,1)$, the argument $\pi y$ lies in $(0, \pi)$ and the modulus $e^{\pi x}$ is any positive number, so $e^{\pi z}$ ranges over all of $\HH$ (indeed over all nonzero complex numbers with argument in $(0,\pi)$).
:::

<1>2. $e^{\pi z}$ is injective on $S$.
::: {.proof}
If $e^{\pi z_1} = e^{\pi z_2}$, then $\pi(z_1 - z_2) \in 2\pi i \ZZ$, i.e. $z_1 - z_2 \in 2i\ZZ$; but for $z_1, z_2 \in S$, $\Im(z_1 - z_2) \in (-1, 1)$, so the only integer multiple of $2i$ in that range is $0$, hence $z_1 = z_2$.
:::

<1>3. $e^{\pi z}$ is holomorphic with nowhere-vanishing derivative on $S$.
::: {.proof}
The exponential is entire and $\ddd{z} e^{\pi z} = \pi e^{\pi z} \neq 0$ for all $z$.
:::

<1>4. $T(z) = e^{\pi z}$ is a conformal map from $S$ onto $\HH$.
::: {.proof}
By <1>1 it is onto, by <1>2 it is injective, and by <1>3 it is holomorphic with nonzero derivative; a bijective holomorphic map with nonzero derivative is a biholomorphism, i.e. conformal.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4 gives the conformal map $z \mapsto e^{\pi z}$ from the strip to the upper half-plane.
:::
:::
