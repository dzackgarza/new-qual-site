---
schema: qual/card@1
id: P-2CKBC
kind: problem
title: $\int_{-\infty}^\infty\frac{1+x^2}{1+x^4}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
---

::: {.problem}
Calculate
\[
\int_{-\infty}^\infty {1+x^2 \over 1+x^4}\, dx
.\]

:::

::: {.solution}
The integrand is even, so
\[
I=2\int_0^\infty\frac{1+x^2}{1+x^4}\,dx.
\]
Under the substitution $x=1/t$,
\[
\int_0^\infty\frac{x^2}{1+x^4}\,dx
=\int_0^\infty\frac{1}{1+t^4}\,dt.
\]
Hence
\[
I=4\int_0^\infty\frac{dx}{1+x^4}.
\]
The standard residue computation in the upper half-plane gives
\[
\int_{-\infty}^{\infty}\frac{dx}{1+x^4}
=2\pi i\left(
\operatorname{Res}_{z=e^{i\pi/4}}\frac1{1+z^4}
+\operatorname{Res}_{z=e^{3i\pi/4}}\frac1{1+z^4}
\right)
=\frac{\pi}{\sqrt2}.
\]
Therefore
\[
\int_0^\infty\frac{dx}{1+x^4}=\frac{\pi}{2\sqrt2},
\]
and so
\[
\boxed{I=\sqrt2\,\pi.}
\]
:::
