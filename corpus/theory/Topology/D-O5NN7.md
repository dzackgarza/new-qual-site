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
Let $X/G\coloneqq X/{\sim}$ be the set of orbits and $q\colon X\to X/G$ the map sending $x$ to its orbit.
The \dfn{orbit space} is $X/G$ with the quotient topology: $U\subseteq X/G$ is open if and only if $q\inv(U)$ is open in $X$, so that $q$ is a [[D-ITBUT|quotient map]].
:::
