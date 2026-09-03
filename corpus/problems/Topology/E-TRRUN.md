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
---

::: exercise
Show that a compact Hausdorff space is is metrizable iff it is second-countable.
:::

::: {.solution}
<1>1. ($\Rightarrow$) If $X$ is compact and metrizable, then $X$ is second-countable.
::: {.proof}
a compact metric space is separable (totally bounded), and a separable metric space is second-countable.
:::

<1>2. ($\Leftarrow$) Suppose $X$ is compact Hausdorff and second-countable.
::: {.proof}
assume the hypotheses.
:::

<1>3. A second-countable compact Hausdorff space is regular (compact Hausdorff implies normal, hence regular).
::: {.proof}
compact Hausdorff spaces are normal.
:::

<1>4. By the Urysohn metrization theorem, a second-countable regular space is metrizable.
::: {.proof}
Urysohn metrization theorem.
:::

<1>5. Hence $X$ is metrizable.
::: {.proof}
<1>3 and <1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>1 and <1>5.
:::
:::
