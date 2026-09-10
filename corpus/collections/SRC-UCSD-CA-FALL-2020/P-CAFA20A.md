---
schema: qual/card@1
id: P-CAFA20A
kind: problem
title: "Contour integral of sin(izπ/2)/(z^2+1) around a circle"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $\gamma$ be the closed curve given by the circle $|z - i/2| = 1$ traversed once in the positive (counterclockwise) direction.
Compute $$\int_\gamma \frac{\sin(i\pi z/2)}{z^2 + 1}\,dz.$$
:::

::: solution
The integrand has possible simple poles at $z=\pm i$. The circle has center
$i/2$ and radius $1$, so $i$ lies inside it while $-i$ lies outside it.
Thus the residue theorem gives
\[
\int_\gamma\frac{\sin(i\pi z/2)}{z^2+1}\,dz
=2\pi i\operatorname{Res}_{z=i}
\frac{\sin(i\pi z/2)}{(z-i)(z+i)}.
\]
Now
\[
\operatorname{Res}_{z=i}
=\frac{\sin(i\pi i/2)}{2i}
=\frac{\sin(-\pi/2)}{2i}
=-\frac1{2i}.
\]
Therefore
\[
\boxed{\displaystyle
\int_\gamma\frac{\sin(i\pi z/2)}{z^2+1}\,dz=-\pi.}
\]
:::
