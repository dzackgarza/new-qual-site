---
schema: qual/card@1
id: P-ALGS20E
kind: problem
title: "Finitely generated submodules, maximal non-finitely generated ideals are prime"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
---

::: problem
Suppose $A$ is a unital commutative ring.

(a) Let $M$ and $N$ be two submodules of an $A$-module $K$.
Suppose $M + N$ and $M \cap N$ are finitely generated $A$-modules.
Prove that $M$ is a finitely generated $A$-module.

(b) Let $\Sigma := \{\mathfrak{a} \leq A \mid \mathfrak{a} \text{ is not a finitely generated ideal}\}$.
Suppose $\Sigma$ is not empty.
Prove that $\Sigma$ has a maximal element.

(c) Let $\mathfrak{p}$ be a maximal element of $\Sigma$.
Prove that $\mathfrak{p}$ is a prime ideal.

Hint: Suppose to the contrary that $ab \in \mathfrak{p}$ and $a, b \notin \mathfrak{p}$ for some $a, b \in A$; consider $\mathfrak{p} + \langle a \rangle$ and $\mathfrak{p} \cap \langle a \rangle$.
:::
