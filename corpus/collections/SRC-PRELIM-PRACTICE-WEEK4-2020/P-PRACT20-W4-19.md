---
schema: qual/card@1
id: P-PRACT20-W4-19
kind: problem
title: Matrix of reflection in the $x$-axis followed by doubling
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Matrices
  - Linear Transformations
relations: []
review: draft
---

::: {.problem}
Find the matrix for the transformation of the xy-plane which reflects each vector through the x-axis and doubles its length.
:::

::: {.solution}
<1>1. Reflection in the $x$-axis followed by doubling sends
$$
(x,y)\longmapsto(2x,-2y).
$$
::: {.proof}
Reflection in the $x$-axis sends $(x,y)$ to $(x,-y)$. Multiplying the reflected vector by $2$ gives $(2x,-2y)$.
:::

<1>2. The matrix of the transformation is
$$
\boxed{
\begin{pmatrix}
2&0\\
0&-2
\end{pmatrix}.
}
$$
::: {.proof}
The first column is the image of $(1,0)$, namely $(2,0)$, and the second column is the image of $(0,1)$, namely $(0,-2)$.
:::

<1>3. Q.E.D.
::: {.proof}
Step <1>2 gives the requested matrix.
:::
:::
