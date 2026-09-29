---
schema: qual/card@1
id: P-TOPF03E
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

::: {.problem}
Let $M^4$ be a closed connected simply-connected $4$-manifold.
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
The Hurewicz theorem in degree one identifies $H_1(M;\mathbb Z)$ with the abelianization of $\pi_1(M)$.
:::

:::

::: pf-step
The manifold $M$ is orientable.

::: pf-proof
The orientation character is a homomorphism $\pi_1(M)\to\{\pm1\}$, hence is trivial because $\pi_1(M)=1$.
:::

:::

::: {.pf-step #h3-zero}
Poincaré duality gives
$$
H_3(M;\mathbb Z)\cong H^1(M;\mathbb Z)=0.
$$

::: pf-proof
For the closed orientable $4$-manifold, $H_3\cong H^{1}$. The universal coefficient theorem gives
$$
H^1(M;\mathbb Z)\cong\operatorname{Hom}(H_1(M),\mathbb Z)=0
$$
by step [](#h1-zero){.pf-ref}.
:::

:::

::: pf-step
Poincaré duality and the universal coefficient theorem give
$$
H_2(M;\mathbb Z)\cong H^2(M;\mathbb Z)
\cong \operatorname{Hom}(H_2(M;\mathbb Z),\mathbb Z).
$$

::: pf-proof
The UCT exact sequence
$$
0\to\operatorname{Ext}(H_1(M),\mathbb Z)\to H^2(M;\mathbb Z)
\to\operatorname{Hom}(H_2(M),\mathbb Z)\to0
$$
has zero left term by step [](#h1-zero){.pf-ref}.
:::

:::

::: {.pf-step #h2-free}
Hence $H_2(M;\mathbb Z)$ is free abelian.

::: pf-proof
Because $M$ is compact, $H_2(M)$ is finitely generated. The group $\operatorname{Hom}(H_2(M),\mathbb Z)$ is free abelian, so the isomorphic group $H_2(M)$ is free abelian as well.
:::

:::

::: pf-qed
Steps [](#h1-zero){.pf-ref}, [](#h3-zero){.pf-ref} and [](#h2-free){.pf-ref} give $H_1(M;\mathbb Z)=H_3(M;\mathbb Z)=0$ with $H_2(M;\mathbb Z)$ free abelian.
:::

:::

:::
