---
schema: qual/card@1
id: D-UH3L5
kind: definition
title: "Deformation"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

::: {.definition title="Deformation"}
A **deformation** of $X$ is a homotopy $f_t: X\to X$ starting at $f_0 = \id_X$, continuous as a map $X\cross I \to X$.
It is a **deformation retraction** onto a subspace $A\subseteq X$ iff additionally $f_1(X) = A$ and $\ro{f_t}{A} = \id_A$ for every $t$; in that case the inclusion $A\injects X$ is a homotopy equivalence.
:::

::: {.concept}
See Hatcher, p. 2.
:::
