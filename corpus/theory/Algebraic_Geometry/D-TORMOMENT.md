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
has image exactly $P$, with $\inverseof{\mu}(\text{relative interior of } F)$ the orbit attached to the face $F$.
So $P$ is the quotient $X_P / T_c$, and the orbit-cone correspondence is visible as the face structure of $P$.
:::

::: {.remark}
For a smooth projective fan $\Sigma$ with $r=\size\Sigma(1)$ rays spanning $N_\RR$, the ray map gives an exact sequence of compact tori
$$
1\longrightarrow K
\longrightarrow (S^1)^r
\longrightarrow T_c
\longrightarrow1,
$$
where $\dim K=r-n$.
The standard Hamiltonian action of $K$ on $\CC^r$ has a moment map
$$
\mu_K\colon\CC^r\longrightarrow\mathfrak k^*.
$$
For the level $\xi$ determined by an ample class, the symplectic reduction
$$
\mu_K^{-1}(\xi)/K
$$
is the projective toric variety with its corresponding Kähler form.
This is the symplectic counterpart of the algebraic Cox quotient; the level and ampleness data are part of the construction.

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
