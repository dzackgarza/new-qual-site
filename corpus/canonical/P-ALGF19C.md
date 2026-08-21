---
schema: qual/card@1
id: P-ALGF19C
kind: problem
title: Units of $A[x]$ via units and nilradical of $A$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
solved: false
---

::: problem
Suppose $A$ is a unital commutative ring. Let $A[x]$ be the ring of polynomials, $A^\times$ be the group of units of $A$, and $\mathrm{Nil}(A)$ be the nilradical of $A$. Prove that
\[
A[x]^\times = \{ a_0 + a_1 x + \cdots + a_n x^n \mid a_0 \in A^\times,\; a_1,\ldots,a_n \in \mathrm{Nil}(A),\; n \in \mathbb{Z}^+ \},
\]
where $A[x]^\times$ is the group of units of $A[x]$. (Hint. Without proof you can use that $\sum_i a_i x^i \mapsto \sum_i (a_i + \mathfrak{a}) x^i$ is a ring homomorphism from $A[x]$ to $(A/\mathfrak{a})[x]$ for any $\mathfrak{a} \trianglelefteq A$. Show that if $u$ is a unit and $n$ is nilpotent, then $u + n = u(1 + u^{-1}n)$ is a unit.)
:::
