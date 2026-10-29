---
schema: qual/card@1
id: P-BLAR-02
kind: problem
title: Determine inverses of four matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Review Problem 2 in the deterministic MinerU Flash extraction assets/attachments/Basic_Linear_Algebra_Review_extracted.md.
---

::: {.problem}
Find the inverse of each matrix, or explain why it does not exist:
$$
\text{(a)}\quad
\begin{bmatrix}3&2\\1&3\end{bmatrix},
\qquad
\text{(b)}\quad
\begin{bmatrix}1&2&4\\-1&2&0\end{bmatrix},
$$
$$
\text{(c)}\quad
\begin{bmatrix}1&3&3\\1&4&3\\1&3&4\end{bmatrix},
\qquad
\text{(d)}\quad
\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix}.
$$
:::

::: {.solution}

::: pf

::: pf-step
For
$$
A=\begin{bmatrix}3&2\\1&3\end{bmatrix},
$$
one has
$$
\boxed{
A^{-1}=\frac17
\begin{bmatrix}3&-2\\-1&3\end{bmatrix}}.
$$

::: pf-proof
The determinant is
$$
\det A=3\cdot3-2\cdot1=7\neq0.
$$
The $2\times2$ inverse formula therefore gives the displayed matrix.
:::

:::

::: pf-step
The matrix
$$
B=\begin{bmatrix}1&2&4\\-1&2&0\end{bmatrix}
$$
has no inverse.

::: pf-proof
An inverse $B^{-1}$ in the usual matrix sense can exist only for a square matrix: if an $m\times n$ matrix had both a left and a right inverse, then its rank would be both $m$ and $n$, forcing $m=n$. Here $B$ is $2\times3$, so it is not invertible.
:::

:::

::: pf-step
For
$$
C=\begin{bmatrix}
1&3&3\\
1&4&3\\
1&3&4
\end{bmatrix},
$$
one has
$$
\boxed{
C^{-1}=
\begin{bmatrix}
7&-3&-3\\
-1&1&0\\
-1&0&1
\end{bmatrix}}.
$$

::: pf-proof
Let
$$
D=
\begin{bmatrix}
7&-3&-3\\
-1&1&0\\
-1&0&1
\end{bmatrix}.
$$
Direct multiplication gives
$$
CD=
\begin{bmatrix}
7-3-3&-3+3&-3+3\\
7-4-3&-3+4&-3+3\\
7-3-4&-3+3&-3+4
\end{bmatrix}
=I_3.
$$
Since $C$ and $D$ are square, a right inverse is also the inverse; hence $D=C^{-1}$.
:::

:::

::: pf-step
For
$$
P=\begin{bmatrix}
0&1&0\\
0&0&1\\
1&0&0
\end{bmatrix},
$$
one has
$$
\boxed{
P^{-1}=
\begin{bmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{bmatrix}}.
$$

::: pf-proof
The columns of $P$ are a permutation of the standard basis, so $P$ is a permutation matrix. Hence
$$
P^{-1}=P^T,
$$
which is exactly the displayed matrix. Equivalently, direct multiplication gives $PP^T=P^TP=I_3$.
:::

:::

:::

:::
