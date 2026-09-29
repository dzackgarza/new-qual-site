---
schema: qual/card@1
id: P-PRACT20-W4-16
kind: problem
title: Rank of the $n\times n$ matrix with entries $1,\dots,n^2$
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Matrices
  - Rank and Nullity
relations: []
review: draft
---

::: {.problem}
Find the rank of the $n \times n$ matrix with entries which simply count up from 1 to $n ^ { 2 }$ in increasing order.
For example, if $n = 3$ , we are considering the matrix $\left( \begin{array} { l l l } { 1 } & { 2 } & { 3 } \\ { 4 } & { 5 } & { 6 } \\ { 7 } & { 8 } & { 9 } \end{array} \right)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $n=1$, the matrix has rank $1$.

::: pf-proof

The matrix is $(1)$.

:::

:::

::: {.pf-step #s2}

If $n\ge2$, every row lies in the span of the first two rows.

::: pf-proof

Let $A=(A_{ij})$, so
$$
A_{ij}=(i-1)n+j.
$$
For $i>2$ and every $j$,
$$
\begin{aligned}
A_{ij}
&=(i-1)n+j\\
&=(i-1)(n+j)-(i-2)j\\
&=(i-1)A_{2j}-(i-2)A_{1j}.
\end{aligned}
$$
Hence
$$
R_i=(i-1)R_2-(i-2)R_1,
$$
where $R_i$ denotes the $i$th row. Thus $\operatorname{rank}A\le2$.

:::

:::

::: {.pf-step #s3}

If $n\ge2$, the first two rows are linearly independent.

::: pf-proof

Their first two coordinates form the minor
$$
\begin{pmatrix}
1&2\\
n+1&n+2
\end{pmatrix},
$$
whose determinant is
$$
(n+2)-2(n+1)=-n\ne0.
$$
Therefore $\operatorname{rank}A\ge2$.

:::

:::

::: {.pf-step #s4}

The rank is
$$
\boxed{
\operatorname{rank}A=
\begin{cases}
1,&n=1,\\
2,&n\ge2.
\end{cases}
}
$$

::: pf-proof

Combine steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the rank for every positive integer $n$.

:::

:::

:::
