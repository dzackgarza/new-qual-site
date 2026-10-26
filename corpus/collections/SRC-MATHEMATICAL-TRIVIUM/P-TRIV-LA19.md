---
schema: qual/card@1
id: P-TRIV-LA19
kind: problem
title: Pauli matrices as a basis of $2\times 2$ Hermitian matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 19, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the garbled Pauli matrices from Linear Algebra Problem 19 on page 3 of the source PDF.
---

::: {.problem}
Consider the Pauli matrices,
$$
\sigma_1 = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \quad
\sigma_2 = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}, \quad
\sigma_3 = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}.
$$

(a) Calculate $\sigma_i^\dagger$, $i = 1, 2, 3$.

(b) Decompose a matrix $A = \begin{bmatrix} a & b + ic \\ b - ic & -a \end{bmatrix}$, $a, b, c \in \mathbb{R}$, into a sum of $\sigma_i$.

(c) Prove that $\sigma_i$, $i = 1, 2, 3$, constitute a basis in the space of $2 \times 2$ hermitian matrices with zero trace.

(d) Prove that $\{\sigma_i, i = 1, 2, 3;\ 1\}$ constitute a basis in the space of $2 \times 2$ hermitian matrices.

(e) Calculate the eigenvalues and the eigenvectors of $\sigma_i$, $i = 1, 2, 3$.
:::

::: pf

::: pf-step

Each Pauli matrix is Hermitian:
$$
\boxed{\sigma_i^\dagger=\sigma_i,\qquad i=1,2,3.}
$$


::: pf-proof

For $\sigma_1$ and $\sigma_3$, all entries are real and the matrices are
symmetric, so the conjugate transpose is unchanged. For $\sigma_2$,
transpose exchanges the off-diagonal entries and complex conjugation sends
$i\leftrightarrow -i$, again recovering $\sigma_2$.

:::

:::

::: pf-step

The matrix
$$
A=
\begin{pmatrix}
a&b+ic\\
b-ic&-a
\end{pmatrix}
$$
decomposes as
$$
\boxed{A=b\sigma_1-c\sigma_2+a\sigma_3.}
$$


::: pf-proof

One has
$$
b\sigma_1-c\sigma_2+a\sigma_3
=
\begin{pmatrix}
a&b+ic\\
b-ic&-a
\end{pmatrix}.
$$

:::

:::

::: pf-step

Every $2\times2$ Hermitian matrix of trace zero has the form in step
<1>2 with $a,b,c\in\mathbb R$.


::: pf-proof

Let
$$
H=
\begin{pmatrix}
u&z\\
\overline z&v
\end{pmatrix}
$$
be Hermitian. Then $u,v\in\mathbb R$. If $\operatorname{Tr}H=0$, then
$$
v=-u.
$$
Write
$$
z=b+ic
$$
with $b,c\in\mathbb R$. Then $H$ has the form of step <1>2.

:::

:::

::: pf-step

The matrices $\sigma_1,\sigma_2,\sigma_3$ are linearly independent over
$\mathbb R$.


::: pf-proof

Suppose
$$
r_1\sigma_1+r_2\sigma_2+r_3\sigma_3=0,
\qquad
r_j\in\mathbb R.
$$
Comparing the diagonal entries gives $r_3=0$. Comparing the upper-right entry
then gives
$$
r_1-ir_2=0.
$$
Since $r_1,r_2$ are real, both vanish.

:::

:::

::: pf-step

Therefore
$$
\boxed{\{\sigma_1,\sigma_2,\sigma_3\}}
$$
is a basis of the real vector space of trace-zero $2\times2$ Hermitian
matrices.


::: pf-proof

Step <1>3 together with step <1>2 gives spanning, and step <1>4 gives linear
independence.

:::

:::

::: pf-step

Every $2\times2$ Hermitian matrix can be written uniquely as
$$
\boxed{
H=\alpha I+\beta_1\sigma_1+\beta_2\sigma_2+\beta_3\sigma_3,
\qquad
\alpha,\beta_j\in\mathbb R.
}
$$


::: pf-proof

Let
$$
\alpha=\frac12\operatorname{Tr}H.
$$
Then
$$
H-\alpha I
$$
is Hermitian and trace zero, so step <1>5 writes it uniquely as a real linear
combination of the three Pauli matrices. Since $I$ has nonzero trace while
each $\sigma_i$ has trace zero, $I$ is not in their span; hence the four
matrices are linearly independent.

:::

:::

::: pf-step

Parts (a)--(d) follow.


::: pf-proof

Step <1>1 proves (a), step <1>2 proves (b), step <1>5 proves (c), and step
<1>6 proves (d).

:::

:::

::: pf-step

The eigenvalues of $\sigma_1$ are $1$ and $-1$, with eigenvectors
$$
\boxed{
\begin{pmatrix}1\\1\end{pmatrix}
\text{ for }1,
\qquad
\begin{pmatrix}1\\-1\end{pmatrix}
\text{ for }-1.
}
$$


::: pf-proof

Directly,
$$
\sigma_1
\begin{pmatrix}1\\1\end{pmatrix}
=
\begin{pmatrix}1\\1\end{pmatrix},
$$
and
$$
\sigma_1
\begin{pmatrix}1\\-1\end{pmatrix}
=
-
\begin{pmatrix}1\\-1\end{pmatrix}.
$$
The two independent eigenvectors account for both eigenvalues of a $2\times2$
matrix.

:::

:::

::: pf-step

The eigenvalues of $\sigma_2$ are $1$ and $-1$, with eigenvectors
$$
\boxed{
\begin{pmatrix}1\\i\end{pmatrix}
\text{ for }1,
\qquad
\begin{pmatrix}1\\-i\end{pmatrix}
\text{ for }-1.
}
$$


::: pf-proof

One has
$$
\sigma_2
\begin{pmatrix}1\\i\end{pmatrix}
=
\begin{pmatrix}1\\i\end{pmatrix},
$$
and
$$
\sigma_2
\begin{pmatrix}1\\-i\end{pmatrix}
=
-
\begin{pmatrix}1\\-i\end{pmatrix}.
$$

:::

:::

::: pf-step

The eigenvalues of $\sigma_3$ are $1$ and $-1$, with eigenvectors
$$
\boxed{
\begin{pmatrix}1\\0\end{pmatrix}
\text{ for }1,
\qquad
\begin{pmatrix}0\\1\end{pmatrix}
\text{ for }-1.
}
$$


::: pf-proof

This is immediate from
$$
\sigma_3=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
$$

:::

:::

::: pf-step

Part (e) follows.


::: pf-proof

Steps <1>8--<1>10 list the eigenvalues and eigenvectors of all three Pauli
matrices.

:::

:::

::: pf-qed

Steps <1>7 and <1>11 establish parts (a)--(e).

:::

:::
