---
schema: qual/card@1
id: E-Q7TSH
kind: problem
title: Every countable discrete space is separable
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
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
Show that any countable space with the discrete topology is separable.
:::

::: {.solution}

Let $X$ be a countable set with the discrete topology. Recall that $X$ is separable when it has a countable dense subset.

::: pf

::: {.pf-step #dense}

$X$ is dense in $X$.

::: pf-proof

The closure of the whole space is the whole space, since $X$ is closed in itself.

:::

:::

::: pf-step

$X$ is separable.

::: pf-proof

The subset $D = X$ is countable by hypothesis and dense by step [](#dense){.pf-ref}.

:::

:::

:::

:::
