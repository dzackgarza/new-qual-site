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
$$
\frac{1}{2 \pi i} \int_{\gamma} \frac{f(\xi)}{\xi-z} d \xi=\left\{\begin{array}{ll}
A, & \text { if } z \in \Omega_{1} \\
-f(z)+A, & \text { if } z \in \Omega_{2}
\end{array}\right.
.$$
:::

::: {.solution}
Write $I(z)$ for the left side, orient $\gamma$ positively, and let $C_R$ be the positively oriented circle $\abs\xi=R$, with $R$ so large that $C_R$ encloses $\gamma$ and $z$.

::: pf

::: {.pf-step #big-circle}
$\displaystyle\lim_{R\to\infty}\frac1{2\pi i}\int_{C_R}\frac{f(\xi)}{\xi-z}\,d\xi = A$.

::: pf-proof
Split the integrand as $\frac{A}{\xi-z}+\frac{f(\xi)-A}{\xi-z}$. The first term integrates to $2\pi i A$. For the second, $\sup_{C_R}\abs{f-A}\to 0$ and $\abs{\xi-z}\geq R-\abs z$ on $C_R$, so its integral is at most $2\pi R\sup_{C_R}\abs{f-A}/(R-\abs z)\to 0$.
:::

:::

::: pf-step
If $z\in\Omega_1$, then $I(z)=A$.

::: pf-proof
$\xi\mapsto f(\xi)/(\xi-z)$ is holomorphic on a neighborhood of the closed region between $\gamma$ and $C_R$, so by Cauchy's theorem its integrals over $\gamma$ and $C_R$ agree for every large $R$. Apply step [](#big-circle){.pf-ref}.
:::

:::

::: pf-step
If $z\in\Omega_2$, then $I(z)=A-f(z)$.

::: pf-proof
Now $z$ lies in the region between $\gamma$ and $C_R$. Cauchy's integral formula on that region gives
$$
\frac1{2\pi i}\int_{C_R}\frac{f(\xi)}{\xi-z}\,d\xi - I(z) = f(z).
$$
Let $R\to\infty$ and apply step [](#big-circle){.pf-ref}: $A - I(z) = f(z)$.
:::

:::

:::

:::
