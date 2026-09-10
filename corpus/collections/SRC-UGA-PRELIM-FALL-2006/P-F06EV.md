---
schema: qual/card@1
id: P-F06EV
kind: problem
title: Eigenvalues and eigenvectors of $\begin{pmatrix}1&-2\\3&-4\end{pmatrix}$
classification:
  areas:
  - prelim
  topics:
  - Eigenvalues
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Find the eigenvalues and eigenvectors of the matrix $A = \begin{bmatrix} 1 & -2 \\ 3 & -4 \end{bmatrix}$.
:::

::: solution
The characteristic polynomial is
\[
\det(A-\lambda I)
=\det\begin{bmatrix}1-\lambda&-2\\3&-4-\lambda\end{bmatrix}
=(\lambda+1)(\lambda+2).
\]
Thus the eigenvalues are $-1$ and $-2$.

For $\lambda=-1$,
\[
A+I=\begin{bmatrix}2&-2\\3&-3\end{bmatrix},
\]
so the eigenspace is
\[
\ker(A+I)=\operatorname{span}\{(1,1)^T\}.
\]
For $\lambda=-2$,
\[
A+2I=\begin{bmatrix}3&-2\\3&-2\end{bmatrix},
\]
so
\[
\ker(A+2I)=\operatorname{span}\{(2,3)^T\}.
\]
Hence every nonzero multiple of $(1,1)^T$ is an eigenvector for $-1$, and every nonzero multiple of $(2,3)^T$ is an eigenvector for $-2$.
:::
