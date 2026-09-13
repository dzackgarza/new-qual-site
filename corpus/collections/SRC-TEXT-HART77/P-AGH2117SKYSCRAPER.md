---
schema: qual/card@1
id: P-AGH2117SKYSCRAPER
kind: problem
title: Skyscraper sheaves as pushforwards from the closure of a point
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Skyscraper Sheaves
  - Direct Image
relations: []
review: draft
---

::: problem
Let $X$ be a topological space, let $P$ be a point, and let $A$ be an abelian group.
Define a sheaf $i_P(A)$ on $X$ by $i_P(A)(U) = A$ if $P \in U$ and $0$ otherwise.

Verify that the stalk of $i_P(A)$ is $A$ at every point $Q \in \cl\qty{\ts{P}}$ and $0$ elsewhere, where $\cl\qty{\ts{P}}$ denotes the closure of the set consisting of the point $P$.
Hence the name "skyscraper sheaf".

Show that this sheaf can also be described as $i_*(A)$, where $A$ denotes the constant sheaf $A$ on the closed subspace $\cl\qty{\ts{P}}$ and $i: \cl\qty{\ts{P}} \to X$ is the inclusion.
:::
