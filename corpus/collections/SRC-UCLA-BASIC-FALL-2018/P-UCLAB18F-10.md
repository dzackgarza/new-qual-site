---
schema: qual/card@1
id: P-UCLAB18F-10
kind: problem
title: Limit of powers of a triangular stochastic matrix
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2018, `assets/attachments/basic-18F.pdf`.
---

::: {.problem}
Let
$$
A=\begin{pmatrix}
1&0&0\\[2pt]
\tfrac12&\tfrac12&0\\[2pt]
\tfrac13&\tfrac13&\tfrac13
\end{pmatrix}.
$$
Compute $\lim_{n\to\infty}A^n$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The eigenvalues of $A$ are
$$
1,\qquad \frac12,\qquad \frac13.
$$


::: pf-proof

The matrix $A$ is lower triangular, so its eigenvalues are its diagonal entries.

:::

:::

::: {.pf-step #s1-2}

Corresponding eigenvectors are
$$
v_1=
\begin{pmatrix}
1\\
1\\
1
\end{pmatrix},
\qquad
v_{1/2}=
\begin{pmatrix}
0\\
1\\
2
\end{pmatrix},
\qquad
v_{1/3}=
\begin{pmatrix}
0\\
0\\
1
\end{pmatrix}.
$$


::: pf-proof

Direct multiplication gives
$$
Av_1=v_1,
$$
$$
Av_{1/2}
=
\begin{pmatrix}
0\\
\frac12\\
1
\end{pmatrix}
=
\frac12
\begin{pmatrix}
0\\
1\\
2
\end{pmatrix},
$$
and
$$
Av_{1/3}
=
\begin{pmatrix}
0\\
0\\
\frac13
\end{pmatrix}
=
\frac13
\begin{pmatrix}
0\\
0\\
1
\end{pmatrix}.
$$

:::

:::

::: {.pf-step #s1-3}

The vectors in step [](#s1-2){.pf-ref} form a basis of $\RR^3$.


::: pf-proof

The matrix with these vectors as columns is
$$
S=
\begin{pmatrix}
1&0&0\\
1&1&0\\
1&2&1
\end{pmatrix},
$$
which is lower triangular with determinant $1$.
Hence $S$ is invertible.

:::

:::

::: {.pf-step #s1-4}

One has
$$
A
=
S
\begin{pmatrix}
1&0&0\\
0&\frac12&0\\
0&0&\frac13
\end{pmatrix}
S^{-1}.
$$


::: pf-proof

The columns of $S$ are eigenvectors of $A$ for the three eigenvalues listed in step [](#s1-1){.pf-ref}.
Thus this is the diagonalization of $A$ in the eigenbasis from step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
A^n
=
S
\begin{pmatrix}
1&0&0\\
0&2^{-n}&0\\
0&0&3^{-n}
\end{pmatrix}
S^{-1}.
$$


::: pf-proof

Raise the diagonalization in step [](#s1-4){.pf-ref} to the $n$th power.

:::

:::

::: {.pf-step #s1-6}

As $n\to\infty$,
$$
A^n
\longrightarrow
S
\begin{pmatrix}
1&0&0\\
0&0&0\\
0&0&0
\end{pmatrix}
S^{-1}.
$$


::: pf-proof

Since
$$
2^{-n}\to0
\qquad\text{and}\qquad
3^{-n}\to0,
$$
the diagonal matrix in step [](#s1-5){.pf-ref} converges entrywise to
$$
\operatorname{diag}(1,0,0).
$$
Multiplication by the fixed matrices $S$ and $S^{-1}$ is continuous.

:::

:::

::: {.pf-step #s1-7}

The matrix in step [](#s1-6){.pf-ref} equals
$$
\boxed{
\begin{pmatrix}
1&0&0\\
1&0&0\\
1&0&0
\end{pmatrix}
}.
$$


::: pf-proof

The limit is the projection onto
$$
\operatorname{span}\{v_1\}
$$
along
$$
\operatorname{span}\{v_{1/2},v_{1/3}\}.
$$
Since
$$
v_{1/2}
=
\begin{pmatrix}
0\\
1\\
2
\end{pmatrix}
$$
and
$$
v_{1/3}
=
\begin{pmatrix}
0\\
0\\
1
\end{pmatrix}
$$
both have first coordinate $0$, the coefficient of $v_1$ in the eigenbasis expansion of
$$
x=
\begin{pmatrix}
x_1\\x_2\\x_3
\end{pmatrix}
$$
is exactly $x_1$.
Hence the projection sends
$$
x
\longmapsto
x_1
\begin{pmatrix}
1\\1\\1
\end{pmatrix},
$$
whose standard matrix is the displayed matrix.

:::

:::

::: {.pf-step #s1-8}

Thus
$$
\boxed{
\lim_{n\to\infty}A^n
=
\begin{pmatrix}
1&0&0\\
1&0&0\\
1&0&0
\end{pmatrix}
}.
$$


::: pf-proof

Combine steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required limit.

:::

:::

:::
