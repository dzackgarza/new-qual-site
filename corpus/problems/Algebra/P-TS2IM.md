---
schema: qual/card@1
id: P-TS2IM
kind: problem
title: Conjugacy classes of $3\times 3$ rational matrices satisfying $A^4-A^3-A+1=0$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Rational Canonical Form
  - Minimal and Characteristic Polynomials
relations: []
review: draft
---

::: problem
Describe all conjugacy classes of $3\times3$ matrices $A\in M_3(\QQ)$ satisfying
\[
A^4-A^3-A+I=0.
\]
Give a representative of each class.
:::

::: solution
Factor the annihilating polynomial:
\[
x^4-x^3-x+1=(x-1)(x^3-1)=(x-1)^2(x^2+x+1).
\]
Over $\QQ$, the factors
\[
x-1,\qquad x^2+x+1
\]
are irreducible. Therefore the minimal polynomial of $A$ divides
\[
(x-1)^2(x^2+x+1).
\]

View $\QQ^3$ as a $\QQ[x]$-module via $x\cdot v=Av$. The possible elementary divisors have total degree $3$, with $(x-1)$-primary blocks of size at most $2$ and an $(x^2+x+1)$-primary block of size at most $1$.

There are exactly three possibilities:

<1>1. Three size-$1$ $(x-1)$ blocks:
\[
A\sim I_3.
\]

<1>2. One size-$2$ $(x-1)$ block and one size-$1$ block:
\[
A\sim
\begin{pmatrix}
1&1&0\\
0&1&0\\
0&0&1
\end{pmatrix}.
\]

<1>3. One $(x-1)$ block and one block for $x^2+x+1$:
\[
A\sim
\begin{pmatrix}
1&0&0\\
0&0&-1\\
0&1&-1
\end{pmatrix}.
\]
The lower-right block is a companion matrix for $x^2+x+1$.

These three matrices have distinct minimal polynomials
\[
x-1,
\qquad
(x-1)^2,
\qquad
(x-1)(x^2+x+1),
\]
so they are pairwise nonconjugate. Hence these are exactly the conjugacy classes.
:::
