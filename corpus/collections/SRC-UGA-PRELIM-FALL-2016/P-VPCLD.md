---
schema: qual/card@1
id: P-VPCLD
kind: problem
title: Spectral theorem diagonalization with eigenvalues $1$ and $-2$
classification:
  areas:
  - prelim
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
relations: []
review: draft
---

::: problem
Find an invertible matrix $A$ and a diagonal matrix $B$ such that
\[
\begin{pmatrix}4&-6\\3&-5\end{pmatrix}=ABA^{-1}.
\]
:::

::: solution
The eigenvalues are $1$ and $-2$. Corresponding eigenvectors are $(2,1)^t$ and $(1,1)^t$. Thus one can take
\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},
\qquad
B=\begin{pmatrix}1&0\\0&-2\end{pmatrix}.
\]
The columns of $A$ are linearly independent, and the eigenvector equations give $MA=AB$ for the given matrix $M$. Hence $M=ABA^{-1}$.
:::
