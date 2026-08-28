---
schema: qual/card@1
id: E-20CHL
kind: exercise
title: Continuity implies separate continuity
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Product Topology
relations: []
review: draft
---

::: {.exercise}

Let $F: X \times Y \to Z$.
We say that $F$ is continuous in each variable separately if for each $y_0$ in $Y$, the map $h: X \to Z$ defined by $h(x) = F(x \times y_0)$ is continuous, and for each $x_0$ in $X$, the map $k: Y \to Z$ defined by $k(y) = F(x_0 \times y)$ is continuous.
Show that if $F$ is continuous, then $F$ is continuous in each variable separately.
:::
