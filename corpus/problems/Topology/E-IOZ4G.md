---
schema: qual/card@1
id: E-IOZ4G
kind: problem
title: Every indiscrete space is separable
classification:
  areas:
  - topology
  topics:
  - Countability
  - Density
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that any topological space $X$ equipped with the indiscrete (trivial) topology is separable.
:::

::: {.solution}

::: pf

::: pf-step

If $X=\varnothing$, then $X$ is separable.

::: pf-proof

The empty set is a countable dense subset of itself.

:::

:::

::: {.pf-step #dense}

If $X\ne\varnothing$, every nonempty subset of $X$ is dense.

::: pf-proof

In the indiscrete topology the only nonempty open set is $X$, and every nonempty subset meets $X$.

:::

:::

::: pf-step

If $X\ne\varnothing$, then $X$ is separable.

::: pf-proof

Choose $x\in X$. By step [](#dense){.pf-ref}, the finite set $\{x\}$ is dense.

:::

:::

:::

:::
