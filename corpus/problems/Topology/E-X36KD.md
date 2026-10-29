---
schema: qual/card@1
id: E-X36KD
kind: problem
title: A continuous map from a compact space to a Hausdorff space is closed
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}
Show that a continuous map from a compact space to a Hausdorff space is closed.
:::

::: {.solution}

Let $f : X \to Y$ be continuous, with $X$ compact and $Y$ Hausdorff, and let $C \subseteq X$ be closed.

::: pf

::: {.pf-step #c-compact}

$C$ is compact.

::: pf-proof

A closed subset of a compact space is compact.

:::

:::

::: {.pf-step #image-compact}

$f(C)$ is compact.

::: pf-proof

The continuous image of a compact set is compact, and $C$ is compact by step [](#c-compact){.pf-ref}.

:::

:::

::: pf-step

$f(C)$ is closed in $Y$, so $f$ is a closed map.

::: pf-proof

A compact subset of a Hausdorff space is closed; apply this to step [](#image-compact){.pf-ref}.

:::

:::

:::

:::
