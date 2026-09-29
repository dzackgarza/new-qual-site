---
schema: qual/card@1
id: E-FMCFR
kind: problem
title: Continuous maps from compact spaces to Hausdorff spaces are closed
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Continuity
relations: []
review: draft
---

::: {.exercise}
Show that a continuous map from a compact space to a Hausdorff space is closed.

#### Exercise
:::

::: {.solution}

::: pf

::: pf-step

Let $f:X\to Y$ be continuous, with $X$ compact and $Y$ Hausdorff, and let $F\subseteq X$ be closed.

::: pf-proof

To show that $f$ is closed, it suffices to prove that $f(F)$ is closed for every closed $F$.

:::

:::

::: pf-step

The subset $F$ is compact.

::: pf-proof

A closed subset of a compact space is compact.

:::

:::

::: pf-step

The image $f(F)$ is compact.

::: pf-proof

Continuous images of compact spaces are compact.

:::

:::

::: {.pf-step #s4}

Since $Y$ is Hausdorff, $f(F)$ is closed in $Y$.

::: pf-proof

Compact subsets of Hausdorff spaces are closed.

:::

:::

::: pf-step

Therefore $f$ is a closed map.

::: pf-proof

Apply step [](#s4){.pf-ref} to every closed subset $F\subseteq X$.

:::

:::

:::

:::
