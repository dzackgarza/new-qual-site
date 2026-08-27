---
schema: qual/card@1
id: D-UHTGH
kind: definition
title: Closure of a set
classification:
  areas:
  - topology
  topics:
  - Closure
  - Point-Set Topology
relations: []
review: draft
---

::: {.definition}
For $U \subseteq X$, the closure of $U$ in $X$ is given by $\Cl_X(U) = \intersect_{\substack{ B\supseteq U \\ \text{ closed} }} B$, the intersection of all closed sets in $X$ containing $U$.
For $Y\subseteq X$ a subspace containing $U$, the closure of $U$ in $Y$ is $\Cl_Y(U) = \Cl_X(U) \intersect Y$.[^closure_relative_theorem-qrs] In general, we write $\bar{U} \da \cl_X(U)$.

An equivalent condition: $x\in \bar{U} \iff$ every neighborhood of $x$ intersects $U$.[^munkres_pt_in_closure-qrs] This is theorem 17.4 in Munkres Munkres 17.5
:::

[^closure_relative_theorem-qrs]:

[^munkres_pt_in_closure-qrs]:
