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

::: {.solution}
For each matrix $X$ in the list, write
\[
N_X=X-I.
\]

<1>1. For each of
\[
X=A,B,C,D,E,
\]
one has
\[
\boxed{N_X\ne0,\qquad N_X^2=0}.
\]

::: {.proof}
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

<1>2. For each
\[
X=A,B,C,D,E,
\]
the minimal polynomial is
\[
\boxed{(t-1)^2}.
\]

::: {.proof}
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

<1>3. Each of
\[
A,B,C,D,E
\]
has Jordan form
\[
\boxed{
J_2(1)\oplus[1].
}
\]

::: {.proof}
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

<1>4. Therefore any two matrices among
\[
\boxed{A,B,C,D,E}
\]
are similar over $\mathbb R$.

::: {.proof}
By step <1>3, all five have the same real Jordan normal form.
Matrices with the same Jordan form are similar.
:::

<1>5. For
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

::: {.proof}
Multiply $N_F$ by itself directly.
Only the path
\[
1\to2\to3
\]
contributes a nonzero entry, namely the $(1,3)$ entry.
:::

<1>6. One has
\[
\boxed{N_F^3=0}.
\]

::: {.proof}
The only nonzero entry of $N_F^2$ is in column $3$, while the third row of $N_F$ is zero.
Thus
\[
N_F^3=N_F^2N_F=0.
\]
:::

<1>7. The minimal polynomial of $F$ is
\[
\boxed{(t-1)^3}.
\]

::: {.proof}
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

<1>8. Thus $F$ has Jordan form
\[
\boxed{J_3(1)}.
\]

::: {.proof}
The characteristic polynomial is
\[
(t-1)^3,
\]
and step <1>7 says the largest Jordan block has size $3$.
Since the whole space has dimension $3$, there is exactly one block.
:::

<1>9. The matrix $F$ is not similar to any of
\[
A,B,C,D,E.
\]

::: {.proof}
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

<1>10. Therefore the complete similarity classification is:
\[
\boxed{
A\sim B\sim C\sim D\sim E,
\qquad
F\text{ is in a separate similarity class}.
}
\]

::: {.proof}
Step <1>4 proves all similarities among the first five matrices.
Step <1>9 separates $F$ from that class.
There are no other matrices in the list.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>10 gives all and only the similar pairs.
:::
:::
