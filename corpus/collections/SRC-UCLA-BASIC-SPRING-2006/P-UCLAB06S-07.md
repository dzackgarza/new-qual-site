---
schema: qual/card@1
id: P-UCLAB06S-07
kind: problem
title: Non-diagonalizable $3\times3$ upper triangular matrix with a repeated eigenvalue
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 7 of the retained UCLA Basic Examination Spring 2006 PDF.
---

::: {.problem}
A matrix T (with entries, say, in the field $\mathbf { C }$ of complex numbers) is diagonalizable if there exists a non-singular matrix S such that $S T S ^ { - 1 }$ is diagonal.
Prove that if $a , \lambda \in \mathbf { C }$ with $a \neq 0$ , then the following matrix is not diagonalizable:

$$
T = { \left( \begin{array} { l l l } { 1 } & { a } & { 0 } \\ { 0 } & { 1 } & { a } \\ { 0 } & { 0 } & { \lambda } \end{array} \right) }
$$
:::

::: {.solution}
<1>1. The characteristic polynomial of $T$ is
\[
\chi_T(t)
=(t-1)^2(t-\lambda).
\]

::: {.proof}
The matrix $T$ is upper triangular, so its characteristic polynomial is the product
\[
\prod_{j=1}^3(t-T_{jj})
=(t-1)(t-1)(t-\lambda).
\]
:::

<1>2. Suppose first that
\[
\lambda\ne1.
\]
Then the eigenspace for eigenvalue $1$ is one-dimensional.

::: {.proof}
Compute
\[
T-I
=
\begin{pmatrix}
0&a&0\\
0&0&a\\
0&0&\lambda-1
\end{pmatrix}.
\]
Let
\[
v=
\begin{pmatrix}
x\\y\\z
\end{pmatrix}
\]
lie in
\[
\ker(T-I).
\]
The first row gives
\[
ay=0,
\]
so
\[
y=0
\]
because
\[
a\ne0.
\]
The second row gives
\[
az=0,
\]
so
\[
z=0.
\]
Thus
\[
v=
\begin{pmatrix}
x\\0\\0
\end{pmatrix},
\]
and therefore
\[
\dim\ker(T-I)=1.
\]
:::

<1>3. If
\[
\lambda\ne1,
\]
then $T$ is not diagonalizable.

::: {.proof}
By step <1>1, the eigenvalue $1$ has algebraic multiplicity $2$.
By step <1>2, its eigenspace has dimension $1$.
A diagonalizable matrix must have, for each eigenvalue, geometric multiplicity equal to algebraic multiplicity.
Therefore $T$ is not diagonalizable.
:::

<1>4. Suppose now that
\[
\lambda=1.
\]
Then the only eigenvalue of $T$ is $1$.

::: {.proof}
Step <1>1 gives
\[
\chi_T(t)=(t-1)^3.
\]
:::

<1>5. If
\[
\lambda=1,
\]
then
\[
\ker(T-I)
=
\operatorname{span}
\left\{
\begin{pmatrix}
1\\0\\0
\end{pmatrix}
\right\}.
\]

::: {.proof}
Now
\[
T-I
=
\begin{pmatrix}
0&a&0\\
0&0&a\\
0&0&0
\end{pmatrix}.
\]
The equations
\[
(T-I)
\begin{pmatrix}
x\\y\\z
\end{pmatrix}
=0
\]
give
\[
ay=0,
\qquad
az=0.
\]
Since
\[
a\ne0,
\]
one gets
\[
y=z=0.
\]
Thus the eigenspace is one-dimensional.
:::

<1>6. If
\[
\lambda=1,
\]
then $T$ is not diagonalizable.

::: {.proof}
The only eigenvalue is $1$ by step <1>4, so if $T$ were diagonalizable, there would have to be a basis of three eigenvectors for eigenvalue $1$.
But step <1>5 shows that the eigenspace has dimension only $1$.
Hence $T$ is not diagonalizable.
:::

<1>7. Therefore for every
\[
a,\lambda\in\mathbb C
\]
with
\[
a\ne0,
\]
the matrix $T$ is not diagonalizable.

::: {.proof}
Step <1>3 covers the case
\[
\lambda\ne1,
\]
and step <1>6 covers the case
\[
\lambda=1.
\]
These cases exhaust all possibilities.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
