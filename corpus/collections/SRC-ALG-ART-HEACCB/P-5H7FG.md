---
schema: qual/card@1
id: P-5H7FG
kind: problem
title: Rational and Jordan canonical forms of a given matrix in $M_4(\mathbb{C})$
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Jordan Canonical Form
  - Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Exhibit the rational and Jordan canonical forms for the following matrix $A\in M_4(\CC)$:
\[
A=\left(\begin{array}{cccc}
2 & 0 & 0 & 0 \\
1 & 1 & 0 & 0 \\
-2 & -2 & 0 & 1 \\
-2 & 0 & -1 & -2
\end{array}\right).
\]
:::

::: {.solution}
<1>1. The characteristic polynomial is
\[
\chi_A(x)=(x-2)(x-1)(x+1)^2
=x^4-x^3-3x^2+x+2.
\]
::: {.proof}
A direct determinant computation of $xI-A$ gives the displayed factorization.
:::

<1>2. The eigenspaces for $2$ and $1$ are one-dimensional, as expected for simple eigenvalues. For the eigenvalue $-1$ one has
\[
\dim\ker(A+I)=1.
\]
::: {.proof}
The eigenvalues $2$ and $1$ have algebraic multiplicity $1$. Direct row reduction of $A+I$ gives rank $3$, hence nullity $1$.
:::

<1>3. Therefore the Jordan canonical form is
\[
J=J_2(-1)\oplus[1]\oplus[2]
=
\begin{pmatrix}
-1&1&0&0\\
0&-1&0&0\\
0&0&1&0\\
0&0&0&2
\end{pmatrix},
\]
up to permutation of the Jordan blocks.
::: {.proof}
The eigenvalue $-1$ has algebraic multiplicity $2$ but geometric multiplicity $1$, so it contributes one Jordan block of size $2$. The simple eigenvalues contribute one $1\times1$ block each.
:::

<1>4. The minimal polynomial is
\[
m_A(x)=(x+1)^2(x-1)(x-2)=\chi_A(x).
\]
::: {.proof}
The size-$2$ Jordan block at $-1$ forces the exponent $2$ of $x+1$, while the eigenvalues $1$ and $2$ force the factors $x-1$ and $x-2$. Thus the minimal polynomial has degree $4$ and equals the characteristic polynomial.
:::

<1>5. Hence $A$ has a single invariant factor, namely $m_A(x)$, so its rational canonical form is the companion matrix
\[
C(m_A)=
\begin{pmatrix}
0&0&0&-2\\
1&0&0&-1\\
0&1&0&3\\
0&0&1&1
\end{pmatrix}.
\]
::: {.proof}
The invariant factors multiply to the characteristic polynomial and the largest invariant factor is the minimal polynomial. Since these two polynomials are equal, there can be only one nonconstant invariant factor. For
\[
m_A(x)=x^4-x^3-3x^2+x+2,
\]
the displayed matrix is its standard companion matrix.
:::
:::
