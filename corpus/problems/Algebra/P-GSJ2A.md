---
schema: qual/card@1
id: P-GSJ2A
kind: problem
title: Eigenvalues of a symmetric matrix
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Matrices
  - Inner Product Spaces
relations: []
review: draft
---

::: {.problem}
What can you say about the eigenvalues of a real symmetric matrix?
:::


::: {.solution}
Let $A\in M_n(\RR)$ satisfy $A^t=A$. Regard an eigenpair $Av=\lambda v$ in $\CC^n$. Then
\[
\lambda\langle v,v\rangle
=\langle Av,v\rangle
=\langle v,Av\rangle
=\overline\lambda\langle v,v\rangle.
\]
Since $v\ne0$, this gives $\lambda=\overline\lambda$, so every eigenvalue is real.

The real spectral theorem strengthens this: there is an orthogonal matrix $Q$ and real numbers $\lambda_1,\ldots,\lambda_n$ such that
\[
Q^tAQ=\operatorname{diag}(\lambda_1,\ldots,\lambda_n).
\]
Thus a real symmetric matrix has only real eigenvalues, is diagonalizable over $\RR$, and admits an orthonormal basis of eigenvectors. Eigenspaces belonging to distinct eigenvalues are orthogonal.
:::
