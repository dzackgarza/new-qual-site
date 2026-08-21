---
schema: qual/card@1
id: E-2BCY2
kind: exercise
title: Intersections of nested families of closed connected sets are connected
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Connectedness
relations: []
review: draft
solved: false
---

::: {.exercise title="Munkres §26.11"}

Theorem.
Let $X$ be a compact Hausdorff space.
Let $\mathcal{A}$ be a collection of closed connected subsets of $X$ that is simply ordered by proper inclusion.
Then

$$
Y = \bigcap_{A \in \mathcal{A}} A
$$

is connected.
[Hint: If $C \cup D$ is a separation of $Y$, choose disjoint open sets $U$ and $V$ of $X$ containing $C$ and $D$, respectively, and show that

$$
\bigcap_{A \in \mathcal{A}} (A - (U \cup V))
$$

is not empty.]
:::
