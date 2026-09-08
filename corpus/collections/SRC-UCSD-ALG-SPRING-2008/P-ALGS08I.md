---
schema: qual/card@1
id: P-ALGS08I
kind: problem
title: "Example of a ring with right but not left minimum condition, and without nilpotent ideals"
classification:
  areas:
  - algebra
  topics:
  - Ring Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 9 of the official UCSD Spring 2008 algebra qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: "Verified the triangular-ring example by finite right-module length and an explicit infinite descending chain of left ideals; proved the semiprime variant impossible using the Artinian radical theorem and Wedderburn-Artin."
---

::: problem
Give an example of a ring with the right minimum condition, but not the left.
Can you find such an example with no nonzero nilpotent ideals?
Why?
:::

::: {.solution}
<1>1. Let $K\subset L$ be a field extension with $[L:K]=\infty$, and set
\[
R=
\begin{pmatrix}
K & L\\
0 & L
\end{pmatrix}.
\]
Then $R$ satisfies the minimum condition on right ideals.
::: {.proof}
Let
\[
e_1=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
 e_2=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}.
\]
As a right $R$-module,
\[
R_R=e_1R\oplus e_2R.
\]
The module $e_2R$ is simple: via
\[
\begin{pmatrix}
0&0\\
0&\ell
\end{pmatrix}
\longleftrightarrow \ell,
\]
its right action factors through the lower-right copy of the field $L$, so it is one-dimensional over $L$.

Inside $e_1R$, let
\[
N=
\left\{
\begin{pmatrix}
0&m\\
0&0
\end{pmatrix}:m\in L
\right\}.
\]
This is a simple right $R$-submodule, again one-dimensional over the lower-right copy of $L$.
Moreover,
\[
e_1R/N\cong K
\]
as a right module through the upper-left copy of $K$, hence is simple.
Thus $e_1R$ has composition length $2$, while $e_2R$ has composition length $1$.
Therefore $R_R$ has finite length, so it is Artinian.
Equivalently, $R$ satisfies the minimum condition on right ideals.
:::

<1>2. The ring $R$ does not satisfy the minimum condition on left ideals.
::: {.proof}
For every $K$-subspace $U\subseteq L$, define
\[
I_U=
\left\{
\begin{pmatrix}
0&u\\
0&0
\end{pmatrix}:u\in U
\right\}.
\]
For
\[
r=
\begin{pmatrix}
k&m\\0&\ell\end{pmatrix}
\quad\text{and}\quad
x=
\begin{pmatrix}0&u\\0&0\end{pmatrix},
\]
we have
\[
rx=
\begin{pmatrix}0&ku\\0&0\end{pmatrix}.
\]
Hence $I_U$ is a left ideal precisely because $U$ is a $K$-subspace.

Since $[L:K]=\infty$, choose $K$-linearly independent elements
\[
u_1,u_2,u_3,\ldots\in L.
\]
Set
\[
U_n=\operatorname{span}_K\{u_n,u_{n+1},u_{n+2},\ldots\}.
\]
Then
\[
U_1\supsetneq U_2\supsetneq U_3\supsetneq\cdots,
\]
so
\[
I_{U_1}\supsetneq I_{U_2}\supsetneq I_{U_3}\supsetneq\cdots
\]
is an infinite strictly descending chain of left ideals.
Thus $R$ is not left Artinian.
:::

<1>3. This example necessarily has a nonzero nilpotent ideal.
::: {.proof}
The ideal
\[
N=
\left\{
\begin{pmatrix}
0&m\\
0&0
\end{pmatrix}:m\in L
\right\}
\]
is nonzero and satisfies
\[
N^2=0.
\]
:::

<1>4. There is no example with the right minimum condition, not the left minimum condition, and no nonzero nilpotent ideals.
::: {.proof}
Suppose $A$ is right Artinian and has no nonzero nilpotent ideals.
For every right-Artinian ring, the Jacobson radical $J(A)$ is nilpotent.
Hence the hypothesis forces
\[
J(A)=0.
\]
Also, a right-Artinian ring modulo its Jacobson radical is semisimple Artinian.
Therefore
\[
A=A/J(A)
\]
is semisimple Artinian.
By the Wedderburn--Artin theorem, a semisimple Artinian ring is a finite product of full matrix rings over division rings, and in particular is Artinian on both the right and the left.
Thus a right-Artinian ring with no nonzero nilpotent ideals must also be left Artinian, so the requested stronger example cannot exist.
:::
:::
