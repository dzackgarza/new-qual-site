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

Two $n \times n$ matrices $A$ and $B$ over a field $F$ are said to be similar if there exists an $n \times n$ invertible matrix $T$ over $F$ such that $TAT^{-1} = B$.
Exhibit three $3 \times 3$ matrices over $\mathbb{Q}$ no two of which are similar such that $-2$ is the only rational eigenvalue of each of the matrices.
For each, determine its elementary divisors, minimal polynomial and characteristic polynomial.

::: {.solution}
<1>1. We need three $3 \times 3$ matrices over $\QQ$ with $-2$ as the only rational eigenvalue, pairwise non-similar.
::: {.proof}
restate the goal.
:::

<1>2. Take
$$A_1 = \begin{pmatrix} -2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -2 \end{pmatrix}, \qquad
A_2 = \begin{pmatrix} -2 & 1 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -2 \end{pmatrix}, \qquad
A_3 = \begin{pmatrix} -2 & 1 & 0 \\ 0 & -2 & 1 \\ 0 & 0 & -2 \end{pmatrix}.$$
::: {.proof}
three Jordan forms with eigenvalue $-2$ and Jordan blocks of sizes $(1,1,1)$, $(2,1)$, and $(3)$ respectively.
:::

<1>3. Each has characteristic polynomial $(x + 2)^3$.
::: {.proof}
all eigenvalues are $-2$ with algebraic multiplicity $3$.
:::

<1>4. The minimal polynomials are:
- $A_1$: $x + 2$ (elementary divisors $x+2, x+2, x+2$);
- $A_2$: $(x+2)^2$ (elementary divisors $(x+2)^2, x+2$);
- $A_3$: $(x+2)^3$ (elementary divisor $(x+2)^3$).
::: {.proof}
the minimal polynomial is the product of the elementary divisors (the invariant factors), and the elementary divisors are the $(x+2)^k$ for the Jordan blocks of size $k$.
:::

<1>5. The three matrices are pairwise non-similar.
::: {.proof}
similar matrices have the same elementary divisors (or the same rational canonical form / Jordan form); the three sets of elementary divisors are distinct, so no two are similar.
:::

<1>6. Q.E.D.
::: {.proof}
<1>2–<1>5.
:::
:::
