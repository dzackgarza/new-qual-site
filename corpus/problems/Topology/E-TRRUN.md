---
schema: qual/card@1
id: E-TRRUN
kind: problem
title: A compact Hausdorff space is metrizable iff it is second-countable
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
  by: gemini-3.7-flash
  date: 2026-08-30
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source reads "is is metrizable"; the repeated word is removed.
---

::: {.exercise}
Show that a compact Hausdorff space is metrizable iff it is second-countable.
:::

::: {.solution}

Let $X$ be a compact Hausdorff space.

::: pf

::: pf-step

If $X$ is metrizable, then $X$ is second-countable.

::: pf-proof

A compact metric space is totally bounded, so for each $n$ finitely many balls of radius $1/n$ cover it; their centers over all $n$ form a countable dense set. A separable metric space is second-countable: the balls of rational radius about the points of a countable dense set form a countable basis.

:::

:::

::: pf-step

If $X$ is second-countable, then $X$ is metrizable.

::: pf-proof

A compact Hausdorff space is normal, hence regular. By the Urysohn metrization theorem, a second-countable regular Hausdorff space is metrizable.

:::

:::

:::

:::
