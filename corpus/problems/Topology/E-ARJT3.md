---
schema: qual/card@1
id: E-ARJT3
kind: problem
title: Separable space
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
- What is a **separable** space?
:::

::: {.solution}
A topological space $X$ is separable if it has a countable subset $D$ that is dense, $\overline{D} = X$.

::: pf

::: pf-step

$X$ is separable if and only if some countable $D \subseteq X$ meets every nonempty open subset of $X$.

::: pf-proof

A point $x$ lies in $\overline{D}$ exactly when every open neighborhood of $x$ meets $D$, so $\overline{D}=X$ exactly when every nonempty open set meets $D$.

:::

:::

:::

:::

::: {.remark}
Every second-countable space is separable: choose one point from each nonempty member of a countable basis. For metric spaces, separability, second countability, and the Lindelöf property are equivalent. The space $\RR^n$ is separable, with countable dense subset $\QQ^n$.
:::
