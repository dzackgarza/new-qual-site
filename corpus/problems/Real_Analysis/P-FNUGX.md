---
schema: qual/card@1
id: P-FNUGX
kind: problem
title: Uniform limits of bounded and continuous functions, termwise differentiation,
  and $\sum x^n/n!$ on compacta
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Convergence of Functions
  - Differentiation
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
- Show that a uniform limit of bounded functions is bounded.

- Show that a uniform limit of continuous function is continuous.

  - I.e. if $f_n\to f$ uniformly with each $f_n$ continuous then $f$ is continuous.

- Show that

  - $f_n: [a, b]\to \RR$ are continuously differentiable with derivatives $f_n'$

  - The sequence of derivatives $f_n'$ converges uniformly to some function $g$

  - There exists *at least one* point $x_0$ such that $\lim_n f_n(x_0)$ exists,

  - Then $f_n \to f$ uniformly to some differentiable $f$, and $f' = g$.

- Prove that uniform convergence implies pointwise convergence implies a.e. convergence, but none of the implications may be reversed.

- Show that $\sum {x^n \over n!}$ converges uniformly on any compact subset of $\RR$.
:::
::: {.solution}
<1>1. If $f_n \to f$ uniformly and each $f_n$ is bounded, then $f$ is bounded.

::: {.proof}
Choose $N$ with $\|f_N - f\|_\infty < 1$; then $\|f\|_\infty \le \|f_N\|_\infty + 1$. See [[E-TZFC7]].
:::

<1>2. If $f_n \to f$ uniformly and each $f_n$ is continuous, then $f$ is continuous.

::: {.proof}
Fix $x$ and $\eps > 0$. Choose $n$ with $\|f_n - f\|_\infty < \eps/3$, and $\delta > 0$ with $|f_n(x) - f_n(y)| < \eps/3$ for $|x-y| < \delta$. For such $y$, $|f(x) - f(y)| \le |f(x) - f_n(x)| + |f_n(x) - f_n(y)| + |f_n(y) - f(y)| < \eps$. See [[E-TZFC7]].
:::

<1>3. If $f_n \in C^1[a,b]$, $f_n' \to g$ uniformly, and $f_n(x_0)$ converges for some $x_0$, then $f_n \to f$ uniformly for a differentiable $f$ with $f' = g$.

<2>1. $(f_n)$ is uniformly Cauchy, so $f_n \to f$ uniformly for some continuous $f$.

::: {.proof}
By the mean value theorem applied to $f_m - f_n$, $|f_m(x) - f_n(x)| \le |f_m(x_0) - f_n(x_0)| + (b-a)\|f_m' - f_n'\|_\infty$ for every $x$, and both terms tend to $0$ as $m, n \to \infty$. A uniformly Cauchy sequence of continuous functions converges uniformly to a continuous function.
:::

<2>2. Q.E.D.

::: {.proof}
$g$ is continuous as a uniform limit of continuous functions. By the fundamental theorem of calculus $f_n(t) = f_n(x_0) + \int_{x_0}^t f_n'(s)\,ds$, and uniform convergence passes to the limit: $f(t) = f(x_0) + \int_{x_0}^t g(s)\,ds$. The fundamental theorem of calculus for continuous $g$ gives $f' = g$. See [[E-7EL3U]].
:::

<1>4. Uniform convergence implies pointwise convergence, which implies a.e. convergence, and neither implication reverses.

::: {.proof}
$|f_n(x) - f(x)| \le \sup|f_n - f|$ for each $x$, and a set where convergence fails that is empty is null. On $[0,1]$, $x^n \to \chi_{\theset{1}}$ pointwise, but $\sup_{[0,1]}|x^n - \chi_{\theset1}(x)| = 1$ for every $n$. On $[0,1]$, $\chi_{[0,1/n)} \to 0$ at every $x > 0$, so a.e., but $\chi_{[0,1/n)}(0) = 1$ for every $n$. See [[E-UYQED]].
:::

<1>5. $\sum x^n/n!$ converges uniformly on every compact subset of $\RR$.

::: {.proof}
A compact set lies in some $[-M, M]$, where $\left|\frac{x^n}{n!}\right| \le \frac{M^n}{n!}$ and $\sum_n M^n/n! = e^M < \infty$; the Weierstrass M-test applies.
:::
:::
