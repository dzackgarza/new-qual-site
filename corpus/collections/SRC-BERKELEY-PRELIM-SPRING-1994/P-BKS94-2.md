---
schema: qual/card@1
id: P-BKS94-2
kind: problem
title: Spectral radius bounds the norm of a symmetric matrix
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
  note: Checked against the vendored UC Berkeley Spring 1994 preliminary examination.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the garbled norm notation against Spring94.pdf page 1 problem 2.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used an orthonormal eigenbasis in the symmetric case and the nonzero
    nilpotent 2-by-2 Jordan block as a nonsymmetric counterexample with
    spectral radius zero.
---

::: {.problem}
Let $A$ be a real $n \times n$ matrix. Let $M$ denote the maximum of the absolute values of the eigenvalues of $A$.

1. Prove that if $A$ is symmetric, then $\|Ax\| \leqslant M \|x\|$ for all $x$ in $\mathbb{R}^n$. (Here, $\|\cdot\|$ denotes the Euclidean norm.)

2. Prove that the preceding inequality can fail if $A$ is not symmetric.
:::

::: {.solution}
<1>1. Suppose $A$ is symmetric. Then there is an orthonormal basis
$$
v_1,\ldots,v_n
$$
of $\RR^n$ consisting of eigenvectors of $A$.

::: {.proof}
This is the spectral theorem for real symmetric matrices.
:::

<1>2. If
$$
Av_j=\lambda_jv_j
$$
and
$$
x=\sum_{j=1}^n c_jv_j,
$$
then
$$
\norm{Ax}^2
\leq
M^2\norm{x}^2.
$$

::: {.proof}
Since the basis from step <1>1 is orthonormal,
$$
\norm{x}^2
=
\sum_{j=1}^n c_j^2.
$$
Moreover,
$$
Ax
=
\sum_{j=1}^n c_j\lambda_jv_j,
$$
so
$$
\norm{Ax}^2
=
\sum_{j=1}^n\lambda_j^2c_j^2
\leq
M^2\sum_{j=1}^n c_j^2
=
M^2\norm{x}^2,
$$
because $\abs{\lambda_j}\leq M$ for every $j$.
:::

<1>3. If $A$ is symmetric, then
$$
\norm{Ax}\leq M\norm{x}
$$
for every $x\in\RR^n$.

::: {.proof}
Both sides are nonnegative, so taking square roots in step <1>2 gives the
desired inequality.
:::

<1>4. The inequality can fail for nonsymmetric matrices.

::: {.proof}
Take
$$
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
$$
This matrix is not symmetric, and both of its eigenvalues are $0$. Hence
$$
M=0.
$$
For
$$
x=
\begin{pmatrix}
0\\
1
\end{pmatrix},
$$
one has
$$
Ax=
\begin{pmatrix}
1\\
0
\end{pmatrix},
$$
so
$$
\norm{Ax}=1
\qquad\text{while}\qquad
M\norm{x}=0.
$$
Thus the asserted inequality fails.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 proves part 1, and step <1>4 proves part 2.
:::
:::
