---
schema: qual/card@1
id: E-HAT-3.D-3
kind: exercise
title: "Pontryagin ring of $SO(5)$"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

Compute the Pontryagin ring structure in $H_*(SO(5); \mathbb{Z})$.

::: {.solution}
<1>1. $SO(5)$ has $H_*(SO(5); \mathbb{Z}) \cong \Lambda_\mathbb{Z}[x_1, x_3]$ (exterior algebra on generators of degrees $1$ and $3$), as an abelian group.
::: {.proof}
the homology of $SO(5)$ is the exterior algebra on generators in degrees $1$ and $3$ (from the standard computation of the homology of $SO(n)$).
:::

<1>2. The Pontryagin product (induced by the group multiplication) makes $H_*(SO(5))$ into a graded-commutative Hopf algebra.
::: {.proof}
the group structure gives a Hopf algebra structure on homology.
:::

<1>3. Since $H_*(SO(5))$ is an exterior algebra on primitive generators $x_1$ (degree $1$) and $x_3$ (degree $3$), the Pontryagin ring is exactly the exterior algebra $\Lambda_\mathbb{Z}[x_1, x_3]$.
::: {.proof}
the generators are primitive (they come from the sphere factors in the CW structure), and the Pontryagin product of primitives in an exterior algebra is the exterior product.
:::

<1>4. Hence the Pontryagin ring is $H_*(SO(5)) \cong \Lambda_\mathbb{Z}[x_1, x_3]$ with $|x_1| = 1$, $|x_3| = 3$, and $x_1^2 = x_3^2 = 0$, $x_1 x_3 = -x_3 x_1$.
::: {.proof}
<1>1–<1>3.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.
:::
:::
