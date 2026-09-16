---
schema: qual/card@1
id: D-O5NN7
kind: definition
title: Orbit space
classification:
  areas:
  - topology
  topics:
  - Group Actions
  - Quotient Spaces
relations: []
review: draft
---

::: {.definition}
Let $G$ be a group [[D-3T6O2|acting]] on a topological space $X$.
For $x,y\in X$ write $x\sim y$ if there exists $g\in G$ with $g\cdot x=y$; this is an equivalence relation whose classes are the orbits of the action.
The \dfn{orbit space} is the set $X/G\coloneqq X/{\sim}$ of orbits with the quotient topology: $U\subseteq X/G$ is open if and only if $q\inv(U)$ is open in $X$, where $q\colon X\to X/G$ sends $x$ to its orbit.
:::
