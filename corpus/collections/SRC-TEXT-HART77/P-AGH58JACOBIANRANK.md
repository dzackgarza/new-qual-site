---
schema: qual/card@1
id: P-AGH58JACOBIANRANK
kind: problem
title: Jacobian rank criterion for nonsingularity in $\PP^n$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nonsingular Varieties
  - Projective Varieties
  - Jacobian Criterion
relations: []
review: draft
---

::: problem
Let $Y \subseteq \PP^n$ be a projective variety of dimension $r$. Let $f_1, \ldots, f_t \in S = k[x_0, \ldots, x_n]$ be homogeneous polynomials generating the ideal of $Y$. Let $P \in Y$ be a point with homogeneous coordinates $P = (a_0, \ldots, a_n)$. Show that $P$ is nonsingular on $Y$ if and only if the matrix
$$
\left[ \frac{\partial f_i}{\partial x_j}(a_0, \ldots, a_n) \right]
$$
has rank $n - r$.

*Hint:* Show that this rank does not depend on the homogeneous coordinates chosen for $P$; pass to an open affine $U \subseteq \PP^n$ containing $P$ and use the affine Jacobian matrix; and use Euler's lemma, which says that a homogeneous polynomial $f$ of degree $d$ satisfies $\sum_i x_i \frac{\partial f}{\partial x_i} = d \cdot f$.
:::
