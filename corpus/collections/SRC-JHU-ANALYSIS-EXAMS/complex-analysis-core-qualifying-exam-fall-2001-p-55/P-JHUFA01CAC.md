---
schema: qual/card@1
id: P-JHUFA01CAC
kind: problem
title: Evaluating $\int_0^\infty(1+x^3)^{-1}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the cubic denominator and half-line integration limits with Fall 2001 Complex Analysis problem 3."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Used a 120-degree sector contour, checked both radial contributions and the large-arc decay, identified the single enclosed cubic pole, and simplified the residue quotient."
---

Problem 3. Compute: $\int _ { 0 } ^ { \infty } { \frac { d x } { 1 + x ^ { 3 } } } .$


::: solution
The value is
$$
\boxed{\frac{2\pi}{3\sqrt3}}.
$$

<1>1. A sector of angle $2\pi/3$ relates the two radial integrals.
::: proof
Let
$$
F(z)=\frac1{1+z^3}
$$
and use the positively oriented boundary of the sector
$$
0\le\arg z\le\frac{2\pi}{3},\qquad |z|\le R,
$$
with $R>2$. Along the positive real ray the contribution is
$$
\int_0^R\frac{dx}{1+x^3}.
$$
Along the upper ray, traversed from $Re^{2\pi i/3}$ back to zero, put
$z=e^{2\pi i/3}x$. Since $z^3=x^3$ and $dz=e^{2\pi i/3}dx$, that contribution is
$$
-e^{2\pi i/3}\int_0^R\frac{dx}{1+x^3}.
$$
Thus the two radial sides contribute
$$
\left(1-e^{2\pi i/3}\right)I_R,
\qquad
I_R=\int_0^R\frac{dx}{1+x^3}.
$$
:::

<1>2. The arc vanishes and exactly one pole lies in the sector.
::: proof
On the circular arc $|z|=R$,
$$
|F(z)|\le\frac1{R^3-1},
$$
so its integral has modulus at most
$$
\frac{(2\pi/3)R}{R^3-1}\longrightarrow0.
$$
The poles are the roots of $z^3=-1$, namely
$e^{i\pi/3}$, $-1$, and $e^{5i\pi/3}$. Only
$$
\zeta=e^{i\pi/3}
$$
lies in the interior of the sector. It is simple, with residue
$$
\operatorname{Res}_{z=\zeta}F
=\frac1{3\zeta^2}
=\frac{e^{-2\pi i/3}}3.
$$
Hence the residue theorem and the limit $R\to\infty$ give
$$
\left(1-e^{2\pi i/3}\right)I
=\frac{2\pi i}{3}e^{-2\pi i/3},
$$
where $I=\int_0^\infty(1+x^3)^{-1}dx$. The improper integral converges because
the integrand is bounded near zero and is $O(x^{-3})$ at infinity.
:::

<1>3. Simplifying the complex quotient gives the real value.
::: proof
Let $\omega=e^{2\pi i/3}=-1/2+i\sqrt3/2$. Since
$e^{-2\pi i/3}=\overline\omega=-1/2-i\sqrt3/2$,
$$
\frac{i\overline\omega}{1-\omega}
=\frac1{\sqrt3}.
$$
Therefore step <1>2 yields
$$
I=\frac{2\pi}{3}\frac1{\sqrt3}
=\frac{2\pi}{3\sqrt3}.
$$
:::
:::
