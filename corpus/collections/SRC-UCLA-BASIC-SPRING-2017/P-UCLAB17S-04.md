---
schema: qual/card@1
id: P-UCLAB17S-04
kind: problem
title: Derivative at zero of a $5\times5$ determinant with monomial entries
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2017, `assets/attachments/basic-17S.pdf`.
---

::: {.problem}
Define
\[
F(x)=\det\begin{pmatrix}
1&1&1&1&1\\
1&x&x^2&x^3&x^4\\
x&1&x&x^2&x^3\\
x^2&x&1&x&x^2\\
x^3&x^2&x&1&x
\end{pmatrix}.
\]
Compute $F'(0)$.
:::

::: {.solution}
Let the rows of the matrix defining $F(x)$ be
\[
R_1(x),\ldots,R_5(x).
\]

<1>1. At $x=0$,
\[
\begin{aligned}
R_1(0)&=(1,1,1,1,1),\\
R_2(0)&=(1,0,0,0,0),\\
R_3(0)&=(0,1,0,0,0),\\
R_4(0)&=(0,0,1,0,0),\\
R_5(0)&=(0,0,0,1,0).
\end{aligned}
\]

::: {.proof}
Substitute $x=0$ into each row.
:::

<1>2. The row derivatives at $x=0$ are
\[
\begin{aligned}
R_1'(0)&=(0,0,0,0,0),\\
R_2'(0)&=(0,1,0,0,0),\\
R_3'(0)&=(1,0,1,0,0),\\
R_4'(0)&=(0,1,0,1,0),\\
R_5'(0)&=(0,0,1,0,1).
\end{aligned}
\]

::: {.proof}
Differentiate each polynomial entry and then substitute $x=0$.
:::

<1>3. By multilinearity of the determinant,
\[
F'(0)
=
\sum_{j=1}^5 D_j,
\]
where $D_j$ is the determinant obtained from the matrix at $x=0$ by replacing its $j$th row by $R_j'(0)$.

::: {.proof}
For differentiable row vectors,
\[
\frac d{dx}
\det(R_1(x),\ldots,R_5(x))
\]
is the sum of the five determinants obtained by differentiating exactly one row at a time.
Evaluate at $x=0$.
:::

<1>4. One has
\[
D_1=0.
\]

::: {.proof}
The first row in $D_1$ is
\[
R_1'(0)=0,
\]
so the determinant vanishes.
:::

<1>5. One has
\[
D_2=0.
\]

::: {.proof}
In $D_2$, the second row is
\[
R_2'(0)
=(0,1,0,0,0),
\]
which equals
\[
R_3(0).
\]
Thus the matrix has two equal rows and determinant zero.
:::

<1>6. One has
\[
D_3=0.
\]

::: {.proof}
The replacement row
\[
R_3'(0)
=(1,0,1,0,0)
\]
is
\[
R_2(0)+R_4(0).
\]
By linearity of the determinant in the third row,
\[
D_3
\]
is the sum of two determinants.
In the first, the third row equals $R_2(0)$; in the second, it equals $R_4(0)$.
Each determinant therefore has two equal rows and vanishes.
:::

<1>7. One has
\[
D_4=0.
\]

::: {.proof}
The replacement row is
\[
R_4'(0)
=(0,1,0,1,0)
=
R_3(0)+R_5(0).
\]
By linearity in the fourth row,
\[
D_4
\]
splits into two determinants, each with a repeated row.
Hence both vanish.
:::

<1>8. One has
\[
\boxed{D_5=-1}.
\]

::: {.proof}
The matrix defining $D_5$ is
\[
\begin{pmatrix}
1&1&1&1&1\\
1&0&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&1&0&1
\end{pmatrix}.
\]
Subtract the fourth row from the fifth:
\[
R_5\longleftarrow R_5-R_4.
\]
This does not change the determinant and gives
\[
\begin{pmatrix}
1&1&1&1&1\\
1&0&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&0&1
\end{pmatrix}.
\]
Expanding along the fifth row reduces the determinant to
\[
\det
\begin{pmatrix}
1&1&1&1\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{pmatrix}.
\]
Expanding this determinant along its fourth column leaves the $3\times3$ identity with cofactor sign
\[
(-1)^{1+4}=-1.
\]
Thus
\[
D_5=-1.
\]
:::

<1>9. Therefore
\[
\boxed{F'(0)=-1}.
\]

::: {.proof}
By step <1>3,
\[
F'(0)
=
D_1+D_2+D_3+D_4+D_5.
\]
Steps <1>4--<1>8 give
\[
F'(0)=0+0+0+0-1=-1.
\]
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the required value.
:::
:::
