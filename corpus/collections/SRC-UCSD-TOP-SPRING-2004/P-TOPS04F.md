---
schema: qual/card@1
id: P-TOPS04F
kind: problem
title: "RP^2 is not the boundary of a compact 3-manifold; is RP^3 a boundary?"
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Boundaries
  - Projective Spaces
relations: []
review: draft
---

::: {.problem}
Show that $\mathbb{RP}^2$ is not the boundary of a compact $3$-manifold.
Do you think that $\mathbb{RP}^3$ is the boundary of a compact $4$-manifold?
:::

::: {.solution}
<1>1. If $M$ is a compact odd-dimensional manifold, then
$$
\chi(\partial M)=2\chi(M).
$$
::: {.proof}
Double $M$ along its boundary to obtain the closed odd-dimensional manifold $DM$. Inclusion-exclusion gives
$$
\chi(DM)=2\chi(M)-\chi(\partial M).
$$
A closed odd-dimensional manifold has Euler characteristic zero (with $\mathbb F_2$ coefficients, by Poincaré duality), yielding the formula.
:::

<1>2. Therefore $\mathbb{RP}^2$ cannot be the boundary of a compact $3$-manifold.
::: {.proof}
Since $\chi(\mathbb{RP}^2)=1$, the equation in <1>1 would require $1=2\chi(M)$, impossible for an integer $\chi(M)$.
:::

<1>3. In contrast, $\mathbb{RP}^3$ does bound a compact $4$-manifold.
::: {.proof}
Take the oriented $D^2$-bundle over $S^2$ with Euler number $2$. Its boundary is the associated oriented circle bundle over $S^2$ with Euler class $2$. The total space of that circle bundle is the lens space
$$
L(2,1)\cong\mathbb{RP}^3.
$$
Thus the disk bundle is a compact $4$-manifold with boundary $\mathbb{RP}^3$.
:::
:::
