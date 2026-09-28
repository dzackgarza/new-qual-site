---
schema: qual/card@1
id: P-BERK86S-08
kind: problem
title: Count the points in the unit disk where a polynomial matrix is singular
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The extraction garbles the matrix size, but the displayed source matrix is 3-by-3.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Computed det A(z)=8z^4+6z^2+1=(4z^2+1)(2z^2+1) and checked all four
    distinct roots lie strictly inside the unit disk.
---

::: {.problem}
Let
\[
A(z)=\begin{pmatrix}
4z^2&1&-1\\
-1&2z^2&0\\
3&0&1
\end{pmatrix}.
\]
How many distinct values $z$ satisfy
\[
|z|<1
\]
and make $A(z)$ noninvertible?
:::

::: {.solution}
<1>1. The determinant of $A(z)$ is
$$
\det A(z)
=
8z^4+6z^2+1.
$$

::: {.proof}
Expanding along the first row gives
$$
\begin{aligned}
\det A(z)
&=
4z^2
\begin{vmatrix}
2z^2&0\\
0&1
\end{vmatrix}
-
\begin{vmatrix}
-1&0\\
3&1
\end{vmatrix}
-
\begin{vmatrix}
-1&2z^2\\
3&0
\end{vmatrix}\\
&=
8z^4+1+6z^2.
\end{aligned}
$$
:::

<1>2. The determinant factors as
$$
\det A(z)
=
(4z^2+1)(2z^2+1).
$$

::: {.proof}
Direct multiplication gives
$$
(4z^2+1)(2z^2+1)
=
8z^4+6z^2+1.
$$
:::

<1>3. The matrix $A(z)$ is noninvertible exactly for
$$
z
\in
\left\{
\frac{i}{2},
-\frac{i}{2},
\frac{i}{\sqrt2},
-\frac{i}{\sqrt2}
\right\}.
$$

::: {.proof}
A square matrix over $\CC$ is noninvertible exactly when its determinant
is zero. By step <1>2,
$$
\det A(z)=0
$$
if and only if
$$
z^2=-\frac14
\qquad\text{or}\qquad
z^2=-\frac12,
$$
which gives the four displayed values.
:::

<1>4. All four values from step <1>3 lie in the open unit disk and are
distinct.

::: {.proof}
Their absolute values are respectively
$$
\frac12
\qquad\text{and}\qquad
\frac1{\sqrt2},
$$
both strictly less than $1$. The two absolute values are different, and
within each pair the two roots are negatives of one another and nonzero,
so all four roots are distinct.
:::

<1>5. Therefore the requested number of values is
$$
\boxed{4}.
$$

::: {.proof}
Steps <1>3 and <1>4 identify exactly four distinct points in
$\abs{z}<1$ at which $A(z)$ is noninvertible.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required count.
:::
:::
