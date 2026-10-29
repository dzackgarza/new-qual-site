---
schema: qual/card@1
id: P-HM21B18-FIN-08
kind: problem
title: Rank, nullity, bases, and inversion for Game-of-Life matrices
classification: {areas: [applied-algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
For the “Beacon Oscillator” matrix
$$
A=\begin{pmatrix}
0&0&0&0&0&0\\
0&1&1&0&0&0\\
0&1&0&0&0&0\\
0&0&0&0&1&0\\
0&0&0&1&1&0\\
0&0&0&0&0&0
\end{pmatrix},
$$

(a) find the rank and nullity;

(b) find a basis for the kernel and a basis for the image.

(c) For the “glider” matrix
$$
B=\begin{pmatrix}1&0&0\\0&1&1\\1&1&0\end{pmatrix},
$$
find $B^{-1}$ by row reduction.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The four middle columns of $A$ are linearly independent.


::: pf-proof

Write these columns as
$$
c_2=(0,1,1,0,0,0)^T,\quad
c_3=(0,1,0,0,0,0)^T,
$$
$$
c_4=(0,0,0,0,1,0)^T,\quad
c_5=(0,0,0,1,1,0)^T.
$$
If
$a_2c_2+a_3c_3+a_4c_4+a_5c_5=0$, then the third coordinate gives
$a_2=0$, the second gives $a_3=0$, the fourth gives $a_5=0$, and the
fifth gives $a_4=0$. Hence the four columns are linearly independent.

:::

:::

::: {.pf-step #s1-2}

The rank of $A$ is $4$, its nullity is $2$, and
$$
\ker A=\operatorname{span}\{e_1,e_6\}.
$$


::: pf-proof

The first and sixth columns are zero, while step [](#s1-1){.pf-ref} shows that columns
$2,3,4,5$ are independent. Thus $\operatorname{rank}A=4$. By
rank-nullity,
$$
\operatorname{nullity}A=6-4=2.
$$
Since $Ae_1=Ae_6=0$ and $e_1,e_6$ are linearly independent, they form a
basis of the two-dimensional kernel.

:::

:::

::: {.pf-step #s1-3}

A basis for $\operatorname{im}A$ is
$$
\{c_2,c_3,c_4,c_5\}.
$$


::: pf-proof

The image is the column space of $A$. The only nonzero columns are
$c_2,c_3,c_4,c_5$, and step [](#s1-1){.pf-ref} shows that they are linearly
independent. Hence they form a basis of the image.

:::

:::

::: {.pf-step #s1-4}

Row reduction of $[B\mid I_3]$ gives
$$
\left[
\begin{array}{ccc|ccc}
1&0&0&1&0&0\\
0&1&0&-1&0&1\\
0&0&1&1&1&-1
\end{array}
\right].
$$


::: pf-proof

Start with
$$
\left[
\begin{array}{ccc|ccc}
1&0&0&1&0&0\\
0&1&1&0&1&0\\
1&1&0&0&0&1
\end{array}
\right].
$$
Apply
$$
R_3\leftarrow R_3-R_1,\qquad
R_2\leftarrow R_2-R_3,
$$
which yields
$$
\left[
\begin{array}{ccc|ccc}
1&0&0&1&0&0\\
0&0&1&1&1&-1\\
0&1&0&-1&0&1
\end{array}
\right].
$$
Swapping $R_2$ and $R_3$ gives the displayed reduced augmented matrix.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\begin{gathered}
\operatorname{rank}A=4,\qquad
\operatorname{nullity}A=2,\qquad
\ker A=\operatorname{span}\{e_1,e_6\},\\
\operatorname{im}A=\operatorname{span}\{c_2,c_3,c_4,c_5\},\\
B^{-1}=
\begin{pmatrix}
1&0&0\\
-1&0&1\\
1&1&-1
\end{pmatrix}.
\end{gathered}}
$$


::: pf-proof

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} give parts (a) and (b). In step [](#s1-4){.pf-ref}, the left block
is $I_3$, so the right block is $B^{-1}$, giving part (c).

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} records all requested quantities.

:::

:::

:::
