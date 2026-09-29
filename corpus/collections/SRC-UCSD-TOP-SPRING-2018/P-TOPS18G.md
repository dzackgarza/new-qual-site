---
schema: qual/card@1
id: P-TOPS18G
kind: problem
title: "H_1 of complementary pieces in S^3 are isomorphic; RP^2 cannot embed in S^3"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Manifolds
  - Embeddings
  - Mayer-Vietoris
relations: []
review: draft
---

::: {.problem}
Suppose that $S^3 = M \cup_\Sigma N$ is a decomposition of the $3$-sphere into two compact $3$-manifolds, glued along their common boundary surface $\Sigma$.
Prove that $H_1(N) \cong H_1(M)$, and conclude that $\mathbb{RP}^2$ cannot be embedded in $S^3$.
:::

::: {.solution}

::: pf

::: {.pf-step #h1-iso}
In any decomposition $S^3=M\cup_\Sigma N$ as in the problem,
$$\boxed{H_1(M;\mathbb Z)\cong H_1(N;\mathbb Z).}$$

::: pf-proof
Alexander duality identifies $H_1(M)$ with $H^1(N)$ and $H_1(N)$ with $H^1(M)$. The universal coefficient theorem gives $H^1(P;\mathbb Z)\cong\operatorname{Hom}(H_1(P),\mathbb Z)$ for either side $P$. These identifications imply first that both $H_1(M)$ and $H_1(N)$ are free abelian, and then that they have the same rank, hence are isomorphic.
:::

:::

::: {.pf-step #regular-neighborhood-retracts}
Suppose $\mathbb{RP}^2$ embedded in $S^3$. A closed regular neighborhood $M$ of the embedded surface would be the twisted interval bundle over $\mathbb{RP}^2$ and would deformation retract onto $\mathbb{RP}^2$.

::: pf-proof
A nonorientable surface in an orientable $3$-manifold is one-sided; its regular neighborhood is the corresponding twisted $I$-bundle. The interval fibers contract, so the neighborhood retracts to the zero section.
:::

:::

::: {.pf-step #contradiction-freeness}
Hence
$$H_1(M;\mathbb Z)\cong\mathbb Z/2,$$
contradicting the freeness forced in step [](#h1-iso){.pf-ref} for a codimension-zero submanifold of $S^3$.

::: pf-proof
The deformation retraction in step [](#regular-neighborhood-retracts){.pf-ref} identifies $H_1(M)$ with $H_1(\mathbb{RP}^2)=\mathbb Z/2$, while the proof of step [](#h1-iso){.pf-ref} shows that first homology of either complementary piece must be free abelian.
:::

:::

::: pf-step
Therefore
$$\boxed{\mathbb{RP}^2\text{ does not embed in }S^3.}$$

::: pf-proof
This is the contradiction in step [](#contradiction-freeness){.pf-ref}.
:::

:::

:::

:::
