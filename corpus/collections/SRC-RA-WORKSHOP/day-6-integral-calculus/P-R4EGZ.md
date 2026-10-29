---
schema: qual/card@1
id: P-R4EGZ
kind: problem
title: A continuous nonnegative $f$ on $[0,1]$ with $f(0)>0$ has $\int_0^1 f>0$
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Suppose that $f$ is continuous and $f(x)\geq 0$ on $[0,1]$.
If $f(0)>0$, prove that $\int_0^1 f(x)dx>0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There is $\delta \in (0,1)$ with $f(x) > f(0)/2$ for all $x \in [0,\delta]$.

::: pf-proof

Continuity at $0$ with $\varepsilon=f(0)/2>0$ supplies $\eta>0$ such that $\abs{f(x)-f(0)}<f(0)/2$ whenever $x\in[0,1]$ and $\abs{x}<\eta$. Choose $0<\delta<\min\{1,\eta\}$. For every $x\in[0,\delta]$, one has $f(x)>f(0)/2$.

:::

:::

::: pf-step

$\int_0^1 f(x)\,dx>0$.

::: pf-proof

Continuity guarantees Riemann integrability. Nonnegativity of $f$ on $[0,1]$ and the lower bound from step [](#s1){.pf-ref} give
$$
\int_0^1 f(x)\,dx\geq\int_0^\delta f(x)\,dx
\geq\int_0^\delta\frac{f(0)}2\,dx
=\frac{\delta f(0)}2>0.
$$

:::

:::

:::

:::
