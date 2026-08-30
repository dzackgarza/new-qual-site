---
schema: qual/card@1
id: P-JHUMAY11ANF
kind: problem
title: "(continuous functions on the circle S1)."
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $f \in L^1(S^1)$ such that $\widehat{f} \in \ell^1(\mathbb{Z})$.
Prove that $f \in C(S^1)$ (that is, $f$ is equal almost everywhere to a continuous function on the circle $S^1$).
:::

::: {.solution}
<1>1. Construct a candidate continuous function $g$ via the Fourier inversion formula: <2>1. Define $g(x) = \sum_{n=-\infty}^\infty \widehat{f}(n) e^{inx}$ for $x \in \mathbb{R}$.
Proof: definition.
<2>2. Since $|\widehat{f}(n) e^{inx}| = |\widehat{f}(n)|$ and $\sum_{n=-\infty}^\infty |\widehat{f}(n)| < \infty$ (as $\widehat{f} \in \ell^1(\mathbb{Z})$), the series converges absolutely and uniformly on $\mathbb{R}$ by the Weierstrass $M$-test.
Proof: Weierstrass $M$-test with majorant $M_n = |\widehat{f}(n)|$.
<2>3. Each term $x \mapsto \widehat{f}(n) e^{inx}$ is continuous and $2\pi$-periodic.
Proof: exponential functions are smooth and periodic.
<2>4. The uniform limit of continuous, $2\pi$-periodic functions is continuous and $2\pi$-periodic, so $g \in C(S^1)$.
Proof: uniform limit theorem for continuous functions.

<1>2. Show that $\widehat{g}(k) = \widehat{f}(k)$ for all $k \in \mathbb{Z}$: <2>1. The $k$-th Fourier coefficient of $g$ is:
\[
\widehat{g}(k) = \frac{1}{2\pi} \int_{-\pi}^\pi g(x) e^{-ikx}\,dx = \frac{1}{2\pi} \int_{-\pi}^\pi \left(\sum_{n=-\infty}^\infty \widehat{f}(n) e^{inx}\right) e^{-ikx}\,dx.
\]
Proof: definition of Fourier coefficients.
<2>2. By uniform convergence, summation and integration commute:
\[
\widehat{g}(k) = \sum_{n=-\infty}^\infty \widehat{f}(n) \left(\frac{1}{2\pi}\int_{-\pi}^\pi e^{i(n-k)x}\,dx\right).
\]
Proof: term-by-term integration of uniformly convergent series.
<2>3. By orthogonality of the complex exponentials on $[-\pi, \pi]$:
\[
\frac{1}{2\pi} \int_{-\pi}^\pi e^{i(n-k)x}\,dx = \delta_{n, k} = \begin{cases} 1 & n = k, \\ 0 & n \neq k. \end{cases}
\]
Proof: $\int_{-\pi}^\pi e^{imx}\,dx = 0$ for $m \neq 0$ and $2\pi$ for $m = 0$.
<2>4. Thus $\widehat{g}(k) = \widehat{f}(k)$ for all $k \in \mathbb{Z}$.
Proof: <2>2 and <2>3.

<1>3. Show that $f = g$ almost everywhere: <2>1. Consider the difference $h = f - g \in L^1(S^1)$.
Proof: $f \in L^1(S^1)$ and $g \in C(S^1) \subset L^1(S^1)$.
<2>2. By linearity of the Fourier transform, $\widehat{h}(k) = \widehat{f}(k) - \widehat{g}(k) = 0$ for all $k \in \mathbb{Z}$.
Proof: <1>2. <2>3. By the Uniqueness Theorem for Fourier coefficients on $L^1(S^1)$ (via Fejér kernels / density of trigonometric polynomials), an $L^1(S^1)$ function whose Fourier coefficients all vanish is zero almost everywhere.
Proof: Fejér's theorem on Cesàro summability of Fourier series in $L^1$.
<2>4. Hence $h(x) = 0$ a.e., so $f(x) = g(x)$ almost everywhere on $S^1$.
Proof: <2>2 and <2>3.

<1>4. Conclusion: $f$ coincides almost everywhere with the continuous function $g \in C(S^1)$, so $f \in C(S^1)$.
Q.E.D. Proof: <1>1 and <1>3.
:::
