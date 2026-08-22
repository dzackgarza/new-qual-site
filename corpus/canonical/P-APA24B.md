---
schema: qual/card@1
id: P-APA24B
kind: problem
title: A matrix is unitarily diagonalizable if and only if it is normal
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Diagonalization
  - Normal Operators
relations: []
review: draft
solved: false
---

::: problem
Consider $A \in M_n(\mathbb{C}) = \mathbb{C}^{n \times n}$.
Prove the result: $A$ is unitarily diagonalizable if and only if $A$ is normal.

Note, mathematically, this can be written as: there exists $U \in M_n(\mathbb{C}) = \mathbb{C}^{n \times n}$, satisfying $U^H U = U U^H = I$, such that $U^H A U$ is diagonal if and only if $A^H A = A A^H$, where $U^H = \overline{U}^T$ and $A^H = \overline{A}^T$.
:::
