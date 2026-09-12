---
schema: qual/card@1
id: P-AMD-FV5LNKN4
kind: problem
title: Cellular homology of a cube with paired faces
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Cell Complexes
  - Homology
relations: []
review: draft
---

::: {.problem}
Use cellular chain complexes to compute the homology of the cube whose faces are identified in pairs according to the scheme shown.

![Cube with paired faces](../../../assets/Topology/650_UCSD_Qual_Questions/Quals/assets/1518395458668.png)
:::

::: {.solution}
<1>1. The source diagram shows that the $P$- and $Q$-face pairs are identified by translations, while the $R$-face pair is identified by a $180^\circ$ rotation.
::: {.proof}
The repeated $P$ and $Q$ glyphs have the same orientation on their paired parallel faces. The $R$ glyph on the opposite face is rotated by $180^\circ$. These glyph orientations are the pairing data in the original Fall 2022 exam diagram.
:::

<1>2. First quotient by the two translation pairings. A cross-section perpendicular to the $R$-direction becomes a torus $T^2$, and the remaining $R$-pairing makes $X$ the mapping torus of the half-turn
$$
f:T^2\to T^2,\qquad f_*|_{H_1(T^2)}=-I.
$$
::: {.proof}
The $P$- and $Q$-translations identify opposite sides in the two transverse coordinate directions, producing $T^2\times I$. The half-turn of the remaining square face descends to the torus automorphism represented on $H_1(T^2)\cong\mathbb Z^2$ by $-I$.
:::

<1>3. The induced maps are
$$
f_*=\operatorname{id}\text{ on }H_0(T^2),\qquad
f_*=-I\text{ on }H_1(T^2),\qquad
f_*=\operatorname{id}\text{ on }H_2(T^2).
$$
::: {.proof}
The half-turn is orientation-preserving on the torus, hence acts by $+1$ on $H_2$, and it negates each standard $H_1$ generator.
:::

<1>4. The Wang sequence for the mapping torus gives
$$
0\to\operatorname{coker}(1-f_*:H_k(T^2)\to H_k(T^2))
\to H_k(X)
\to\ker(1-f_*:H_{k-1}(T^2)\to H_{k-1}(T^2))\to0.
$$
::: {.proof}
This is the standard homology exact sequence of a mapping torus.
:::

<1>5. Therefore
$$
\boxed{H_k(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,3,\\
\mathbb Z\oplus(\mathbb Z/2)^2,&k=1,\\
\mathbb Z,&k=2,\\
0,&k>3.
\end{cases}}
$$
::: {.proof}
On $H_1(T^2)$, $1-f_*=2I$, so its cokernel is $(\mathbb Z/2)^2$ and its kernel is $0$. On $H_0$ and $H_2$, $1-f_*=0$. Thus $H_1$ is an extension of $\mathbb Z$ by $(\mathbb Z/2)^2$, which splits because $\mathbb Z$ is free; $H_2\cong\mathbb Z$; and $H_3\cong\mathbb Z$.
:::
:::
