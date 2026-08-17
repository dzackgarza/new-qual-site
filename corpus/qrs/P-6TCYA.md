---
schema: qual/card@1
id: P-6TCYA
kind: problem
title: "Let $P$ be a finite $p\\dash$group. Prove that every nontrivial normal\u2026"
classification:
  areas:
  - algebra
  topics:
  - p-groups
  - normal-subgroups
  - class-equation
relations: []
review: draft
solved: true
---
Let $P$ be a finite $p\dash$group.

Prove that every nontrivial normal subgroup of $P$ intersects the center of $P$ nontrivially.

:::{.solution}
\envlist

- Let $N\normal P$ be nontrivial.
  Since $N$ is normal it is a union of $P\dash$conjugacy classes: for each class $[g_i]$ of $P$, either $[g_i]\subseteq N$ or $[g_i]\intersect N = \emptyset$.
- Writing $P = \disjoint_{i\leq M} [g_i]$ as a disjoint union of conjugacy classes, $N$ is the union of those classes it contains.
- Then pull out the center, whose elements are exactly the ones in singleton classes:
\[
N = \Disjoint_{i\leq M} \qty{ [g_i] \intersect N } = \qty{ Z(P) \intersect N } \disjoint \Disjoint_{i\leq M'} [g_i]
,\]
  where the second union runs over the classes inside $N$ of size greater than one.
- Taking cardinalities, 
\[
\# N = \# \qty{ Z(P) \intersect N} + \sum_{i\leq M'} \# [g_i]
.\]
- $p$ divides $\# N$, since $N\leq P$ is nontrivial and $\# P = p^k$.
- Each $\# [g_i]$ in the second sum divides $\# P = p^k$ by orbit-stabilizer, and is greater than one, so it is at least $p$.
  In particular $p$ divides each of them.
- So $p$ divides the remaining term $\# \qty{Z(P) \intersect N}$.
  That term is at least $1$, since the identity lies in it, so it is at least $p$, and the intersection is nontrivial.

:::
