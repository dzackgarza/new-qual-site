---
schema: qual/card@1
id: E-P3RLK
kind: problem
title: Closed subsets of compact spaces are compact
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

Let $A\subset X$ with $A$ closed and $X$ compact, and show that $A$ is compact.

::: {.solution}
\envlist

- Let $A$ be a compact subset of $X$ a Hausdorff space, we will show $X\setminus A$ is open

- Fix $x\in X\setminus A$.

- Since $X$ is Hausdorff, for every $y\in A$ we can find $U_y \ni y$ and $V_x(y) \ni x$ depending on $y$ such that $U_x(y) \intersect U_y = \emptyset$.

- Then $\theset{U_y \suchthat y\in A} \covers A$, and by compactness of $A$ there is a finite subcover corresponding to a finite collection $\theset{y_1, \cdots, y_n}$.

- Set $U = \union U_{y_i}$ and $V = \intersect V_x(y_i)$;

  - We have $A\subset U$: each $y \in A$ lies in some $U_{y_i}$ (the $U_{y_i}$ cover $A$), so $y \in \bigcup_i U_{y_i} = U$.
  - We have $x\in V$: $x \in V_x(y_i)$ for every $i$ by construction, so $x \in \bigcap_i V_x(y_i) = V$.
  - We have $U\intersect V = \emptyset$: if $z \in U \cap V$, then $z \in U_{y_i}$ for some $i$ and $z \in V_x(y_i)$ for that same $i$, contradicting $U_{y_i} \cap V_x(y_i) = \emptyset$.

- Done: for every $x\in X\setminus A$, we have found an open set $V\ni x$ such that $V\intersect A = \emptyset$, so $x$ is an interior point and a set is open iff every point is an interior point.

![](../../assets/Topology/figures/image_2020-06-11-20-14-26.png)

![](../../assets/Topology/figures/image_2020-06-11-20-35-11.png)
:::
