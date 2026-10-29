---
schema: qual/card@1
id: P-UCLAB15F-08
kind: problem
title: Compute the negative square of an inverse matrix
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Basic Examination, Fall 2015, `assets/attachments/basic-15F.pdf`; the PDF is image-only and the preserved extraction supplies the statement text.
---

::: {.problem}
Find $M^{-2}$ for
$$
M=\begin{pmatrix}
2&3&2&1\\
3&6&4&2\\
4&8&6&3\\
2&4&3&1
\end{pmatrix}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The inverse of $M$ is
$$
\boxed{
M^{-1}
=
\begin{pmatrix}
2&-1&0&0\\
-1&2&-1&0\\
0&-2&1&1\\
0&0&1&-2
\end{pmatrix}
}.
$$


::: pf-proof

Let
$$
N=
\begin{pmatrix}
2&-1&0&0\\
-1&2&-1&0\\
0&-2&1&1\\
0&0&1&-2
\end{pmatrix}.
$$
Direct matrix multiplication gives
$$
MN
=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}.
$$
Hence
$$
N=M^{-1}.
$$

:::

:::

::: pf-step

One has
$$
M^{-2}
=
(M^{-1})^2.
$$


::: pf-proof

By definition,
$$
M^{-2}
=(M^2)^{-1}.
$$
Since $M$ is invertible,
$$
(M^2)^{-1}
=
M^{-1}M^{-1}
=(M^{-1})^2.
$$

:::

:::

::: {.pf-step #s1-3}

Squaring the matrix in step [](#s1-1){.pf-ref} gives
$$
\boxed{
M^{-2}
=
\begin{pmatrix}
5&-4&1&0\\
-4&7&-3&-1\\
2&-6&4&-1\\
0&-2&-1&5
\end{pmatrix}
}.
$$


::: pf-proof

Multiply
$$
\begin{pmatrix}
2&-1&0&0\\
-1&2&-1&0\\
0&-2&1&1\\
0&0&1&-2
\end{pmatrix}
$$
by itself.
For example, the first row becomes
$$
(2,-1,0,0)
\begin{pmatrix}
2&-1&0&0\\
-1&2&-1&0\\
0&-2&1&1\\
0&0&1&-2
\end{pmatrix}
=(5,-4,1,0),
$$
and the remaining rows similarly give
$$
(-4,7,-3,-1),
\quad
(2,-6,4,-1),
\quad
(0,-2,-1,5).
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the requested value of $M^{-2}$.

:::

:::

:::
