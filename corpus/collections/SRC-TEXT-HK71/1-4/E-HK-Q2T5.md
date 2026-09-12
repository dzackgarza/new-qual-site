---
schema: qual/card@1
id: E-HK-Q2T5
kind: problem
title: Solving a homogeneous system by row reduction
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the four equations with Hoffman--Kunze 1.4.1 and retained the requested row-reduction method."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the exact row operations, reduced matrix and one-parameter solution by substitution into all four original equations."
---

::: {.exercise}
Find all solutions to the following system of equations by row-reducing the coefficient matrix:

$$
\begin{array}{r l} \frac {1}{3} x _ {1} + 2 x _ {2} - 6 x _ {3} & = 0 \\ - 4 x _ {1} + 5 x _ {3} & = 0 \\ - 3 x _ {1} + 6 x _ {2} - 1 3 x _ {3} & = 0 \\ - \frac {7}{3} x _ {1} + 2 x _ {2} - \frac {8}{3} x _ {3} & = 0 \end{array}
$$
:::

::: solution
The complete solution set is
$$
\boxed{
(x_1,x_2,x_3)
=t\left(\frac54,\frac{67}{24},1\right),
\qquad t\in\mathbb C.}
$$

<1>1. Row-reduce the coefficient matrix.
::: proof
The coefficient matrix is
$$
A=
\begin{pmatrix}
1/3&2&-6\\
-4&0&5\\
-3&6&-13\\
-7/3&2&-8/3
\end{pmatrix}.
$$
First replace $R_1$ by $3R_1$. Then apply
$$
R_2\leftarrow R_2+4R_1,
\qquad
R_3\leftarrow R_3+3R_1,
\qquad
R_4\leftarrow R_4+\frac73R_1.
$$
This gives
$$
\begin{pmatrix}
1&6&-18\\
0&24&-67\\
0&24&-67\\
0&16&-134/3
\end{pmatrix}.
$$
Replace $R_2$ by $R_2/24$, then use
$$
R_1\leftarrow R_1-6R_2,
\qquad
R_3\leftarrow R_3-24R_2,
\qquad
R_4\leftarrow R_4-16R_2.
$$
The row-reduced matrix is
$$
\begin{pmatrix}
1&0&-5/4\\
0&1&-67/24\\
0&0&0\\
0&0&0
\end{pmatrix}.
$$
Elementary row operations preserve the solution set of a homogeneous system
[@HK71].
:::

<1>2. Read off the solutions.
::: proof
The reduced equations are
$$
x_1-\frac54x_3=0,
\qquad
x_2-\frac{67}{24}x_3=0.
$$
Thus $x_3=t$ is free and
$$
x_1=\frac54t,
\qquad
x_2=\frac{67}{24}t.
$$
Conversely every such triple satisfies the reduced system, hence also the
original system. Therefore the displayed family is exhaustive.
:::
:::
