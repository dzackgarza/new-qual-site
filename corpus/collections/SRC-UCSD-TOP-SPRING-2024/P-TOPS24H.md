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

::: problem
Show that if $M$ is a closed 4-manifold which is homotopy-equivalent to the suspension $\Sigma X$ of some path-connected topological space $X$, then $H_*(M; \mathbb{Z}) = H_*(S^4; \mathbb{Z})$ (that is, $M$ must be a homology sphere).
:::

::: {.solution}
<1>1. Because $X$ is path-connected, its suspension $\Sigma X$ is simply connected. Hence the homotopy-equivalent closed $4$-manifold $M$ is simply connected and therefore orientable.
::: {.proof}
Van Kampen applied to the two cone neighborhoods of a suspension gives trivial fundamental group when the equatorial space is connected. Orientability follows because the orientation character factors through $\pi_1(M)$.
:::

<1>2. Thus
$$H_1(M;\mathbb Z)=H_3(M;\mathbb Z)=0,\qquad H_0(M)=H_4(M)=\mathbb Z.$$
::: {.proof}
Simple connectivity gives $H_1=0$. Poincaré duality gives $H_3\cong H^1=0$, and connected orientability gives the bottom and top groups.
:::

<1>3. Every cup product of positive-degree reduced cohomology classes on a suspension is zero. Therefore the intersection pairing
$$H^2(M;\mathbb Z)/\mathrm{tors}\times H^2(M;\mathbb Z)/\mathrm{tors}\to\mathbb Z$$
is identically zero.
::: {.proof}
The reduced diagonal of a suspension is null-homotopic, which makes all positive-degree cup products vanish. A homotopy equivalence transfers this ring structure to $M$.
:::

<1>4. Poincaré duality makes the intersection pairing on the free part of $H^2(M;\mathbb Z)$ unimodular, so <1>3 forces that free part to vanish.
::: {.proof}
A zero bilinear form is nondegenerate only on the zero group.
:::

<1>5. In fact $H_2(M;\mathbb Z)=0$.
::: {.proof}
Since $H_1(M)=0$, the universal coefficient theorem gives
$$H^2(M;\mathbb Z)\cong\operatorname{Hom}(H_2(M),\mathbb Z).$$
Poincaré duality gives $H_2(M)\cong H^2(M)$. Thus $H_2(M)$ is isomorphic to its torsion-free dual and is therefore free. By <1>4 its free rank is zero, so it vanishes.
:::

<1>6. Consequently
$$\boxed{H_*(M;\mathbb Z)\cong H_*(S^4;\mathbb Z).}$$
::: {.proof}
Combine <1>2 and <1>5.
:::
:::
