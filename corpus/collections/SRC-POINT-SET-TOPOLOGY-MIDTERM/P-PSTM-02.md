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
Suppose X is a Hausdorff space.
We need to show that the complement of the diagonal, $\Delta ^ { \mathrm { { c } } } : = X \times X \setminus \Delta$ , is open.
So let $( x , y ) \in \Delta ^ { \mathrm { c } }$ . Then $x \neq y ,$ and so there are disjoint open sets U and $V$ , containing x and y, respectively.
By definition of the product topology, $U \times V$ is an open subset of $X \times X$ , and clearly $U \times V \subset \Delta ^ { \mathrm { { c } } }$ (for otherwise $U \cap V \neq \emptyset )$ . This shows that $\Delta ^ { \mathrm { c } }$ is open.

Conversely, suppose $\Delta$ is closed, that is to say, $\Delta ^ { \mathrm { c } }$ is open.
Let x and y be two distinct elements of X. Then $( x , y ) \in \Delta ^ { \mathrm { c } }$ , and so there is a basis open set $U \times V \subset \Delta ^ { \mathrm { { c } } }$ containing $( x , y )$ . Now note that U and V are open, disjoint subsets of X, containing x and y, respectively.
This shows that X is Hausdorff.
:::
