---
schema: qual/card@1
id: C-ILVEB
kind: corollary
title: Every subgroup of a free group is free
slogan: 'Subgroups of free groups are free.'
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - Groups
  - Cell Complexes
relations: []
review: draft
---

::: {.corollary title="Nielsen--Schreier"}
Let $F$ be a free group and let $H \leq F$ be a subgroup.
Then $H$ is free.
:::

::: {.concept}
Realize $F$ as the fundamental group of a wedge of circles $X$.
The subgroup $H$ is the fundamental group of the connected covering space of $X$ that corresponds to $H$.
A covering space of a graph is a graph, and a connected graph is homotopy equivalent to a wedge of circles, so $H$ is free [@Hat02].
:::
