---
schema: qual/card@1
id: P-UCTOP-SU14-4
kind: problem
title: H_2 of simply-connected closed 4-manifold is torsion-free
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Suppose $M$ is a compact connected 4-manifold without boundary, and that $\pi_1(M) = 1$.
Prove that $H_2(M)$ is torsion-free.
:::

::: {.solution}

::: pf

::: pf-step
The manifold $M$ is orientable.

::: pf-proof
The orientation character is a homomorphism $\pi_1(M)\to\{\pm1\}$. Since $\pi_1(M)=1$, it is trivial.
:::

:::

::: {.pf-step #h1-zero}
We have $H_1(M;\mathbb Z)=0$.

::: pf-proof
$H_1$ is the abelianization of $\pi_1$.
:::

:::

::: {.pf-step #h2-cohomology-iso}
Poincaré duality gives
$$
H_2(M;\mathbb Z)\cong H^2(M;\mathbb Z).
$$

::: pf-proof
Cap product with the fundamental class is an isomorphism for the closed orientable $4$-manifold $M$.
:::

:::

::: {.pf-step #h2-cohomology-hom}
The universal coefficient theorem gives
$$
H^2(M;\mathbb Z)\cong\operatorname{Hom}(H_2(M;\mathbb Z),\mathbb Z).
$$

::: pf-proof
The exact sequence
$$
0\to\operatorname{Ext}(H_1(M),\mathbb Z)\to H^2(M)\to\operatorname{Hom}(H_2(M),\mathbb Z)\to0
$$
has zero left term by step [](#h1-zero){.pf-ref}.
:::

:::

::: pf-step
Therefore $H_2(M;\mathbb Z)$ is torsion-free.

::: pf-proof
The group $H_2(M)$ is finitely generated because $M$ is compact. By steps [](#h2-cohomology-iso){.pf-ref} and [](#h2-cohomology-hom){.pf-ref} it is isomorphic to the free abelian group $\operatorname{Hom}(H_2(M),\mathbb Z)$. Hence it is free, in particular torsion-free.
:::

:::

:::

:::
