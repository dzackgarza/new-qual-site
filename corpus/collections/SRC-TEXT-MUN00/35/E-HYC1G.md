---
schema: qual/card@1
id: E-HYC1G
kind: exercise
title: Topology coherent with an increasing sequence of closed subspaces
subtitle: Munkres §35.9
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
relations: []
review: draft
---

::: {.exercise}

Let $X_1 \subset X_2 \subset \cdots$ be a sequence of spaces, where $X_i$ is a closed subspace of $X_{i+1}$ for each $i$.
Let $X$ be the union of the $X_i$; let us topologize $X$ by declaring a set $U$ to be open in $X$ if $U \cap X_i$ is open in $X_i$ for each $i$.

(a) Show that this is a topology on $X$ and that each space $X_i$ is a subspace (in fact, a closed subspace) of $X$ in this topology.
This topology is called the topology coherent with the subspaces $X_i$.

(b) Show that $f: X \to Y$ is continuous if $f \mid X_i$ is continuous for each $i$.

(c) Show that if each space $X_i$ is normal, then $X$ is normal.
[Hint: Given disjoint closed sets $A$ and $B$ in $X$, set $f$ equal to 0 on $A$ and 1 on $B$, and extend $f$ successively to $A \cup B \cup X_i$ for $i = 1, 2, \ldots$.]
:::
