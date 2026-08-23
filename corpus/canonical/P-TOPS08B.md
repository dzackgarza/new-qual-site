---
schema: qual/card@1
id: P-TOPS08B
kind: problem
title: "Homology of a space as the colimit of homology of its compact subsets"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Colimits
  - Compactness
relations: []
review: draft
solved: false
---

::: problem
Given a topological space $X$, let $I$ denote the directed set of compact subsets of $X$ under inclusion. Show that the following canonical map is an isomorphism:
$$
\operatorname{colim}_{K \in I} H_i(K; R) \longrightarrow H_i(X; R),
$$
for any ring $R$.
:::