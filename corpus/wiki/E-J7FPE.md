---
schema: qual/card@1
id: E-J7FPE
kind: exercise
title: Coverings of the torus are classified by rank
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
solved: false
---

Let $T = S^1 \times S^1$ be the torus; let $x_0 = b_0 \times b_0$.

(a) Prove the following.

Theorem. Every isomorphism of $\pi_1(T, x_0)$ with itself is induced by a homeomorphism of $T$ with itself that maps $x_0$ to $x_0$.

[Hint: Let $p: \mathbb{R}^2 \to T$ be the usual covering map. If $A$ is a $2 \times 2$ matrix with integer entries, the linear map $T_A: \mathbb{R}^2 \to \mathbb{R}^2$ with matrix $A$ induces a continuous map $f: T \to T$. Furthermore, $f$ is a homeomorphism if $A$ is invertible over the integers.]

(b) Prove the following.

Theorem. If $E$ is a covering space of $T$, then $E$ is homeomorphic either to $\mathbb{R}^2$, or to $S^1 \times \mathbb{R}$, or to $T$.

[Hint: You may use the following result from algebra: if $F$ is a free abelian group of rank 2 and $N$ is a nontrivial subgroup, then there is a basis $a_1, a_2$ for $F$ such that either (1) $ma_1$ is a basis for $N$, for some positive integer $m$, or (2) $ma_1, na_2$ is a basis for $N$, where $m$ and $n$ are positive integers.]

::: {.remark}
Munkres, *Topology*, §79 Exercise 5 (starred in the text).
:::
