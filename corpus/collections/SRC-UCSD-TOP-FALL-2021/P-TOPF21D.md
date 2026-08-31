---
schema: qual/card@1
id: P-TOPF21D
kind: problem
title: "Homology of a quartic K3 surface in CP^3 from Euler characteristic"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Manifolds
  - Projective Spaces
  - Algebraic Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $K$ be the space $\{[x, y, z, w] \in \mathbb{CP}^3 : x^4 + y^4 + z^4 + w^4 = 0\}$.
It is known that $K$ is a simply-connected closed manifold with Euler characteristic $24$.
Compute $H_*(K; \mathbb{Z})$.
:::

::: {.solution}
<1>1. $K$ is a closed orientable $4$-manifold (a quartic K3 surface).
::: {.proof}
a smooth quartic hypersurface in $\CP^3$ is a closed orientable $4$-manifold.
:::

<1>2. $H_0(K) = \ZZ$ and $H_4(K) = \ZZ$.
::: {.proof}
$K$ is connected and orientable, so $H_0 = \ZZ$ and $H_4 = \ZZ$ (Poincaré duality).
:::

<1>3. $H_1(K) = 0$.
::: {.proof}
$K$ is simply connected, so $H_1 = \pi_1^{\text{ab}} = 0$.
:::

<1>4. $H_3(K) = 0$.
::: {.proof}
by Poincaré duality, $H_3(K) \cong H^1(K) \cong \operatorname{Hom}(H_1(K), \ZZ) = 0$ (using $H_1 = 0$ and the universal coefficient theorem).
:::

<1>5. $H_2(K) = \ZZ^{22}$.
<2>1. The Euler characteristic is $\chi(K) = 24 = b_0 - b_1 + b_2 - b_3 + b_4 = 1 - 0 + b_2 - 0 + 1 = 2 + b_2$.
::: {.proof}
$\chi = \sum (-1)^i b_i$, and $b_0 = b_4 = 1$, $b_1 = b_3 = 0$.
:::
<2>2. Hence $b_2 = 22$.
::: {.proof}
$24 = 2 + b_2$.
:::
<2>3. $H_2(K)$ is free abelian of rank $22$.
::: {.proof}
$H_2$ of a simply connected closed $4$-manifold is free (by the universal coefficient theorem and $H_1 = 0$, there is no torsion in $H_2$).
:::

<1>6. Q.E.D.
::: {.proof}
$H_0 = \ZZ$, $H_1 = 0$, $H_2 = \ZZ^{22}$, $H_3 = 0$, $H_4 = \ZZ$ (<1>2–<1>5).
:::
:::
