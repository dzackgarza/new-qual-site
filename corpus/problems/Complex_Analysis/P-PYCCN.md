---
schema: qual/card@1
id: P-PYCCN
kind: problem
title: A conformal map from the lens $|z-1|<2\cap|z+1|<2$ onto $\HH$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: problem
Find a conformal  map from $\theset{\abs{z-1} < 2} \intersect \theset{\abs{z+1} < 2}$ to $\HH$.
:::

::: solution
The two boundary circles meet at
\[
z=\pm i\sqrt3.
\]
Set
\[
T(z)=\frac{z-i\sqrt3}{z+i\sqrt3}.
\]
Then $T$ sends the two intersection points to $0$ and $\infty$, so each of the
two boundary circles is sent to a line through the origin, hence to a ray on
the relevant boundary arc.

To identify the rays, note that $-1$ lies on the circle $|z-1|=2$ and $1$ lies
on $|z+1|=2$. Direct computation gives
\[
T(-1)=e^{2\pi i/3},
\qquad
T(1)=e^{4\pi i/3}.
\]
Also $0$ lies in the lens and $T(0)=-1=e^{i\pi}$. Thus $T$ maps the lens
biholomorphically onto the sector
\[
\frac{2\pi}{3}<\arg w<\frac{4\pi}{3}.
\]
After rotating by $e^{-2\pi i/3}$ we obtain the sector
$0<\arg w<2\pi/3$. On this sector choose the branch of $w^{3/2}$ with
$0<\arg(w^{3/2})<\pi$. Therefore
\[
\boxed{
\Phi(z)=
\left(
e^{-2\pi i/3}\frac{z-i\sqrt3}{z+i\sqrt3}
\right)^{3/2}}
\]
is a conformal bijection from the lens onto the upper half-plane.
:::
