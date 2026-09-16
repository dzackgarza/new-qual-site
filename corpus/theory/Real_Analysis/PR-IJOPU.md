---
schema: qual/card@1
id: PR-IJOPU
kind: proposition
title: Reverse triangle inequality
classification:
  areas:
  - real-analysis
  topics:
  - Norms
relations: []
review: draft
---

::: {.proposition}
Let $(V,\norm{\cdot})$ be a normed vector space.
For all $x,y\in V$,
$$
\abs{\norm{x} - \norm{y}} \leq \norm{x - y} .
$$
:::

::: {.proof}
By the triangle inequality, $\norm{x}\leq\norm{x-y}+\norm{y}$ and $\norm{y}\leq\norm{y-x}+\norm{x}$, and $\norm{y-x}=\norm{x-y}$.
:::
