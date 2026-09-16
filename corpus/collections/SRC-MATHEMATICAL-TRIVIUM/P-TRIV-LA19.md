---
schema: qual/card@1
id: P-TRIV-LA19
kind: problem
title: Pauli matrices as a basis of $2\times 2$ Hermitian matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 19, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the garbled Pauli matrices from Linear Algebra Problem 19 on page 3 of the source PDF.
---

::: problem
Consider the Pauli matrices,
$$
\sigma_1 = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \quad
\sigma_2 = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}, \quad
\sigma_3 = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}.
$$

(a) Calculate $\sigma_i^\dagger$, $i = 1, 2, 3$.

(b) Decompose a matrix $A = \begin{bmatrix} a & b + ic \\ b - ic & -a \end{bmatrix}$, $a, b, c \in \mathbb{R}$, into a sum of $\sigma_i$.

(c) Prove that $\sigma_i$, $i = 1, 2, 3$, constitute a basis in the space of $2 \times 2$ hermitian matrices with zero trace.

(d) Prove that $\{\sigma_i, i = 1, 2, 3;\ 1\}$ constitute a basis in the space of $2 \times 2$ hermitian matrices.

(e) Calculate the eigenvalues and the eigenvectors of $\sigma_i$, $i = 1, 2, 3$.
:::
