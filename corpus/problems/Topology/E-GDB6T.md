---
schema: qual/card@1
id: E-GDB6T
kind: exercise
title: Compact Hausdorff spaces are metrizable if and only if second-countable
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
  - Countability
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: exercise
Show that a compact Hausdorff space is is metrizable iff it is second-countable.

#### Exercise
:::

::: solution
**Goal:** Use standard metrization theorems in each direction.

<1> If $X$ is compact and metrizable, then it has a countable base.
    Choose a dense sequence $\{x_n\}$ and radii $q\in\mathbb Q_{>0}$.
    The balls $B(x_n,q)$ form a countable base, so $X$ is second-countable.

<1> If $X$ is compact Hausdorff and second-countable, then $X$ is regular and second-countable.
    The Urysohn metrization theorem gives a metric inducing the topology on $X$.

Authored by **Codex 5.3 Spark Extra High**.
:::
