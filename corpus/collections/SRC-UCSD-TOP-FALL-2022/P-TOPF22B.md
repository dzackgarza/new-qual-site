---
schema: qual/card@1
id: P-TOPF22B
kind: problem
title: 'Fundamental group and $H_2$ of the universal cover of a torus with two meridian discs'
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Universal Cover
  - Homology
  - Group Ring
  - Surfaces
relations: []
review: draft
---

::: {.problem}
Let $X$ be the space obtained from a torus by attaching discs along the two curves shown in the source figure (two disjoint meridian circles, each running once around the tube).
Find the fundamental group of $X$, and identify the homology group $H_2(\widetilde{X})$ of the universal cover of $X$ as a module over the group ring $\ZZ[\pi_1(X)]$.
:::

::: {.solution}

::: pf

::: {.pf-step #curves}

The two curves in the source figure are disjoint meridians of the torus: each runs once around the tube, one on the near side of the hole and one on the far side.

::: pf-proof

This is read from the figure (a solid arc on the visible side continued by a dashed arc on the hidden side, twice, with no crossing).

:::

:::

::: {.pf-step #homotopy-type}

$X\simeq S^2\vee S^2\vee S^1$.

::: pf-proof

The two meridians cut the torus into two annuli $A_1,A_2$, each with one boundary circle on each meridian. Let $D_1,D_2$ be the attached discs. Then $X=(A_1\cup D_1\cup D_2)\cup(A_2\cup D_1\cup D_2)$, and each $A_j\cup D_1\cup D_2$ is a $2$-sphere $S_j$; the two spheres meet exactly in $D_1\sqcup D_2$.
Collapsing each of the disjoint contractible subcomplexes $D_1$ and $D_2$ to a point is a homotopy equivalence. The result is two $2$-spheres glued at two pairs of points $p_1\sim p_1'$ and $p_2\sim p_2'$. Gluing at the first pair gives $S^2\vee S^2$; gluing the second pair of distinct points of this connected complex adds an arc between them up to homotopy, which gives $S^2\vee S^2\vee S^1$.

:::

:::

::: {.pf-step #pi1}

$$\boxed{\pi_1(X)\cong\ZZ.}$$

::: pf-proof

By van Kampen, $\pi_1(S^2\vee S^2\vee S^1)\cong\ZZ$, since the spheres are simply connected. In terms of the torus, with $a$ the meridian and $b$ the longitude, $\pi_1(X)=\langle a,b\mid [a,b],\,a,\,a\rangle\cong\langle b\rangle$: both discs kill the same class $a$, and the longitude survives.

:::

:::

::: {.pf-step #cover}

The universal cover $\widetilde X$ is homotopy equivalent to $\bigvee_{n\in\ZZ}(S^2_n\vee S'^2_n)$, two $2$-spheres for each integer, permuted by the generator $t$ of $\pi_1(X)$ through $n\mapsto n+1$.

::: pf-proof

The universal cover of $S^2\vee S^2\vee S^1$ is the real line with two $2$-spheres wedged on at each integer point, and the deck generator is translation by $1$. Collapsing the contractible line is a homotopy equivalence.

:::

:::

::: pf-qed

By Step [](#cover){.pf-ref},
$$
H_2(\widetilde X)\cong\bigoplus_{n\in\ZZ}(\ZZ[S^2_n]\oplus\ZZ[S'^2_n])\cong \ZZ[t,t^{-1}]^2,
$$
the free module of rank $2$ over $\ZZ[\pi_1(X)]=\ZZ[t,t^{-1}]$, with basis the classes of the two spheres over one integer.

:::

:::

:::
