---
schema: qual/card@1
id: E-HK-0YG3
kind: problem
title: Row-reduced echelon form is unique given the solution set
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hoffman--Kunze, Section 1.4.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
Suppose R and $R'$ are $2 \times 3$ row-reduced echelon matrices and that the systems RX = 0 and $R'X = 0$ have exactly the same solutions.
Prove that $R = R'$ .
:::

::: solution
Let
\[
N=\{X\in F^3:RX=0\}=\{X\in F^3:R'X=0\}.
\]
We show that a $2\times3$ row-reduced echelon matrix is uniquely determined by
$N$.

<1>1. If $\dim N=3$, then $R=R'=0$.
::: proof
Rank-nullity gives $\operatorname{rank}R=\operatorname{rank}R'=0$.
:::

<1>2. If $\dim N=2$, then $R=R'$.
::: proof
Both matrices have rank $1$. Their row spaces are the one-dimensional
annihilator
\[
N^\perp=\{w\in F^3:wX=0\text{ for all }X\in N\}.
\]
A one-dimensional row space has a unique row-reduced generator: take any
nonzero $w\in N^\perp$, divide by its first nonzero coordinate, and place that
normalized vector in the first row, with zero second row. Thus both RREF
matrices coincide.
:::

<1>3. If $\dim N=1$, then $R=R'$.
::: proof
Write $N=Fv$ with $v=(v_1,v_2,v_3)^t\ne0$. Both matrices have rank $2$.

If $v_3\ne0$, the free variable in the reduced system is $x_3$, and
\[
x_1=-\frac{v_1}{v_3}x_3,
\qquad
x_2=-\frac{v_2}{v_3}x_3.
\]
Hence the unique RREF is
\[
\begin{bmatrix}
1&0&-v_1/v_3\\
0&1&-v_2/v_3
\end{bmatrix}.
\]

If $v_3=0$ but $v_2\ne0$, the free variable is $x_2$ and $x_3=0$, so the
unique RREF is
\[
\begin{bmatrix}
1&-v_1/v_2&0\\
0&0&1
\end{bmatrix}.
\]

Finally, if $v_2=v_3=0$, then $v_1\ne0$, so the nullspace is the $x_1$-axis
and the unique RREF is
\[
\begin{bmatrix}
0&1&0\\
0&0&1
\end{bmatrix}.
\]
Thus in every rank-$2$ case the common nullspace determines the matrix.
:::

<1>4. Therefore $R=R'$.
::: proof
The possibilities in <1>1--<1>3 exhaust all dimensions of the nullspace of a
$2\times3$ matrix.
:::
:::
