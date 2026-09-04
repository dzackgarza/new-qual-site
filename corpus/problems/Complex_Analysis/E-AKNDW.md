---
schema: qual/card@1
id: E-AKNDW
kind: problem
title: $1/(1+x^2)^2$
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

:::{.exercise}
\[
\int_\RR {1 \over (1+x^2)^2} = {\pi \over 2}
.\]

 

:::

::: {.solution}
Let
\[
f(z)=\frac{1}{(1+z^2)^2}.
\]
Integrate over the positively oriented upper semicircle of radius $R>1$.
The only enclosed pole is the double pole at $z=i$, with residue
\[
\Res_{z=i}f(z)
=\left.\dd{}{z}\frac{1}{(z+i)^2}\right|_{z=i}
=-\frac{2}{(2i)^3}
=\frac{1}{4i}.
\]
Hence
\[
\int_{-R}^R f(x)\,dx+\int_{C_R}f(z)\,dz
=2\pi i\Res_{z=i}f(z)
=\frac{\pi}{2}.
\]
On $C_R$,
\[
|1+z^2|\ge R^2-1,
\]
so the ML estimate gives
\[
\abs{\int_{C_R}f(z)\,dz}
\le \pi R\frac{1}{(R^2-1)^2}\to0.
\]
Letting $R\to\infty$ yields
\[
\int_{\RR}\frac{dx}{(1+x^2)^2}=\frac{\pi}{2}.
\]
:::
