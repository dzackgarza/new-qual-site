---
schema: qual/card@1
id: E-JN4QP
kind: exercise
title: Continuous bijections from compact spaces to Hausdorff spaces are homeomorphisms
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Homeomorphisms
relations: []
review: draft
solved: true
---

Show that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism.

::: {.solution}
\envlist

- It suffices to show that $f$ is a closed map, i.e. if $U\subseteq X$ is closed then $f(U)\subseteq Y$ is again closed.

- Let $U\in X$ be closed; since $X$ is closed, $U$ is compact

  - Since closed subsets of compact spaces are compact.

- Since $f$ is continuous, $f(U)$ is compact

  - Since the continuous image of a compact set is compact.

- Since $Y$ is Hausdorff and $f(U)$ is compact, $f(U)$ is closed

  - Since compact subsets of Hausdorff spaces are closed.
:::
