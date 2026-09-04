---
schema: qual/card@1
id: E-2HIKG
kind: problem
title: $\int_0^\infty x^{1/3}/(1+x^2)\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---

::: {.exercise}
\[
I\da \int_0^\infty {x^{1\over 3} \over 1 + x^2} \dx = {\pi \over \sqrt 3}.
\]
:::

::: {.solution}
Let
\[
f(z)=\frac{z^{1/3}}{1+z^2},
\]
using the branch $0<\Arg z<\pi$ on the upper half-plane.
Integrate over the upper semicircle of radius $R$, indented by a semicircle of radius $\varepsilon$ around the branch point $0$.

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-26_20-04-14.png)

On the large arc,
\[
\abs{\int_{C_R}f(z)\,dz}
\le \pi R\frac{R^{1/3}}{R^2-1}
=O(R^{-2/3})\to0,
\]
and similarly the small arc is $O(\varepsilon^{4/3})\to0$.

Along the positive real axis, $z^{1/3}=x^{1/3}$.
Along the negative real axis approached from above, $(-x)^{1/3}=e^{i\pi/3}x^{1/3}$ for $x>0$.
Taking account of the orientation, the two straight pieces therefore tend to
\[
\qty{1+e^{i\pi/3}}I.
\]

The only enclosed pole is $z=i$, and on the chosen branch
\[
\Res_{z=i}f(z)
=\frac{i^{1/3}}{2i}
=\frac{e^{i\pi/6}}{2i}.
\]
Hence the residue theorem gives
\[
\qty{1+e^{i\pi/3}}I
=2\pi i\frac{e^{i\pi/6}}{2i}
=\pi e^{i\pi/6}.
\]
Since
\[
1+e^{i\pi/3}=2e^{i\pi/6}\cos\qty{\pi\over6}
=\sqrt3\,e^{i\pi/6},
\]
we obtain
\[
I={\pi\over\sqrt3}.
\]
:::
