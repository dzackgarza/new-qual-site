---
schema: qual/card@1
id: P-BKF11-8A
kind: problem
title: Nonsingularity of matrices with positive off-diagonal entries and negative row sums
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 8A of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the induction after column elimination, including preservation of
    positive off-diagonal entries and strictly negative row sums.
---

::: {.problem}
Let $A$ be an $n\times n$ real matrix such that every off-diagonal entry is positive and the sum of the entries in each row is negative.
Show that $\det A\ne0$.
:::

::: {.solution}
Write $A=(a_{ij})$.

<1>1. Every diagonal entry of $A$ is strictly negative.

::: {.proof}
For each row $i$, all off-diagonal entries are positive, while
$$
a_{ii}+\sum_{j\ne i}a_{ij}<0.
$$
Hence
$$
a_{ii}< -\sum_{j\ne i}a_{ij}<0.
$$
:::

<1>2. Suppose $n\ge2$. For each $j=2,\ldots,n$, put
$$
t_j\coloneqq-\frac{a_{1j}}{a_{11}}>0
$$
and perform the column operation
$$
C_j\longmapsto C_j+t_jC_1.
$$
The resulting matrix has the block form
$$
\widetilde A=
\begin{pmatrix}
a_{11}&0\\
*&B
\end{pmatrix},
$$
where $B$ is an $(n-1)\times(n-1)$ real matrix.

::: {.proof}
Step <1>1 gives $a_{11}<0$, while $a_{1j}>0$ for $j>1$, so
$t_j>0$. The first-row entry in transformed column $j$ is
$$
a_{1j}+t_ja_{11}
=a_{1j}-\frac{a_{1j}}{a_{11}}a_{11}
=0.
$$
Column $1$ is unchanged, which gives the displayed block form.
:::

<1>3. Every off-diagonal entry of $B$ is positive.

::: {.proof}
For $i,j>1$, the corresponding entry of $B$ is
$$
b_{ij}=a_{ij}+t_ja_{i1}.
$$
If $i\ne j$, then both $a_{ij}$ and $a_{i1}$ are positive, and
$t_j>0$ by step <1>2. Therefore $b_{ij}>0$.
:::

<1>4. The sum of the entries in each row of $B$ is strictly negative.

::: {.proof}
Put
$$
T\coloneqq\sum_{j=2}^n t_j
=-\frac{\sum_{j=2}^n a_{1j}}{a_{11}}.
$$
The first row of $A$ has negative sum, so
$$
a_{11}+\sum_{j=2}^n a_{1j}<0.
$$
Since $a_{11}<0$, this implies
$$
0<T<1.
$$

For a row $i>1$, the sum of the corresponding row of $B$ is
$$
\begin{aligned}
\sum_{j=2}^n b_{ij}
&=\sum_{j=2}^n(a_{ij}+t_ja_{i1})\\
&=\sum_{j=1}^n a_{ij}-a_{i1}+Ta_{i1}\\
&=\sum_{j=1}^n a_{ij}-(1-T)a_{i1}.
\end{aligned}
$$
The first term is negative by hypothesis, while
$(1-T)a_{i1}>0$. Hence the row sum of $B$ is strictly negative.
:::

<1>5. For every $n\ge1$, every matrix satisfying the hypotheses has
nonzero determinant.

::: {.proof}
Proceed by induction on $n$. If $n=1$, the unique row sum is the
single entry $a_{11}<0$, so the determinant is nonzero.

Assume the result for size $n-1$ and let $A$ have size $n\ge2$.
Column additions do not change determinant, so
$$
\det A=\det\widetilde A.
$$
By steps <1>3 and <1>4, the matrix $B$ satisfies the same hypotheses
as the original problem. Hence the induction hypothesis gives
$$
\det B\ne0.
$$
Using the block form from step <1>2,
$$
\det A
=a_{11}\det B.
$$
Step <1>1 gives $a_{11}\ne0$, so $\det A\ne0$.
:::

<1>6. Therefore
$$
\boxed{\det A\ne0}.
$$

::: {.proof}
This is the conclusion of step <1>5 for the given matrix $A$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is exactly the required statement.
:::
:::
