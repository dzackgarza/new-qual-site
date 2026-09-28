---
schema: qual/card@1
id: P-BKF80-9
kind: problem
title: Distance from $\operatorname{diag}(1,2)$ to the singular two-by-two matrices
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction mangles the displayed generic matrix and the layout of A, but preserves the four coordinates x,y,z,t and the diagonal entries 1,2 of A. It also prints ||X||=x^2+y^2+z^2+t^2 while calling d(X,Y)=||X-Y|| a metric; this may have lost either a square root or a square on the norm symbol. The printed formula is preserved rather than silently repaired.
---

::: {.problem}
For
$$
X=\begin{pmatrix}x&y\\z&t\end{pmatrix},
$$
define
$$
\|X\|=x^2+y^2+z^2+t^2,
\qquad
d(X,Y)=\|X-Y\|.
$$
Let
$$
\Sigma=\{X:\det X=0\},
\qquad
A=\begin{pmatrix}1&0\\0&2\end{pmatrix}.
$$
Find the minimum distance from $A$ to $\Sigma$, and exhibit a matrix $S\in\Sigma$ attaining the minimum.
:::

::: {.solution}
For a real $2\times2$ matrix $B=(b_{ij})$, write
$$
\norm{B}_F^2\coloneqq\sum_{i,j}b_{ij}^2.
$$
With the convention printed in the problem,
$$
d(A,X)=\norm{A-X}_F^2.
$$

<1>1. For every real $2\times2$ matrix $B$ and every unit vector $u\in\RR^2$,
$$
\norm{Bu}_2^2\leq\norm{B}_F^2.
$$

::: {.proof}
Let $r_1,r_2\in\RR^2$ be the two rows of $B$. By Cauchy--Schwarz,
$$
\norm{Bu}_2^2
=\abs{r_1\cdot u}^2+\abs{r_2\cdot u}^2
\leq\norm{r_1}_2^2\norm{u}_2^2+\norm{r_2}_2^2\norm{u}_2^2.
$$
Since $\norm u_2=1$, the right-hand side is $\norm B_F^2$.
:::

<1>2. Every $X\in\Sigma$ satisfies
$$
d(A,X)\geq1.
$$

::: {.proof}
Since $X$ is singular, choose a unit vector
$$
u=\begin{pmatrix}p\\q\end{pmatrix}\in\ker X.
$$
Apply step <1>1 to $B=A-X$. Since $Xu=0$,
$$
d(A,X)
=\norm{A-X}_F^2
\geq\norm{(A-X)u}_2^2
=\norm{Au}_2^2.
$$
But
$$
\norm{Au}_2^2
=p^2+4q^2
\geq p^2+q^2
=1.
$$
Hence $d(A,X)\geq1$.
:::

<1>3. The minimum distance is $\boxed{1}$, attained by
$$
\boxed{S=\begin{pmatrix}0&0\\0&2\end{pmatrix}}.
$$

::: {.proof}
The matrix $S$ is singular. Moreover,
$$
A-S=\begin{pmatrix}1&0\\0&0\end{pmatrix},
$$
so the printed distance convention gives
$$
d(A,S)=\norm{A-S}_F^2=1.
$$
Together with the lower bound in step <1>2, this proves that the minimum is $1$ and that $S$ attains it.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives both requested conclusions.
:::
:::

::: {.remark}
With $\|X\|$ the sum of the squared entries, $d(X,Y)=\norm{X-Y}_F^2$ is the square of the Frobenius distance and does not satisfy the triangle inequality. For the Frobenius distance $\norm{X-Y}_F$ itself, the minimum distance from $A$ to $\Sigma$ is also $1$, attained at the same $S$.
:::
