---
schema: qual/card@1
id: FD-COPFN
kind: definition
title: Deformation retract
prompts:
- What map exhibits $A \subset X$ as a deformation retract of $X$?
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Homotopy
relations:
- kind: variant-of
  target: FD-BDEI2
review: draft
---

::: {.definition}
Let $X$ be a topological space, $A \subseteq X$ a subspace, and $I = [0,1]$.
The subspace $A$ is a \dfn{deformation retract} of $X$ if there exists a continuous map $F\colon X\cross I\to X$ with $F(x, 0) = x$ and $F(x, 1)\in A$ for all $x\in X$, and $F(a, 1) = a$ for all $a\in A$.
:::

::: {.remark}
Equivalently, there is a [[D-NCLVD|retraction]] $r\colon X\to A$ such that $\iota\circ r$ is [[D-Z7I7F|homotopic]] to $\id_X$, where $\iota\colon A\injects X$ is the inclusion.
:::
