---
schema: qual/card@1
id: P-EMCA2
kind: problem
title: Cauchy integral formula
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
State and prove the Cauchy integral formula for holomorphic functions.
:::

::: solution
Let $\Omega\subset\mathbb C$ be open, let $f$ be holomorphic on $\Omega$, and let
$D$ be a closed disk whose interior and boundary are contained in $\Omega$. If
$a$ lies in the interior of $D$, then
\[
\boxed{\displaystyle
f(a)=\frac{1}{2\pi i}\int_{\partial D}\frac{f(z)}{z-a}\,dz.}
\]

To prove this, choose $\varepsilon>0$ so small that
$\overline{B(a,\varepsilon)}\subset\operatorname{int}D$. The function
$f(z)/(z-a)$ is holomorphic on the region between the two boundary circles, so
Cauchy's theorem gives
\[
\int_{\partial D}\frac{f(z)}{z-a}\,dz
=\int_{|z-a|=\varepsilon}\frac{f(z)}{z-a}\,dz.
\]
Write the latter integral as
\[
f(a)\int_{|z-a|=\varepsilon}\frac{dz}{z-a}
+\int_{|z-a|=\varepsilon}\frac{f(z)-f(a)}{z-a}\,dz.
\]
The first term is $2\pi i f(a)$. For the second term,
\[
\left|\int_{|z-a|=\varepsilon}
\frac{f(z)-f(a)}{z-a}\,dz\right|
\le 2\pi\max_{|z-a|=\varepsilon}|f(z)-f(a)|,
\]
which tends to $0$ as $\varepsilon\downarrow0$ by continuity of $f$ at $a$.
Thus the outer integral equals $2\pi i f(a)$, proving the formula.

More generally, the same proof together with the winding-number form of
Cauchy's theorem gives
\[
\frac{1}{2\pi i}\int_\gamma\frac{f(z)}{z-a}\,dz
=\operatorname{Ind}(\gamma,a)f(a)
\]
for any closed contour $\gamma$ null-homologous in $\Omega$ and avoiding $a$.
:::
