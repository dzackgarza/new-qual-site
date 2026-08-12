---
schema: qual/card@1
id: P-6TCYA
kind: problem
title: "Let $P$ be a finite $p\\dash$group. Prove that every nontrivial normal\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Let $P$ be a finite $p\dash$group.

Prove that every nontrivial normal subgroup of $P$ intersects the center of $P$ nontrivially.

:::{.solution}
\envlist

- Let $N\normal P$, then for each conjugacy class $[n_i]$ in $N$, $H \intersect [g_i] = [g_i]$ or is empty.
- $G = \disjoint_{i\leq M} [g_i]$ is a disjoint union of conjugacy classes, and the conjugacy classes of $H$ are of the form $[g_i] \intersect H$.
- Then pull out the center
\[
H = \Disjoint_{i\leq M} [g_i] \intersect H = \qty{ Z(G) \intersect H } \disjoint \Disjoint_{i\leq M'} [g_i]
.\]
- Taking cardinalities, 
\[
\# H = \# \qty{ Z(G) \intersect H} + \sum_{i\leq M'} \# [g_i]
.\]
- $p$ divides $H$ since $H\leq P$ and $P$ is a $p\dash$group.
- Each $\# [g_i] \geq 2$ since the trivial conjugacy classes appear in the center, forcing $\# [g_i] \geq p$.
- $p$ divides $\# [g_i]$ since $\# [g_i]$ must divide $\# P = p^k$
- So $p$ must divide the remaining term $Z(G) \intersect H$, which makes it nontrivial.

:::
