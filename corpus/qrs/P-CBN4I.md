---
schema: qual/card@1
id: P-CBN4I
kind: problem
title: "For a prime $p$, let $G$ be a finite $p\\dash$group and let $N$ be a no\u2026"
classification:
  areas:
  - algebra
  topics: []
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
    Then $\# \OO(x) = \# G / \# \Stab(x)$, so $\# \OO(x)$ divides $\# G$.
:::

:::{.solution}
\envlist

- Use that $N\normal G \iff N = \disjoint' [n_i]$ is a *disjoint* union of (full) conjugacy classes.
- Take cardinalities:
\[
p = \# N = \sum_{i=1}^m \# [n_i] = 1 + \sum_{i=2}^m [n_i]
.\]
- The size of each conjugacy class divides the size of $H$ by orbit-stabilizer, so $\# [n_i] \divides p$ for each $i$.
- But the entire second term must sum to $p-1$ for this equality to hold, which forces $\#[n_i] = 1$ (and incidentally $m=p-1$)
- Then $[n_i] = \ts{ n_i } \iff n_i \in Z(G)$, and this holds for all $i$, so $N \subseteq Z(G)$.
:::

