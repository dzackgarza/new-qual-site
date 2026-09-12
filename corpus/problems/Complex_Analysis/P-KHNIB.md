---
schema: qual/card@1
id: P-KHNIB
kind: problem
title: $\int_{\RR}\frac{dx}{1+x^4}$ and the poles of $\frac{1}{1+z^4}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Poles
relations: []
review: draft
---

::: problem
Evaluate the integral
$$
\int_\mathbb{R} {dx \over 1 + x^4}
.$$

What are the poles of ${1\over 1 + z^4}$ ?
:::

::: solution
The poles are the four roots of
\[
z^4=-1=e^{i(\pi+2\pi k)},
\]
namely
\[
\boxed{
e^{i\pi/4},\quad e^{3i\pi/4},\quad e^{5i\pi/4},\quad e^{7i\pi/4}.}
\]
All are simple.

To evaluate the integral, integrate
\[
F(z)=\frac1{1+z^4}
\]
over the upper semicircle of radius $R$ and let $R\to\infty$. The arc integral
vanishes because $F(z)=O(R^{-4})$. The enclosed poles are
\[
\zeta_1=e^{i\pi/4},
\qquad
\zeta_2=e^{3i\pi/4}.
\]
Since the poles are simple,
\[
\operatorname{Res}(F;\zeta)=\frac1{4\zeta^3}.
\]
Hence
\[
\operatorname{Res}(F;\zeta_1)
+\operatorname{Res}(F;\zeta_2)
=\frac1{4}\left(e^{-3i\pi/4}+e^{-9i\pi/4}\right)
=-\frac{i}{2\sqrt2}.
\]
Therefore
\[
\int_{-\infty}^{\infty}\frac{dx}{1+x^4}
=2\pi i\left(-\frac{i}{2\sqrt2}\right)
=\boxed{\frac{\pi}{\sqrt2}}.
\]
:::
