---
schema: qual/card@1
id: P-KBQZ5
kind: problem
title: The nullspace of a given $3\times 3$ matrix is $\mathrm{span}\{(1,3,5)\}$
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: problem
Let
$$
A = \begin{pmatrix} 1 & -2 & 1 \\ 0 & 5 & -3 \\ 0 & 0 & 0 \end{pmatrix}.
$$
Show that $\ker A = \operatorname{span}\{(1,3,5)\}$.
:::

::: {.solution}
Row-reducing $A$ (already nearly echelon) gives the system $x-2y+z=0$ and $5y-3z=0$.
Thus $y=\frac{3}{5}z$ and $x=2y-z=\frac{1}{5}z$.
Taking $z=5$ yields the basis vector $(1,3,5)$.
The kernel is one-dimensional, so $\ker A = \operatorname{span}\{(1,3,5)\}$.
:::
