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

::: exercise
Show that a continuous map from a compact space to a Hausdorff space is closed.

#### Exercise
:::

::: {.solution}
<1>1. Let $f:X\to Y$ be continuous, with $X$ compact and $Y$ Hausdorff, and let $F\subseteq X$ be closed.
::: {.proof}
To show that $f$ is closed, it suffices to prove that $f(F)$ is closed for every closed $F$.
:::

<1>2. The subset $F$ is compact.
::: {.proof}
A closed subset of a compact space is compact.
:::

<1>3. The image $f(F)$ is compact.
::: {.proof}
Continuous images of compact spaces are compact.
:::

<1>4. Since $Y$ is Hausdorff, $f(F)$ is closed in $Y$.
::: {.proof}
Compact subsets of Hausdorff spaces are closed.
:::

<1>5. Therefore $f$ is a closed map.
::: {.proof}
Apply <1>4 to every closed subset $F\subseteq X$.
:::
:::
