---
schema: qual/card@1
id: P-TRIV-LA19
kind: problem
title: Pauli matrices as a basis of $2\times 2$ Hermitian matrices
classification:
  areas: [prelim]
  topics:
  - Pauli Matrices
  - Hermitian Matrices
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

(b) Decompose a matrix $A = \begin{bmatrix} a & b + ic \\ b - ic & -a \end{bmatrix}$, $a, b, c \in \RR$, into a sum of $\sigma_i$.

(c) Prove that $\sigma_i$, $i = 1, 2, 3$, constitute a basis in the space of $2 \times 2$ hermitian matrices with zero trace.

(d) Prove that $\{\sigma_i, i = 1, 2, 3;\ 1\}$ constitute a basis in the space of $2 \times 2$ hermitian matrices.

(e) Calculate the eigenvalues and the eigenvectors of $\sigma_i$, $i = 1, 2, 3$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

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

::: {.pf-step #s1-3}

Every $2\times2$ Hermitian matrix of trace zero has the form in step
[](#s1-2){.pf-ref} with $a,b,c\in\RR$.


::: pf-proof

Let
$$
H=
\begin{pmatrix}
u&z\\
\overline z&v
\end{pmatrix}
$$
be Hermitian. Then $u,v\in\RR$. If $\operatorname{Tr}H=0$, then
$$
v=-u.
$$
Write
$$
z=b+ic
$$
with $b,c\in\RR$. Then $H$ has the form of step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The matrices $\sigma_1,\sigma_2,\sigma_3$ are linearly independent over
$\RR$.


::: pf-proof

Suppose
$$
r_1\sigma_1+r_2\sigma_2+r_3\sigma_3=0,
\qquad
r_j\in\RR.
$$
Comparing the diagonal entries gives $r_3=0$. Comparing the upper-right entry
then gives
$$
r_1-ir_2=0.
$$
Since $r_1,r_2$ are real, both vanish.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{\{\sigma_1,\sigma_2,\sigma_3\}}
$$
is a basis of the real vector space of trace-zero $2\times2$ Hermitian
matrices.


::: pf-proof

Step [](#s1-3){.pf-ref} together with step [](#s1-2){.pf-ref} gives spanning, and step [](#s1-4){.pf-ref} gives linear
independence.

:::

:::

::: {.pf-step #s1-6}

Every $2\times2$ Hermitian matrix can be written uniquely as
$$
\boxed{
H=\alpha I+\beta_1\sigma_1+\beta_2\sigma_2+\beta_3\sigma_3,
\qquad
\alpha,\beta_j\in\RR.
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
is Hermitian and trace zero, so step [](#s1-5){.pf-ref} writes it uniquely as a real linear
combination of the three Pauli matrices. Since $I$ has nonzero trace while
each $\sigma_i$ has trace zero, $I$ is not in their span; hence the four
matrices are linearly independent.

:::

:::

::: {.pf-step #s1-7}

Parts (a)--(d) follow.


::: pf-proof

Step [](#s1-1){.pf-ref} proves (a), step [](#s1-2){.pf-ref} proves (b), step [](#s1-5){.pf-ref} proves (c), and step
[](#s1-6){.pf-ref} proves (d).

:::

:::

::: {.pf-step #s1-8}

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

::: {.pf-step #s1-9}

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

::: {.pf-step #s1-10}

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

::: {.pf-step #s1-11}

Part (e) follows.


::: pf-proof

Steps [](#s1-8){.pf-ref} through [](#s1-10){.pf-ref} list the eigenvalues and eigenvectors of all three Pauli
matrices.

:::

:::

::: pf-qed

Steps [](#s1-7){.pf-ref} and [](#s1-11){.pf-ref} establish parts (a)--(e).

:::

:::

:::
