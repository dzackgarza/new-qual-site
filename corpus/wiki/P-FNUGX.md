---
schema: qual/card@1
id: P-FNUGX
kind: problem
title: "Show that a uniform limit of bounded functions is bounded.\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
  - convergence-of-functions
  - differentiation
  - series-of-functions
relations: []
review: draft
---

::: problem
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
> **AI-Generated Solution**

<1>1. A uniform limit of bounded functions is bounded.
    Proof: pick $N$ with $\|f_n - f\|_\infty < 1$ for $n \ge N$; then $\|f\|_\infty \le \|f_N\|_\infty + 1 < \infty$.

<1>2. A uniform limit of continuous functions is continuous.
    Proof: given $\eps > 0$, choose $n$ with $\|f_n - f\|_\infty < \eps/3$; by continuity of $f_n$ choose $\delta$ with $|x-y| < \delta \Rightarrow |f_n(x) - f_n(y)| < \eps/3$; then $|f(x) - f(y)| \le |f(x) - f_n(x)| + |f_n(x) - f_n(y)| + |f_n(y) - f(y)| < \eps$ ($\eps/3$ trick).

<1>3. If $f_n \in C^1[a,b]$, $f_n' \to g$ uniformly, and $f_n(x_0)$ converges for some $x_0$, then $f_n \to f$ uniformly for some differentiable $f$ with $f' = g$.
    <2>1. For $m, n$ and any $x$: $|f_m(x) - f_n(x)| \le |f_m(x_0) - f_n(x_0)| + (b-a)\|f_m' - f_n'\|_\infty$.
        Proof: $f_m - f_n$ is differentiable with derivative $f_m' - f_n'$; by the Mean Value Theorem, $|(f_m - f_n)(x) - (f_m - f_n)(x_0)| \le \|f_m' - f_n'\|_\infty |x - x_0|$.
    <2>2. $(f_n)$ is uniformly Cauchy, so $f_n \to f$ uniformly.
        Proof: <2>1 bounds the uniform distance by the Cauchy data (convergent at $x_0$, uniformly Cauchy derivatives); completeness of $C_b[a,b]$.
    <2>3. $f$ is differentiable with $f' = g$.
        Proof: fix $x$; write $f_n(t) = f_n(x_0) + \int_{x_0}^t f_n'(s)\,ds$ (FTC), pass to the limit: $f(t) = f(x_0) + \int_{x_0}^t g(s)\,ds$ (uniform convergence passes under the integral), and the right side is differentiable with derivative $g(t)$ (FTC for continuous $g$).

<1>4. Uniform convergence $\Rightarrow$ pointwise $\Rightarrow$ a.e. convergence; neither implication reverses.
    <2>1. Uniform $\Rightarrow$ pointwise: convergence at each $x$ is a special case of uniform convergence.
        Proof: definition.
    <2>2. Pointwise $\Rightarrow$ a.e.: a.e. convergence allows failure on a null set.
        Proof: definition.
    <2>3. Pointwise $\not\Rightarrow$ uniform: $f_n(x) = x^n$ on $[0,1]$ converges pointwise to $\chi_{\{1\}}$ but not uniformly.
        Proof: $\sup_{[0,1]}|x^n - \chi_{\{1\}}(x)| = 1 \not\to 0$.
    <2>4. A.e. $\not\Rightarrow$ pointwise: $f_n = \chi_{[0, 1/n)}$ on $[0,1]$ converges to $0$ a.e. (pointwise for every $x > 0$) but not pointwise everywhere: $f_n(0) = 1 \not\to 0$.
        Proof: for $x > 0$, eventually $1/n < x$, so $f_n(x) = 0$; but at $x = 0$ every $f_n(0) = 1$.
    <2>5. Q.E.D.
        Proof: <2>3 and <2>4 exhibit non-reversibility.

<1>5. $\sum x^n/n!$ converges uniformly on every compact subset of $\RR$.
    Proof: on $[-M, M]$, $\left|\frac{x^n}{n!}\right| \le \frac{M^n}{n!}$ and $\sum M^n/n! = e^M < \infty$; the Weierstrass $M$-test applies.
:::
