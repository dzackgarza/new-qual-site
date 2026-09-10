---
schema: qual/card@1
id: E-SS2.EX-2
kind: problem
title: 'SS 2.2: $\int_0^\infty\frac{\sin x}{x}\,dx$'
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: exercise
2. Show that $\int _ { 0 } ^ { \infty } { \frac { \sin { x } } { x } } d x = { \frac { \pi } { 2 } }$

[Hint: The integral equals $\begin{array} { r } { \frac { 1 } { 2 i } \int _ { - \infty } ^ { \infty } \frac { e ^ { i x } - 1 } { x } } \end{array}$ dx. Use the indented semicircle.]
:::

::: solution
For $R>0$, let $C_R$ be the positively oriented upper semicircle from $R$ to $-R$. The function
\[
F(z)=\frac{e^{iz}-1}{z}
\]
has a removable singularity at $0$, so after defining $F(0)=i$ it is entire. Integrating around the upper half-disc gives
\[
\int_{-R}^R\frac{e^{ix}-1}{x}\,dx
+\int_{C_R}\frac{e^{iz}-1}{z}\,dz=0.
\tag{1}
\]

Split the arc integral. Parametrizing $C_R$ by $z=Re^{i\theta}$, $0\le\theta\le\pi$, gives
\[
\int_{C_R}\frac{dz}{z}=i\pi.
\tag{2}
\]
Also
\[
\left|\int_{C_R}\frac{e^{iz}}{z}\,dz\right|
\le\int_0^\pi e^{-R\sin\theta}\,d\theta.
\]
Using $\sin\theta\ge2\theta/\pi$ on $[0,\pi/2]$ and symmetry,
\[
\int_0^\pi e^{-R\sin\theta}\,d\theta
\le2\int_0^{\pi/2}e^{-2R\theta/\pi}\,d\theta
\le\frac\pi R\longrightarrow0.
\tag{3}
\]
Thus (1)--(3) imply
\[
\lim_{R\to\infty}\int_{-R}^R\frac{e^{ix}-1}{x}\,dx=i\pi.
\tag{4}
\]
The real part of the integrand, $(\cos x-1)/x$, is odd, while its imaginary part, $\sin x/x$, is even. Hence
\[
\int_{-R}^R\frac{e^{ix}-1}{x}\,dx
=2i\int_0^R\frac{\sin x}{x}\,dx.
\]
Taking $R\to\infty$ and using (4) gives
\[
2i\int_0^\infty\frac{\sin x}{x}\,dx=i\pi,
\]
so
\[
\boxed{\displaystyle \int_0^\infty\frac{\sin x}{x}\,dx=\frac\pi2}.
\]
:::
