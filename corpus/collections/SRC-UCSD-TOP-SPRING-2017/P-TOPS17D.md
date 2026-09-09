---
schema: qual/card@1
id: P-TOPS17D
kind: problem
title: "Homology of a closed simply-connected 4-manifold"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Manifolds
relations: []
review: draft
---

::: problem
Let $M$ be a closed connected simply-connected $4$-manifold.
Show that $H_1(M; \mathbb{Z}) = H_3(M; \mathbb{Z}) = 0$ and that $H_2(M; \mathbb{Z})$ is a free abelian group.
:::

::: {.solution}
<1>1. Since $M$ is simply connected,
$$
H_1(M;\mathbb Z)=0.
$$
::: {.proof}
The Hurewicz theorem in degree one identifies $H_1(M;\mathbb Z)$ with the abelianization of $\pi_1(M)$.
:::

<1>2. The manifold $M$ is orientable.
::: {.proof}
The orientation character is a homomorphism $\pi_1(M)\to\{\pm1\}$, hence is trivial because $\pi_1(M)=1$.
:::

<1>3. Poincaré duality gives
$$
H_3(M;\mathbb Z)\cong H^1(M;\mathbb Z)=0.
$$
::: {.proof}
For the closed orientable $4$-manifold, $H_3\cong H^{1}$. The universal coefficient theorem gives
$$
H^1(M;\mathbb Z)\cong\operatorname{Hom}(H_1(M),\mathbb Z)=0
$$
by <1>1.
:::

<1>4. Poincaré duality and the universal coefficient theorem give
$$
H_2(M;\mathbb Z)\cong H^2(M;\mathbb Z)
\cong \operatorname{Hom}(H_2(M;\mathbb Z),\mathbb Z).
$$
::: {.proof}
The UCT exact sequence
$$
0\to\operatorname{Ext}(H_1(M),\mathbb Z)\to H^2(M;\mathbb Z)
\to\operatorname{Hom}(H_2(M),\mathbb Z)\to0
$$
has zero left term by <1>1.
:::

<1>5. Hence $H_2(M;\mathbb Z)$ is free abelian.
::: {.proof}
Because $M$ is compact, $H_2(M)$ is finitely generated. The group $\operatorname{Hom}(H_2(M),\mathbb Z)$ is free abelian, so the isomorphic group $H_2(M)$ is free abelian as well.
:::
:::
