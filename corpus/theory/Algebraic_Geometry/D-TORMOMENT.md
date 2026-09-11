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
\[
\mu : X_P \to M_\RR \cong \RR^n
\]
has image exactly $P$, with $\mu\inv(\text{relative interior of } F)$ the orbit attached to the face $F$.
So $P$ is the quotient $X_P / T_c$, and the orbit-cone correspondence is visible as the face structure of $P$.
:::

::: {.remark}
The construction of $\mu$ is the symplectic-quotient picture: realise $X_\Sigma$ as a quotient of an open subset of $\CC^{\Sigma(1)}$ by a torus of rank $\size\Sigma(1) - n$, and the moment map of that torus is
\[
\mu_\Sigma : \CC^{\size \Sigma(1)} \to \RR^{\size\Sigma(1) - n} .
\]
For $\PP^n$ this is $\mu(z) = \abs{z}^{-2}(\abs{z_0}^2, \ldots, \abs{z_n}^2)$ with image the standard simplex, and the vertices are the coordinate points.

It is enough to know the statement.
Nothing else on a revision list depends on it, and the combinatorial content is already in the orbit-cone correspondence.
:::
