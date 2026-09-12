---
schema: qual/card@1
id: P-HCAX15
kind: problem
title: Schwarz--Christoffel map from the disk to a polygon
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz--Christoffel Formula
relations: []
review: draft
---

::: problem
State the formula for a conformal map from the unit disk onto the interior of a polygon whose angles are $(2-\beta_i)\pi$.
:::

::: solution
Let $\zeta_1,\dots,\zeta_n\in \partial\mathbb D$ be the prevertices corresponding to the vertices of the polygon. If the interior angle at the $i$th vertex is
\[
\alpha_i\pi=(2-\beta_i)\pi,
\]
then the Schwarz--Christoffel formula on the disk gives
\[
f'(z)=C\prod_{i=1}^n\left(1-\frac{z}{\zeta_i}\right)^{\alpha_i-1}
=C\prod_{i=1}^n\left(1-\frac{z}{\zeta_i}\right)^{1-\beta_i},
\]
where the branches are chosen holomorphically on $\mathbb D$ and $C\ne0$.

Thus one may write
\[
f(z)=A+C\int_{z_0}^z
\prod_{i=1}^n\left(1-\frac{w}{\zeta_i}\right)^{1-\beta_i}\,dw,
\]
with constants $A,C$ and prevertices $\zeta_i$ chosen so that the boundary arcs map to the required sides with the prescribed side lengths.

The exponent $1-\beta_i$ is exactly $\alpha_i-1$: when one crosses the prevertex $\zeta_i$, the argument of $f'$ changes by $(\alpha_i-1)\pi$, so the image boundary turns through the exterior angle $(1-\alpha_i)\pi=(\beta_i-1)\pi$, producing the interior angle $(2-\beta_i)\pi$ stated in the problem.
:::
