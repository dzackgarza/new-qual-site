---
schema: qual/card@1
id: E-22IOS
kind: problem
title: Metric spaces are Hausdorff
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Hausdorff Spaces
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that every metric space is Hausdorff in its metric topology.
:::

::: {.solution}

Let $x\ne y$ be points of a metric space $(X,d)$, and set $r=d(x,y)/2>0$.

::: pf

::: pf-step

The open balls $B(x,r)$ and $B(y,r)$ are disjoint open neighborhoods of $x$ and $y$, so $X$ is Hausdorff.

::: pf-proof

Open balls are open in the metric topology. If $z\in B(x,r)\cap B(y,r)$, then the triangle inequality gives
$$
d(x,y)\le d(x,z)+d(z,y)<r+r=d(x,y),
$$
a contradiction.

:::

:::

:::

:::
