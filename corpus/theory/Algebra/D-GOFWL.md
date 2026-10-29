---
schema: qual/card@1
id: D-GOFWL
kind: definition
title: Ideal
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Rings
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring.
An \dfn{ideal} $I\normal R$ is a subset $I\subseteq R$ such that $(I,+)$ is a subgroup of $(R,+)$ and
$$
ri\in I
\qquad\text{and}\qquad
ir\in I
\qquad
\text{for all } r\in R \text{ and } i\in I.
$$
Thus "ideal" means two-sided ideal when $R$ is not commutative.
:::

::: {.proposition}
Let $R$ be a ring.
A nonempty subset $I\subseteq R$ is an ideal if and only if
$$
I+I\subseteq I,
\qquad
RI\subseteq I,
\qquad
IR\subseteq I.
$$
:::
