---
schema: qual/card@1
id: P-HCAX18
kind: problem
title: Evaluate an improper integral by complex analysis
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
relations: []
review: draft
---

::: problem
Evaluate
\[
\int_0^\infty \frac{x^{1/2}}{1+x^2}\,dx
\]
by complex-analytic methods.
:::

::: solution
Use the branch
\[
z^{1/2}=e^{\frac12(\log|z|+i\arg z)},
\qquad 0<\arg z<2\pi,
\]
so the branch cut is the positive real axis, and integrate
\[
F(z)=\frac{z^{1/2}}{1+z^2}
\]
around a keyhole contour about that axis.

On the upper side of the cut, $z^{1/2}=x^{1/2}$. On the lower side, $\arg z\to2\pi$, so $z^{1/2}=-x^{1/2}$; because the lower side is traversed from $R$ to $\varepsilon$, its contribution has the same sign as the upper one. The circular arcs tend to zero as $\varepsilon\downarrow0$ and $R\to\infty$. Hence
\[
\oint F(z)\,dz
\longrightarrow
2\int_0^\infty\frac{x^{1/2}}{1+x^2}\,dx.
\]

The poles inside the contour are $i$ and $-i$. With the chosen branch,
\[
i^{1/2}=e^{i\pi/4},
\qquad
(-i)^{1/2}=e^{3i\pi/4}.
\]
Therefore
\[
\operatorname{Res}(F,i)
=\frac{e^{i\pi/4}}{2i}
=\frac{1-i}{2\sqrt2},
\]
and
\[
\operatorname{Res}(F,-i)
=\frac{e^{3i\pi/4}}{-2i}
=\frac{-1-i}{2\sqrt2}.
\]
Their sum is $-i/\sqrt2$. By the residue theorem,
\[
2\int_0^\infty\frac{x^{1/2}}{1+x^2}\,dx
=2\pi i\left(-\frac{i}{\sqrt2}\right)
=\sqrt2\,\pi.
\]
Thus
\[
\boxed{\displaystyle
\int_0^\infty\frac{x^{1/2}}{1+x^2}\,dx
=\frac{\pi}{\sqrt2}.}
\]
:::
