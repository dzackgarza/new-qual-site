---
schema: qual/card@1
id: P-LZRAH
kind: problem
title: Matrices with $\tr(A^k)=0$ for all $k$
classification:
  areas:
  - algebra
  topics:
  - Trace
  - Nilpotence
  - Eigenvalues and Eigenvectors
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
Let $A\in M_n(F)$, where $F$ has characteristic $0$. Suppose
$$
\tr(A^k)=0
$$
for every $k\ge1$. What can you conclude about $A$?
:::

::: {.solution}
Over an algebraic closure of $F$, let $\lambda_1,\ldots,\lambda_n$ be the eigenvalues of $A$ with algebraic multiplicity, let $p_k=\sum_i\lambda_i^k$, and let $e_j$ be the elementary symmetric functions of the $\lambda_i$, with $e_0=1$.

::: pf

::: {.pf-step #power-sums}
$p_k=0$ for every $k\ge1$.

::: pf-proof
Triangularizing $A$ shows that $A^k$ has eigenvalues $\lambda_i^k$, so $p_k=\tr(A^k)=0$.
:::

:::

::: {.pf-step #char-poly}
$\chi_A(x)=x^n$.

::: pf-proof
$\chi_A(x)=\sum_{j=0}^n(-1)^je_jx^{n-j}$. Newton's identities give $me_m=\sum_{i=1}^m(-1)^{i-1}e_{m-i}p_i$ for $1\le m\le n$. By step [](#power-sums){.pf-ref} the right side is $0$, and $m$ is invertible in characteristic $0$, so $e_m=0$ for $1\le m\le n$.
:::

:::

::: pf-step
$A$ is $\boxed{\text{nilpotent}}$: $A^n=0$.

::: pf-proof
By step [](#char-poly){.pf-ref} and the Cayley--Hamilton theorem, $A^n=\chi_A(A)=0$.
:::

:::

:::

:::
