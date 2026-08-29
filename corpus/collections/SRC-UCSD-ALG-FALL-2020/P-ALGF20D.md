---
schema: qual/card@1
id: P-ALGF20D
kind: problem
title: Jordan form of the all-ones matrix over an algebraically closed field
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $F$ be an algebraically closed field.
Let $A$ be the $n \times n$ matrix over $F$ such that every entry of $A$ is $1$.
Find the Jordan canonical form of $A$.
(The answer may depend on the properties of the field $F$).
:::

::: {.solution}
<1>1. $A$ is the all-ones matrix, so $A = \mathbf{1}\mathbf{1}^t$ where $\mathbf{1} = (1, \ldots, 1)^t$.
Proof: the all-ones matrix is the outer product of the all-ones vector with itself.

<1>2. $A$ has rank $1$ (its columns are all equal to $\mathbf{1}$).
Proof: <1>1.

<1>3. $A\mathbf{1} = n\mathbf{1}$, so $n$ is an eigenvalue with eigenvector $\mathbf{1}$.
Proof: each row of $A$ sums to $n$.

<1>4. The kernel of $A$ is $\{x : \sum_i x_i = 0\}$, of dimension $n - 1$, so $0$ is an eigenvalue of geometric multiplicity $n - 1$.
Proof: $Ax = (\sum_i x_i)\mathbf{1}$, so $Ax = 0$ iff $\sum_i x_i = 0$.

<1>5. Hence the eigenvalues are $n$ (multiplicity $1$) and $0$ (multiplicity $n - 1$).
Proof: <1>3 and <1>4.

<1>6. $A$ is diagonalizable (it is symmetric, or equivalently its minimal polynomial is $x(x - n)$, which has distinct roots).
Proof: $A^2 = nA$, so $A$ satisfies $x^2 - nx = x(x - n)$, which has distinct roots.

<1>7. Hence the Jordan form of $A$ is $\operatorname{diag}(n, 0, \ldots, 0)$ (one $1 \times 1$ block for $n$ and $n - 1$ blocks of size $1$ for $0$).
Proof: <1>5 and <1>6.

<1>8. If $\operatorname{char} F \mid n$ (i.e. $n = 0$ in $F$), then the eigenvalue $n$ coincides with $0$, so $A$ is nilpotent (with $A^2 = nA = 0$), and the Jordan form is one $2 \times 2$ block for $0$ and $n - 2$ blocks of size $1$ for $0$ (since $A$ has rank $1$ and $A^2 = 0$).
Proof: <1>6 and <1>7, specialized to the case $n = 0$ in $F$.

<1>9. Q.E.D.
Proof: <1>7 and <1>8.
:::
