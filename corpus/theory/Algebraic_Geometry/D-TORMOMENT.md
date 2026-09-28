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
has image exactly $P$, with $\mu\inv(\text{relative interior of } F)$ the orbit attached to the face $F$.
So $P$ is the quotient $X_P / T_c$, and the torus orbits of $X_P$ correspond to the faces of $P$, the orbit of a face $F$ having dimension $\dim F$.
:::

::: {.remark}
To construct $\mu$, realise $X_\Sigma$ as a quotient of an open subset of $\CC^{\Sigma(1)}$ by a torus of rank $\size\Sigma(1) - n$; the moment map of that torus is
$$
\mu_\Sigma : \CC^{\size \Sigma(1)} \to \RR^{\size\Sigma(1) - n} ,
$$
and, for $X_\Sigma$ smooth and projective, $X_\Sigma$ is the symplectic quotient $\mu_\Sigma^{-1}(c)/T_c'$ for a regular value $c$ determined by $P$, where $T_c'$ is the compact part of that torus.
For $\PP^n$, $\mu([z]) = \abs{z}^{-2}(\abs{z_0}^2, \ldots, \abs{z_n}^2)$ has image the standard simplex, whose vertices are the images of the coordinate points.
:::
