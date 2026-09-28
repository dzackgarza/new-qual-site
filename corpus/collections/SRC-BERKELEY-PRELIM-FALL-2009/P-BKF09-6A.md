---
schema: qual/card@1
id: P-BKF09-6A
kind: problem
title: Finite continued fractions as ratios of determinants
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the omitted definition of Delta_n as a tridiagonal determinant, completing the truncated statement, against f09solutions.pdf page 3 problem 6A.
---

::: {.problem}
For $n \geq 1$, prove that

$$
a_n + \cfrac{1}{a_{n-1} + \cfrac{1}{\cdots + \cfrac{1}{a_1 + \cfrac{1}{a_0}}}} = \frac{\Delta_n}{\Delta_{n-1}},
$$

where

$$
\Delta_n = \begin{vmatrix}
a_0 & 1 & 0 & \cdots & 0 \\
-1 & a_1 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \ddots & \vdots \\
0 & \cdots & -1 & a_{n-1} & 1 \\
0 & \cdots & 0 & -1 & a_n
\end{vmatrix}.
$$
:::

::: {.solution}
Using the cofactor expansion with respect to the last row, we find that $\Delta _ { n } =$ $a _ { n } \Delta _ { n - 1 } + \Delta _ { n - 2 }$.
Dividing by$\Delta _ { n - 1 }$, we get:$$\Delta _ { n } / \Delta _ { n - 1 } = a _ { n } + \frac { 1 } { \Delta _ { n - 1 } / \Delta _ { n - 2 } } .$$The required result follows by induction on n since it obviously holds for$n = 1$
:::
