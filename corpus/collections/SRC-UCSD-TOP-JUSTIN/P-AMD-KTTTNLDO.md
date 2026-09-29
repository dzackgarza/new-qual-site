---
schema: qual/card@1
id: P-AMD-KTTTNLDO
kind: problem
title: $S^2 - \{p_0, p_1\} \simeq S^1$
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Retracts
relations: []
review: draft
---

::: {.problem}
Show that $S^2 - \{p_0, p_1\} \simeq S^1$.
:::

::: {.solution}

::: pf

::: pf-step

After a homeomorphism of $S^2$, we may take $p_0$ and $p_1$ to be the north and south poles.

::: pf-proof

Any two distinct points of the sphere can be carried to the two poles by a homeomorphism of $S^2$.

:::

:::

::: pf-step

The complement of the two poles is homeomorphic to $S^1\times\mathbb R$.

::: pf-proof

Write a non-polar point in spherical coordinates as
$$
(\cos\theta\sin\phi,\sin\theta\sin\phi,\cos\phi),
\qquad \theta\in S^1,\quad 0<\phi<\pi.
$$
Thus the complement is $S^1\times(0,\pi)$, and $(0,\pi)\cong\mathbb R$.

:::

:::

::: pf-step

Hence
$$
\boxed{S^2\setminus\{p_0,p_1\}\simeq S^1}.
$$

::: pf-proof

The product $S^1\times\mathbb R$ deformation-retracts onto $S^1\times\{0\}$.

:::

:::

:::

:::
