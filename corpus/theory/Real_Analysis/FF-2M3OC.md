---
schema: qual/card@1
id: FF-2M3OC
kind: fact
title: Reverse triangle inequality
prompts:
- State the reverse triangle inequality.
classification:
  areas:
  - real-analysis
  topics:
  - Norms
relations: []
review: draft
---

::: {.fact}
Let $(V,\norm{\cdot})$ be a normed vector space.
For all $x, y\in V$,
$$
\abs{\norm{x} - \norm{y}} \leq \norm{x-y}.
$$
:::

::: {.proof}
By the triangle inequality, $\norm{x}\leq\norm{x-y}+\norm{y}$ and $\norm{y}\leq\norm{y-x}+\norm{x}$, and $\norm{y-x} = \norm{x-y}$.
Hence $\norm{x}-\norm{y}\leq\norm{x-y}$ and $\norm{y}-\norm{x}\leq\norm{x-y}$.
:::
