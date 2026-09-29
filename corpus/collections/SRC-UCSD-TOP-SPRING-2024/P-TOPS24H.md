---
schema: qual/card@1
id: P-TOPS24H
kind: problem
title: Closed 4-manifold homotopy equivalent to a suspension is a homology sphere
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: {.problem}
Show that if $M$ is a closed 4-manifold which is homotopy-equivalent to the suspension $\Sigma X$ of some path-connected topological space $X$, then $H_*(M; \mathbb{Z}) = H_*(S^4; \mathbb{Z})$ (that is, $M$ must be a homology sphere).
:::

::: {.solution}

::: pf

::: pf-step
Because $X$ is path-connected, its suspension $\Sigma X$ is simply connected. Hence the homotopy-equivalent closed $4$-manifold $M$ is simply connected and therefore orientable.

::: pf-proof
Van Kampen applied to the two cone neighborhoods of a suspension gives trivial fundamental group when the equatorial space is connected. Orientability follows because the orientation character factors through $\pi_1(M)$.
:::

:::

::: {.pf-step #h1-h3-vanish}
Thus
$$H_1(M;\mathbb Z)=H_3(M;\mathbb Z)=0,\qquad H_0(M)=H_4(M)=\mathbb Z.$$

::: pf-proof
Simple connectivity gives $H_1=0$. Poincaré duality gives $H_3\cong H^1=0$, and connected orientability gives the bottom and top groups.
:::

:::

::: {.pf-step #cup-products-vanish}
Every cup product of positive-degree reduced cohomology classes on a suspension is zero. Therefore the intersection pairing
$$H^2(M;\mathbb Z)/\mathrm{tors}\times H^2(M;\mathbb Z)/\mathrm{tors}\to\mathbb Z$$
is identically zero.

::: pf-proof
The reduced diagonal of a suspension is null-homotopic, which makes all positive-degree cup products vanish. A homotopy equivalence transfers this ring structure to $M$.
:::

:::

::: {.pf-step #free-part-h2-vanishes}
Poincaré duality makes the intersection pairing on the free part of $H^2(M;\mathbb Z)$ unimodular, so step [](#cup-products-vanish){.pf-ref} forces that free part to vanish.

::: pf-proof
A zero bilinear form is nondegenerate only on the zero group.
:::

:::

::: {.pf-step #h2-vanishes}
In fact $H_2(M;\mathbb Z)=0$.

::: pf-proof
Since $H_1(M)=0$, the universal coefficient theorem gives
$$H^2(M;\mathbb Z)\cong\operatorname{Hom}(H_2(M),\mathbb Z).$$
Poincaré duality gives $H_2(M)\cong H^2(M)$. Thus $H_2(M)$ is isomorphic to its torsion-free dual and is therefore free. By step [](#free-part-h2-vanishes){.pf-ref} its free rank is zero, so it vanishes.
:::

:::

::: pf-step
Consequently
$$\boxed{H_*(M;\mathbb Z)\cong H_*(S^4;\mathbb Z).}$$

::: pf-proof
Combine steps [](#h1-h3-vanish){.pf-ref} and [](#h2-vanishes){.pf-ref}.
:::

:::

:::

:::
