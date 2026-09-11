---
schema: qual/card@1
id: E-SS8.EX-17
kind: problem
title: "If  for  , prove that"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
17. If $\psi _ { \alpha } ( z ) = ( \alpha - z ) / ( 1 - \overline { { \alpha } } z )$ for $| \alpha | < 1$ , prove that

$$
\frac {1}{\pi} \iint_ {\mathbb {D}} | \psi_ {\alpha} ^ {\prime} | ^ {2} d x d y = 1 \quad \mathrm{and} \quad \frac {1}{\pi} \iint_ {\mathbb {D}} | \psi_ {\alpha} ^ {\prime} | d x d y = \frac {1 - | \alpha | ^ {2}}{| \alpha | ^ {2}} \log \frac {1}{1 - | \alpha | ^ {2}},
$$

where in the case $\alpha = 0$ the expression on the right is understood as the limit as $| \alpha | \to 0$

[Hint: The first integral can be evaluated without a calculation. For the second, use polar coordinates, and for each fixed r use contour integration to evaluate the integral in θ.]
:::

::: solution
Let $r=|\alpha|$. Since
\[
\psi_\alpha'(z)
=-\frac{1-r^2}{(1-\overline\alpha z)^2},
\]
and $\psi_\alpha$ is an automorphism of $\mathbb D$, the change-of-variables formula for area gives
\[
\iint_{\mathbb D}|\psi_\alpha'(z)|^2\,dx\,dy
=\operatorname{Area}(\psi_\alpha(\mathbb D))
=\pi.
\]
Therefore
\[
\frac1\pi\iint_{\mathbb D}|\psi_\alpha'|^2\,dx\,dy=1.
\]

For the second integral, rotate coordinates so that $\alpha=r\ge0$. In polar coordinates $z=\rho e^{i\theta}$,
\[
\frac1\pi\iint_{\mathbb D}|\psi_\alpha'(z)|\,dx\,dy
=\frac{1-r^2}{\pi}
\int_0^1\int_0^{2\pi}
\frac{\rho\,d\theta\,d\rho}{|1-r\rho e^{i\theta}|^2}.
\]
The Poisson-kernel identity gives, for $0\le r\rho<1$,
\[
\int_0^{2\pi}\frac{d\theta}{1-2r\rho\cos\theta+r^2\rho^2}
=\frac{2\pi}{1-r^2\rho^2}.
\]
Hence
\[
\frac1\pi\iint_{\mathbb D}|\psi_\alpha'|
=2(1-r^2)\int_0^1\frac{\rho}{1-r^2\rho^2}\,d\rho
=\frac{1-r^2}{r^2}\log\frac1{1-r^2}.
\]
As $r\to0$, the right-hand side tends to $1$, which agrees with $\psi_0(z)=-z$ and $|\psi_0'|=1$.
:::
