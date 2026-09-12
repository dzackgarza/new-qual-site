---
schema: qual/card@1
id: P-TOPF23B
kind: problem
title: "Homology of a cube with faces identified in pairs"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
---

::: problem
Let $X$ be the space obtained by identifying the faces of a standard cube $I^3$ in pairs, as shown.
Compute the integral homology groups $H_*(X; \mathbb{Z})$.
:::

::: {.solution}
<1>1. Reading the glyph orientations in the original Fall 2023 diagram, the front/back and top/bottom face pairs are identified by translations, while the left/right pair is identified by a $180^\circ$ rotation.
::: {.proof}
The paired glyphs on the front/back faces have the same orientation, as do the paired flag-shaped glyphs on the top/bottom faces. The glyphs on the two side faces differ by a half-turn. These orientations specify the face identifications in the source figure.
:::

<1>2. Quotienting first by the two translation pairings gives $T^2\times I$. The remaining side pairing therefore realizes $X$ as the mapping torus of the half-turn
$$f:T^2\to T^2,$$
which acts as $-I$ on $H_1(T^2;\mathbb Z)$.
::: {.proof}
The two translations identify opposite edges in each transverse square direction, producing torus fibers. The $180^\circ$ rotation of the remaining face descends to the torus automorphism represented by $-I$ on the standard basis of first homology.
:::

<1>3. Thus
$$f_*=1\text{ on }H_0(T^2),\qquad f_*=-I\text{ on }H_1(T^2),\qquad f_*=1\text{ on }H_2(T^2).$$
::: {.proof}
The half-turn reverses both generators of $H_1$ and preserves the orientation class of the torus.
:::

<1>4. The Wang sequence gives short exact sequences
$$
0\to\operatorname{coker}(1-f_*:H_k(T^2)\to H_k(T^2))
\to H_k(X)
\to\ker(1-f_*:H_{k-1}(T^2)\to H_{k-1}(T^2))\to0.
$$
::: {.proof}
This is the standard homology exact sequence for a mapping torus.
:::

<1>5. Hence
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
On $H_1(T^2)$, $1-f_*=2I$, whose cokernel is $(\mathbb Z/2)^2$ and whose kernel is zero. On $H_0$ and $H_2$, $1-f_*=0$. The degree-one short exact sequence splits because its quotient is the free group $\mathbb Z$.
:::
:::
