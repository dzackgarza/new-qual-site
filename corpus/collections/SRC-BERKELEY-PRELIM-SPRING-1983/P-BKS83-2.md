---
schema: qual/card@1
id: P-BKS83-2
kind: problem
title: A strictly column-diagonally-dominant $Z$-matrix has positive determinant
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the strict column diagonal dominance, nonsingularity argument, and determinant-sign homotopy to the positive diagonal matrix.
---

::: {.problem}
Let $A=(a_{ij})$ be a real $n\times n$ matrix satisfying
\[
a_{ii}>0,
\qquad
a_{ij}\le0\quad(i\ne j),
\]
and
\[
\sum_{i=1}^n a_{ij}>0
\qquad(1\le j\le n).
\]
Prove that
\[
\det A>0.
\]
:::

::: {.solution}
<1>1. For each column $j$,
$$
a_{jj}
>
\sum_{i\ne j}\abs{a_{ij}}.
$$

::: {.proof}
Since $a_{ij}\le0$ for $i\ne j$,
$$
\sum_{i=1}^n a_{ij}
=
a_{jj}
-
\sum_{i\ne j}\abs{a_{ij}}.
$$
The column-sum hypothesis says that the left-hand side is positive, giving
the stated strict inequality.
:::

<1>2. Any real matrix $M=(m_{ij})$ satisfying
$$
\abs{m_{jj}}
>
\sum_{i\ne j}\abs{m_{ij}}
$$
for every column $j$ is nonsingular.

::: {.proof}
Suppose $M$ were singular. Then $M^T$ would be singular, so there would be
a nonzero vector $x=(x_1,\ldots,x_n)^T$ such that
$$
M^Tx=0.
$$
Choose $k$ with
$$
\abs{x_k}
=
\max_i\abs{x_i}
>0.
$$
The $k$th equation of $M^Tx=0$ is
$$
m_{kk}x_k
+
\sum_{i\ne k}m_{ik}x_i
=0.
$$
Hence
$$
\begin{aligned}
\abs{m_{kk}}\abs{x_k}
&\le
\sum_{i\ne k}\abs{m_{ik}}\abs{x_i}\\
&\le
\left(
\sum_{i\ne k}\abs{m_{ik}}
\right)
\abs{x_k}.
\end{aligned}
$$
Dividing by $\abs{x_k}>0$ contradicts strict column diagonal dominance.
Thus $M$ is nonsingular.
:::

<1>3. Let
$$
D
\coloneqq
\operatorname{diag}(a_{11},\ldots,a_{nn})
$$
and, for $0\le t\le1$, define
$$
A_t
\coloneqq
D+t(A-D).
$$
Then every $A_t$ is nonsingular.

::: {.proof}
The diagonal entries of $A_t$ are $a_{jj}$, while its off-diagonal entries
are $t a_{ij}$. By step <1>1,
$$
a_{jj}
>
\sum_{i\ne j}\abs{a_{ij}}
\ge
t\sum_{i\ne j}\abs{a_{ij}}
=
\sum_{i\ne j}\abs{(A_t)_{ij}}.
$$
Thus $A_t$ is strictly column diagonally dominant for every
$t\in[0,1]$. Step <1>2 implies that every $A_t$ is nonsingular.
:::

<1>4. The function
$$
t\longmapsto\det A_t
$$
has constant sign on $[0,1]$.

::: {.proof}
The determinant is a polynomial in the matrix entries, so
$t\mapsto\det A_t$ is continuous. By step <1>3 it never vanishes on the
connected interval $[0,1]$. A continuous nonzero real-valued function on a
connected set cannot change sign.
:::

<1>5. One has
$$
\boxed{\det A>0}.
$$

::: {.proof}
At $t=0$,
$$
A_0=D,
$$
so
$$
\det A_0
=
\prod_{j=1}^n a_{jj}
>0
$$
because every diagonal entry is positive. By step <1>4,
$\det A_t$ has the same positive sign for all $t\in[0,1]$. Since
$A_1=A$, it follows that
$$
\det A>0.
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the desired conclusion.
:::
:::
