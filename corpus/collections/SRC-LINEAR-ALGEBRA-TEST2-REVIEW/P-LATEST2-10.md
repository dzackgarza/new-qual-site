---
schema: qual/card@1
id: P-LATEST2-10
kind: problem
title: Decode a matrix-encrypted four-letter message
classification:
  areas:
  - applied-algebra
  topics:
  - Matrix Multiplication
  - Matrix Inverses
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained PDF extraction for linear_algebra_from_test2.pdf; the source PDF has no usable text layer, so this audit is limited to the preserved extraction generated from that PDF.
---

::: {.problem}
Each letter of a four-letter message is replaced by its position in the alphabet and entered in a $2\times2$ matrix $M$; for example, ``DEAD'' becomes
$$
M=\begin{pmatrix}4&5\\1&4\end{pmatrix}.
$$
The encoded message is $MC$, where
$$
C=\begin{pmatrix}2&-1\\1&1\end{pmatrix}.
$$
If the agent receives
$$
\begin{pmatrix}51&-3\\31&-8\end{pmatrix},
$$
which message was sent?

(A) RUSH  (B) COME  (C) ROME  (D) CALL  (E) not uniquely determined by the information given
:::

::: {.solution}

Let
$$
E=\begin{pmatrix}51&-3\\31&-8\end{pmatrix}.
$$
By hypothesis,
$$
E=MC.
$$

::: pf

::: pf-step

The matrix $C$ is invertible.


::: pf-proof

One has
$$
\det C
=
\det\begin{pmatrix}2&-1\\1&1\end{pmatrix}
=
2\cdot1-(-1)\cdot1
=
3\ne0.
$$
Hence $C$ is invertible.

:::

:::

::: {.pf-step #s1-2}

The inverse of $C$ is
$$
\boxed{
C^{-1}
=
\frac13
\begin{pmatrix}1&1\\-1&2\end{pmatrix}.
}
$$


::: pf-proof

This is the standard $2\times2$ inverse formula applied to
$$
C=\begin{pmatrix}2&-1\\1&1\end{pmatrix}
$$
with determinant $3$.

:::

:::

::: pf-step

The message matrix is
$$
M=EC^{-1}.
$$


::: pf-proof

From $E=MC$, multiply on the right by $C^{-1}$:
$$
EC^{-1}=MCC^{-1}=M.
$$

:::

:::

::: pf-step

One computes
$$
\boxed{
M=\begin{pmatrix}18&15\\13&5\end{pmatrix}.
}
$$


::: pf-proof

Using step [](#s1-2){.pf-ref},
$$
\begin{aligned}
M
&=
\begin{pmatrix}51&-3\\31&-8\end{pmatrix}
\frac13
\begin{pmatrix}1&1\\-1&2\end{pmatrix}\\
&=
\frac13
\begin{pmatrix}
51+3&51-6\\
31+8&31-16
\end{pmatrix}\\
&=
\frac13
\begin{pmatrix}54&45\\39&15\end{pmatrix}\\
&=
\begin{pmatrix}18&15\\13&5\end{pmatrix}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

The entries decode to ROME.


::: pf-proof

The encoding uses alphabet positions, so
$$
18=R,\qquad 15=O,\qquad 13=M,\qquad 5=E.
$$
Reading the matrix in the same row order as the example ``DEAD'' gives the message
$$
\boxed{\text{ROME}}.
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives answer choice $\boxed{\text{(C)}}$.

:::

:::

:::
