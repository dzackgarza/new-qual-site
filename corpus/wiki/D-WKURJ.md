---
schema: qual/card@1
id: D-WKURJ
kind: definition
title: "Basis for a topology"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
:::{.definition title="Basis for a topology"}
A set $\mathcal{B}$ is a **basis** for a topology iff

- $\mathcal{B}$ is closed under intersections,
- Every $x\in X$ is in some basic set,
- If $x$ is in the intersection of two basis sets $B_1 \intersect B_2$, there is a third basic open $B_3 \ni x$ with $B_3 \subset B_1 \intersect B_2$.

The topology **generated** by \( \mathcal{B}  \) is the following: $U\subseteq X$ is open iff for each $x\in U$ there is a basic open $B$ with $x\in B \subset U$.
Equivalently, every open set is a union of basic open sets.
:::
