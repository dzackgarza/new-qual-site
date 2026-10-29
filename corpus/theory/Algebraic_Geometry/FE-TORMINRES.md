---
schema: qual/card@1
id: FE-TORMINRES
kind: example
title: The minimal resolution of a toric surface singularity
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Resolution of Singularities
  - Surfaces
relations:
- kind: uses
  target: PR-D2F15
- kind: uses
  target: FE-TORCD
review: draft
prompts:
- Describe the minimal resolution of a two-dimensional toric singularity.
- Resolve the cone over the rational normal curve of degree 3 and compute the exceptional self-intersection.
---

::: {.example title="The construction"}
Let $N\cong\ZZ^2$ be a lattice and let $\sigma\subseteq N_\RR$ be a two-dimensional strongly convex rational polyhedral cone.
Put
$$
P=\operatorname{conv}\bigl((\sigma\intersect N)\sm\theset{0}\bigr).
$$
The compact boundary of $P$ is a broken line through finitely many lattice points. The rays through those points form the fan of the minimal toric resolution.
Every cone of the refined fan is smooth, and no exceptional curve has self-intersection $-1$.
:::

::: {.example title="Degree three"}
For $N=\ZZ^2$, let $\sigma = \Cone\big( (0,1),\ (3,-1) \big)$. Its affine toric variety is the cone over the rational normal cubic and satisfies $\Cl(U_\sigma)\cong\ZZ/3$.
The determinant has absolute value $\abs{0 \cdot (-1) - 1 \cdot 3} = 3$, so $\sigma$ is not smooth.
The only compact-boundary lattice point not already on an original ray is $(1,0)$. Subdivision along the ray $\RR_{\geq0}(1,0)$ gives two cones satisfying
$$
\det\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = -1 , \qquad
\det\begin{bmatrix} 1 & 0 \\ 3 & -1 \end{bmatrix} = -1 ,
$$
so the subdivision resolves $U_\sigma$.
For the exceptional curve $E = D_{(1,0)}$, the relation
$$
(0,1) + (3,-1) = (3,0) = 3 \cdot (1,0)
$$
gives $E^2=-3$.
:::

::: {.remark}
The same computation for $\Cone\big( (0,1), (d,-1) \big)$ gives one exceptional curve with $E^2 = -d$: the resolution is the total space of $\OO_{\PP^1}(-d)$ with $E$ its zero section, and contracting the negative section of $\FF_d$ gives the projective cone over the rational normal curve of degree $d$.

For a general cone the boundary lattice points give a chain of rational curves with self-intersections $-b_1, \ldots, -b_r$, all $b_i \geq 2$, and the $b_i$ are the Hirzebruch--Jung continued fraction of the singularity.
The inequalities $b_i\geq2$ are the toric minimality criterion: an exceptional component of self-intersection $-1$ can be contracted.
:::
