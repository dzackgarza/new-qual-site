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
$$
F(x)=\det\begin{pmatrix}
1&1&1&1&1\\
1&x&x^2&x^3&x^4\\
x&1&x&x^2&x^3\\
x^2&x&1&x&x^2\\
x^3&x^2&x&1&x
\end{pmatrix}.
$$
Compute $F'(0)$.
:::

::: {.solution}

Let the rows of the matrix defining $F(x)$ be
$$
R_1(x),\ldots,R_5(x).
$$

::: pf

::: pf-step

At $x=0$,
$$
\begin{aligned}
R_1(0)&=(1,1,1,1,1),\\
R_2(0)&=(1,0,0,0,0),\\
R_3(0)&=(0,1,0,0,0),\\
R_4(0)&=(0,0,1,0,0),\\
R_5(0)&=(0,0,0,1,0).
\end{aligned}
$$


::: pf-proof

Substitute $x=0$ into each row.

:::

:::

::: pf-step

The row derivatives at $x=0$ are
$$
\begin{aligned}
R_1'(0)&=(0,0,0,0,0),\\
R_2'(0)&=(0,1,0,0,0),\\
R_3'(0)&=(1,0,1,0,0),\\
R_4'(0)&=(0,1,0,1,0),\\
R_5'(0)&=(0,0,1,0,1).
\end{aligned}
$$


::: pf-proof

Differentiate each polynomial entry and then substitute $x=0$.

:::

:::

::: {.pf-step #s1-3}

By multilinearity of the determinant,
$$
F'(0)
=
\sum_{j=1}^5 D_j,
$$
where $D_j$ is the determinant obtained from the matrix at $x=0$ by replacing its $j$th row by $R_j'(0)$.


::: pf-proof

For differentiable row vectors,
$$
\frac d{dx}
\det(R_1(x),\ldots,R_5(x))
$$
is the sum of the five determinants obtained by differentiating exactly one row at a time.
Evaluate at $x=0$.

:::

:::

::: {.pf-step #s1-4}

One has
$$
D_1=0.
$$


::: pf-proof

The first row in $D_1$ is
$$
R_1'(0)=0,
$$
so the determinant vanishes.

:::

:::

::: {.pf-step #s1-5}

One has
$$
D_2=0.
$$


::: pf-proof

In $D_2$, the second row is
$$
R_2'(0)
=(0,1,0,0,0),
$$
which equals
$$
R_3(0).
$$
Thus the matrix has two equal rows and determinant zero.

:::

:::

::: {.pf-step #s1-6}

One has
$$
D_3=0.
$$


::: pf-proof

The replacement row
$$
R_3'(0)
=(1,0,1,0,0)
$$
is
$$
R_2(0)+R_4(0).
$$
By linearity of the determinant in the third row,
$$
D_3
$$
is the sum of two determinants.
In the first, the third row equals $R_2(0)$; in the second, it equals $R_4(0)$.
Each determinant therefore has two equal rows and vanishes.

:::

:::

::: {.pf-step #s1-7}

One has
$$
D_4=0.
$$


::: pf-proof

The replacement row is
$$
R_4'(0)
=(0,1,0,1,0)
=
R_3(0)+R_5(0).
$$
By linearity in the fourth row,
$$
D_4
$$
splits into two determinants, each with a repeated row.
Hence both vanish.

:::

:::

::: {.pf-step #s1-8}

One has
$$
\boxed{D_5=-1}.
$$


::: pf-proof

The matrix defining $D_5$ is
$$
\begin{pmatrix}
1&1&1&1&1\\
1&0&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&1&0&1
\end{pmatrix}.
$$
Subtract the fourth row from the fifth:
$$
R_5\longleftarrow R_5-R_4.
$$
This does not change the determinant and gives
$$
\begin{pmatrix}
1&1&1&1&1\\
1&0&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&0&1
\end{pmatrix}.
$$
Expanding along the fifth row reduces the determinant to
$$
\det
\begin{pmatrix}
1&1&1&1\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{pmatrix}.
$$
Expanding this determinant along its fourth column leaves the $3\times3$ identity with cofactor sign
$$
(-1)^{1+4}=-1.
$$
Thus
$$
D_5=-1.
$$

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\boxed{F'(0)=-1}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
F'(0)
=
D_1+D_2+D_3+D_4+D_5.
$$
Steps [](#s1-4){.pf-ref} through [](#s1-8){.pf-ref} give
$$
F'(0)=0+0+0+0-1=-1.
$$

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required value.

:::

:::

:::
