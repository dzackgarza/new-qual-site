---
schema: qual/card@1
id: P-BKF84-7
kind: problem
title: The Vandermonde determinant
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 of the deterministic MinerU Flash extraction of the Berkeley Fall 1984 preliminary exam.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Checked the induction in the last variable, including the roots, leading coefficient, and sign of the Vandermonde product.
---

::: {.problem}
Let $A$ be the $n\times n$ matrix whose $i$-th row is
\[
(1,x_i,x_i^2,\ldots,x_i^{n-1}).
\]
Show that
\[
\det A=\prod_{i>j}(x_i-x_j).
\]
:::

::: {.solution}
<1>1. The formula holds for $n=1$.

::: {.proof}
Then
$$
A=(1),
$$
so $\det A=1$, while the product over pairs $i>j$ is empty and hence
also equals $1$.
:::

<1>2. Assume the formula holds for size $n-1$. Regard
$$
D_n(x_1,\ldots,x_n)
\coloneqq
\det
\begin{pmatrix}
1&x_1&\cdots&x_1^{n-1}\\
\vdots&\vdots&&\vdots\\
1&x_n&\cdots&x_n^{n-1}
\end{pmatrix}
$$
as a polynomial in $x_n$. Then each
$$
x_n-x_j,
\qquad
1\leq j<n,
$$
divides $D_n$.

::: {.proof}
If $x_n=x_j$ for some $j<n$, then the $n$-th row equals the $j$-th
row, so the determinant vanishes. Hence $x_j$ is a root of the
polynomial $D_n$ in the variable $x_n$, and the factor theorem gives
the stated divisibility.
:::

<1>3. The coefficient of $x_n^{n-1}$ in $D_n$ is
$$
D_{n-1}(x_1,\ldots,x_{n-1}).
$$

::: {.proof}
Only the last entry of the last row contains the power $x_n^{n-1}$.
Expanding the determinant along the last row, its cofactor has sign
$$
(-1)^{n+n}=1
$$
and is exactly the $(n-1)\times(n-1)$ Vandermonde determinant
$$
D_{n-1}(x_1,\ldots,x_{n-1}).
$$
:::

<1>4. Therefore
$$
D_n
=
D_{n-1}(x_1,\ldots,x_{n-1})
\prod_{j=1}^{n-1}(x_n-x_j).
$$

::: {.proof}
As a polynomial in $x_n$, the determinant has degree at most $n-1$.
By step <1>2 it is divisible by the monic polynomial
$$
\prod_{j=1}^{n-1}(x_n-x_j),
$$
which already has degree $n-1$. Thus the quotient is independent of
$x_n$. Step <1>3 identifies that quotient with the leading coefficient
$D_{n-1}$.
:::

<1>5. One has
$$
\boxed{
\det A
=
\prod_{i>j}(x_i-x_j)
}.
$$

::: {.proof}
By the induction hypothesis,
$$
D_{n-1}
=
\prod_{n-1\geq i>j}(x_i-x_j).
$$
Insert this into step <1>4:
$$
\begin{aligned}
D_n
&=
\left(
\prod_{n-1\geq i>j}(x_i-x_j)
\right)
\left(
\prod_{j=1}^{n-1}(x_n-x_j)
\right)\\
&=
\prod_{n\geq i>j}(x_i-x_j).
\end{aligned}
$$
Together with step <1>1, induction proves the formula for every $n$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required determinant identity.
:::
:::
