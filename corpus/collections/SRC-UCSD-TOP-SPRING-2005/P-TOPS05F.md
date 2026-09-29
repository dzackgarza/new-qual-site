---
schema: qual/card@1
id: P-TOPS05F
kind: problem
title: 'Manifold and H-space realizability of $S^3\vee S^5$'
classification:
  areas:
  - topology
  topics:
  - Homotopy Type
  - Manifolds
  - H-Spaces
relations: []
review: draft
---

::: {.problem}
Let $X$ be a compact space having the homotopy type of $S^3 \vee S^5$.
Determine if $X$ can be a manifold or an $H$-space.
:::

::: {.solution}

::: pf

::: pf-step

A compact manifold homotopy-equivalent to $S^3\vee S^5$ cannot have boundary.

::: pf-proof

The wedge has $H_5\cong\mathbb Z$. A compact connected $5$-manifold with nonempty boundary has zero absolute top homology; a manifold of dimension larger than $5$ would have its nonzero top homology in a higher degree if closed. Thus any such manifold would have to be a closed orientable $5$-manifold.

:::

:::

::: {.pf-step #s2}

No closed $5$-manifold has this homotopy type.

::: pf-proof

For the wedge,
$$
H_3\cong\mathbb Z,\qquad H^2=0.
$$
But Poincaré duality for a closed orientable $5$-manifold gives
$$
H_3\cong H^2,
$$
a contradiction.

:::

:::

::: {.pf-step #s3}

The space $S^3\vee S^5$ cannot be an $H$-space either.

::: pf-proof

Assume a multiplication $\mu:X\times X\to X$ with a homotopy unit exists. Let $x\in H^3(X;\mathbb Z)$ and $y\in H^5(X;\mathbb Z)$ be generators. The unit property forces
$$
\mu^*x=x\otimes1+1\otimes x,\qquad
\mu^*y=y\otimes1+1\otimes y,
$$
since there are no lower positive-degree classes from which extra terms could be formed. In $H^*(X)$ we have $xy=0$ because $H^8(X)=0$. But
$$
0=\mu^*(xy)=\mu^*x\,\mu^*y
=x\otimes y-y\otimes x,
$$
which is nonzero in $H^8(X\times X;\mathbb Z)$ by Künneth. Contradiction.

:::

:::

::: pf-step

Therefore a compact space of this homotopy type can be neither a manifold nor an $H$-space.

::: pf-proof

Combine steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
