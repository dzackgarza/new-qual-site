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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source writes L^p and L^q without naming the underlying space; the statement names R^n, on which the solution works.
---

::: {.problem}
Suppose $1\leq p,q,r \leq \infty$ with
$$
{1\over p } + {1 \over q} = 1 + {1 \over r}
.$$

Prove that
$$
f \in L^p(\RR^n), g\in L^q(\RR^n) \implies f \convolve g \in L^r \text{ and } \norm{f \convolve g}_r \leq \norm{f}_p \norm{g}_q
.$$
:::

::: {.solution}
Fix $f \in L^p$, let $p'$ be the conjugate exponent of $p$, and let $Tg = f \ast g$.

::: pf

::: {.pf-step #s1}

$\norm{f \ast g}_p \le \norm{f}_p\norm{g}_1$ for $g \in L^1$.

::: pf-proof

Write $f \ast g(x) = \int f(x-y)g(y)\,dy$. By Minkowski's inequality for integrals and translation invariance of the $L^p$ norm, $\norm{f\ast g}_p \le \int \norm{f(\cdot - y)}_p\,\abs{g(y)}\,dy = \norm{f}_p\norm{g}_1$.

:::

:::

::: {.pf-step #s2}

$\norm{f \ast g}_\infty \le \norm{f}_p\norm{g}_{p'}$ for $g \in L^{p'}$.

::: pf-proof

By Hölder's inequality, $\abs{(f\ast g)(x)} \le \int \abs{f(x-y)}\abs{g(y)}\,dy \le \norm{f}_p\norm{g}_{p'}$ for every $x$.

:::

:::

::: {.pf-step #s3}

With $\theta = 1 - p/r \in [0,1]$, $\frac1q = \frac{1-\theta}{1} + \frac{\theta}{p'}$ and $\frac1r = \frac{1-\theta}{p} + \frac{\theta}{\infty}$.

::: pf-proof

$\frac{1-\theta}{p} = \frac{p/r}{p} = \frac1r$. Also $1 - \theta + \theta\left(1 - \frac1p\right) = 1 - \frac\theta p = 1 - \frac1p + \frac1r = \frac1q$ by the hypothesis. Since $\frac1q \le 1$, $\frac1p \ge \frac1r$, so $p \le r$ and $\theta \in [0,1]$.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $T$ is bounded $L^1 \to L^p$ and $L^{p'} \to L^\infty$, both with norm at most $\norm{f}_p$. By step [](#s3){.pf-ref} and the Riesz--Thorin interpolation theorem, $T$ is bounded $L^q \to L^r$ with norm at most $\norm{f}_p^{1-\theta}\norm{f}_p^{\theta} = \norm{f}_p$.

:::

:::

:::
