---
schema: qual/card@1
id: P-TOPF23G
kind: problem
title: "Half die half alive: H_1 of complementary pieces in S^3 are isomorphic; RP^3 minus a ball cannot embed in S^3"
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
Prove that $H_1(N; \mathbb{Z}) \cong H_1(M; \mathbb{Z})$.
Let $X$ be the compact $3$-manifold-with-boundary obtained by removing the interior of a small ball from $\mathbb{RP}^3$.
Conclude that $X$ cannot be embedded in $S^3$.
:::

::: {.solution}
<1>1. For a compact codimension-zero submanifold $M\subset S^3$ with complementary closure $N$, Alexander duality gives
$$\widetilde H_1(M;\mathbb Z)\cong \widetilde H^1(N;\mathbb Z),$$
and symmetrically
$$\widetilde H_1(N;\mathbb Z)\cong \widetilde H^1(M;\mathbb Z).$$
::: {.proof}
The complement of the interior of one side deformation retracts onto the other side, and Alexander duality for compact locally contractible subsets of $S^3$ identifies $\widetilde H_i(M)$ with $\widetilde H^{2-i}(S^3-M)$. For $i=1$ this gives the displayed isomorphisms.
:::

<1>2. The groups $H_1(M;\mathbb Z)$ and $H_1(N;\mathbb Z)$ are free abelian.
::: {.proof}
By the universal coefficient theorem, $H^1(N;\mathbb Z)\cong\operatorname{Hom}(H_1(N),\mathbb Z)$ is free abelian. By <1>1 this is isomorphic to $H_1(M)$. Interchanging $M,N$ gives the same conclusion for $H_1(N)$.
:::

<1>3. Moreover they have the same rank, hence
$$\boxed{H_1(M;\mathbb Z)\cong H_1(N;\mathbb Z).}$$
::: {.proof}
From <1>1 and UCT,
$$H_1(M)\cong H^1(N)\cong\operatorname{Hom}(H_1(N),\mathbb Z).$$
Since $H_1(N)$ is free by <1>2, its dual has the same rank and is isomorphic to it as an abstract abelian group.
:::

<1>4. Let $X=\mathbb{RP}^3-\operatorname{int}B^3$. Then
$$H_1(X;\mathbb Z)\cong\mathbb Z/2.$$
::: {.proof}
Removing an open ball from a $3$-manifold does not change its fundamental group, so $H_1(X)$ is the abelianization of $\pi_1(\mathbb{RP}^3)\cong\mathbb Z/2$.
:::

<1>5. Therefore $X$ cannot embed in $S^3$.
::: {.proof}
If it embedded as a codimension-zero compact submanifold, <1>2 would force $H_1(X;\mathbb Z)$ to be free abelian, contradicting <1>4.
:::
:::
