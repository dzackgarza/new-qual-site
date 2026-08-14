---
schema: qual/card@1
id: D-2PNEG
kind: definition
title: "Free and Properly Discontinuous"
classification:
  areas:
  - topology
  topics:
  - group-actions
  - covering-spaces
relations: []
review: draft
---

::: {.definition title="Free and Properly Discontinuous"}
An action $G\actson X$ is **properly discontinuous** if each $x\in X$ has a neighborhood $U$ such that all of the images $g(U)$ for $g\in G$ are disjoint, i.e. $g_1(U) \intersect g_2(U) \neq \emptyset \implies g_1 = g_2$.
The action is **free** if there are no fixed points.

Sometimes a slightly weaker condition is used: every point $x\in X$ has a neighborhood $U$ such that $U \intersect G(U) \neq \emptyset$ for only finitely many $G$.
:::
