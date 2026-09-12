---
schema: qual/card@1
id: P-F12PD
kind: problem
title: Diagonalize $\begin{pmatrix}7&-3\\1&3\end{pmatrix}$
classification:
  areas:
  - prelim
  topics:
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $A = \begin{pmatrix} 7 & -3 \\ 1 & 3 \end{pmatrix}$.
Find an invertible matrix $P$ and a diagonal matrix $D$ with $P^{-1}AP = D$.
[You should not have to compute $P^{-1}$.]
:::

::: solution
The characteristic polynomial is
\[
\det(\lambda I-A)=(\lambda-7)(\lambda-3)+3
=\lambda^2-10\lambda+24=(\lambda-4)(\lambda-6).
\]
For $\lambda=4$, an eigenvector is $(1,1)^t$; for $\lambda=6$, an eigenvector is $(3,1)^t$. Thus
\[
P=\begin{pmatrix}1&3\\1&1\end{pmatrix},\qquad
D=\begin{pmatrix}4&0\\0&6\end{pmatrix}.
\]
Since $\det P=-2\ne0$, $P$ is invertible, and because its columns are eigenvectors in the displayed order,
\[
P^{-1}AP=D.
\]
:::
