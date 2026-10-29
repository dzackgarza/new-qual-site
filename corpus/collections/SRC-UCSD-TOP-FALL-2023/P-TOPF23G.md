---
schema: qual/card@1
id: P-TOPF23G
kind: problem
title: 'Half lives, half dies: complementary pieces of $S^3$ have isomorphic $H_1$, and $\RP^3$ minus a ball does not embed in $S^3$'
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
Suppose that $S^3 = M \cup_\Sigma N$ is a decomposition of the $3$-sphere into two compact $3$-manifolds-with-boundary, glued along their common boundary surface $\Sigma$.
Prove that $H_1(N; \ZZ) \cong H_1(M; \ZZ)$.
Let $X$ be the compact $3$-manifold-with-boundary obtained by removing the interior of a small ball from $\RP^3$.
Conclude that $X$ cannot be embedded in $S^3$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For a compact codimension-zero submanifold $M\subset S^3$ with complementary closure $N$, Alexander duality gives
$$\widetilde H_1(M;\ZZ)\cong \widetilde H^1(N;\ZZ),$$
and symmetrically
$$\widetilde H_1(N;\ZZ)\cong \widetilde H^1(M;\ZZ).$$

::: pf-proof

The complement of the interior of one side deformation retracts onto the other side, and Alexander duality for compact locally contractible subsets of $S^3$ identifies $\widetilde H_i(M)$ with $\widetilde H^{2-i}(S^3-M)$. For $i=1$ this gives the displayed isomorphisms.

:::

:::

::: {.pf-step #s2}

The groups $H_1(M;\ZZ)$ and $H_1(N;\ZZ)$ are free abelian.

::: pf-proof

By the universal coefficient theorem, $H^1(N;\ZZ)\cong\operatorname{Hom}(H_1(N),\ZZ)$ is free abelian. By step [](#s1){.pf-ref} this is isomorphic to $H_1(M)$. Interchanging $M,N$ gives the same conclusion for $H_1(N)$.

:::

:::

::: pf-step

Moreover they have the same rank, hence
$$\boxed{H_1(M;\ZZ)\cong H_1(N;\ZZ).}$$

::: pf-proof

From step [](#s1){.pf-ref} and UCT,
$$H_1(M)\cong H^1(N)\cong\operatorname{Hom}(H_1(N),\ZZ).$$
Since $H_1(N)$ is free by step [](#s2){.pf-ref}, its dual has the same rank and is isomorphic to it as an abstract abelian group.

:::

:::

::: {.pf-step #s4}

Let $X=\RP^3-\operatorname{int}B^3$. Then
$$H_1(X;\ZZ)\cong\ZZ/2.$$

::: pf-proof

Removing an open ball from a $3$-manifold does not change its fundamental group, so $H_1(X)$ is the abelianization of $\pi_1(\RP^3)\cong\ZZ/2$.

:::

:::

::: pf-step

Therefore $X$ cannot embed in $S^3$.

::: pf-proof

If it embedded as a codimension-zero compact submanifold, step [](#s2){.pf-ref} would force $H_1(X;\ZZ)$ to be free abelian, contradicting step [](#s4){.pf-ref}.

:::

:::

:::

:::
