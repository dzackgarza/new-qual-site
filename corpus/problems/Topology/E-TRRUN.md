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

::: {.exercise}
Show that a compact Hausdorff space is is metrizable iff it is second-countable.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

($\Rightarrow$) If $X$ is compact and metrizable, then $X$ is second-countable.

::: pf-proof

a compact metric space is separable (totally bounded), and a separable metric space is second-countable.

:::

:::

::: pf-step

($\Leftarrow$) Suppose $X$ is compact Hausdorff and second-countable.

::: pf-proof

assume the hypotheses.

:::

:::

::: {.pf-step #s3}

A second-countable compact Hausdorff space is regular (compact Hausdorff implies normal, hence regular).

::: pf-proof

compact Hausdorff spaces are normal.

:::

:::

::: {.pf-step #s4}

By the Urysohn metrization theorem, a second-countable regular space is metrizable.

::: pf-proof

Urysohn metrization theorem.

:::

:::

::: {.pf-step #s5}

Hence $X$ is metrizable.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

:::
