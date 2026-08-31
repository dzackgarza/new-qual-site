---
schema: qual/card@1
id: E-HQ8N3
kind: exercise
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
<1>1. Well-pointed basepoints and fundamental groups of the summands:
<2>1. The circle $S^1$ and the 2-sphere $S^2$ are CW complexes, so any choice of basepoints $x_0 \in S^1$ and $y_0 \in S^2$ yields a well-pointed pair (the basepoints have contractible open neighborhoods in $S^1$ and $S^2$, respectively).
<2>2. The fundamental groups of the individual spaces are:
\[
\pi_1(S^1, x_0) \cong \mathbb{Z}, \qquad \pi_1(S^2, y_0) \cong \{0\}.
\]

<1>2. Application of the Seifert–van Kampen Theorem:
<2>1. By the Seifert–van Kampen Theorem for wedge sums of well-pointed spaces:
\[
\pi_1(S^1 \vee S^2, p) \cong \pi_1(S^1, x_0) * \pi_1(S^2, y_0).
\]
<2>2. Substituting the fundamental groups of $S^1$ and $S^2$:
\[
\pi_1(S^1 \vee S^2, p) \cong \mathbb{Z} * \{0\} \cong \mathbb{Z}.
\]

<1>3. Conclusion:
The fundamental group of $S^1 \vee S^2$ is isomorphic to $\mathbb{Z}$. Q.E.D.
:::
