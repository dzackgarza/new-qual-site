---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-14
kind: problem
title: Uniform convergence along a convergent sequence of points
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Continuity
  - Sequences of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
(June 2009 #4a) Let $\{f_n\}$ be a sequence of real-valued continuous functions such that $f_n\to f$ uniformly on $[0,1]$, and let $\{x_n\}\subset[0,1]$ be a sequence which converges to $x$.
Show that $$\lim_{n\to\infty}f_n(x_n)=f(x).$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The uniform limit $f$ is continuous on $[0,1]$.

::: pf-proof

Every $f_n$ is continuous, and the convergence $f_n\to f$ is uniform. The uniform limit theorem therefore gives continuity of $f$.

:::

:::

::: {.pf-step #s2}

The quantities $\abs{f_n(x_n)-f(x_n)}$ and $\abs{f(x_n)-f(x)}$ both tend to zero.

::: pf-proof

Uniform convergence gives
$$
\abs{f_n(x_n)-f(x_n)}\leq\norm{f_n-f}_\infty\longrightarrow0,
$$
because $x_n\in[0,1]$. By step [](#s1){.pf-ref}, $f$ is continuous at $x$, so $x_n\to x$ implies $f(x_n)\to f(x)$.

:::

:::

::: pf-step

$\lim_{n\to\infty}f_n(x_n)=f(x)$.

::: pf-proof

By the triangle inequality,
$$
\abs{f_n(x_n)-f(x)}
\leq\abs{f_n(x_n)-f(x_n)}+\abs{f(x_n)-f(x)}.
$$
Both terms on the right tend to zero by step [](#s2){.pf-ref}, so the left-hand side does as well.

:::

:::

:::

:::
