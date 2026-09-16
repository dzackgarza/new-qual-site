---
schema: qual/card@1
id: P-5HVC4
kind: problem
title: Diagonalizability of $\begin{pmatrix}0&1\\6&-1\end{pmatrix}$ and a closed form
  for $A^k\begin{pmatrix}1\\7\end{pmatrix}$
classification:
  areas:
  - prelim
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $A = \begin{bmatrix} 0 & 1 \\ 6 & -1 \end{bmatrix}$.
Prove that $A$ is diagonalizable and find a closed-form expression for $A^k \begin{bmatrix} 1 \\ 7 \end{bmatrix}$, $k \in \mathbb{N}$.
:::

::: {.solution}
The characteristic polynomial is
\[
\det(\lambda I-A)=\lambda^2+\lambda-6=(\lambda-2)(\lambda+3).
\]
Thus $A$ has two distinct eigenvalues and is diagonalizable. Corresponding eigenvectors are
\[
v_2=\binom12,\qquad v_{-3}=\binom1{-3}.
\]
Since
\[
\binom17=2v_2-v_{-3},
\]
we obtain for every $k\in\mathbb N$
\[
A^k\binom17
=2\,2^k v_2-(-3)^k v_{-3}.
\]
Equivalently,
\[
\boxed{A^k\binom17=
\binom{2^{k+1}-(-3)^k}{2^{k+2}+3(-3)^k}}.
\]
:::
