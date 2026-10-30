---
schema: qual/card@1
id: P-TOPS18G
kind: problem
title: '$H^1(N)\cong H_1(M)$ for complementary pieces of $S^3$, and $\RP^2$ does not embed in $S^3$'
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
Prove that $H^1(N) \cong H_1(M)$, and conclude that $\RP^2$ cannot be embedded in $S^3$.
:::

::: {.solution}

::: pf

::: {.pf-step #h1-iso}
In any decomposition $S^3=M\cup_\Sigma N$ as in the problem,
$$\boxed{H^1(N;\ZZ)\cong H_1(M;\ZZ)},$$
and $H_1(M;\ZZ)$ is free abelian. By symmetry the same holds with $M$ and $N$ exchanged.

::: pf-proof
The interior of $M$ is $S^3\setminus N$ and is homotopy equivalent to $M$ by a collar of $\partial M$, so Alexander duality for the compact, locally contractible subspace $N\subset S^3$ gives $H_1(M)\cong\widetilde H_1(S^3\setminus N)\cong\widetilde H^{1}(N)=H^1(N)$. The universal coefficient theorem gives $H^1(N;\ZZ)\cong\operatorname{Hom}(H_1(N),\ZZ)$, which is free abelian because $H_1(N)$ is finitely generated.
:::

:::

::: {.pf-step #regular-neighborhood-retracts}
Suppose $\RP^2$ embedded in $S^3$. A closed regular neighborhood $M$ of the embedded surface would be the twisted interval bundle over $\RP^2$ and would deformation retract onto $\RP^2$.

::: pf-proof
A nonorientable surface in an orientable $3$-manifold is one-sided; its regular neighborhood is the corresponding twisted $I$-bundle. The interval fibers contract, so the neighborhood retracts to the zero section.
:::

:::

::: {.pf-step #contradiction-freeness}
Hence
$$H_1(M;\ZZ)\cong\ZZ/2,$$
contradicting the freeness forced in step [](#h1-iso){.pf-ref} for a codimension-zero submanifold of $S^3$.

::: pf-proof
The deformation retraction in step [](#regular-neighborhood-retracts){.pf-ref} identifies $H_1(M)$ with $H_1(\RP^2)=\ZZ/2$, while the proof of step [](#h1-iso){.pf-ref} shows that first homology of either complementary piece must be free abelian.
:::

:::

::: pf-step
Therefore
$$\boxed{\RP^2\text{ does not embed in }S^3.}$$

::: pf-proof
This is the contradiction in step [](#contradiction-freeness){.pf-ref}.
:::

:::

:::

:::
