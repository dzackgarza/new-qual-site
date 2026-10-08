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
<1>1. The hypotheses give $\int_0^1 f(x)\,x^{99}p(x)\,dx = 0$ for every polynomial $p$.

::: {.proof}
Write $p(x)=\sum_{j=0}^N a_jx^j$. By linearity of integration,
\[
\int_0^1 f(x)x^{99}p(x)\,dx
=\sum_{j=0}^N a_j\int_0^1 f(x)x^{99+j}\,dx=0.
\]
:::

<1>2. Consequently $\int_0^1 f(x)\,x^{99}h(x)\,dx = 0$ for every $h \in C([0,1])$.

<2>1. For every $h\in C([0,1])$ there are polynomials $p_k$ converging uniformly to $h$.

::: {.proof}
This is the Weierstrass approximation theorem on $[0,1]$.
:::

<2>2. The integrals of $fx^{99}p_k$ converge to the integral of $fx^{99}h$.

::: {.proof}
Since $0\le x^{99}\le1$ and $f$ is bounded,
\[
\left|\int_0^1 f(x)x^{99}(p_k(x)-h(x))\,dx\right|
\leq\|f\|_\infty\|p_k-h\|_\infty\longrightarrow0.
\]
:::

<2>3. Q.E.D.

::: {.proof}
By step <2>2 and step <1>1, the integral of $fx^{99}h$ is the limit of integrals equal to zero.
:::

<1>3. Take $h = f$: $\int_0^1 x^{99}f(x)^2\,dx = 0$.

::: {.proof}
Apply step <1>2 with $h=f$, which is continuous by hypothesis.
:::

<1>4. $f \equiv 0$.

::: {.proof}
The continuous function $x\mapsto x^{99}f(x)^2$ is nonnegative. If it were positive at some point, continuity would give a subinterval of positive length on which it has a positive lower bound, contradicting step <1>3. Hence $x^{99}f(x)^2=0$ throughout $[0,1]$. For $x>0$ this implies $f(x)=0$, and continuity at zero gives $f(0)=0$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 establishes the required identity $f\equiv0$.
:::
:::
