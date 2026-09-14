---
schema: qual/card@1
id: P-UCLAB02W-11
kind: problem
title: Triangularization in an orthonormal basis
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 11 of the official UCLA Basic Examination, Winter 2002 PDF. The source calls the matrix "upper triangular" but then specifies $A_{ij}=0$ for $i<j$, which is the standard lower-triangular index condition.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Records the terminology/index mismatch. Standard Schur triangularization gives the upper-triangular convention $A_{ij}=0$ for $i>j$; reversing an orthonormal basis converts it to the printed lower-triangular convention.
---

::: {.problem}
Let $V$ be a finite-dimensional complex inner-product space and let $T:V\to V$ be linear.
Prove that there exists an ordered orthonormal basis of $V$ such that the matrix $A=(A_{ij})$ of $T$ in this basis is, in the wording of the source, "upper triangular," with
\[
A_{ij}=0
\qquad\text{if }i<j.
\]

Hint: first show that if $S:V\to V$ is linear and $W\subset V$ is a subspace, then $W$ is $S$-invariant if and only if $W^\perp$ is $S^*$-invariant.
:::

::: {.solution}
The source's terminology and index condition disagree: under the standard convention, $A_{ij}=0$ for $i<j$ means that $A$ is lower triangular.
Both triangularization orientations exist.

For the standard upper-triangular form, use induction on $n=\dim V$.
Over $\mathbb C$, the adjoint $T^*$ has an eigenvector $0\ne w\in V$.
Let $W=\mathbb Cw$.
Then $W$ is $T^*$-invariant, so by the hinted orthogonal-complement criterion, $W^\perp$ is $T$-invariant.
By induction, $T|_{W^\perp}$ has an orthonormal basis in which its matrix is upper triangular.
Appending the unit vector $w/\|w\|$ gives an orthonormal basis of $V$ in which the matrix of $T$ is upper triangular, i.e. its entries vanish for $i>j$.

Finally, reverse the order of this orthonormal basis.
Conjugation by the reversal permutation matrix converts an upper-triangular matrix to a lower-triangular one, so in the reversed basis the entries satisfy
\[
A_{ij}=0\qquad(i<j),
\]
which is exactly the index condition printed in the source.
:::
