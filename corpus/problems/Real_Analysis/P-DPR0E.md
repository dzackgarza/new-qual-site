---
schema: qual/card@1
id: P-DPR0E
kind: problem
title: 'Lipschitz functions are absolutely continuous, and an absolutely continuous $f$ is Lipschitz iff $f''\in L^\infty$'
classification:
  areas:
  - real-analysis
  topics:
  - Absolute Continuity
  - L∞
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
  note: 'Split from P-4FH62, where it was part (l).'
---

::: {.problem}
A real-valued function $f$ on an interval $I$ for which there exists a constant $C$ such that
$$
\abs{f(x) - f(y)} \leq C\abs{x - y}
$$
for all $x$ and $y$ in $I$ is called a *Lipschitz function*.

1. Show that a Lipschitz function is absolutely continuous.

2. Show that an absolutely continuous function $f$ on an interval is Lipschitz if and only if $f'$ is essentially bounded.
:::

::: {.solution}

::: pf

::: pf-step

A Lipschitz function on an interval is absolutely continuous, and an absolutely continuous $f$ is Lipschitz if and only if $f'\in L^\infty$.

::: pf-proof

If $\abs{f(x)-f(y)}\le C\abs{x-y}$, then for pairwise disjoint intervals $(a_j,b_j)$,
$$
\sum_j\abs{f(b_j)-f(a_j)}\le C\sum_j(b_j-a_j),
$$
so $f$ is absolutely continuous. If $f$ is absolutely continuous, then $f(y)-f(x)=\int_x^y f'(t)\,dt$, so $f'\in L^\infty$ implies $\abs{f(y)-f(x)}\le\norm{f'}_\infty\abs{y-x}$. Conversely, at each point where a Lipschitz $f$ is differentiable, $\abs{f'}$ is at most the Lipschitz constant, and $f$ is differentiable a.e.

:::

:::

:::

:::
