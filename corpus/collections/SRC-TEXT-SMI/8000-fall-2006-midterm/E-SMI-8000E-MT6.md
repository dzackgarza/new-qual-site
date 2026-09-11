---
schema: qual/card@1
id: E-SMI-8000E-MT6
kind: problem
title: Characteristic polynomial, minimal polynomial, and Jordan form of a five-by-five matrix
classification:
  areas:
  - algebra
  topics:
  - Modules over PIDs
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared both parts and the displayed matrix with Smith 8000 Fall 2006 midterm problem 6."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Computed the characteristic polynomial from the block-upper-triangular form, determined the eigenvalue-one Jordan partition from kernel dimensions, obtained the minimal polynomial, and split the Jordan form into semisimple and nilpotent parts."
---

::: {.exercise}
(a) Compute both the characteristic and the minimal polynomials, and also the Jordan form $J$, of this matrix:

$$
A = \begin{bmatrix}
-1 & 1 & 0 & 0 & 0 \\
-4 & 3 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 & 1 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 2
\end{bmatrix}.
$$

You do not need to find a matrix $Q$ such that $Q^{-1}AQ = J$.

(b) Write the matrix $J$ as the sum of a diagonal matrix plus a nilpotent matrix.
:::

::: solution
<1>1. Compute the characteristic polynomial.
::: proof
The matrix is block upper triangular with diagonal blocks
$$
B=\begin{pmatrix}-1&1\\-4&3\end{pmatrix}
$$
and
$$
C=\begin{pmatrix}
1&0&1\\
0&1&0\\
0&0&2
\end{pmatrix}.
$$
Therefore
$$
\chi_A(x)=\chi_B(x)\chi_C(x).
$$
Now
$$
\begin{aligned}
\chi_B(x)
&=\det\begin{pmatrix}x+1&-1\\4&x-3\end{pmatrix}\\
&=(x+1)(x-3)+4\\
&=(x-1)^2,
\end{aligned}
$$
while $C$ is upper triangular, so
$$
\chi_C(x)=(x-1)^2(x-2).
$$
Hence
$$
\boxed{\chi_A(x)=(x-1)^4(x-2).}
$$
:::

<1>2. Determine the Jordan blocks for eigenvalue $1$.
::: proof
Let
$$
N=A-I.
$$
Row reduction gives
$$
\ker N
=\operatorname{span}\{(1,2,0,0,0),(0,0,0,1,0)\},
$$
so
$$
\dim\ker(A-I)=2.
$$
Thus the eigenvalue $1$, whose algebraic multiplicity is four, has exactly two
Jordan blocks.

Moreover
$$
(A-I)^2=
\begin{pmatrix}
0&0&1&0&0\\
0&0&2&0&1\\
0&0&0&0&1\\
0&0&0&0&0\\
0&0&0&0&1
\end{pmatrix},
$$
and therefore
$$
\dim\ker(A-I)^2=3.
$$
For two Jordan blocks totaling dimension four, the partition $(2,2)$ would
give a four-dimensional kernel for the square, whereas the partition $(3,1)$
gives dimension $2+1=3$. Hence the blocks at eigenvalue $1$ have sizes
$$
3\quad\text{and}\quad1.
$$
:::

<1>3. Determine the Jordan form and minimal polynomial.
::: proof
The eigenvalue $2$ has algebraic multiplicity one, so it contributes a single
$1\times1$ block. Thus, up to the ordering of blocks,
$$
\boxed{
J=J_3(1)\oplus[1]\oplus[2].}
$$
Explicitly,
$$
J=
\begin{pmatrix}
1&1&0&0&0\\
0&1&1&0&0\\
0&0&1&0&0\\
0&0&0&1&0\\
0&0&0&0&2
\end{pmatrix}.
$$

The exponent of $(x-1)$ in the minimal polynomial is the size of the largest
Jordan block at eigenvalue $1$, namely $3$, and the eigenvalue $2$ contributes
one factor $(x-2)$. Therefore
$$
\boxed{m_A(x)=(x-1)^3(x-2).}
$$
:::

<1>4. Split $J$ into a diagonal matrix plus a nilpotent matrix.
::: proof
Write
$$
J=D+N_J,
$$
where
$$
D=\operatorname{diag}(1,1,1,1,2)
$$
and
$$
N_J=
\begin{pmatrix}
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&0&0\\
0&0&0&0&0\\
0&0&0&0&0
\end{pmatrix}.
$$
The matrix $N_J$ is nilpotent, with
$$
N_J^3=0.
$$
Thus the requested decomposition is
$$
\boxed{J=D+N_J.}
$$
:::
:::
