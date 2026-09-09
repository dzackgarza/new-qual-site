---
schema: qual/card@1
id: P-HCAX6
kind: problem
title: Areas of spherical and hyperbolic triangles
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Geometry
relations: []
review: draft
---

::: problem
Determine and prove the area formulas for spherical and hyperbolic triangles in terms of their angles.
:::

::: solution
Let a geodesic triangle have interior angles $\alpha,\beta,\gamma$.

For the unit sphere, whose Gaussian curvature is $K=1$,
\[
\boxed{
\operatorname{Area}
=\alpha+\beta+\gamma-\pi.}
\]
For the hyperbolic plane normalized to curvature $K=-1$,
\[
\boxed{
\operatorname{Area}
=\pi-(\alpha+\beta+\gamma).}
\]

Both formulas are immediate from Gauss--Bonnet. Along each side of a geodesic triangle the geodesic curvature is zero. The exterior turning angle at a vertex with interior angle $\alpha$ is $\pi-\alpha$, and similarly at the other two vertices. Thus Gauss--Bonnet gives
\[
\int_T K\,dA
+(\pi-\alpha)+(\pi-\beta)+(\pi-\gamma)
=2\pi.
\]
If the curvature is the constant $K$, this becomes
\[
K\operatorname{Area}(T)
=\alpha+\beta+\gamma-\pi.
\]
Substituting $K=1$ gives the spherical excess formula, while substituting $K=-1$ gives the hyperbolic defect formula.

For a sphere of radius $R$, where $K=1/R^2$, the spherical formula becomes
\[
\operatorname{Area}
=R^2(\alpha+\beta+\gamma-\pi),
\]
and for a hyperbolic plane of curvature $-1/R^2$ it becomes
\[
\operatorname{Area}
=R^2(\pi-\alpha-\beta-\gamma).
\]
:::
