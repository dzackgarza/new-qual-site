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
<1>1. We need three $3 \times 3$ matrices over $\QQ$ with $-2$ as the only rational eigenvalue, pairwise non-similar.

<1>2. Take
$$A_1 = \begin{pmatrix} -2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -2 \end{pmatrix}, \qquad
A_2 = \begin{pmatrix} -2 & 1 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -2 \end{pmatrix}, \qquad
A_3 = \begin{pmatrix} -2 & 1 & 0 \\ 0 & -2 & 1 \\ 0 & 0 & -2 \end{pmatrix}.$$
::: {.proof}
These are the three Jordan forms with sole eigenvalue $-2$ and Jordan-block partitions $(1,1,1)$, $(2,1)$, and $(3)$, respectively.
:::

<1>3. Each has characteristic polynomial $(x + 2)^3$.
::: {.proof}
Each matrix is upper triangular with diagonal entries $-2,-2,-2$. Therefore each characteristic polynomial is $(x+2)^3$, and $-2$ is the only eigenvalue.
:::

<1>4. The minimal polynomials are:
- $A_1$: $x + 2$ (elementary divisors $x+2, x+2, x+2$);
- $A_2$: $(x+2)^2$ (elementary divisors $(x+2)^2, x+2$);
- $A_3$: $(x+2)^3$ (elementary divisor $(x+2)^3$).
::: {.proof}
For a Jordan block $J_k(-2)$, the corresponding elementary divisor is $(x+2)^k$. Thus the elementary divisors are exactly those listed above. The minimal polynomial is the least common multiple of the elementary divisors, equivalently $(x+2)^m$ where $m$ is the largest Jordan-block size. Hence the three displayed minimal polynomials follow.
:::

<1>5. The three matrices are pairwise non-similar.
::: {.proof}
Similar matrices have the same minimal polynomial. The three minimal polynomials in step <1>4 are distinct, so no two of $A_1,A_2,A_3$ are similar.
:::

<1>6. Q.E.D.
::: {.proof}
Step <1>2 gives the matrices, step <1>3 gives their characteristic polynomials and verifies the eigenvalue condition, step <1>4 gives their elementary divisors and minimal polynomials, and step <1>5 proves pairwise nonsimilarity.
:::
:::
