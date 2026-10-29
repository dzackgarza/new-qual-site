---
schema: qual/card@1
id: P-AIDWR
kind: problem
title: A continuous function on $[0,1]$ orthogonal to $x^n$ for all $n\ge 99$ vanishes
classification:
  areas:
  - real-analysis
  topics:
  - Stone-Weierstrass
  - Density
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Suppose that $f\in C([0,1])$ and that $\displaystyle \int_0^1 f(x)x^n\,dx=0$ for all $n=99,100,101,\ldots$.
Show that $f\equiv 0$.\

> Note: Many variations on this problem exist.
> See June 2012 6b and others.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The hypotheses give $\int_0^1 f(x)\,x^{99}p(x)\,dx = 0$ for every polynomial $p$.

::: pf-proof

Write $p(x)=\sum_{j=0}^N a_jx^j$. By linearity of integration,
$$
\int_0^1 f(x)x^{99}p(x)\,dx
=\sum_{j=0}^N a_j\int_0^1 f(x)x^{99+j}\,dx=0.
$$

:::

:::

::: {.pf-step #s2}

Consequently $\int_0^1 f(x)\,x^{99}h(x)\,dx = 0$ for every $h \in C([0,1])$.

::: pf-proof

::: pf-step

For every $h\in C([0,1])$ there are polynomials $p_k$ converging uniformly to $h$.

::: pf-proof

This is the Weierstrass approximation theorem on $[0,1]$.

:::

:::

::: {.pf-step #s2-2}

The integrals of $fx^{99}p_k$ converge to the integral of $fx^{99}h$.

::: pf-proof

Since $0\le x^{99}\le1$ and $f$ is bounded,
$$
\abs{\int_0^1 f(x)x^{99}(p_k(x)-h(x))\,dx}
\leq\norm{f}_\infty\norm{p_k-h}_\infty\longrightarrow0.
$$

:::

:::

::: pf-qed

By step [](#s2-2){.pf-ref} and step [](#s1){.pf-ref}, the integral of $fx^{99}h$ is the limit of integrals equal to zero.

:::

:::

:::

::: {.pf-step #s3}

$\int_0^1 x^{99}f(x)^2\,dx = 0$.

::: pf-proof

Apply step [](#s2){.pf-ref} with $h=f$, which is continuous by hypothesis.

:::

:::

::: pf-step

$f \equiv 0$.

::: pf-proof

The continuous function $x\mapsto x^{99}f(x)^2$ is nonnegative. If it were positive at some point, continuity would give a subinterval of positive length on which it has a positive lower bound, contradicting step [](#s3){.pf-ref}. Hence $x^{99}f(x)^2=0$ throughout $[0,1]$. For $x>0$ this implies $f(x)=0$, and continuity at zero gives $f(0)=0$.

:::

:::

:::

:::
