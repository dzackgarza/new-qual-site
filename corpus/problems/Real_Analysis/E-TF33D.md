---
schema: qual/card@1
id: E-TF33D
kind: problem
title: Fourier multiplication formula fails for unbounded $g$; $C^1$ functions equal
  their Fourier series
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - Series of Functions
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: exercise
- Give an example showing that this fails if $g$ is not bounded.

- Show that if $f\in C^1$ then $f$ is equal to its Fourier *series*.
:::

::: {.solution}
**Context:** part (a) refers to the identity $\int \hat f\,g = \int f\,\hat g$ from the parent problem (valid for $f, g \in L^1$ by Fubini).
It asks what goes wrong when $g$ is not bounded.

<1>1. The identity fails when $g$ is unbounded.
<2>1. Take $f(x) = e^{-|x|}$ and $g(\xi) = 1 + \xi^2$ on $\RR$.
::: {.proof}
$f \in L^1(\RR)$; $g$ is unbounded and not integrable.
:::
<2>2. $\hat f(\xi) = \frac{2}{1 + \xi^2}$ (up to the convention-dependent constant), so $\int \hat f(\xi) g(\xi)\,d\xi = \int 2\,d\xi = \infty$.
::: {.proof}
direct computation of the transform of $e^{-|x|}$; then the product $\hat f g \equiv 2$ has infinite integral.
:::
<2>3. $\hat g$ does not exist as a function (since $g \notin L^1$), so $\int f\,\hat g$ is not defined; in particular the identity fails.
::: {.proof}
the identity requires both integrals to make sense; here the left side diverges and the right side is undefined.
:::
<2>4. Q.E.D.
::: {.proof}
<2>2 and <2>3 exhibit a failure with $g$ unbounded.
:::
(When both sides are defined, the identity holds by Fubini — the failure is exactly the loss of integrability.)

<1>2. If $f \in C^1$ on the circle, its Fourier series converges absolutely, hence uniformly, to $f$.
<2>1. For $n \ne 0$, $\hat f(n) = \frac{1}{in}\widehat{f'}(n)$.
::: {.proof}
integration by parts: $\hat f(n) = \frac{1}{2\pi}\int_0^{2\pi} f(x)e^{-inx}\,dx = \frac{1}{2\pi}\Big[\frac{f(x)e^{-inx}}{-in}\Big]_0^{2\pi} + \frac{1}{in}\cdot\frac{1}{2\pi}\int_0^{2\pi} f'(x)e^{-inx}\,dx$, and the boundary terms cancel by $2\pi$-periodicity of $f$.
:::
<2>2. $\sum_{n \in \ZZ}|\hat f(n)| < \infty$.
::: {.proof}
$\sum_{n\ne0}|\hat f(n)| = \sum_{n\ne0}\frac{|\widehat{f'}(n)|}{|n|} \le \Big(\sum_{n\ne0}|\widehat{f'}(n)|^2\Big)^{1/2}\Big(\sum_{n\ne0}\frac{1}{n^2}\Big)^{1/2} < \infty$ by Cauchy–Schwarz, by Parseval ($\sum|\widehat{f'}(n)|^2 = \|f'\|_2^2 < \infty$, as $f'$ is continuous), and by convergence of $\sum 1/n^2$.
:::
<2>3. The series $\sum_n \hat f(n)e^{inx}$ converges uniformly to a continuous function $g$ with $\hat g(n) = \hat f(n)$ for all $n$.
::: {.proof}
Weierstrass M-test from <2>2 since $|e^{inx}| = 1$; the uniform limit of continuous partial sums is continuous; and uniform convergence passes under the integral, so $\hat g(n) = \lim_N \widehat{S_N}(n) = \hat f(n)$.
:::
<2>4. $g = f$.
::: {.proof}
$h = f - g$ is continuous with $\hat h \equiv 0$; by Fejér's theorem $h \ast F_N \to h$ uniformly, where $F_N$ is the Fejér kernel, but $h \ast F_N = \sum_{|k|\le N}\big(1 - \frac{|k|}{N+1}\big)\hat h(k)e^{ikx} = 0$; hence $h = 0$.
:::
<2>5. Q.E.D.
::: {.proof}
<2>2–<2>4 show the Fourier series of $f$ converges to $f$ (uniformly).
:::
:::
