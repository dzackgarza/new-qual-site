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

Suppose $M$ is a compact connected 4-manifold without boundary, and that $\pi_1(M) = 1$.
Prove that $H_2(M)$ is torsion-free.

::: {.solution}
<1>1. The manifold $M$ is orientable.
::: {.proof}
The orientation character is a homomorphism $\pi_1(M)\to\{\pm1\}$. Since $\pi_1(M)=1$, it is trivial.
:::

<1>2. We have $H_1(M;\mathbb Z)=0$.
::: {.proof}
$H_1$ is the abelianization of $\pi_1$.
:::

<1>3. Poincaré duality gives
$$
H_2(M;\mathbb Z)\cong H^2(M;\mathbb Z).
$$
::: {.proof}
Cap product with the fundamental class is an isomorphism for the closed orientable $4$-manifold $M$.
:::

<1>4. The universal coefficient theorem gives
$$
H^2(M;\mathbb Z)\cong\operatorname{Hom}(H_2(M;\mathbb Z),\mathbb Z).
$$
::: {.proof}
The exact sequence
$$
0\to\operatorname{Ext}(H_1(M),\mathbb Z)\to H^2(M)\to\operatorname{Hom}(H_2(M),\mathbb Z)\to0
$$
has zero left term by <1>2.
:::

<1>5. Therefore $H_2(M;\mathbb Z)$ is torsion-free.
::: {.proof}
The group $H_2(M)$ is finitely generated because $M$ is compact. By <1>3--<1>4 it is isomorphic to the free abelian group $\operatorname{Hom}(H_2(M),\mathbb Z)$. Hence it is free, in particular torsion-free.
:::
:::
