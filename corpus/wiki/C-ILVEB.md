---
schema: qual/card@1
id: C-ILVEB
kind: corollary
title: "Every subgroup of a free group is free"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

::: {.corollary title="Every subgroup of a free group is free"}
Idea for a particular case: use the fact that $\pi_1\qty{\bigvee^k S^1} = \ZZ^{\ast k}$, so if $G \leq \ZZ^{\ast k}$ then there is a covering space $X \surjects \bigvee^k S^1$ such that $\pi_1(X) = G$.
Since $X$ can be explicitly constructed as a graph, i.e. a CW complex with only a 1-skeleton, $\pi_1(X)$ is free on the edges in the complement of a maximal tree.
:::
