---
schema: qual/card@1
id: P-PSTM-04
kind: problem
title: Separating a compact set from an exterior point
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let X be a Hausdorff space.
Suppose A is a compact subspace, and $x \in X \setminus A$ Show that there exist disjoint open sets U and V containing A and x, respectively.
:::

::: {.solution}
Let $y \in A$. Since $x \in X \setminus A$, we have $y \neq x$. Since $X$ is Hausdorff, there are open, disjoint sets $U_y$ and $V_y$ containing $y$ and $x$, respectively.

The family $\{U_y\}_{y \in A}$ is an open cover of $A$. Since $A$ is compact, this cover admits a finite subcover $U_{y_1}, \ldots, U_{y_n}$. Define

$$
U \coloneqq \bigcup_{i=1}^{n} U_{y_i} \quad \text{and} \quad V \coloneqq \bigcap_{i=1}^{n} V_{y_i}.
$$

Then $U$ is open and contains $A$, and $V$ is a finite intersection of open sets containing $x$. They are disjoint, since $U_{y_i} \cap V \subseteq U_{y_i} \cap V_{y_i} = \emptyset$ for each $i$.
:::
