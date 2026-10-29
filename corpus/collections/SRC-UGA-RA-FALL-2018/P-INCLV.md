---
schema: qual/card@1
id: P-INCLV
kind: problem
title: '$1/x$ is uniformly continuous on $(1,\infty)$ but not on $(0,\infty)$'
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
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
  note: 'Split from P-4FH62, where it was part (e).'
---

::: {.problem}
Let $f(x) = \frac{1}{x}$. Show that $f$ is uniformly continuous on $(1,\infty)$ but not on $(0,\infty)$.
:::

::: {.solution}

::: pf

::: pf-step

$1/x$ is uniformly continuous on $(1,\infty)$ but not on $(0,\infty)$.

::: pf-proof

On $(1,\infty)$,
$$
\abs{\frac1x-\frac1y}=\frac{\abs{x-y}}{xy}\le \abs{x-y},
$$
so $1/x$ is Lipschitz and therefore uniformly continuous. On $(0,\infty)$ take $x_n=1/n$ and $y_n=1/(n+1)$. Then $\abs{x_n-y_n}\to0$, but $\abs{1/x_n-1/y_n}=1$, so uniform continuity fails.

:::

:::

:::

:::
