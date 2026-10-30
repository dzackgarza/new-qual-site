---
schema: qual/card@1
id: P-BLAR-03
kind: problem
title: Compute four determinants
classification:
  areas: [prelim]
  topics:
  - Determinants
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Review Problem 3 in the deterministic MinerU Flash extraction assets/attachments/Basic_Linear_Algebra_Review_extracted.md.
---

::: {.problem}
Find the determinant of each matrix:
$$
\text{(a)}\quad
\begin{bmatrix}5&2\\3&1\end{bmatrix},
\qquad
\text{(b)}\quad
\begin{bmatrix}6&1&3\\0&3&3\\0&0&-3\end{bmatrix},
$$
$$
\text{(c)}\quad
\begin{bmatrix}2&0&4\\1&3&-2\\3&3&2\end{bmatrix},
\qquad
\text{(d)}\quad
\begin{bmatrix}2&3&-2\\1&0&1\\4&1&2\end{bmatrix}.
$$
:::

::: {.solution}
For the matrices in parts (a)--(d), write $A,B,C,D$, respectively.

::: pf

::: pf-step
$\det A=\boxed{-1}$.

::: pf-proof
By the $2\times2$ determinant formula,
$$
\det A=5\cdot1-2\cdot3=-1.
$$
:::

:::

::: pf-step
$\det B=\boxed{-54}$.

::: pf-proof
The matrix $B$ is upper triangular, so its determinant is the product of its diagonal entries:
$$
\det B=6\cdot3\cdot(-3)=-54.
$$
:::

:::

::: pf-step
$\det C=\boxed{0}$.

::: pf-proof
Expanding along the first row gives
$$
\begin{aligned}
\det C
&=2\det\begin{bmatrix}3&-2\\3&2\end{bmatrix}
  +4\det\begin{bmatrix}1&3\\3&3\end{bmatrix}\\
&=2(6+6)+4(3-9)\\
&=24-24=0.
\end{aligned}
$$
:::

:::

::: pf-step
$\det D=\boxed{2}$.

::: pf-proof
Expanding along the second row gives
$$
\begin{aligned}
\det D
&=-\det\begin{bmatrix}3&-2\\1&2\end{bmatrix}
  -\det\begin{bmatrix}2&3\\4&1\end{bmatrix}\\
&=-(6+2)-(2-12)\\
&=-8+10=2.
\end{aligned}
$$
:::

:::

:::

:::
