---
schema: qual/card@1
id: E-X36KD
kind: exercise
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

::: exercise
Show that a continuous map from a compact space to a Hausdorff space is closed.
:::

::: {.solution}
<1>1. Let $f : X \to Y$ be continuous, with $X$ compact and $Y$ Hausdorff, and let $C \subseteq X$ be closed.
::: {.proof}
setup.
:::

<1>2. $C$ is compact (a closed subset of a compact space is compact).
::: {.proof}
<1>1.
:::

<1>3. $f(C)$ is compact (the continuous image of a compact set is compact).
::: {.proof}
<1>2 and continuity.
:::

<1>4. $f(C)$ is closed (a compact subset of a Hausdorff space is closed).
::: {.proof}
<1>3 and $Y$ Hausdorff.
:::

<1>5. Hence $f$ maps closed sets to closed sets, so $f$ is a closed map.
::: {.proof}
<1>1 and <1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
