---
schema: qual/card@1
id: P-QVCO4
kind: problem
title: $F[x]\oplus F$ as the cokernel of a $2\times 2$ Smith normal form matrix
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Smith Normal Form
  - Modules
relations: []
review: draft
---

::: problem
Construct a $2\times2$ matrix $A$ over $F[x]$ whose cokernel is
\[
F[x]\oplus F.
\]
:::

::: {.solution}
Choose any linear polynomial $f(x)\in F[x]$, for example
\[
f(x)=x+1.
\]
Since
\[
F[x]/(x+1)\cong F,
\]
we want a Smith normal form with one nonzero invariant factor $x+1$ and one zero diagonal entry.

Take
\[
A=
\begin{pmatrix}
x+1&0\\
0&0
\end{pmatrix}.
\]
Then
\[
\operatorname{coker}(A)
\cong
F[x]/(x+1)\oplus F[x]/(0)
\cong
F\oplus F[x].
\]
Thus, after reordering the summands,
\[
\operatorname{coker}(A)\cong F[x]\oplus F.
\]
:::
