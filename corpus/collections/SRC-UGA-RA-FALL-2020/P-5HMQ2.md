---
schema: qual/card@1
id: P-5HMQ2
kind: problem
title: '$nx_n\to0$ for a decreasing summable sequence of positive numbers'
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Series of Numbers
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
  note: 'Split from P-4FH62, where it was part (q).'
---

::: {.problem}
Show that if $x_n$ is a decreasing sequence of positive real numbers such that $\sum_{n=1}^\infty x_n$ converges, then
$$
\lim_{n\to\infty} nx_n = 0.
$$
:::

::: {.solution}

::: pf

::: pf-step

A decreasing summable sequence of positive numbers satisfies $nx_n\to0$.

::: pf-proof

Since $(x_n)$ is decreasing,
$$
\sum_{k=\lfloor n/2\rfloor+1}^{n}x_k
\ge \bigl(n-\lfloor n/2\rfloor\bigr)x_n
\ge \frac n2x_n.
$$
The left side is a block of the tail of a convergent series of positive terms and therefore tends to $0$. Hence $nx_n\to0$.

:::

:::

:::

:::
