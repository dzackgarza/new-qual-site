---
schema: qual/card@1
id: D-TORMOMENT
kind: concept
title: The moment map and the polytope as an orbit space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Polytopes
  - Orbits
relations:
- kind: uses
  target: D-TORPOLY
- kind: uses
  target: PR-O8V3I
review: draft
prompts:
- What does the moment map of a projective toric variety do, and what is its image?
---

::: {.concept}
A projective toric variety $X_P$ carries an action of the compact torus $T_c \cong (S^1)^n \subseteq T$, and the moment map
$$
\mu : X_P \to M_\RR \cong \RR^n
$$
has image exactly $P$: the preimage of the relative interior of a $k$-dimensional face $F$ is the orbit attached to $F$, which has complex dimension $k$, and the fibre over a point of that interior is the compact torus $(S^1)^k$ [Cox--Little--Schenck, *Toric Varieties*, Theorem 12.2.5 and Proposition 12.2.3(b); both are stated for the algebraic moment map, and [*ibid.*, Exercise 12.2.8] carries Theorem 12.2.5 over to the symplectic $\mu$; @Ful93, §4.2].
So $P$ is the quotient $X_P / T_c$ — the homeomorphism of [*ibid.*, Proposition 12.2.3(a)] — and the orbit-cone correspondence is visible as the face structure of $P$.
:::

::: {.remark}
For $\PP^n$, using the standard simplex
$$
\Delta^n
=
\theset{
(x_1,\ldots,x_n)\in\RR^n
\st
x_i\geq0,\ \sum_{i=1}^n x_i\leq1
},
$$
the moment map is
$$
\mu([z_0:\cdots:z_n])
=
\frac{(\abs{z_1}^2,\ldots,\abs{z_n}^2)}
{\sum_{i=0}^n\abs{z_i}^2},
$$
whose image is $\Delta^n$; the coordinate points map to its vertices.

The combinatorial content of the moment-map statement is already encoded by the orbit-cone correspondence.
:::
