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

::: {.example title="The recipe"}
Let $\sigma \subseteq \RR^2$ be a two-dimensional cone.
Take the convex hull of $(\sigma \intersect N) \sm \ts{0}$.
Its compact boundary is a broken line through finitely many lattice points; the rays through those points are exactly the rays of the minimal resolution.
Every cone of the refined fan is then smooth, and the resolution is minimal because no exceptional curve has self-intersection $-1$.
:::

::: {.example title="Degree three"}
Take $\sigma = \Cone\big( (0,1),\ (3,-1) \big)$, whose affine toric variety is the cone over the rational normal cubic and has $\Cl = \ZZ/3$.
The determinant is $\abs{0 \cdot (-1) - 1 \cdot 3} = 3$, so $\sigma$ is singular.
The only lattice point on the compact boundary of the hull is $(1,0)$, so insert that ray.
Check both new cones:
\[
\det\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = -1 , \qquad
\det\begin{bmatrix} 1 & 0 \\ 3 & -1 \end{bmatrix} = -1 ,
\]
both smooth, so a single blowup resolves.
The exceptional curve $E = D_{(1,0)}$ has self-intersection read from
\[
(0,1) + (3,-1) = (3,0) = 3 \cdot (1,0) \rightsquigarrow E^2 = -3 .
\]
:::

::: {.remark}
The same computation for $\Cone\big( (0,1), (d,-1) \big)$ gives one exceptional curve with $E^2 = -d$, which is the standard model of the cone over the rational normal curve of degree $d$: contract the negative section of $\FF_d$.

For a general cone the boundary lattice points give a chain of rational curves with self-intersections $-b_1, \ldots, -b_r$, all $b_i \geq 2$, and the $b_i$ are the Hirzebruch--Jung continued fraction of the singularity.
The $b_i \geq 2$ is exactly the statement that the resolution is minimal.
:::
