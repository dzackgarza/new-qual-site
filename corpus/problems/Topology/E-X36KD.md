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

::: pf

::: {.pf-step #s1}

Let $f : X \to Y$ be continuous, with $X$ compact and $Y$ Hausdorff, and let $C \subseteq X$ be closed.

::: pf-proof

setup.

:::

:::

::: {.pf-step #s2}

$C$ is compact (a closed subset of a compact space is compact).

::: pf-proof

Step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

$f(C)$ is compact (the continuous image of a compact set is compact).

::: pf-proof

Step [](#s2){.pf-ref} and continuity.

:::

:::

::: {.pf-step #s4}

$f(C)$ is closed (a compact subset of a Hausdorff space is closed).

::: pf-proof

Step [](#s3){.pf-ref} and $Y$ Hausdorff.

:::

:::

::: {.pf-step #s5}

Hence $f$ maps closed sets to closed sets, so $f$ is a closed map.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref}.

:::

:::

:::
