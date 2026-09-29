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

::: {.problem}
Let $M^4$ be a closed connected simply-connected 4-manifold.
Show that $H_1(M; \mathbb{Z}) = H_3(M; \mathbb{Z}) = 0$ and that $H_2(M; \mathbb{Z})$ is a free abelian group.
:::

::: {.solution}

::: pf

::: {.pf-step #h1-zero}
Since $M$ is simply connected,
$$
H_1(M;\mathbb Z)=0.
$$

::: pf-proof
The first homology group is the abelianization of the fundamental group.
:::

:::

::: {.pf-step #h3-zero}
The manifold is orientable and
$$
H_3(M;\mathbb Z)=0.
$$

::: pf-proof
Simple connectivity makes the orientation character trivial, so $M$ is orientable. Poincaré duality gives
$$
H_3(M)\cong H^1(M),
$$
and the universal coefficient theorem gives
$$
H^1(M)\cong\operatorname{Hom}(H_1(M),\mathbb Z)=0.
$$
:::

:::

::: {.pf-step #h2-cohomology-iso}
Poincaré duality gives
$$
H_2(M;\mathbb Z)\cong H^2(M;\mathbb Z).
$$

::: pf-proof
Cap product with the fundamental class is an isomorphism in the closed orientable $4$-manifold.
:::

:::

::: {.pf-step #h2-cohomology-free}
The group $H^2(M;\mathbb Z)$ is free abelian.

::: pf-proof
The universal coefficient theorem gives
$$
0\to\operatorname{Ext}(H_1(M),\mathbb Z)\to H^2(M)\to\operatorname{Hom}(H_2(M),\mathbb Z)\to0.
$$
The first term is zero by step [](#h1-zero){.pf-ref}, so $H^2(M)$ is isomorphic to $\operatorname{Hom}(H_2(M),\mathbb Z)$, which is free abelian because $H_2(M)$ is finitely generated.
:::

:::

::: {.pf-step #h2-free}
Therefore $H_2(M;\mathbb Z)$ is free abelian.

::: pf-proof
Combine the isomorphism in step [](#h2-cohomology-iso){.pf-ref} with step [](#h2-cohomology-free){.pf-ref}.
:::

:::

::: pf-qed
Steps [](#h1-zero){.pf-ref}, [](#h3-zero){.pf-ref} and [](#h2-free){.pf-ref} give $H_1(M;\mathbb Z)=H_3(M;\mathbb Z)=0$ with $H_2(M;\mathbb Z)$ free abelian.
:::

:::

:::
