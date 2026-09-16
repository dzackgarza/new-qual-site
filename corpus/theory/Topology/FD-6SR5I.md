---
schema: qual/card@1
id: FD-6SR5I
kind: definition
title: Retract
prompts:
- What does it mean for a subspace $A \subset X$ to be a retract of $X$?
classification:
  areas:
  - topology
  topics:
  - Retracts
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, $A \subseteq X$ a subspace, and $\iota\colon A\injects X$ the inclusion.
The subspace $A$ is a \dfn{retract} of $X$ if there exists a [[D-AEAAD|continuous map]] $f\colon X\to A$ with $f\vert_{A} = \id_A$, that is, $f\circ\iota = \id_A$; such an $f$ is a left inverse of $\iota$.
:::
