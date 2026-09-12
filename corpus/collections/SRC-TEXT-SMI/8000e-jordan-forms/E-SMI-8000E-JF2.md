---
schema: qual/card@1
id: E-SMI-8000E-JF2
kind: problem
title: Characteristic roots lie in the minimal polynomial; primary subspaces
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
  note: "Compared all three parts and the four matrices with the PDF text layer and local 8000e extraction, Jordan forms exercise 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Enumerated the three partitions of 3, proved characteristic roots lie in the minimal polynomial via eigenvectors, identified primary dimensions by characteristic-polynomial multiplicity, and checked the four determinant computations with exact arithmetic."
---

::: {.exercise}
(i) If $A$ is a $3 \times 3$ matrix with $\mathrm{ch}(t) = (X - 4)^3$, find all Jordan forms for $A$, each with its minimal polynomial.

(ii) If $\mathrm{ch}(t) = \prod (X - t)^{m_t}$ is the characteristic polynomial of $f: M \to M$, prove every root of $\mathrm{ch}(t)$ is also a root of the minimal polynomial $m(t)$, and if

$$
M_t = \ts{v \in M : \text{for some } r > 0, \ (T - t)^r v = 0}
$$

is the primary subspace of $M$ corresponding to the root $t$, prove that $\dim(M_t) = m_t$.

(iii) Use determinants to compute $\mathrm{ch}(t)$ for these matrices:

$$
A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}, \quad
B = \begin{bmatrix} 3 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 1 & 2 \end{bmatrix}, \quad
C = \begin{bmatrix} 1 & -1 & 4 \\ 3 & 2 & -1 \\ 2 & 1 & -1 \end{bmatrix}, \quad
D = \begin{bmatrix} 1 & -2 & -1 & 0 \\ 1 & 0 & -3 & 0 \\ -1 & -2 & 1 & 0 \\ 1 & 2 & 1 & 2 \end{bmatrix}.
$$
:::


::: solution
<1>1. List the Jordan forms in part (i) and their minimal polynomials.
::: proof
The characteristic polynomial
$$
(X-4)^3
$$
shows that $4$ is the only eigenvalue and that the Jordan block sizes form a
partition of $3$. The three partitions give:
$$
\boxed{
\begin{array}{c|c}
\text{Jordan form} & \text{minimal polynomial}\\ \hline
J_3(4) & (X-4)^3\\
J_2(4)\oplus J_1(4) & (X-4)^2\\
J_1(4)^{\oplus3}=4I_3 & X-4.
\end{array}}
$$
The exponent in the minimal polynomial is the size of the largest Jordan
block.
:::

<1>2. Every root of the characteristic polynomial is a root of the minimal polynomial.
::: proof
Let $c$ be a root of the characteristic polynomial. Then
$$
\det(T-cI)=0,
$$
so there is a nonzero vector $v$ with
$$
Tv=cv.
$$
Let $m(X)$ be the minimal polynomial. Since $m(T)=0$,
$$
0=m(T)v=m(c)v.
$$
Because $v\ne0$, one must have
$$
m(c)=0.
$$
Thus every characteristic root occurs among the roots of the minimal
polynomial.
:::

<1>3. The primary subspace $M_c$ has dimension equal to the algebraic multiplicity $m_c$.
::: proof
By the primary decomposition theorem,
$$
M=\bigoplus_c M_c,
$$
where the sum runs over the roots of the characteristic polynomial and the
restriction of $T-cI$ to $M_c$ is nilpotent.

Let
$$
d_c=\dim M_c.
$$
Since $T|_{M_c}=cI+N_c$ with $N_c$ nilpotent, the only characteristic root of
the restriction is $c$, and therefore
$$
\operatorname{ch}_{T|M_c}(X)=(X-c)^{d_c}.
$$
The matrix of $T$ in a basis adapted to the direct sum of the $M_c$ is block
diagonal, so its characteristic polynomial is the product of the
characteristic polynomials of the restrictions:
$$
\operatorname{ch}_T(X)
=\prod_c (X-c)^{d_c}.
$$
Comparing this with
$$
\operatorname{ch}_T(X)=\prod_c(X-c)^{m_c}
$$
gives
$$
\boxed{\dim M_c=d_c=m_c}
$$
for every characteristic root $c$.
:::

<1>4. Compute the characteristic polynomial of $A$.
::: proof
$$
XI-A=
\begin{pmatrix}
X&1\\
-1&X
\end{pmatrix},
$$
so
$$
\boxed{\operatorname{ch}_A(X)=X^2+1.}
$$
:::

<1>5. Compute the characteristic polynomial of $B$.
::: proof
Expanding along the first column of
$$
XI-B=
\begin{pmatrix}
X-3&-1&0\\
0&X-2&-1\\
0&-1&X-2
\end{pmatrix}
$$
gives
$$
\begin{aligned}
\operatorname{ch}_B(X)
&=(X-3)\bigl((X-2)^2-1\bigr)\\
&=(X-3)(X-1)(X-3).
\end{aligned}
$$
Hence
$$
\boxed{\operatorname{ch}_B(X)=(X-1)(X-3)^2.}
$$
:::

<1>6. Compute the characteristic polynomial of $C$.
::: proof
One has
$$
XI-C=
\begin{pmatrix}
X-1&1&-4\\
-3&X-2&1\\
-2&-1&X+1
\end{pmatrix}.
$$
Expanding along the first row gives
$$
\begin{aligned}
\det(XI-C)
&=(X-1)\bigl((X-2)(X+1)+1\bigr)\\
&\quad-\bigl(-3(X+1)+2\bigr)-4(2X-1)\\
&=X^3-2X^2-5X+6\\
&=(X-3)(X-1)(X+2).
\end{aligned}
$$
Thus
$$
\boxed{\operatorname{ch}_C(X)=(X-3)(X-1)(X+2).}
$$
:::

<1>7. Compute the characteristic polynomial of $D$.
::: proof
The last column of $XI-D$ is $(0,0,0,X-2)^t$. Expanding along it gives
$$
\det(XI-D)
=(X-2)
\det
\begin{pmatrix}
X-1&2&1\\
-1&X&3\\
1&2&X-1
\end{pmatrix}.
$$
The $3\times3$ determinant equals
$$
\begin{aligned}
&(X-1)\bigl(X(X-1)-6\bigr)
-2\bigl(-(X-1)-3\bigr)
+(-2-X)\\
&=(X-1)(X^2-X-6)+X+2\\
&=(X+2)(X-2)^2.
\end{aligned}
$$
Therefore
$$
\boxed{\operatorname{ch}_D(X)=(X+2)(X-2)^3.}
$$
:::
:::
