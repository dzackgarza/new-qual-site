---
schema: qual/card@1
id: P-15UQB
kind: problem
title: '$\sum_n 1/(1+n^2x)$ is continuously differentiable on $(0,\infty)$ but not uniformly convergent there'
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-30
  note: 'Split from P-4FH62, where it was part (i).'
---

::: {.problem}
Let
$$
g(x) = \sum_{n=0}^\infty \frac{1}{1+n^2x}.
$$

1. Show that the series defining $g$ does not converge uniformly on $(0,\infty)$, but nonetheless still defines a continuous function on $(0,\infty)$.

2. Is $g$ differentiable on $(0,\infty)$? If so, is the derivative function $g'$ continuous on $(0,\infty)$?
:::

::: {.hint}
For part 1: if $\sum_{n=0}^\infty g_n(x)$ converges uniformly on a set $X$, then the sequence of functions $\theset{g_n}$ must converge uniformly to $0$ on $X$.
:::

::: {.solution}

::: pf

::: pf-step

The series for $g$ does not converge uniformly on $(0,\infty)$, $g$ is continuous on $(0,\infty)$, and $g$ is differentiable on $(0,\infty)$ with $g'$ continuous.

::: pf-proof

The term $n=0$ is the constant $1$. Uniform convergence on $(0,\infty)$ would force
$$
\sup_{x>0}\frac1{1+n^2x}\to0,
$$
but the supremum is $1$ for every $n$. On every $[a,\infty)$, $a>0$,
$$
\frac1{1+n^2x}\le\frac1{n^2a} \qquad (n \geq 1),
$$
so the series converges uniformly there and $g$ is continuous on $(0,\infty)$. The series of derivatives is
$$
-\sum_{n\ge1}\frac{n^2}{(1+n^2x)^2},
$$
and on $[a,\infty)$ its terms are bounded by $1/(n^2a^2)$, so it converges uniformly there. Hence $g$ is differentiable on $(0,\infty)$, $g'$ is this series, and $g'$ is continuous there.

:::

:::

:::

:::
