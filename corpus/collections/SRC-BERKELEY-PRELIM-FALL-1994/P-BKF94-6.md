---
schema: qual/card@1
id: P-BKF94-6
kind: problem
title: Invertibility from diagonal lower bounds and small off-diagonal norm
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Split A into diagonal and off-diagonal parts; the diagonal part expands
    Euclidean norm by at least one, while the off-diagonal Frobenius bound
    makes its operator norm strictly less than one.
---

::: {.problem}
Let $A=(a_{ij})$ be a real $n\times n$ matrix with $a_{ii}\ge1$ for every $i$ and
\[
\sum_{i\ne j}a_{ij}^2<1.
\]
Prove that $A$ is invertible.
:::

::: {.solution}
Write
$$
A=D+E,
$$
where
$$
D=\operatorname{diag}(a_{11},\ldots,a_{nn})
$$
and $E$ has entries
$$
e_{ij}
=
\begin{cases}
a_{ij},&i\neq j,\\
0,&i=j.
\end{cases}
$$

<1>1. For every $x\in\RR^n$,
$$
\norm{Dx}\geq\norm{x}.
$$

::: {.proof}
Since $a_{ii}\geq1$,
$$
\norm{Dx}^2
=
\sum_{i=1}^n a_{ii}^2x_i^2
\geq
\sum_{i=1}^n x_i^2
=
\norm{x}^2.
$$
Taking square roots gives the claim.
:::

<1>2. For every $x\in\RR^n$,
$$
\norm{Ex}^2
\leq
\left(
\sum_{i\neq j}a_{ij}^2
\right)
\norm{x}^2.
$$

::: {.proof}
For each row $i$, Cauchy--Schwarz gives
$$
\left(
\sum_{j\neq i}a_{ij}x_j
\right)^2
\leq
\left(
\sum_{j\neq i}a_{ij}^2
\right)
\left(
\sum_{j\neq i}x_j^2
\right)
\leq
\left(
\sum_{j\neq i}a_{ij}^2
\right)
\norm{x}^2.
$$
Summing over $i$ yields the displayed inequality.
:::

<1>3. If $x\neq0$, then
$$
\norm{Ex}<\norm{x}.
$$

::: {.proof}
The hypothesis says
$$
\sum_{i\neq j}a_{ij}^2<1.
$$
Combine this with step <1>2 and take square roots.
:::

<1>4. The kernel of $A$ is trivial.

::: {.proof}
Suppose
$$
Ax=0.
$$
Then
$$
Dx=-Ex.
$$
If $x\neq0$, steps <1>1 and <1>3 give
$$
\norm{x}
\leq
\norm{Dx}
=
\norm{Ex}
<
\norm{x},
$$
a contradiction. Hence $x=0$.
:::

<1>5. The matrix $A$ is invertible.

::: {.proof}
Step <1>4 shows that the linear map
$$
A:\RR^n\longrightarrow\RR^n
$$
is injective. An injective linear endomorphism of a finite-dimensional
vector space is bijective, hence $A$ is invertible.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
