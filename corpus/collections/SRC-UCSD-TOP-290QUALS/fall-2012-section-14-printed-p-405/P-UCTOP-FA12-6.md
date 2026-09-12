---
schema: qual/card@1
id: P-UCTOP-FA12-6
kind: problem
title: H_1 = H_3 = 0 and H_2 is free for simply-connected closed 4-manifold
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
---

Let $M^4$ be a closed connected simply-connected 4-manifold.
Show that $H_1(M; \mathbb{Z}) = H_3(M; \mathbb{Z}) = 0$ and that $H_2(M; \mathbb{Z})$ is a free abelian group.

::: {.solution}
<1>1. Since $M$ is simply connected,
$$
H_1(M;\mathbb Z)=0.
$$
::: {.proof}
The first homology group is the abelianization of the fundamental group.
:::

<1>2. The manifold is orientable and
$$
H_3(M;\mathbb Z)=0.
$$
::: {.proof}
Simple connectivity makes the orientation character trivial, so $M$ is orientable. Poincaré duality gives
$$
H_3(M)\cong H^1(M),
$$
and the universal coefficient theorem gives
$$
H^1(M)\cong\operatorname{Hom}(H_1(M),\mathbb Z)=0.
$$
:::

<1>3. Poincaré duality gives
$$
H_2(M;\mathbb Z)\cong H^2(M;\mathbb Z).
$$
::: {.proof}
Cap product with the fundamental class is an isomorphism in the closed orientable $4$-manifold.
:::

<1>4. The group $H^2(M;\mathbb Z)$ is free abelian.
::: {.proof}
The universal coefficient theorem gives
$$
0\to\operatorname{Ext}(H_1(M),\mathbb Z)\to H^2(M)\to\operatorname{Hom}(H_2(M),\mathbb Z)\to0.
$$
The first term is zero by <1>1, so $H^2(M)$ is isomorphic to $\operatorname{Hom}(H_2(M),\mathbb Z)$, which is free abelian because $H_2(M)$ is finitely generated.
:::

<1>5. Therefore $H_2(M;\mathbb Z)$ is free abelian.
::: {.proof}
Combine the isomorphism in <1>3 with <1>4.
:::
:::
