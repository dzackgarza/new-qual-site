---
schema: qual/card@1
id: P-STSCQ
kind: problem
title: Orders of elements of $\mathrm{SL}_2(\ZZ)$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Cyclic Groups
relations: []
review: draft
---

::: {.problem}
What are all possible orders of elements of $\SL_2(\ZZ)$?
:::

::: {.solution}
The possible orders are
\[
1,2,3,4,6,\quad\text{and }\infty.
\]

Let $A\in SL_2(\ZZ)$ have finite order. Its eigenvalues are roots of unity and their product is $1$. Thus
\[
\chi_A(x)=x^2-(\operatorname{tr}A)x+1.
\]
Since the eigenvalues lie on the unit circle,
\[
|\operatorname{tr}A|\le2.
\]
The trace is an integer, so
\[
\operatorname{tr}A\in\{-2,-1,0,1,2\}.
\]
Because $A$ has finite order in characteristic $0$, its minimal polynomial divides a separable polynomial $x^m-1$, so $A$ is diagonalizable over $\CC$.

- If $\operatorname{tr}A=2$, both eigenvalues are $1$, hence $A=I$ and $|A|=1$.
- If $\operatorname{tr}A=-2$, both eigenvalues are $-1$, hence $A=-I$ and $|A|=2$.
- If $\operatorname{tr}A=-1$, Cayley--Hamilton gives $A^2+A+I=0$, so $A^3=I$ and $|A|=3$.
- If $\operatorname{tr}A=0$, then $A^2+I=0$, so $|A|=4$.
- If $\operatorname{tr}A=1$, then $A^2-A+I=0$, whence $A^3=-I$ and $|A|=6$.

All five finite orders occur, for example via
\[
I,\quad -I,\quad
\begin{pmatrix}0&-1\\1&-1\end{pmatrix},\quad
\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
\begin{pmatrix}0&-1\\1&1\end{pmatrix}.
\]
Finally,
\[
\begin{pmatrix}1&1\\0&1\end{pmatrix}^k
=\begin{pmatrix}1&k\\0&1\end{pmatrix}
\]
for $k\ge1$, so infinite order also occurs.
:::
