---
schema: qual/card@1
id: P-U2YKB
kind: problem
title: Uniform limits of continuous functions are continuous
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Continuity
  - Sequences of Functions
relations: []
review: draft
---

::: {.problem}
Show that a uniform limit of continuous functions is continuous.
:::

::: {.solution}
Let $X$ be a topological space, let $f_n:X\to\CC$ be continuous, and suppose $f_n\to f$ uniformly on $X$. Fix $x_0\in X$ and $\varepsilon>0$.

::: pf

::: {.pf-step #uniform}

There is $N$ with $\abs{f_N(x)-f(x)}<\frac\varepsilon3$ for every $x\in X$.

::: pf-proof

This is the definition of uniform convergence.

:::

:::

::: {.pf-step #local}

There is a neighborhood $U$ of $x_0$ with $\abs{f_N(x)-f_N(x_0)}<\frac\varepsilon3$ for $x\in U$.

::: pf-proof

This is continuity of $f_N$ at $x_0$.

:::

:::

::: pf-step

$f$ is continuous.

::: pf-proof

For $x \in U$, steps [](#uniform){.pf-ref} and [](#local){.pf-ref} give
$$
\abs{f(x)-f(x_0)}
\le \abs{f(x)-f_N(x)}+\abs{f_N(x)-f_N(x_0)}+\abs{f_N(x_0)-f(x_0)}
<\varepsilon.
$$
So $f$ is continuous at $x_0$, and $x_0$ was arbitrary.

:::

:::

:::

:::
