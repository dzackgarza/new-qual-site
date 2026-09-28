---
schema: qual/card@1
id: P-LUYHY
kind: problem
title: Young's convolution inequality
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Lp Spaces
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Suppose $1\leq p,q,r \leq \infty$ with
\[
{1\over p } + {1 \over q} = 1 + {1 \over r}
.\]

Prove that
\[
f \in L^p, g\in L^q \implies f \convolve g \in L^r \text{ and } \norm{f \convolve g}_r \leq \norm{f}_p \norm{g}_q
.\]
:::
::: {.solution}
Work on $\RR^n$, fix $f \in L^p$, let $p'$ be the conjugate exponent of $p$, and let $Tg = f \ast g$.

<1>1. $\|f \ast g\|_p \le \|f\|_p\|g\|_1$ for $g \in L^1$.

::: {.proof}
Write $f \ast g(x) = \int f(x-y)g(y)\,dy$. By Minkowski's inequality for integrals and translation invariance of the $L^p$ norm, $\|f\ast g\|_p \le \int \|f(\cdot - y)\|_p\,|g(y)|\,dy = \|f\|_p\|g\|_1$.
:::

<1>2. $\|f \ast g\|_\infty \le \|f\|_p\|g\|_{p'}$ for $g \in L^{p'}$.

::: {.proof}
By Hölder's inequality, $|(f\ast g)(x)| \le \int |f(x-y)||g(y)|\,dy \le \|f\|_p\|g\|_{p'}$ for every $x$.
:::

<1>3. With $\theta = 1 - p/r \in [0,1]$, $\frac1q = \frac{1-\theta}{1} + \frac{\theta}{p'}$ and $\frac1r = \frac{1-\theta}{p} + \frac{\theta}{\infty}$.

::: {.proof}
$\frac{1-\theta}{p} = \frac{p/r}{p} = \frac1r$. Also $1 - \theta + \theta\left(1 - \frac1p\right) = 1 - \frac\theta p = 1 - \frac1p + \frac1r = \frac1q$ by the hypothesis. Since $\frac1q \le 1$, $\frac1p \ge \frac1r$, so $p \le r$ and $\theta \in [0,1]$.
:::

<1>4. Q.E.D.

::: {.proof}
By steps <1>1 and <1>2, $T$ is bounded $L^1 \to L^p$ and $L^{p'} \to L^\infty$, both with norm at most $\|f\|_p$. By step <1>3 and the Riesz--Thorin interpolation theorem, $T$ is bounded $L^q \to L^r$ with norm at most $\|f\|_p^{1-\theta}\|f\|_p^{\theta} = \|f\|_p$.
:::
:::
