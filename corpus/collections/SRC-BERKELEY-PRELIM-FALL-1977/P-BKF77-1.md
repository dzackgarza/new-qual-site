---
schema: qual/card@1
id: P-BKF77-1
kind: problem
title: Diagonalize a $2\times2$ real matrix
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Computed the characteristic polynomial, exhibited two independent real eigenvectors, and checked that their eigenbasis diagonalizes A."
---

::: problem
Let
\[
A=\begin{pmatrix}7&15\\-2&-4\end{pmatrix}.
\]
Find a real matrix $B$ such that $B^{-1}AB$ is diagonal.
:::

::: solution
The characteristic polynomial of $A$ is
$$
\begin{aligned}
\det(A-\lambda I)
&=\det\begin{pmatrix}7-\lambda&15\\-2&-4-\lambda\end{pmatrix}\\
&=(7-\lambda)(-4-\lambda)+30\\
&=\lambda^2-3\lambda+2\\
&=(\lambda-1)(\lambda-2).
\end{aligned}
$$
Thus the eigenvalues are $1$ and $2$.

<1>1. Find an eigenvector for $\lambda=1$.
::: proof
We have
$$
A-I=\begin{pmatrix}6&15\\-2&-5\end{pmatrix}.
$$
The equation $(A-I)v=0$ is equivalent to
$$
2x+5y=0.
$$
Hence one eigenvector is
$$
v_1=\binom{-5}{2}.
$$
Indeed,
$$
Av_1=v_1.
$$
:::

<1>2. Find an eigenvector for $\lambda=2$.
::: proof
We have
$$
A-2I=\begin{pmatrix}5&15\\-2&-6\end{pmatrix}.
$$
The equation $(A-2I)v=0$ is equivalent to
$$
x+3y=0.
$$
Hence one eigenvector is
$$
v_2=\binom{-3}{1},
$$
and
$$
Av_2=2v_2.
$$
:::

<1>3. Form the eigenvector matrix.
::: proof
Let
$$
B=\begin{pmatrix}-5&-3\\2&1\end{pmatrix}.
$$
Its determinant is
$$
(-5)(1)-(-3)(2)=1,
$$
so $B$ is invertible. Since its columns are the eigenvectors $v_1,v_2$,
$$
AB
=B\begin{pmatrix}1&0\\0&2\end{pmatrix}.
$$
Multiplying by $B^{-1}$ on the left gives
$$
\boxed{
B^{-1}AB=\begin{pmatrix}1&0\\0&2\end{pmatrix}.}
$$
:::
:::
