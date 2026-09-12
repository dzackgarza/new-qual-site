---
schema: qual/card@1
id: E-HK-9X41
kind: problem
title: Solutions of $AX = cX$ for eigenvalue equations
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
  note: Checked against Hoffman--Kunze, Section 1.3.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
If

$$
A = \left[ \begin{array}{r r r} 6 & - 4 & 0 \\ 4 & - 2 & 0 \\ - 1 & 0 & 3 \end{array} \right]
$$

find all solutions of AX = 2X and all solutions of AX = 3X. (The symbol cX denotes the matrix each entry of which is c times the corresponding entry of X.)
:::

::: solution
The equation $AX=cX$ is equivalent to
\[
(A-cI)X=0.
\]

<1>1. The solutions of $AX=2X$ are
\[
X=t\begin{bmatrix}1\\1\\1\end{bmatrix},
\qquad t\in F.
\]
::: proof
For $c=2$,
\[
A-2I=
\begin{bmatrix}
4&-4&0\\
4&-4&0\\
-1&0&1
\end{bmatrix}
\sim
\begin{bmatrix}
1&0&-1\\
0&1&-1\\
0&0&0
\end{bmatrix}.
\]
Hence $x_1=x_3$ and $x_2=x_3$, giving the stated one-dimensional solution
space.
:::

<1>2. The solutions of $AX=3X$ are
\[
X=t\begin{bmatrix}0\\0\\1\end{bmatrix},
\qquad t\in F.
\]
::: proof
For $c=3$,
\[
A-3I=
\begin{bmatrix}
3&-4&0\\
4&-5&0\\
-1&0&0
\end{bmatrix}
\sim
\begin{bmatrix}
1&0&0\\
0&1&0\\
0&0&0
\end{bmatrix}.
\]
Thus $x_1=x_2=0$ and $x_3$ is arbitrary.
:::
:::
