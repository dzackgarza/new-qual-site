---
schema: qual/card@1
id: P-ARTALG-SU05-6
kind: problem
title: Non-similar matrices with same rational eigenvalue
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Two $n \times n$ matrices $A$ and $B$ over a field $F$ are said to be similar if there exists an $n \times n$ invertible matrix $T$ over $F$ such that $TAT^{-1} = B$.
Exhibit three $3 \times 3$ matrices over $\mathbb{Q}$ no two of which are similar such that $-2$ is the only rational eigenvalue of each of the matrices.
For each, determine its elementary divisors, minimal polynomial and characteristic polynomial.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let
$$A_1 = \begin{pmatrix} -2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -2 \end{pmatrix}, \qquad
A_2 = \begin{pmatrix} -2 & 1 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -2 \end{pmatrix}, \qquad
A_3 = \begin{pmatrix} -2 & 1 & 0 \\ 0 & -2 & 1 \\ 0 & 0 & -2 \end{pmatrix}.$$
Each has characteristic polynomial $(x+2)^3$, and $-2$ is its only eigenvalue.

::: pf-proof

Each $A_j$ is upper triangular with every diagonal entry $-2$, so $\det(xI-A_j)=(x+2)^3$.
The eigenvalues are the roots of the characteristic polynomial, so $-2$ is the only one.

:::

:::

::: {.pf-step #s2}

The elementary divisors and minimal polynomials are:

- $A_1$: elementary divisors $x+2,\ x+2,\ x+2$; minimal polynomial $x+2$.
- $A_2$: elementary divisors $(x+2)^2,\ x+2$; minimal polynomial $(x+2)^2$.
- $A_3$: elementary divisor $(x+2)^3$; minimal polynomial $(x+2)^3$.

::: pf-proof

The matrices are in Jordan form with eigenvalue $-2$ and Jordan blocks of sizes $(1,1,1)$, $(2,1)$, and $(3)$.
A Jordan block of size $k$ with eigenvalue $-2$ contributes the elementary divisor $(x+2)^k$.
The characteristic polynomial is the product of the elementary divisors, and the minimal polynomial is their least common multiple, here $(x+2)^m$ for the largest block size $m$ [@DF04].

:::

:::

::: {.pf-step #s3}

No two of $A_1,A_2,A_3$ are similar.

::: pf-proof

Similar matrices have the same elementary divisors [@DF04].
The three lists in step [](#s2){.pf-ref} are distinct.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s3){.pf-ref} show that $A_1,A_2,A_3$ are pairwise nonsimilar $3\times3$ matrices over $\QQ$ whose only rational eigenvalue is $-2$, and steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give their characteristic polynomials, elementary divisors, and minimal polynomials.

:::

:::

:::
