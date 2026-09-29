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

::: {.problem}
Determine the $2 \times 2$ matrix $A$ such that $A \begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 5 \\ -6 \end{bmatrix}$ and $A \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$.
Prove that the matrix $A$ is not diagonalizable.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$A = \begin{bmatrix} 3 & 1 \\ -4 & -1 \end{bmatrix}$.

::: pf-proof

::: {.pf-step #s1-1}

The second column of $A$ is $A e_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$.

::: pf-proof

$e_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$.

:::

:::

::: {.pf-step #s1-2}

The first column of $A$ is $A e_1 = A\begin{bmatrix} 1 \\ 2 \end{bmatrix} - 2A e_2 = \begin{bmatrix} 5 \\ -6 \end{bmatrix} - 2\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 3 \\ -4 \end{bmatrix}$.

::: pf-proof

$\begin{bmatrix} 1 \\ 2 \end{bmatrix} = e_1 + 2e_2$, so $A e_1 = A\begin{bmatrix} 1 \\ 2 \end{bmatrix} - 2A e_2$.

:::

:::

::: pf-step

Hence $A = \begin{bmatrix} 3 & 1 \\ -4 & -1 \end{bmatrix}$.

::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give the two columns.

:::

:::

:::

:::

::: {.pf-step #s2}

The characteristic polynomial of $A$ is $(t-1)^2$.

::: pf-proof

$\det(tI - A) = \det\begin{bmatrix} t-3 & -1 \\ 4 & t+1 \end{bmatrix} = (t-3)(t+1) + 4 = t^2 - 2t + 1 = (t-1)^2$.

:::

:::

::: {.pf-step #s3}

The eigenspace for $\lambda = 1$ has dimension $1$.

::: pf-proof

::: pf-step

$A - I = \begin{bmatrix} 2 & 1 \\ -4 & -2 \end{bmatrix}$.

::: pf-proof

subtract $I$.

:::

:::

::: pf-step

$\operatorname{rank}(A - I) = 1$.

::: pf-proof

the two rows are scalar multiples of each other.

:::

:::

::: pf-step

Hence $\dim \ker(A - I) = 2 - 1 = 1$.

::: pf-proof

rank–nullity theorem.

:::

:::

:::

:::

::: {.pf-step #s4}

$A$ is not diagonalizable.

::: pf-proof

::: {.pf-step #s4-1}

$A$ has a single eigenvalue $\lambda = 1$ of algebraic multiplicity $2$.

::: pf-proof

Step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4-2}

The geometric multiplicity of $\lambda = 1$ is $1$.

::: pf-proof

Step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s4-3}

A matrix is diagonalizable iff for each eigenvalue the geometric multiplicity equals the algebraic multiplicity.

::: pf-proof

standard criterion.

:::

:::

::: pf-step

Hence $A$ is not diagonalizable.

::: pf-proof

Steps [](#s4-1){.pf-ref}, [](#s4-2){.pf-ref} and [](#s4-3){.pf-ref}, since $1 \neq 2$.

:::

:::

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::
