---
schema: qual/card@1
id: P-HH4R3
kind: problem
title: Cauchy integral formula for a function holomorphic outside $\gamma$ with limit
  $A$ at infinity
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Contour Integration
relations: []
review: draft
---

::: {.problem}
Let $\gamma$ be a piecewise smooth simple closed curve with interior $\Omega_1$ and exterior $\Omega_2$.
Assume $f'$ exists in an open set containing $\gamma$ and $\Omega_2$ with $\lim_{z\to \infty} f(z) = A$.
Show that
\[
\frac{1}{2 \pi i} \int_{\gamma} \frac{f(\xi)}{\xi-z} d \xi=\left\{\begin{array}{ll}
A, & \text { if } z \in \Omega_{1} \\
-f(z)+A, & \text { if } z \in \Omega_{2}
\end{array}\right.
.\]
:::

::: {.solution}
Let
\[
I(z)=\frac1{2\pi i}\int_\gamma\frac{f(\xi)}{\xi-z}\,d\xi.
\]
Choose a large positively oriented circle $C_R$ containing $\gamma$ and $z$.
Since $f(\xi)\to A$ as $\xi\to\infty$, the function
\[
h(\xi)=\frac{f(\xi)-A}{\xi-z}
\]
is holomorphic in the exterior of $\gamma$ and satisfies
$h(\xi)=o(1/|\xi|)$ at infinity. Hence
\[
\int_{C_R}h(\xi)\,d\xi\to0.
\]
Also
\[
\frac1{2\pi i}\int_{C_R}\frac{A}{\xi-z}\,d\xi=A.
\]

If $z\in\Omega_1$, then $f(\xi)/(\xi-z)$ is holomorphic in the annulus between
$\gamma$ and $C_R$, so the two contour integrals agree. Letting $R\to\infty$
gives
\[
I(z)=A.
\]

If $z\in\Omega_2$, choose $R$ so large that $z$ lies between $\gamma$ and
$C_R$. Cauchy's theorem on that annular region punctured at $z$ gives
\[
\int_{C_R}\frac{f(\xi)}{\xi-z}\,d\xi
-\int_\gamma\frac{f(\xi)}{\xi-z}\,d\xi
=2\pi i f(z).
\]
Passing to the limit yields
\[
A-I(z)=f(z),
\]
so
\[
I(z)=A-f(z).
\]
Thus
\[
\boxed{
I(z)=
\begin{cases}
A,&z\in\Omega_1,\\
A-f(z),&z\in\Omega_2.
\end{cases}}
\]
:::
