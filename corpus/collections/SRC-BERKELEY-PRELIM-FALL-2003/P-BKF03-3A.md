---
schema: qual/card@1
id: P-BKF03-3A
kind: problem
title: Convergence of the Neumann series $I+A+A^2+\cdots$ for $2\times2$ matrices
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
  note: Checked against Problem 3A of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified necessity from A^n tending to zero on eigenvectors and sufficiency by the two Jordan-form cases.
---

::: {.problem}
Let A be a $2 \times 2$ matrix with complex entries.
Prove that the series $I + A + A ^ { 2 } + . . .$ converges if and only if every eigenvalue of A has absolute value less than 1.
:::


::: {.solution}
Convergence of a matrix series is equivalent in any matrix norm on $M_2(\mathbb C)$, so we may freely conjugate the series by a fixed invertible matrix.

<1>1. If $\sum_{n=0}^\infty A^n$ converges, then every eigenvalue of $A$ has modulus less than $1$.
::: {.proof}
Convergence of the series implies its terms tend to zero:
\[
A^n\longrightarrow0.
\]
Let $v\ne0$ be an eigenvector with eigenvalue $\lambda$.
Then
\[
A^nv=\lambda^n v.
\]
Since $A^nv\to0$ and $v\ne0$, one must have $\lambda^n\to0$.
This is equivalent to $|\lambda|<1$.
:::

<1>2. Suppose every eigenvalue of $A$ has modulus less than $1$.
Reduce $A$ to Jordan normal form.
::: {.proof}
There is an invertible matrix $S$ such that
\[
A=SJS^{-1},
\qquad
A^n=SJ^nS^{-1}.
\]
Hence
\[
\sum_{n=0}^N A^n
=S\left(\sum_{n=0}^N J^n\right)S^{-1}.
\]
Thus the series for $A$ converges if the series for $J$ converges.
For a $2\times2$ matrix, $J$ is either diagonal or a single Jordan block.
:::

<1>3. If $J=\operatorname{diag}(\lambda,\mu)$ with $|\lambda|,|\mu|<1$, then $\sum J^n$ converges.
::: {.proof}
One has
\[
J^n=\begin{pmatrix}\lambda^n&0\\0&\mu^n\end{pmatrix}.
\]
Therefore
\[
\sum_{n=0}^\infty J^n
=\begin{pmatrix}\sum_{n=0}^\infty\lambda^n&0\\0&\sum_{n=0}^\infty\mu^n\end{pmatrix},
\]
and both scalar geometric series converge.
:::

<1>4. If
\[
J=\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix},
\qquad |\lambda|<1,
\]
then $\sum J^n$ also converges.
::: {.proof}
Write $J=\lambda I+N$ with
\[
N=\begin{pmatrix}0&1\\0&0\end{pmatrix},
\qquad N^2=0.
\]
For $n\ge1$, the binomial theorem gives
\[
J^n=\lambda^n I+n\lambda^{n-1}N
=\begin{pmatrix}\lambda^n&n\lambda^{n-1}\\0&\lambda^n\end{pmatrix}.
\]
The geometric series $\sum\lambda^n$ converges, and
\[
\sum_{n=1}^\infty n\lambda^{n-1}=\frac1{(1-\lambda)^2}
\]
also converges absolutely for $|\lambda|<1$.
Hence every entry of $\sum J^n$ converges.
:::

By <1>2--<1>4, if every eigenvalue of $A$ has modulus less than $1$, then $\sum A^n$ converges.
Together with <1>1, this proves the equivalence.
:::
