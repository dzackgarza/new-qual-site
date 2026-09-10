---
schema: qual/card@1
id: P-JHUFA02CAK
kind: problem
title: Evaluating $\int_0^\infty u^2/(u^6+1)\,du$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the numerator, sixth-degree denominator and half-line limits with Fall 2002 Complex Analysis problem 6."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Used the upper semicircle, identified all three upper-half-plane sixth roots of -1, computed their residues as 1/(6 zeta^3), and checked the vanishing arc estimate and evenness factor."
---

6. (20 points) Evaluate the integral:

$$
\int _ { 0 } ^ { \infty } { \frac { u ^ { 2 } d u } { u ^ { 6 } + 1 } }
$$


::: solution
The integral equals
$$
\boxed{\frac{\pi}{6}}.
$$

<1>1. The upper-half-plane residues sum to $-i/6$.
::: proof
Let
$$
F(z)=\frac{z^2}{z^6+1}.
$$
The poles are the six simple roots of $z^6=-1$. In the upper half-plane these
are
$$
\zeta_1=e^{i\pi/6},\qquad \zeta_2=e^{i\pi/2}=i,
\qquad \zeta_3=e^{5i\pi/6}.
$$
Since $(z^6+1)'=6z^5$, the residue at any such root is
$$
\operatorname{Res}_{z=\zeta}F
=\frac{\zeta^2}{6\zeta^5}
=\frac1{6\zeta^3}.
$$
Now
$$
\zeta_1^3=i,\qquad \zeta_2^3=-i,\qquad \zeta_3^3=i,
$$
so
$$
\sum_{j=1}^3\operatorname{Res}_{\zeta_j}F
=-\frac{i}{6}+\frac{i}{6}-\frac{i}{6}
=-\frac{i}{6}.
$$
:::

<1>2. The upper semicircle gives the real-line integral.
::: proof
Integrate $F$ over the contour formed by $[-R,R]$ and the counterclockwise
upper semicircle $\Gamma_R$, with $R>1$. On $|z|=R$,
$$
|F(z)|\le \frac{R^2}{R^6-1},
$$
so
$$
\left|\int_{\Gamma_R}F(z)\,dz\right|
\le \frac{\pi R^3}{R^6-1}\longrightarrow0.
$$
The residue theorem therefore yields, after letting $R\to\infty$,
$$
\int_{-\infty}^{\infty}\frac{x^2}{x^6+1}\,dx
=2\pi i\left(-\frac{i}{6}\right)=\frac{\pi}{3}.
$$
The integral converges absolutely because the integrand is bounded near zero
and is $O(x^{-4})$ at infinity.
:::

<1>3. Evenness gives the requested half-line value.
::: proof
The real integrand is even. Hence
$$
2\int_0^\infty\frac{u^2}{u^6+1}\,du
=\int_{-\infty}^{\infty}\frac{x^2}{x^6+1}\,dx
=\frac{\pi}{3},
$$
so the desired integral is $\pi/6$.
:::
:::
