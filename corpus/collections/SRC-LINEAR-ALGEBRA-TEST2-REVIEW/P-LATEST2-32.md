---
schema: qual/card@1
id: P-LATEST2-32
kind: problem
title: Dimension of a span of six vectors
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained PDF extraction for linear_algebra_from_test2.pdf; the source PDF has no usable text layer, so this audit is limited to the preserved extraction generated from that PDF.
---

::: {.problem}
Find the dimension of the subspace spanned by
\[
\begin{pmatrix}1\\1\\0\\0\end{pmatrix},
\begin{pmatrix}2\\2\\0\\0\end{pmatrix},
\begin{pmatrix}0\\1\\0\\0\end{pmatrix},
\begin{pmatrix}2\\0\\0\\3\end{pmatrix},
\begin{pmatrix}1\\-2\\0\\8\end{pmatrix},
\begin{pmatrix}0\\0\\0\\0\end{pmatrix}.
\]

(A) $2$  (B) $3$  (C) $4$  (D) $5$  (E) $6$
:::

Let
$$
v_1=\begin{pmatrix}1\\1\\0\\0\end{pmatrix},
\quad
v_3=\begin{pmatrix}0\\1\\0\\0\end{pmatrix},
\quad
v_4=\begin{pmatrix}2\\0\\0\\3\end{pmatrix}.
$$

::: pf

::: pf-step

The span of all six listed vectors has dimension at most $3$.


::: pf-proof

Every listed vector has third coordinate equal to $0$.
Hence their span is contained in
$$
W
=
\left\{
\begin{pmatrix}a\\b\\0\\c\end{pmatrix}
:a,b,c\in\mathbb R
\right\}.
$$
The vectors
$$
\begin{pmatrix}1\\0\\0\\0\end{pmatrix},
\quad
\begin{pmatrix}0\\1\\0\\0\end{pmatrix},
\quad
\begin{pmatrix}0\\0\\0\\1\end{pmatrix}
$$
form a basis of $W$, so
$$
\dim W=3.
$$
Therefore the required span has dimension at most $3$.

:::

:::

::: pf-step

The vectors $v_1,v_3,v_4$ are linearly independent.


::: pf-proof

Suppose
$$
av_1+bv_3+cv_4=0.
$$
Looking at the fourth coordinate gives
$$
3c=0,
$$
so
$$
c=0.
$$
The first coordinate then gives
$$
a=0.
$$
Finally, the second coordinate gives
$$
a+b=0,
$$
so
$$
b=0.
$$
Thus only the trivial linear combination vanishes.

:::

:::

::: pf-step

The span has dimension at least $3$.


::: pf-proof

Step <1>2 exhibits three linearly independent vectors among the six given vectors.
Hence the span has dimension at least $3$.

:::

:::

::: pf-step

Therefore the dimension is
$$
\boxed{3}.
$$


::: pf-proof

Step <1>1 gives an upper bound of $3$, while step <1>3 gives a lower bound of $3$.
Thus the dimension is exactly $3$, which is answer choice $\boxed{\text{(B)}}$.

:::

:::

::: pf-qed

Step <1>4 is the required dimension.

:::

:::
