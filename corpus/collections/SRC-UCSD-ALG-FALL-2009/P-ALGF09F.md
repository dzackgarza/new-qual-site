---
schema: qual/card@1
id: P-ALGF09F
kind: problem
title: "A matrix with A^3 = A decomposes C^n into a direct sum of three subspaces"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: problem
Let $n \geq 1$ and consider the ring $M_n(\mathbb{C})$ of $n \times n$ matrices with coefficients in $\mathbb{C}$.
Suppose that $A \in M_n(\mathbb{C})$ satisfies $A^3 = A$.
Let $V = \mathbb{C}^n$, an $n$-dimensional vector space over $\mathbb{C}$.
Thinking of the elements of $V$ as column vectors, consider the linear transformation $\phi: V \to V$ defined by left multiplication by the matrix $A$.
Prove that $V$ decomposes into a direct sum of three $\mathbb{C}$-linear subspaces, say $V = U_1 \oplus U_2 \oplus U_3$, such that given $v \in V$ with $v = u_1 + u_2 + u_3$ where $u_i \in U_i$, then $\phi(v) = u_1 - u_2$.
:::
