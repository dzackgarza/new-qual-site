---
schema: qual/card@1
id: P-PSTM-02
kind: problem
title: Hausdorff spaces and the closed diagonal criterion
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let X be a space.
Show that X is Hausdorff if, and only if, the diagonal $\Delta : =$ $\{ ( x , x ) \mid x \in X \}$ is a closed subspace of $X \times X$.
:::

::: {.solution}
Suppose $X$ is a Hausdorff space.
We show that the complement of the diagonal, $\Delta^{c} \coloneqq X \times X \setminus \Delta$, is open.
Let $(x, y) \in \Delta^{c}$. Then $x \neq y$, and so there are disjoint open sets $U$ and $V$ containing $x$ and $y$, respectively.
By definition of the product topology, $U \times V$ is an open subset of $X \times X$, and $U \times V \subset \Delta^{c}$, since a point $(z,z) \in U \times V$ would lie in $U \cap V = \emptyset$. This shows that $\Delta^{c}$ is open.

Conversely, suppose $\Delta$ is closed, that is to say, $\Delta^{c}$ is open.
Let $x$ and $y$ be two distinct elements of $X$. Then $(x, y) \in \Delta^{c}$, and so there is a basic open set $U \times V \subset \Delta^{c}$ containing $(x, y)$. Then $U$ and $V$ are open, disjoint subsets of $X$ containing $x$ and $y$, respectively.
This shows that $X$ is Hausdorff.
:::
