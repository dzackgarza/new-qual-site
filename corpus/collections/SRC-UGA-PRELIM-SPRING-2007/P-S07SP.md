---
schema: qual/card@1
id: P-S07SP
kind: problem
title: Spectral theorem and an orthogonal diagonalization of $\begin{pmatrix}2&-2\\-2&5\end{pmatrix}$
classification:
  areas:
  - prelim
  topics:
  - Spectral Theorem
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
a) State the Spectral Theorem (over $\mathbb{R}$).

b) Let $A = \begin{bmatrix} 2 & -2 \\ -2 & 5 \end{bmatrix}$.
Find an orthogonal matrix $P$ for which $P^{-1}AP$ is diagonal.
:::

::: {.solution}
**Part (a).**

<1>1. Spectral Theorem (over $\RR$): if $A$ is a real symmetric matrix, then $A$ is orthogonally diagonalizable; i.e. there is an orthogonal matrix $P$ (with $P^{-1} = P^T$) such that $P^{-1} A P$ is diagonal, and the diagonal entries are the (real) eigenvalues of $A$.
Proof: statement of the theorem.

**Part (b).**

<1>1. The eigenvalues of $A$ are $1$ and $6$.
Proof: $\det(A - \lambda I) = (2-\lambda)(5-\lambda) - 4 = \lambda^2 - 7\lambda + 6 = (\lambda - 1)(\lambda - 6)$.

<1>2. An eigenvector for $\lambda = 1$ is $\begin{bmatrix} 2 \\ 1 \end{bmatrix}$.
Proof: $(A - I)\begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 & -2 \\ -2 & 4 \end{bmatrix}\begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$.

<1>3. An eigenvector for $\lambda = 6$ is $\begin{bmatrix} -1 \\ 2 \end{bmatrix}$.
Proof: $(A - 6I)\begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} -4 & -2 \\ -2 & -1 \end{bmatrix}\begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$.

<1>4. The eigenvectors $\begin{bmatrix} 2 \\ 1 \end{bmatrix}$ and $\begin{bmatrix} -1 \\ 2 \end{bmatrix}$ are orthogonal.
Proof: $2(-1) + 1(2) = 0$.

<1>5. Normalize them to get the orthogonal matrix
$$P = \frac{1}{\sqrt{5}}\begin{bmatrix} 2 & -1 \\ 1 & 2 \end{bmatrix}.$$
Proof: each eigenvector has norm $\sqrt{5}$.

<1>6. Then $P^{-1} A P = \begin{bmatrix} 1 & 0 \\ 0 & 6 \end{bmatrix}$.
Proof: $P$ is orthogonal (so $P^{-1} = P^T$) and its columns are eigenvectors of $A$ with eigenvalues $1$ and $6$.

<1>7. Q.E.D.
Proof: <1>6.
:::
