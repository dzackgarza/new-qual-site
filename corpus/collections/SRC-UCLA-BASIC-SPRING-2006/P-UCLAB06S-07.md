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
A matrix $T$ (with entries, say, in the field $\CC$ of complex numbers) is diagonalizable if there exists a non-singular matrix $S$ such that $STS^{-1}$ is diagonal.
Prove that if $a, \lambda \in \CC$ with $a \neq 0$, then the following matrix is not diagonalizable:

$$
T = \begin{pmatrix} 1 & a & 0 \\ 0 & 1 & a \\ 0 & 0 & \lambda \end{pmatrix}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The characteristic polynomial of $T$ is
$$
\chi_T(t)
=(t-1)^2(t-\lambda).
$$


::: pf-proof

The matrix $T$ is upper triangular, so its characteristic polynomial is the product
$$
\prod_{j=1}^3(t-T_{jj})
=(t-1)(t-1)(t-\lambda).
$$

:::

:::

::: {.pf-step #s1-2}

Suppose first that
$$
\lambda\ne1.
$$
Then the eigenspace for eigenvalue $1$ is one-dimensional.


::: pf-proof

Compute
$$
T-I
=
\begin{pmatrix}
0&a&0\\
0&0&a\\
0&0&\lambda-1
\end{pmatrix}.
$$
Let
$$
v=
\begin{pmatrix}
x\\y\\z
\end{pmatrix}
$$
lie in
$$
\ker(T-I).
$$
The first row gives
$$
ay=0,
$$
so
$$
y=0
$$
because
$$
a\ne0.
$$
The second row gives
$$
az=0,
$$
so
$$
z=0.
$$
Thus
$$
v=
\begin{pmatrix}
x\\0\\0
\end{pmatrix},
$$
and therefore
$$
\dim\ker(T-I)=1.
$$

:::

:::

::: {.pf-step #s1-3}

If
$$
\lambda\ne1,
$$
then $T$ is not diagonalizable.


::: pf-proof

By step [](#s1-1){.pf-ref}, the eigenvalue $1$ has algebraic multiplicity $2$.
By step [](#s1-2){.pf-ref}, its eigenspace has dimension $1$.
A diagonalizable matrix must have, for each eigenvalue, geometric multiplicity equal to algebraic multiplicity.
Therefore $T$ is not diagonalizable.

:::

:::

::: {.pf-step #s1-4}

Suppose now that
$$
\lambda=1.
$$
Then the only eigenvalue of $T$ is $1$.


::: pf-proof

Step [](#s1-1){.pf-ref} gives
$$
\chi_T(t)=(t-1)^3.
$$

:::

:::

::: {.pf-step #s1-5}

If
$$
\lambda=1,
$$
then
$$
\ker(T-I)
=
\operatorname{span}
\left\{
\begin{pmatrix}
1\\0\\0
\end{pmatrix}
\right\}.
$$


::: pf-proof

Now
$$
T-I
=
\begin{pmatrix}
0&a&0\\
0&0&a\\
0&0&0
\end{pmatrix}.
$$
The equations
$$
(T-I)
\begin{pmatrix}
x\\y\\z
\end{pmatrix}
=0
$$
give
$$
ay=0,
\qquad
az=0.
$$
Since
$$
a\ne0,
$$
one gets
$$
y=z=0.
$$
Thus the eigenspace is one-dimensional.

:::

:::

::: {.pf-step #s1-6}

If
$$
\lambda=1,
$$
then $T$ is not diagonalizable.


::: pf-proof

The only eigenvalue is $1$ by step [](#s1-4){.pf-ref}, so if $T$ were diagonalizable, there would have to be a basis of three eigenvectors for eigenvalue $1$.
But step [](#s1-5){.pf-ref} shows that the eigenspace has dimension only $1$.
Hence $T$ is not diagonalizable.

:::

:::

::: {.pf-step #s1-7}

Therefore for every
$$
a,\lambda\in\CC
$$
with
$$
a\ne0,
$$
the matrix $T$ is not diagonalizable.


::: pf-proof

Step [](#s1-3){.pf-ref} covers the case
$$
\lambda\ne1,
$$
and step [](#s1-6){.pf-ref} covers the case
$$
\lambda=1.
$$
These cases exhaust all possibilities.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
