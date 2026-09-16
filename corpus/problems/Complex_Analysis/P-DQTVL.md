---
schema: qual/card@1
id: P-DQTVL
kind: problem
title: A conformal map from $\DD\setminus[0,1)$ to $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Let $D$ be the region obtained by deleting the real interval $[0, 1)$ from $\DD$; find a conformal map from $D$ to $\DD$.
:::

::: {.solution}
On
\[
D=\{0<|z|<1:\arg z\in(0,2\pi)\}
\]
choose the square-root branch
\[
s(z)=\sqrt z=|z|^{1/2}e^{i\arg z/2},
\qquad 0<\arg z<2\pi.
\]
Then $s$ maps $D$ biholomorphically onto the upper half-disk
\[
U=\{w:|w|<1,\ \Im w>0\}.
\]

Next
\[
T(w)=\frac{1+w}{1-w}
\]
maps $U$ biholomorphically onto the first quadrant: the diameter $(-1,1)$
goes to the positive real axis, while the upper semicircle goes to the
positive imaginary axis. Therefore $T(w)^2$ maps $U$ biholomorphically onto
the upper half-plane. Finally the Cayley map
\[
C(\zeta)=\frac{\zeta-i}{\zeta+i}
\]
maps the upper half-plane onto $\mathbb D$. Thus one required map is
\[
\boxed{
F(z)=
\frac{\left(\frac{1+\sqrt z}{1-\sqrt z}\right)^2-i}
     {\left(\frac{1+\sqrt z}{1-\sqrt z}\right)^2+i},
}
\]
with the square-root branch specified above.
:::
