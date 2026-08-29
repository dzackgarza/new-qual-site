---
schema: qual/card@1
id: P-A12ND
kind: problem
title: The $2\times 2$ matrix sending $(1,2)$ to $(5,-6)$ and $(0,1)$ to $(1,-1)$
  is not diagonalizable
classification:
  areas:
  - prelim
  topics:
  - Matrices
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Determine the $2 \times 2$ matrix $A$ such that $A \begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 5 \\ -6 \end{bmatrix}$ and $A \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$.
Prove that the matrix $A$ is not diagonalizable.
:::

::: {.solution}
<1>1. $A = \begin{bmatrix} 3 & 1 \\ -4 & -1 \end{bmatrix}$.
<2>1. The second column of $A$ is $A e_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$.
Proof: $e_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$.
<2>2. The first column of $A$ is $A e_1 = A\begin{bmatrix} 1 \\ 2 \end{bmatrix} - 2A e_2 = \begin{bmatrix} 5 \\ -6 \end{bmatrix} - 2\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 3 \\ -4 \end{bmatrix}$.
Proof: $\begin{bmatrix} 1 \\ 2 \end{bmatrix} = e_1 + 2e_2$, so $A e_1 = A\begin{bmatrix} 1 \\ 2 \end{bmatrix} - 2A e_2$.
<2>3. Hence $A = \begin{bmatrix} 3 & 1 \\ -4 & -1 \end{bmatrix}$.
Proof: <2>1 and <2>2 give the two columns.

<1>2. The characteristic polynomial of $A$ is $(t-1)^2$.
Proof: $\det(tI - A) = \det\begin{bmatrix} t-3 & -1 \\ 4 & t+1 \end{bmatrix} = (t-3)(t+1) + 4 = t^2 - 2t + 1 = (t-1)^2$.

<1>3. The eigenspace for $\lambda = 1$ has dimension $1$.
<2>1. $A - I = \begin{bmatrix} 2 & 1 \\ -4 & -2 \end{bmatrix}$.
Proof: subtract $I$.
<2>2. $\operatorname{rank}(A - I) = 1$.
Proof: the two rows are scalar multiples of each other.
<2>3. Hence $\dim \ker(A - I) = 2 - 1 = 1$.
Proof: rank–nullity theorem.

<1>4. $A$ is not diagonalizable.
<2>1. $A$ has a single eigenvalue $\lambda = 1$ of algebraic multiplicity $2$.
Proof: <1>2.
<2>2. The geometric multiplicity of $\lambda = 1$ is $1$.
Proof: <1>3.
<2>3. A matrix is diagonalizable iff for each eigenvalue the geometric multiplicity equals the algebraic multiplicity.
Proof: standard criterion.
<2>4. Hence $A$ is not diagonalizable.
Proof: <2>1–<2>3, since $1 \neq 2$.

<1>5. Q.E.D.
Proof: <1>1 and <1>4.
:::
