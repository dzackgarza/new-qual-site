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

::: {.pf-step #s1}

A closed manifold $M$ homotopy-equivalent to $S^3\vee S^5$ would be a closed orientable $5$-manifold.

::: pf-proof

A closed connected $n$-manifold has $H_n(M;\FF_2)\cong\FF_2$ and $H_k(M;\FF_2)=0$ for $k>n$. The wedge has $H_5(-;\FF_2)\ne0$ and $H_k(-;\FF_2)=0$ for $k>5$, so $n=5$. Then $H_5(M;\ZZ)\cong H_5(S^3\vee S^5;\ZZ)\cong\ZZ$, so $M$ is orientable.

:::

:::

::: {.pf-step #s2}

No closed manifold has this homotopy type.

::: pf-proof

For the wedge,
$$
H_3\cong\ZZ,\qquad H^2=0.
$$
But Poincaré duality for a closed orientable $5$-manifold gives
$$
H_3\cong H^2,
$$
which contradicts step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #thick}

A compact manifold with boundary can have this homotopy type.

::: pf-proof

Let $W$ be the boundary connected sum of $S^3\times D^3$ and $S^5\times[-1,1]$, glued along a $5$-disc in each boundary. It is a compact $6$-manifold with boundary. The two pieces deformation retract onto $S^3$ and $S^5$, and they meet in a contractible disc, so $W\simeq S^3\vee S^5$.

:::

:::

::: {.pf-step #s3}

The space $S^3\vee S^5$ is not an $H$-space.

::: pf-proof

Assume a multiplication $\mu:X\times X\to X$ with a homotopy unit exists. Let $x\in H^3(X;\ZZ)$ and $y\in H^5(X;\ZZ)$ be generators. The unit property forces
$$
\mu^*x=x\otimes1+1\otimes x,\qquad
\mu^*y=y\otimes1+1\otimes y,
$$
since there are no lower positive-degree classes from which extra terms could be formed. In $H^*(X)$ we have $xy=0$ because $H^8(X)=0$. But
$$
0=\mu^*(xy)=\mu^*x\,\mu^*y
=x\otimes y-y\otimes x,
$$
which is nonzero in $H^8(X\times X;\ZZ)$ by Künneth. Contradiction.

:::

:::

::: pf-qed

By steps [](#s2){.pf-ref} and [](#thick){.pf-ref}, $X$ can be a compact manifold only if it has nonempty boundary, and such manifolds exist. By step [](#s3){.pf-ref}, $X$ is never an $H$-space.

:::

:::

:::
