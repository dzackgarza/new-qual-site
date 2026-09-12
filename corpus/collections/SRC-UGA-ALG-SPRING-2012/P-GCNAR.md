---
schema: qual/card@1
id: P-GCNAR
kind: problem
title: Invariant factors, indecomposable $\CC[x]$-modules, and Jordan form of a $5\times
  5$ matrix
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Jordan Canonical Form
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Consider the following matrix as a linear transformation from $V\definedas \CC^5$ to itself:
\[
A=\left(\begin{array}{ccccc}
-1 & 1 & 0 & 0 & 0 \\
-4 & 3 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 & 1 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 2
\end{array}\right)
.\]

a. 
Find the invariant factors of $A$.

b. 
Express $V$ in terms of a direct sum of indecomposable $\CC[x]\dash$modules.

c.
Find the Jordan canonical form of $A$.
:::

::: solution
Let $T$ denote the operator represented by $A$. A direct determinant computation gives
\[
\chi_T(x)=(x-1)^4(x-2).
\]
For the eigenvalue $1$, the nullities of $(T-I)^k$ for $k=1,2,3$ are respectively
\[
2,3,4.
\]
Thus the Jordan blocks for eigenvalue $1$ have sizes $3$ and $1$. The eigenvalue $2$ has algebraic multiplicity $1$, so it contributes one block of size $1$.

Hence the elementary divisors are
\[
(x-1)^3,\qquad x-1,\qquad x-2.
\]
To obtain invariant factors, align equal-prime powers so that divisibility is preserved. This gives
\[
d_1=x-1,
\qquad
d_2=(x-1)^3(x-2),
\]
and indeed $d_1\mid d_2$ and $d_1d_2=\chi_T$.

Therefore the invariant-factor decomposition is
\[
V\cong \mathbb C[x]/(x-1)\oplus
\mathbb C[x]/\bigl((x-1)^3(x-2)\bigr).
\]

For the decomposition into indecomposable $\mathbb C[x]$-modules, split into the primary cyclic summands corresponding to the elementary divisors:
\[
V\cong
\mathbb C[x]/((x-1)^3)
\oplus \mathbb C[x]/(x-1)
\oplus \mathbb C[x]/(x-2).
\]
Each summand is indecomposable because its annihilator is a power of a single irreducible polynomial.

Finally, the Jordan canonical form is
\[
J=J_3(1)\oplus[1]\oplus[2]
=
\begin{bmatrix}
1&1&0&0&0\\
0&1&1&0&0\\
0&0&1&0&0\\
0&0&0&1&0\\
0&0&0&0&2
\end{bmatrix}.
\]
:::
