---
schema: qual/card@1
id: P-EEUV6
kind: problem
title: An injective conformal map from $\{|z|<1\}\setminus\{|z-1/4|\le 1/4\}$ onto
  an annulus
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Biholomorphisms
  - Fractional Linear Transformations
relations: []
review: draft
---

::: problem
Let $\Omega$ be the region inside the unit circle $\abs{z} = 1$ and outside the circle $\abs{z-{1\over 4}} = {1\over 4}$.

Find an injective conformal map from $\Omega$ onto some annulus $\theset{r < \abs{z} < 1}$ for constant $r$.
:::

::: solution
The two boundary circles are coaxial. Let
\[
\alpha=2-\sqrt3,
\qquad
\beta=2+\sqrt3.
\]
Then
\[
\alpha\beta=1,
\qquad
\alpha+\beta=4.
\]
These are the limiting points of the coaxial family: for the outer circle
$|z|=1$ we have $\alpha\beta=1$, while for the inner circle
$|z-1/4|=1/4$,
\[
(\alpha-1/4)(\beta-1/4)=1/16.
\]
Therefore the Möbius transformation
\[
T(z)=\frac{z-\alpha}{z-\beta}
\]
maps both boundary circles to circles centered at the origin.

To determine their radii, evaluate at convenient boundary points. On
$|z|=1$, using $z=1$,
\[
|T(1)|
=\frac{\sqrt3-1}{\sqrt3+1}
=2-\sqrt3
=\alpha.
\]
On $|z-1/4|=1/4$, using $z=1/2$,
\[
|T(1/2)|
=\frac{1/2-\alpha}{\beta-1/2}
=\alpha^2.
\]
Hence
\[
T(\Omega)=\{\alpha^2<|w|<\alpha\}.
\]
After dividing by $\alpha$, we obtain
\[
\boxed{
\Phi(z)=\frac1\alpha\frac{z-\alpha}{z-\beta},
\qquad
\alpha=2-\sqrt3,}
\]
and
\[
\Phi(\Omega)=\{\alpha<|w|<1\}.
\]
Thus the required annulus has inner radius
\[
\boxed{r=2-\sqrt3}.
\]
Since $\beta>1$ lies outside $\Omega$, the Möbius map is holomorphic and
injective on $\Omega$.
:::
