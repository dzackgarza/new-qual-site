---
schema: qual/card@1
id: E-PFQIX
kind: exercise
title: Separation properties of topological groups and coset spaces
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Hausdorff Spaces
relations: []
review: draft
---

::: {.exercise title="Munkres §22 Supplementary"}

If $A$ and $B$ are subsets of the topological group $G$, let $A \cdot B$ denote the set of all points $a \cdot b$ for $a \in A$ and $b \in B$.
Let $A^{-1}$ denote the set of all points $a^{-1}$, for $a \in A$.

(a) A neighborhood $V$ of the identity element $e$ is said to be symmetric if $V = V^{-1}$.
If $U$ is a neighborhood of $e$, show there is a symmetric neighborhood $V$ of $e$ such that $V \cdot V \subset U$.
[Hint: If $W$ is a neighborhood of $e$, then $W \cdot W^{-1}$ is symmetric.]

(b) Show that $G$ is Hausdorff.
In fact, show that if $x \neq y$, there is a neighborhood $V$ of $e$ such that $V \cdot x$ and $V \cdot y$ are disjoint.

(c) Show that $G$ satisfies the following separation axiom, which is called the regularity axiom: given a closed set $A$ and a point $x$ not in $A$, there exist disjoint open sets containing $A$ and $x$, respectively.
[Hint: There is a neighborhood $V$ of $e$ such that $V \cdot x$ and $V \cdot A$ are disjoint.]

(d) Let $H$ be a subgroup of $G$ that is closed in the topology of $G$; let $p: G \to G/H$ be the quotient map.
Show that $G/H$ satisfies the regularity axiom.
[Hint: Examine the proof of (c) when $A$ is saturated.]
:::
