---
schema: qual/card@1
id: P-KCN2B
kind: problem
title: $X$ is Hausdorff iff the diagonal is closed in $X\times X$
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Product Topology
relations: []
review: draft
---

:::{.problem title="?"}
Let $X$ be a topological space and let
$$
\Delta = \theset{(x, y) \in X \times X \mid x = y}
.$$

Show that $X$ is a Hausdorff space if and only if $\Delta$ is closed in $X \times X$.

:::

:::{.solution}
\envlist

$\implies$:

- Let $p\in X^2\setminus \Delta$.
- Then $p$ is of the form $(x, y)$ where $x\neq y$ and $x,y\in X$.
- Since $X$ is Hausdorff, pick $N_x, N_y$ in $X$ such that $N_x \intersect N_y = \emptyset$.
- Then $N_p\definedas N_x \cross N_y$ is an open set in $X^2$ containing $p$.
- Claim: $N_p \intersect \Delta = \emptyset$.
  - If $q \in N_p \intersect \Delta$, then $q = (z, z)$ where $z\in X$, and $q\in N_p \implies q\in N_x \intersect N_y = \emptyset$.
- Then $X^2\setminus \Delta = \union_p N_p$ is open.
 
$\impliedby$:

- Let $x\neq y\in X$.
- Consider $(x, y) \in \Delta^c \subset X^2$, which is open.
- Thus $(x, y) \in B$ for some box in the product topology.
- $B = U \cross V$ where $U\ni x, V\ni y$ are open in $X$, and $B \subset X^2\setminus \Delta$.
- Claim: $U\intersect V = \emptyset$.
  - Otherwise, $z\in U\intersect V \implies (z, z) \in B\intersect \Delta$, but $B \subset X^2\setminus \Delta \implies B \intersect \Delta = \emptyset$. 


:::

