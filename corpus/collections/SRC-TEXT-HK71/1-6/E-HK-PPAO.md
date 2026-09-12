---
schema: qual/card@1
id: E-HK-PPAO
kind: problem
title: Eigenvectors of a triangular matrix
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
  note: Checked against Hoffman--Kunze Exercise 1.6.4.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
Let

$$
A = \left[ \begin{array}{c c c} 5 & 0 & 0 \\ 1 & 5 & 0 \\ 0 & 1 & 5 \end{array} \right].
$$

For which $X$ does there exist a scalar $c$ such that $AX = cX$ ?
:::


::: solution
Let $X=(x_1,x_2,x_3)^t$. If $X=0$, then $AX=cX$ for every scalar $c$.
Assume $X\ne0$. The equation $AX=cX$ is
\[
(5-c)x_1=0,
\]
\[
x_1+(5-c)x_2=0,
\]
\[
x_2+(5-c)x_3=0.
\]
If $c\ne5$, the first equation gives $x_1=0$, then the second gives $x_2=0$, and the third gives $x_3=0$, contrary to $X\ne0$. Thus $c=5$.

For $c=5$, the second equation gives $x_1=0$ and the third gives $x_2=0$, while $x_3$ is arbitrary. Hence the nonzero solutions are precisely
\[
X=t\begin{bmatrix}0\\0\\1\end{bmatrix},\qquad t\ne0,
\]
with $c=5$. Including the zero vector, the vectors for which some scalar $c$ satisfies $AX=cX$ are exactly the multiples of $(0,0,1)^t$.
:::
