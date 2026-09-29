---
schema: qual/card@1
id: E-HAT-2.2-11
kind: problem
title: Homology of cube with opposite faces identified via one-quarter twist (quaternion group)
classification:
  areas:
  - topology
  topics:
  - Homology
  - CW Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
In an exercise for §1.2 we described a 3 dimensional CW complex obtained from the cube $I^3$ by identifying opposite faces via a one-quarter twist.
Compute the homology groups of this complex.
:::

::: {.solution}

::: pf

::: pf-step

The complex $X$ is the quaternionic $3$-manifold $S^3/Q_8$: identifying opposite faces of the cube via a one-quarter twist gives the quotient of $S^3$ by the quaternion group $Q_8$.

::: pf-proof

this is the standard construction of the quaternionic manifold.

:::

:::

::: pf-step

$\pi_1(X) = Q_8$.

::: pf-proof

the fundamental group of this identification space is the quaternion group $Q_8$ (the two edges give generators $i, j$ with relations $i^2 = j^2 = k^2 = ijk$).

:::

:::

::: {.pf-step #s3}

$H_0(X) = \ZZ$.

::: pf-proof

$X$ is connected.

:::

:::

::: {.pf-step #s4}

$H_1(X) = Q_8^{\text{ab}} = \ZZ/2 \times \ZZ/2$.

::: pf-proof

$H_1 = \pi_1^{\text{ab}}$, and the abelianization of $Q_8$ is $\ZZ/2 \times \ZZ/2$ (the commutator subgroup of $Q_8$ is $\{\pm 1\}$, of order $2$, so $Q_8^{\text{ab}}$ has order $4$ and is $\ZZ/2 \times \ZZ/2$).

:::

:::

::: {.pf-step #s5}

$H_2(X) = 0$.

::: pf-proof

by Poincaré duality (and the universal coefficient theorem), $H_2(X) \cong H^1(X) \cong \operatorname{Hom}(H_1(X), \ZZ) = 0$, since $H_1(X) = \ZZ/2 \times \ZZ/2$ is torsion.

:::

:::

::: {.pf-step #s6}

$H_3(X) = \ZZ$.

::: pf-proof

$X$ is a closed orientable $3$-manifold, so $H_3(X) = \ZZ$.

:::

:::

::: pf-qed

$H_0 = \ZZ$, $H_1 = \ZZ/2 \times \ZZ/2$, $H_2 = 0$, $H_3 = \ZZ$ (steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref}).

:::

:::

:::
