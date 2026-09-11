---
schema: qual/card@1
id: E-SMI-8000E-JF3
kind: problem
title: Jordan forms of three explicit matrices
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
  note: "Compared all three matrices with the PDF text layer and local 8000e extraction, Jordan forms exercise 3."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Checked characteristic polynomials and exact ranks/nullities of the relevant powers, then recovered the Jordan block partitions from kernel growth."
---

::: {.exercise}
Find the Jordan forms of these matrices:

$$
\text{(i)} \quad A = \begin{bmatrix} 0 & -1 & 2 \\ 3 & -4 & 6 \\ 2 & -2 & 3 \end{bmatrix}
$$

$$
\text{(ii)} \quad B = \begin{bmatrix} 2 & 0 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ 0 & -1 & 0 & -1 \\ 1 & 1 & 1 & 2 \end{bmatrix}
$$

$$
\text{(iii)} \quad C = \begin{bmatrix} 1 & 0 & -1 & 1 & 0 \\ -4 & 1 & -3 & 2 & 1 \\ -2 & -1 & 0 & 1 & 1 \\ -3 & -1 & -3 & 4 & 1 \\ -8 & -2 & -7 & 5 & 4 \end{bmatrix}
$$
:::


::: solution
<1>1. Determine the Jordan form of $A$.
::: proof
A direct determinant computation gives
$$
\operatorname{ch}_A(X)=(X-1)(X+1)^2.
$$
For the eigenvalue $-1$,
$$
A+I=
\begin{pmatrix}
1&-1&2\\
3&-3&6\\
2&-2&4
\end{pmatrix}
$$
has rank $1$, hence nullity $2$. Thus the $-1$ eigenspace already has
dimension equal to its algebraic multiplicity $2$, so it contributes two
size-$1$ blocks.

The eigenvalue $1$ has algebraic multiplicity $1$, hence contributes one
size-$1$ block. Therefore
$$
\boxed{J(A)=J_1(1)\oplus J_1(-1)\oplus J_1(-1).}
$$
In particular $A$ is diagonalizable.
:::

<1>2. Determine the Jordan form of $B$.
::: proof
The characteristic polynomial is
$$
\operatorname{ch}_B(X)=(X-2)(X-1)^3.
$$
For the eigenvalue $1$, put
$$
N=B-I.
$$
Exact row reduction gives
$$
\operatorname{rank}N=2,
\qquad
\operatorname{rank}N^2=1.
$$
Since $B$ is $4\times4$,
$$
\dim\ker N=2,
\qquad
\dim\ker N^2=3.
$$
The generalized $1$-eigenspace has total dimension $3$. The first nullity
says there are two Jordan blocks at eigenvalue $1$, and the increase from $2$
to $3$ at the second power says exactly one of those blocks has size at least
$2$. Hence their sizes are
$$
2,1.
$$
The eigenvalue $2$ has algebraic multiplicity $1$, so it contributes one
size-$1$ block. Thus
$$
\boxed{J(B)=J_2(1)\oplus J_1(1)\oplus J_1(2).}
$$
:::

<1>3. Determine the Jordan form of $C$.
::: proof
A determinant computation gives
$$
\operatorname{ch}_C(X)=(X-2)^5.
$$
Put
$$
N=C-2I.
$$
Exact row reduction gives
$$
\operatorname{rank}N=3,
\qquad
\operatorname{rank}N^2=1,
\qquad
N^3=0.
$$
Therefore
$$
\dim\ker N=2,
\qquad
\dim\ker N^2=4,
\qquad
\dim\ker N^3=5.
$$
The first nullity says there are two Jordan blocks. The increment
$$
4-2=2
$$
says both blocks have size at least $2$, while the next increment
$$
5-4=1
$$
says exactly one block has size at least $3$. Since the block sizes sum to
$5$, they are
$$
3,2.
$$
Hence
$$
\boxed{J(C)=J_3(2)\oplus J_2(2).}
$$
:::
:::
