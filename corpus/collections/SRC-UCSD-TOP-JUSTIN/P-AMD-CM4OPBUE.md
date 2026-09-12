---
schema: qual/card@1
id: P-AMD-CM4OPBUE
kind: problem
title: Fundamental groups of band-and-disc spaces
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
relations: []
review: draft
---

::: {.problem}
Each figure in Problem 4 of the source sheet depicts a space made by gluing bands, each homeomorphic to $I\times I$, to discs.
For each space, compute its fundamental group and the fundamental group after a disc is glued to each boundary circle.
:::

::: {.remark}
The two band-and-disc diagrams appear on page 1 of the source sheet.
:::

::: {.solution}
<1>1. The left-hand source figure is a disc with three untwisted bands attached in planar cyclic order. It is an orientable genus-$0$ surface with four boundary components.
::: {.proof}
Starting from one disc ($\chi=1$), each band is a $1$-handle and decreases Euler characteristic by $1$, so $\chi=-2$. The cyclic order shown is planar, hence the surface has genus $0$. Therefore $2-b=-2$, so $b=4$.
:::

<1>2. Hence before capping its boundary,
$$\boxed{\pi_1\cong F_3,}$$
and after attaching a disc to every boundary circle the result is $S^2$, so
$$\boxed{\pi_1=1.}$$
::: {.proof}
A genus-$0$ surface with four boundary components deformation retracts to a wedge of three circles. Capping all four boundary components gives the sphere.
:::

<1>3. The right-hand source figure consists of two discs joined by three bands with the opposite cyclic ordering shown. It is an orientable genus-$1$ surface with one boundary component.
::: {.proof}
Here $\chi=2-3=-1$. The opposite cyclic order of the three bands is the standard thickening of a theta graph to a once-punctured torus rather than a pair of pants. Thus $2-2g-b=-1$ with $b=1$, giving $g=1$.
:::

<1>4. Consequently before capping,
$$\boxed{\pi_1\cong F_2,}$$
and after attaching a disc to its boundary circle one obtains $T^2$, so
$$\boxed{\pi_1\cong\mathbb Z^2.}$$
::: {.proof}
A once-punctured torus deformation retracts to a wedge of two circles. Capping its unique boundary component gives the closed torus.
:::
:::
