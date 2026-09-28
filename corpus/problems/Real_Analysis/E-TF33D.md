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

::: {.exercise}
- Give an example showing that this fails if $g$ is not bounded.

- Show that if $f\in C^1$ then $f$ is equal to its Fourier *series*.
:::

::: {.solution}
On $\RR$ use $\hat f(\xi) = \int f(x)e^{-ix\xi}\,dx$; on the circle use $\hat f(n) = \frac{1}{2\pi}\int_0^{2\pi} f(x)e^{-inx}\,dx$.

<1>1. For $f(x) = e^{-|x|}$ and $g(\xi) = 1 + \xi^2$, $f \in L^1(\RR)$ and $\int \hat f\,g = \infty$, while $\hat g$ is not defined as a Lebesgue integral.

<2>1. $\hat f(\xi) = \frac{2}{1 + \xi^2}$.

::: {.proof}
$\int_0^\infty e^{-x}e^{-ix\xi}\,dx = \frac{1}{1+i\xi}$ and $\int_{-\infty}^0 e^{x}e^{-ix\xi}\,dx = \frac{1}{1-i\xi}$, and their sum is $\frac{2}{1+\xi^2}$.
:::

<2>2. Q.E.D.

::: {.proof}
By step <2>1, $\hat f\,g \equiv 2$, whose integral over $\RR$ is infinite. Since $g \notin L^1(\RR)$, the integral $\int g(\xi)e^{-ix\xi}\,d\xi$ does not converge absolutely for any $x$, so the right side $\int f\,\hat g$ is not defined.
:::

<1>2. If $f$ is $2\pi$-periodic and $C^1$, then $\sum_n \hat f(n)e^{inx}$ converges absolutely and uniformly to $f$.

<2>1. For $n \ne 0$, $\hat f(n) = \frac{1}{in}\widehat{f'}(n)$.

::: {.proof}
Integration by parts gives $\hat f(n) = \frac{1}{2\pi}\Big[\frac{f(x)e^{-inx}}{-in}\Big]_0^{2\pi} + \frac{1}{in}\cdot\frac{1}{2\pi}\int_0^{2\pi} f'(x)e^{-inx}\,dx$, and the boundary term vanishes by $2\pi$-periodicity of $f$.
:::

<2>2. $\sum_{n \in \ZZ}|\hat f(n)| < \infty$.

::: {.proof}
By step <2>1 and the Cauchy--Schwarz inequality, $\sum_{n\ne0}|\hat f(n)| = \sum_{n\ne0}\frac{|\widehat{f'}(n)|}{|n|} \le \Big(\sum_{n\ne0}|\widehat{f'}(n)|^2\Big)^{1/2}\Big(\sum_{n\ne0}\frac{1}{n^2}\Big)^{1/2}$. The first factor is finite by Bessel's inequality, since $f'$ is continuous and hence in $L^2$.
:::

<2>3. The series $\sum_n \hat f(n)e^{inx}$ converges uniformly to a continuous function $g$ with $\hat g(n) = \hat f(n)$ for all $n$.

::: {.proof}
Uniform convergence follows from step <2>2 and the Weierstrass M-test, since $|e^{inx}| = 1$. The uniform limit of the continuous partial sums $S_N$ is continuous, and uniform convergence lets the limit pass under the integral, so $\hat g(n) = \lim_N \widehat{S_N}(n) = \hat f(n)$.
:::

<2>4. $g = f$.

::: {.proof}
$h = f - g$ is continuous with $\hat h \equiv 0$ by step <2>3. By Fejér's theorem $h \ast F_N \to h$ uniformly, where $F_N$ is the Fejér kernel, and $h \ast F_N = \sum_{|k|\le N}\big(1 - \frac{|k|}{N+1}\big)\hat h(k)e^{ikx} = 0$. So $h = 0$.
:::

<2>5. Q.E.D.

::: {.proof}
Steps <2>2--<2>4.
:::
:::

::: {.remark}
The first part refers to the identity $\int \hat f\,g = \int f\,\hat g$, which holds for $f, g \in L^1$ by Fubini's theorem.
:::
