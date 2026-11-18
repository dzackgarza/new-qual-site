---
schema: qual/card@1
id: P-F06DT
kind: problem
title: Determinant of a $4\times 4$ integer matrix
classification:
  areas:
  - prelim
  topics:
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into a Lamport proof and repaired false arithmetic. The prose gave the
    three 3x3 minors as -1, -21, -10; they are -2, -14 and -14. The final answer 40 was
    right by coincidence: -1 - (-21) - 2(-10) and -2 - (-14) - 2(-14) both equal 40, so
    the wrong minors were self-consistent. Recomputed by cofactor expansion on each minor
    and checked against an exact determinant of the 4x4 (40) computed independently. The
    cofactor signs of the first-row expansion are now stated. The collection's provenance
    is the examination paper only, so no retained solution set covers the exercise and the
    argument is the card's own.
---

::: {.problem}
Compute the determinant of the matrix $$B = \begin{bmatrix} 1 & 0 & -1 & 2 \\ 3 & 1 & 0 & 1 \\ 4 & -1 & 1 & 1 \\ -1 & 2 & 1 & 2 \end{bmatrix}.$$
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #expansion}
Expanding $\det B$ along the first row,
$$
\det B=\det\begin{bmatrix}1&0&1\\-1&1&1\\2&1&2\end{bmatrix}
-\det\begin{bmatrix}3&1&1\\4&-1&1\\-1&2&2\end{bmatrix}
-2\det\begin{bmatrix}3&1&0\\4&-1&1\\-1&2&1\end{bmatrix}.
$$

::: pf-proof
The cofactor expansion is $\det B=\sum_j(-1)^{1+j}b_{1j}\det M_{1j}$ with $M_{1j}$ the minor obtained by deleting row $1$ and column $j$. The first-row entries are $1,0,-1,2$, the signs $(-1)^{1+j}$ are $+,-,+,-$, and $b_{12}=0$, so only three terms survive: $+1\cdot\det M_{11}+(-1)(+1)\det M_{13}+2(-1)\det M_{14}$, which is the displayed identity.
:::

:::

::: {.pf-step #minor-11}
$\det\begin{bmatrix}1&0&1\\-1&1&1\\2&1&2\end{bmatrix}=-2$.

::: pf-proof
Expand along the first row: $1\cdot(1\cdot2-1\cdot1)-0\cdot(\cdots)+1\cdot\left((-1)\cdot1-1\cdot2\right)=1-3=-2$.
:::

:::

::: {.pf-step #minor-13}
$\det\begin{bmatrix}3&1&1\\4&-1&1\\-1&2&2\end{bmatrix}=-14$.

::: pf-proof
Expand along the first row: $3\left((-1)\cdot2-1\cdot2\right)-1\left(4\cdot2-1\cdot(-1)\right)+1\left(4\cdot2-(-1)(-1)\right)=3(-4)-9+7=-14$.
:::

:::

::: {.pf-step #minor-14}
$\det\begin{bmatrix}3&1&0\\4&-1&1\\-1&2&1\end{bmatrix}=-14$.

::: pf-proof
Expand along the first row: $3\left((-1)\cdot1-1\cdot2\right)-1\left(4\cdot1-1\cdot(-1)\right)+0=3(-3)-5=-14$.
:::

:::

::: {.pf-step}
$\det B=\boxed{40}$.

::: pf-proof
Substituting steps [](#minor-11){.pf-ref}, [](#minor-13){.pf-ref} and [](#minor-14){.pf-ref} into step [](#expansion){.pf-ref},
$$
\det B=-2-(-14)-2(-14)=-2+14+28=40 .
$$
:::

:::

:::
:::
