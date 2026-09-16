---
schema: qual/card@1
id: D-UH3L5
kind: definition
title: Deformation and deformation retraction
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Retracts
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space and $I=[0,1]$.
A \dfn{deformation} of $X$ is a family of maps $f_t\colon X\to X$, $t\in I$, such that $f_0=\id_X$ and $(x,t)\mapsto f_t(x)$ is a continuous map $X\times I\to X$.
For a subspace $A\subseteq X$, a \dfn{deformation retraction} of $X$ onto $A$ is a deformation $(f_t)_{t\in I}$ of $X$ with $f_1(X)=A$ and $f_t(a)=a$ for all $a\in A$ and $t\in I$ [@Hat02].
:::

::: {.proposition}
If $X$ deformation retracts onto $A$, then the inclusion $A\injects X$ is a [[D-HFR32|homotopy equivalence]] [@Hat02].
:::
