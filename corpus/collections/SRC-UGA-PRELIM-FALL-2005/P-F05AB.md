---
schema: qual/card@1
id: P-F05AB
kind: problem
title: Diagonalize $\begin{pmatrix} 8 & 9 \\ -6 & -7 \end{pmatrix}$ as $ABA^{-1}$
classification:
  areas:
  - prelim
  topics:
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Find an invertible matrix $A$ and a diagonal matrix $B$ such that $\begin{pmatrix} 8 & 9 \\ -6 & -7 \end{pmatrix} = ABA^{-1}$.
:::

::: {.solution}
<1>1. Let $M = \begin{pmatrix} 8 & 9 \\ -6 & -7 \end{pmatrix}$; its eigenvalues are $-1$ and $2$.
Proof: $\det(M - \lambda I) = (8-\lambda)(-7-\lambda) + 54 = \lambda^2 - \lambda - 2 = (\lambda + 1)(\lambda - 2)$.

<1>2. An eigenvector for $\lambda = -1$ is $\begin{pmatrix} -1 \\ 1 \end{pmatrix}$.
Proof: $M\begin{pmatrix} -1 \\ 1 \end{pmatrix} = \begin{pmatrix} -8 + 9 \\ 6 - 7 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \end{pmatrix} = -\begin{pmatrix} -1 \\ 1 \end{pmatrix}$.

<1>3. An eigenvector for $\lambda = 2$ is $\begin{pmatrix} -3 \\ 2 \end{pmatrix}$.
Proof: $M\begin{pmatrix} -3 \\ 2 \end{pmatrix} = \begin{pmatrix} -24 + 18 \\ 18 - 14 \end{pmatrix} = \begin{pmatrix} -6 \\ 4 \end{pmatrix} = 2\begin{pmatrix} -3 \\ 2 \end{pmatrix}$.

<1>4. Let $A = \begin{pmatrix} -1 & -3 \\ 1 & 2 \end{pmatrix}$ (columns are the eigenvectors) and $B = \begin{pmatrix} -1 & 0 \\ 0 & 2 \end{pmatrix}$.
Proof: definition.

<1>5. Then $M = A B A^{-1}$.
Proof: $A$ has the eigenvectors as columns, so $A^{-1} M A = B$, equivalently $M = A B A^{-1}$.

<1>6. Q.E.D.
Proof: <1>5.
:::
