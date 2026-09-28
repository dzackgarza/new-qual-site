---
schema: qual/card@1
id: P-APAS18B
kind: problem
title: Sum of $|\lambda_i|^2$ bounded by sum of $\sigma_i^2$; equality and normality
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
  - Normal Operators
relations: []
review: draft
---

::: {.problem}
Let $A\in\mathbb{C}^{n\times n}$ be a matrix with eigenvalues $\lambda_1,\ldots,\lambda_n\in\mathbb{C}$ and singular values $\sigma_1\geq\cdots\geq\sigma_n\geq 0$.
Show that
\[
|\lambda_1|^2+\cdots+|\lambda_n|^2\leq\sigma_1^2+\cdots+\sigma_n^2.
\]
If the above is an equality, is the matrix $A$ normal (i.e., $AA^*=A^*A$)? If yes, explain why; if no, give a counterexample.
:::

::: {.solution}
By Schur decomposition there is a unitary matrix \(U\) such that
\[
U^*AU=T,
\]
where \(T\) is upper triangular and its diagonal entries are the eigenvalues \(\lambda_1,\ldots,\lambda_n\), counted with algebraic multiplicity.

The Frobenius norm is unitarily invariant, and
\[
\|A\|_F^2=\operatorname{tr}(A^*A)=\sum_{i=1}^n\sigma_i^2.
\]
Therefore
\[
\sum_{i=1}^n\sigma_i^2
=\|T\|_F^2
=\sum_{i=1}^n|\lambda_i|^2+\sum_{i<j}|t_{ij}|^2
\ge \sum_{i=1}^n|\lambda_i|^2.
\]
This proves the inequality.

Moreover, equality holds if and only if every strictly upper-triangular entry of \(T\) vanishes. Thus equality holds if and only if \(T\) is diagonal. In that case
\[
A=UTU^*
\]
is unitarily diagonalizable, hence normal.

Conversely, if \(A\) is normal, the spectral theorem gives a unitary diagonalization of \(A\), so its singular values are the absolute values of its eigenvalues (up to ordering), and equality holds. Hence equality occurs exactly for normal matrices.
:::
