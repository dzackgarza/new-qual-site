---
schema: qual/card@1
id: P-DLXGE
kind: problem
title: Connected sum of surfaces, and $\pi_1(\RP^2\# T^2)$
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Fundamental Group
  - van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
a. Let $S_1$ and $S_2$ be disjoint surfaces.
Give the definition of their connected sum $S^1 \#S^2$.

b. Compute the fundamental group of the connected sum of the projective plane and the two-torus.
:::

::: {.solution}
**Goal.** Define the connected sum of two surfaces, and compute $\pi_1(\RP^2 \# T^2)$.

<1>1. Definition of connected sum.
<2>1. Remove an open disk from each surface: $S_i^\circ \definedas S_i \sm \operatorname{int} D^2$.
::: {.proof}
each surface admits an embedded closed disk; remove its interior.
:::
<2>2. Glue the two boundary circles by a homeomorphism.
::: {.proof}
$S_1 \# S_2 \definedas S_1^\circ \sqcup S_2^\circ / \sim$, where $\sim$ identifies $\partial S_1^\circ$ with $\partial S_2^\circ$ via a homeomorphism $S^1 \to S^1$.
:::
<2>3. The result is a surface, independent of the choices up to homeomorphism.
::: {.proof}
gluing along boundary circles of two surfaces yields a surface; the disk and gluing map choices give homeomorphic results.
:::

<1>2. Compute $\pi_1(\RP^2 \# T^2)$.
<2>1. $\pi_1(\RP^2) = \ZZ/2$ and $\pi_1(T^2) = \ZZ^2$.
::: {.proof}
$\RP^2$ has universal cover $S^2$ with deck group $\ZZ/2$; $T^2 = S^1 \times S^1$.
:::
<2>2. The connected sum of two surfaces has fundamental group the free product of the two groups.
::: {.proof}
by van Kampen, the two punctured surfaces intersect in a circle (path-connected), and a punctured surface deformation-retracts onto a wedge of circles, so $\pi_1(S_1 \# S_2) \cong \pi_1(S_1) \ast \pi_1(S_2)$.
:::
<2>3. $\pi_1(\RP^2 \# T^2) \cong (\ZZ/2) \ast \ZZ^2$.
::: {.proof}
apply <1>2.2 with $\pi_1(\RP^2) = \ZZ/2$ and $\pi_1(T^2) = \ZZ^2$.
:::

<1>3. Q.E.D.
::: {.proof}
<1>2.3 is the requested fundamental group.
:::
:::
