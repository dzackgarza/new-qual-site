---
schema: qual/card@1
id: P-EHPA5
kind: problem
title: A normal subgroup of order $p$ in a finite $p$-group lies in the center
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Normal Subgroups
  - Centralizers and Normalizers
relations: []
review: draft
---

For a prime $p$, let $G$ be a finite $p\dash$group and let $N$ be a normal subgroup of $G$ of order $p$.
Prove that $N$ is contained in the center of $G$.

:::{.concept}
\envlist

- Definition of conjugacy class: $[x] = \ts{gxg\inv \st g\in G}$.
- A conjugacy class $[x]$ is trivial iff $[x] = \ts{ x }$ iff $x\in Z(G)$.
- Sizes of conjugacy classes divide the order of the group they live in.
  - This is orbit-stabilizer: $G\actson G$ by $g\cdot x \da gxg\inv$, so $\OO(x) = [x]$.
    Then $\size \OO(x) = \size G / \size \Stab(x)$, so $\size \OO(x)$ divides $\size G$.
:::

:::{.solution}
\envlist

- Use that $N\normal G \iff N = \disjoint' [n_i]$ is a *disjoint* union of (full) conjugacy classes.
- Take cardinalities:
\[
p = \size N = \sum_{i=1}^m \size [n_i] = 1 + \sum_{i=2}^m \size [n_i]
.\]
- The size of each conjugacy class divides the size of the ambient group $G$ by orbit-stabilizer, and $\size G = p^k$, so each $\size [n_i]$ is a power of $p$.
  Note this is a statement about $\size G$, not about $\size N$: the classes $[n_i]$ are $G\dash$conjugacy classes that happen to lie inside $N$.
- So each $\size [n_i]$ is either $1$ or at least $p$.
  If any one of them were at least $p$, the sum would already be at least $1 + p > p$, which is too big.
- Hence every $\size[n_i] = 1$, and there are $m = p$ of them.
- Then $[n_i] = \ts{ n_i } \iff n_i \in Z(G)$, and this holds for all $i$, so $N \subseteq Z(G)$.
:::
