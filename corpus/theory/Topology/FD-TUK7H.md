---
schema: qual/card@1
id: FD-TUK7H
kind: definition
title: Neighborhood basis
prompts:
- What collection of open sets forms a neighborhood basis at $x$?
classification:
  areas:
  - topology
  topics:
  - Bases
  - Countability
  - Point-Set Topology
relations:
- kind: variant-of
  target: FD-QCNG5
review: draft
---

::: {.definition}
Let $X$ be a topological space and $x\in X$.
A \dfn{neighborhood basis} at $x$ is a collection $\ts{B_j}_{j\in J}$ of open subsets of $X$ containing $x$ such that for every [[D-JMRPA|neighborhood]] $U_x$ of $x$ there exists $j\in J$ with $B_j \subseteq U_x$.
:::
