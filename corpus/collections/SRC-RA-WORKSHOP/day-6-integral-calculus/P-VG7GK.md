---
schema: qual/card@1
id: P-VG7GK
kind: problem
title: $\int_0^1\cos x\frac{x\phi'(x)-\phi(x)+\phi(0)}{x^2}\,dx<\frac{3}{2}\norm{\phi''}_\infty$
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Differentiation
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $\phi$ be a real-valued function defined on $[0,1]$ such that $\phi$, $\phi'$, and $\phi''$ are continuous on $[0,1]$.
Prove that $$\int_0^1 \cos x \frac{x\phi'(x)-\phi(x)+\phi(0)}{x^2}\,dx<\frac{3}{2}\norm{\phi''}_\infty,$$ where $\norm{\phi''}_\infty = \sup_{[0,1]}\abs{\phi''(x)}.$ Note that $3/2$ may not be the smallest possible constant.
:::

::: {.solution}

Write $N(x)\coloneqq x\phi'(x)-\phi(x)+\phi(0)$ and $M\coloneqq\norm{\phi''}_\infty$. The strict inequality needs $M>0$: if $\phi''\equiv0$, then $\phi$ is affine, $N\equiv0$, and both sides are $0$. We prove the inequality with $\le$ in general, and with $<$ when $M>0$.

::: pf

::: {.pf-step #s1}

$N(x)=\int_0^x y\,\phi''(y)\,dy$ for $x\in[0,1]$.

::: pf-proof

Differentiating,
$$
N'(x) = \phi'(x) + x\phi''(x) - \phi'(x) = x\phi''(x),
$$
and $N(0) = 0\cdot\phi'(0) - \phi(0) + \phi(0) = 0$. The fundamental theorem of calculus gives the formula.

:::

:::

::: {.pf-step #s2}

$\abs{N(x)}\le Mx^2/2$ for $x\in[0,1]$.

::: pf-proof

By step [](#s1){.pf-ref},
$$
\abs{N(x)} \le \int_0^x y\,\abs{\phi''(y)}\,dy \le M \int_0^x y\,dy = M \frac{x^2}{2} .
$$

:::

:::

::: {.pf-step #s3}

For $0<x\le1$, the integrand satisfies $\abs{\cos x\,N(x)/x^2}\le M/2$.

::: pf-proof

This follows from $\abs{\cos x} \le 1$ and step [](#s2){.pf-ref}. The integrand is continuous and bounded on $(0,1]$, so the integral converges absolutely.

:::

:::

::: pf-step

$\int_0^1 \cos x \,\frac{N(x)}{x^2}\,dx \le \frac12 M \le \frac32 M$, with strict inequality $<\frac32 M$ when $M>0$.

::: pf-proof

Integrating step [](#s3){.pf-ref} over $[0,1]$ gives
$$
\int_0^1 \cos x \,\frac{x\phi'(x) - \phi(x) + \phi(0)}{x^2}\,dx \le \int_0^1 \frac{M}{2}\,dx = \frac{1}{2}M,
$$
and $\frac12 M<\frac32 M$ exactly when $M>0$.

:::

:::

:::

:::

::: {.remark}
As stated, the strict inequality fails for affine $\phi$, where both sides vanish; it holds for every $\phi$ with $\phi''\not\equiv0$. The constant $3/2$ is not optimal: $1/2$ suffices for the non-strict bound.
:::
