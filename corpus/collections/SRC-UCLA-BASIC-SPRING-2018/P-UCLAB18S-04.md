---
schema: qual/card@1
id: P-UCLAB18S-04
kind: problem
title: Similarity classes of six unipotent matrices
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2018, `assets/attachments/basic-18S.pdf`.
---

::: {.problem}
Consider
\[
A=\begin{pmatrix}1&0&0\\0&1&1\\0&0&1\end{pmatrix},\quad
B=\begin{pmatrix}1&1&0\\0&1&0\\0&0&1\end{pmatrix},\quad
C=\begin{pmatrix}1&0&1\\0&1&0\\0&0&1\end{pmatrix},
\]
\[
D=\begin{pmatrix}1&0&0\\0&1&2\\0&0&1\end{pmatrix},\quad
E=\begin{pmatrix}1&0&0\\1&1&0\\0&0&1\end{pmatrix},\quad
F=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}.
\]
Which pairs are similar over $\mathbb R$?
Fully justify your answer.
:::

For each matrix $X$ in the list, write
\[
N_X=X-I.
\]

::: pf

::: pf-step

For each of
\[
X=A,B,C,D,E,
\]
one has
\[
\boxed{N_X\ne0,\qquad N_X^2=0}.
\]


::: pf-proof

The five nilpotent parts are
\[
N_A=
\begin{pmatrix}
0&0&0\\
0&0&1\\
0&0&0
\end{pmatrix},
\quad
N_B=
\begin{pmatrix}
0&1&0\\
0&0&0\\
0&0&0
\end{pmatrix},
\]
\[
N_C=
\begin{pmatrix}
0&0&1\\
0&0&0\\
0&0&0
\end{pmatrix},
\quad
N_D=
\begin{pmatrix}
0&0&0\\
0&0&2\\
0&0&0
\end{pmatrix},
\]
\[
N_E=
\begin{pmatrix}
0&0&0\\
1&0&0\\
0&0&0
\end{pmatrix}.
\]
Each is nonzero and has exactly one nonzero matrix-unit position.
Hence its square is zero.

:::

:::

::: pf-step

For each
\[
X=A,B,C,D,E,
\]
the minimal polynomial is
\[
\boxed{(t-1)^2}.
\]


::: pf-proof

Step <1>1 gives
\[
(X-I)^2=0,
\]
so the minimal polynomial divides
\[
(t-1)^2.
\]
Since
\[
X\ne I,
\]
the polynomial
\[
t-1
\]
does not annihilate $X$.
Therefore the minimal polynomial is exactly
\[
(t-1)^2.
\]

:::

:::

::: pf-step

Each of
\[
A,B,C,D,E
\]
has Jordan form
\[
\boxed{
J_2(1)\oplus[1].
}
\]


::: pf-proof

All six matrices are unipotent upper- or lower-triangular with characteristic polynomial
\[
(t-1)^3.
\]
For the five matrices under consideration, step <1>2 says the largest Jordan block has size $2$.
The total dimension is $3$, so the only possible Jordan block-size partition is
\[
2+1.
\]
Thus the Jordan form is
\[
J_2(1)\oplus[1].
\]

:::

:::

::: pf-step

Therefore any two matrices among
\[
\boxed{A,B,C,D,E}
\]
are similar over $\mathbb R$.


::: pf-proof

By step <1>3, all five have the same real Jordan normal form.
Matrices with the same Jordan form are similar.

:::

:::

::: pf-step

For
\[
F,
\]
one has
\[
N_F
=
F-I
=
\begin{pmatrix}
0&1&1\\
0&0&1\\
0&0&0
\end{pmatrix},
\]
and
\[
\boxed{
N_F^2
=
\begin{pmatrix}
0&0&1\\
0&0&0\\
0&0&0
\end{pmatrix}
\ne0.
}
\]


::: pf-proof

Multiply $N_F$ by itself directly.
Only the path
\[
1\to2\to3
\]
contributes a nonzero entry, namely the $(1,3)$ entry.

:::

:::

::: pf-step

One has
\[
\boxed{N_F^3=0}.
\]


::: pf-proof

The only nonzero entry of $N_F^2$ is in column $3$, while the third row of $N_F$ is zero.
Thus
\[
N_F^3=N_F^2N_F=0.
\]

:::

:::

::: pf-step

The minimal polynomial of $F$ is
\[
\boxed{(t-1)^3}.
\]


::: pf-proof

Step <1>6 gives
\[
(F-I)^3=0.
\]
Step <1>5 gives
\[
(F-I)^2\ne0.
\]
Therefore the least positive power of
\[
F-I
\]
that vanishes is $3$.
Hence the minimal polynomial is
\[
(t-1)^3.
\]

:::

:::

::: pf-step

Thus $F$ has Jordan form
\[
\boxed{J_3(1)}.
\]


::: pf-proof

The characteristic polynomial is
\[
(t-1)^3,
\]
and step <1>7 says the largest Jordan block has size $3$.
Since the whole space has dimension $3$, there is exactly one block.

:::

:::

::: pf-step

The matrix $F$ is not similar to any of
\[
A,B,C,D,E.
\]


::: pf-proof

Similarity preserves the minimal polynomial.
By step <1>2, each of
\[
A,B,C,D,E
\]
has minimal polynomial
\[
(t-1)^2,
\]
while step <1>7 gives
\[
(t-1)^3
\]
for $F$.
Thus no such similarity is possible.

:::

:::

::: pf-step

Therefore the complete similarity classification is:
\[
\boxed{
A\sim B\sim C\sim D\sim E,
\qquad
F\text{ is in a separate similarity class}.
}
\]


::: pf-proof

Step <1>4 proves all similarities among the first five matrices.
Step <1>9 separates $F$ from that class.
There are no other matrices in the list.

:::

:::

::: pf-qed

Step <1>10 gives all and only the similar pairs.

:::

:::
