---
schema: qual/card@1
id: E-8Q9TN
kind: exercise
title: Star-fine refinements of open coverings
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
solved: false
---

::: {.exercise title="Munkres §82 Supplementary"}


Let $X$ be a space; let $\mathcal{A}$ be an open covering of $X$. Under what conditions does there exist an open covering $\mathcal{B}$ of $X$ refining $\mathcal{A}$ such that for each pair $B, B'$ of elements of $\mathcal{B}$ that have nonempty intersection, the union $B \cup B'$ lies in an element of $\mathcal{A}$?

(a) Show that such a covering $\mathcal{B}$ exists if $X$ is metrizable. [Hint: Choose $\epsilon(x)$ so that $B(x, 3\epsilon(x))$ lies in an element of $\mathcal{A}$. Let $\mathcal{B}$ consist of the open sets $B(x, \epsilon(x))$.]

(b) Show that such a covering exists if $X$ is compact Hausdorff. [Hint: Let $A_1, \ldots, A_n$ be a finite subcollection of $\mathcal{A}$ that covers $X$. Choose an open covering $C_1, \ldots, C_n$ of $X$ such that $\overline{C}_i \subset A_i$ for each $i$. For each nonempty subset $J$ of $\ts{1, \ldots, n}$, consider the set

$$
B_J = \bigcap_{j \in J} A_j - \bigcup_{j \notin J} \overline{C}_j.]
$$
:::
