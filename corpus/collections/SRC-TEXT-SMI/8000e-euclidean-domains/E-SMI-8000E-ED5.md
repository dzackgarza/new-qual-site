---
schema: qual/card@1
id: E-SMI-8000E-ED5
kind: problem
title: Matrices over a Euclidean domain are diagonalizable by invertible row and column operations
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
  - Modules
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
Assume $R$ is a Euclidean domain.
Prove every $m \times n$ matrix over $R$ can be diagonalized by invertible row and column operations.

[Hint: use induction on the size of the upper left entry of the matrix instead of on the number of prime factors.]
:::

::: {.solution}
<1>1. Induction on the Euclidean size $N(a_{11})$ of the $(1,1)$-entry (after permuting rows/columns to make $a_{11}\neq0$ minimal).
::: {.proof}
setup; $R$ is Euclidean with size function $N$.
:::

<1>2. If every entry of the first row and column is divisible by $a_{11}$, clear the rest of the first row and column by elementary operations.
::: {.proof}
$a_{1j}=q_j a_{11}$, subtract $q_j$ times column $1$ from column $j$; similarly for rows.
:::

<1>3. Otherwise some entry $a_{1j}$ or $a_{i1}$ is not divisible by $a_{11}$; divide with remainder $a_{1j}=q a_{11}+r$ with $N(r)<N(a_{11})$ and replace column $j$ by column $j - q\cdot$column $1$ to get remainder $r$ in the first row, then permute to bring $r$ to the $(1,1)$-position, strictly decreasing $N$.
::: {.proof}
Euclidean division.
:::

<1>4. By induction on $N(a_{11})$ we reach the case of <1>2, so we can make the matrix $\begin{pmatrix} a_{11} & 0 \\ 0 & A' \end{pmatrix}$ with $a_{11}$ dividing all entries of $A'$.
::: {.proof}
<1>2 and <1>3 (the process terminates).
:::

<1>5. Apply induction on the size of the matrix to $A'$.
::: {.proof}
induction on $m+n$.
:::

<1>6. Hence by invertible row and column operations the matrix is diagonalized (Smith normal form).
::: {.proof}
<1>4 and <1>5.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
