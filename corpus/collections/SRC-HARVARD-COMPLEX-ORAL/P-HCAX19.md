---
schema: qual/card@1
id: P-HCAX19
kind: problem
title: Conformal equivalence of a half-disk and the disk
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
---

::: problem
Show that the upper half of the unit disk is conformally equivalent to the unit disk, and give an explicit conformal isomorphism.
:::

::: solution
Let
\[
H=\{z\in\mathbb C:|z|<1,
\operatorname{Im}z>0\}.
\]
The Möbius map
\[
T(z)=\frac{1+z}{1-z}
\]
sends the unit disk conformally onto the right half-plane. On the diameter $(-1,1)$ it takes positive real values, while on the upper semicircle it takes positive imaginary values. Hence it maps $H$ conformally onto the first quadrant
\[
Q=\{w:\operatorname{Re}w>0,
\operatorname{Im}w>0\}.
\]

The map $S(w)=w^2$ is a conformal bijection from $Q$ onto the upper half-plane, and
\[
C(\zeta)=\frac{\zeta-i}{\zeta+i}
\]
is a conformal bijection from the upper half-plane onto the unit disk. Therefore
\[
F(z)
=C(S(T(z)))
=\frac{\left(\frac{1+z}{1-z}\right)^2-i}
       {\left(\frac{1+z}{1-z}\right)^2+i}
\]
is a conformal isomorphism from the upper half of the unit disk onto the whole unit disk.
:::
