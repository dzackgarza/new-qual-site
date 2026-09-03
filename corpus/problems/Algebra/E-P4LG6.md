---
schema: qual/card@1
id: E-P4LG6
kind: problem
title: Normal subgroups of $p$-groups intersect the center
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Class Equation
  - Centralizers and Normalizers
relations: []
review: draft
---

:::{.exercise}
Prove that if $G$ is a $p\dash$group, every subgroup $N\normal G$ intersects the center $Z(G)$.

> Hint: use the class equation.

:::

:::{.solution}
\envlist

Easy solution:

- Use that $\size  H \mod p = 1$ since $H\leq G$ and $G$ is a $p\dash$group.
- Then use that $H$ is a union of conjugacy classes, and since $e\in H$ there is at least one class of size 1, so
\[
\size  H = \size  \disjoint' [h_i] = \size  [e] + \sum' \size  [h_i] \\
\implies 0 \equiv \size  H \equiv 1 + \sum' \size [h_i] \mod p
,\]
and since each $\size  [h_i]$ divides $\size  H$, not all can be of size $p^\ell$ since then the sum would be $0\mod p$.
So at least one other $\size  [h_i] = 1$, making that $h_i$ central.

Another solution:

- Idea: use the class equation to force $p$ to divide $\size (H \intersect Z(G))$.
  Applying it to $H$ yields
\[
H = Z(H) \disjoint_{i=1}^m [h_i]
,\]
where the $[h_i]$ are conjugacy classes of size greater than 1.

- Now use that $Z(H) = Z(G) \intersect H$, and since $p$ divides the LHS the result will follow if $p$ divides the size of the disjoint union on the RHS.
- This is true because each $\size [h_i] \neq 1$ and $[h_i]$ divides $\size  H$ which divides $\size  G$ which is a power of $p$.
  So $p\divides \size  [h_i]$ for each $i$.

:::
