---
schema: qual/card@1
id: P-HM21B18-FIN-05
kind: problem
title: Least-squares fit for a two-parameter rational-expression model
classification: {areas: [applied-algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Using least squares, find $a,b$ such that
$$
\frac{ax}{3y}-b=2
$$
best fits the data
$$
(x,y)=(9,3),(6,1),(-3,1),(0,1).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The four observations give the least-squares system
$$
M
\begin{pmatrix}a\\b\end{pmatrix}
\approx
\begin{pmatrix}2\\2\\2\\2\end{pmatrix},
\qquad
M=
\begin{pmatrix}
1&-1\\
2&-1\\
-1&-1\\
0&-1
\end{pmatrix}.
$$


::: pf-proof

For each data point, the coefficient of $a$ is $x/(3y)$ and the
coefficient of $b$ is $-1$. The four values of $x/(3y)$ are
$1,2,-1,0$, respectively, which gives the displayed matrix.

:::

:::

::: {.pf-step #s1-2}

The normal equations are
$$
\begin{pmatrix}
6&-2\\
-2&4
\end{pmatrix}
\begin{pmatrix}a\\b\end{pmatrix}
=
\begin{pmatrix}4\\-8\end{pmatrix}.
$$


::: pf-proof

From step [](#s1-1){.pf-ref},
$$
M^TM=
\begin{pmatrix}
1^2+2^2+(-1)^2&-1-2+1\\
-1-2+1&4
\end{pmatrix}
=
\begin{pmatrix}
6&-2\\
-2&4
\end{pmatrix},
$$
and
$$
M^T
\begin{pmatrix}2\\2\\2\\2\end{pmatrix}
=
\begin{pmatrix}
2(1+2-1+0)\\
-2(1+1+1+1)
\end{pmatrix}
=
\begin{pmatrix}4\\-8\end{pmatrix}.
$$

:::

:::

::: {.pf-step #s1-3}

The unique least-squares parameters are
$$
\boxed{a=0,\qquad b=-2}.
$$


::: pf-proof

Substitution into the normal equations of step [](#s1-2){.pf-ref} gives
$$
\begin{pmatrix}
6&-2\\
-2&4
\end{pmatrix}
\begin{pmatrix}0\\-2\end{pmatrix}
=
\begin{pmatrix}4\\-8\end{pmatrix}.
$$
The determinant of the normal-equation matrix is
$24-4=20\neq0$, so this solution is unique. In fact,
$M(0,-2)^T=(2,2,2,2)^T$, so the residual is zero.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required least-squares fit.

:::

:::

:::
