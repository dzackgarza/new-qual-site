---
schema: qual/card@1
id: E-HQ8N3
kind: problem
title: Fundamental group of the wedge of a circle and a sphere
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

What can you say about the fundamental group of $X \vee Y$ if $X$ is homeomorphic to $S^1$ and $Y$ is homeomorphic to $S^2$?
:::

::: {.solution}
::: pf

::: pf-step
Well-pointed basepoints and fundamental groups of the summands:

::: pf-proof

::: pf-step
The circle $S^1$ and the 2-sphere $S^2$ are CW complexes, so any choice of basepoints $x_0 \in S^1$ and $y_0 \in S^2$ yields a well-pointed pair (the basepoints have contractible open neighborhoods in $S^1$ and $S^2$, respectively).
:::

::: pf-step
The fundamental groups of the individual spaces are:
\[
\pi_1(S^1, x_0) \cong \mathbb{Z}, \qquad \pi_1(S^2, y_0) \cong \{0\}.
\]
:::

:::

:::

::: pf-step
Application of the Seifert–van Kampen Theorem:

::: pf-proof

::: pf-step
By the Seifert–van Kampen Theorem for wedge sums of well-pointed spaces:
\[
\pi_1(S^1 \vee S^2, p) \cong \pi_1(S^1, x_0) * \pi_1(S^2, y_0).
\]
:::

::: pf-step
Substituting the fundamental groups of $S^1$ and $S^2$:
\[
\pi_1(S^1 \vee S^2, p) \cong \mathbb{Z} * \{0\} \cong \mathbb{Z}.
\]
:::

:::

:::

::: pf-step
Conclusion:
The fundamental group of $S^1 \vee S^2$ is isomorphic to $\mathbb{Z}$.
:::

:::
