---
schema: qual/card@1
id: P-J77EG
kind: problem
title: Jordan form of the $n\times n$ all-ones matrix
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Diagonalization
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $F$ be a field such that $n\neq0$ in $F$, and let $M\in M_n(F)$ be the matrix whose entries are all $1$.
Find its Jordan canonical form (over a splitting field, if necessary).
:::

::: {.solution}
Write $\mathbf 1=(1,\ldots,1)^t\in F^n$ and $H=\{v\in F^n:v_1+\cdots+v_n=0\}$.

::: pf

::: {.pf-step #eigenvectors}

$M\mathbf 1=n\mathbf 1$, and $Mv=0$ for every $v\in H$.

::: pf-proof

Each coordinate of $Mv$ is $v_1+\cdots+v_n$. For $v=\mathbf 1$ this is $n$, and for $v\in H$ it is $0$.

:::

:::

::: {.pf-step #decomposition}

$F^n=H\oplus F\mathbf 1$.

::: pf-proof

$H$ has dimension $n-1$, and $\mathbf 1\notin H$ because the coordinate sum of $\mathbf 1$ is $n\ne0$ in $F$.

:::

:::

::: pf-step

$M$ is diagonalizable over $F$, with Jordan form
$$
\boxed{\diag(\underbrace{0,\ldots,0}_{n-1},n)}.
$$

::: pf-proof

By steps [](#eigenvectors){.pf-ref} and [](#decomposition){.pf-ref}, $F^n$ is the direct sum of the $0$-eigenspace $H$ of dimension $n-1$ and the $n$-eigenspace $F\mathbf 1$. No extension of $F$ is needed.

:::

:::

:::

:::
