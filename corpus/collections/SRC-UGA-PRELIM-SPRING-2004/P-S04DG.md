---
schema: qual/card@1
id: P-S04DG
kind: problem
title: Diagonalize $\begin{bmatrix} 1 & 2 \\ 4 & -1 \end{bmatrix}$ and compute $A^2$
classification:
  areas:
  - prelim
  topics:
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Diagonalize the matrix $A = \begin{bmatrix} 1 & 2 \\ 4 & -1 \end{bmatrix}$ and use the diagonal form of $A$ to compute $A^2$.
:::

::: {.solution}
<1>1. The characteristic polynomial of $A$ is
\[
\chi_A(\lambda)=\det(\lambda I-A)=\lambda^2-9.
\]
::: {.proof}
Directly,
\[
\det\begin{bmatrix}\lambda-1&-2\\-4&\lambda+1\end{bmatrix}
=(\lambda-1)(\lambda+1)-8
=\lambda^2-9.
\]
:::

<1>2. The eigenvalues are $3$ and $-3$, with eigenvectors
\[
v_+=\begin{bmatrix}1\\1\end{bmatrix},
\qquad
v_-=\begin{bmatrix}1\\-2\end{bmatrix}.
\]
::: {.proof}
For $\lambda=3$, the equation $(A-3I)v=0$ gives $-2x+2y=0$, hence $y=x$. For $\lambda=-3$, the equation $(A+3I)v=0$ gives $4x+2y=0$, hence $y=-2x$.
:::

<1>3. Therefore
\[
P=\begin{bmatrix}1&1\\1&-2\end{bmatrix},
\qquad
D=\begin{bmatrix}3&0\\0&-3\end{bmatrix}
\]
satisfy
\[
A=PDP^{-1}.
\]
::: {.proof}
The columns of $P$ are the two eigenvectors from <1>2. Since they correspond to distinct eigenvalues, they are linearly independent, so $P$ is invertible. The relation $AP=PD$ is exactly the eigenvector equations, and hence $A=PDP^{-1}$.
:::

<1>4. Using the diagonal form,
\[
A^2=PD^2P^{-1}=P(9I_2)P^{-1}=9I_2
=\begin{bmatrix}9&0\\0&9\end{bmatrix}.
\]
:::
