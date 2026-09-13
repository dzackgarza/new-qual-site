---
schema: qual/card@1
id: P-CQNPO
kind: problem
title: A $C^\infty$ function vanishing on $(-\infty,0]$ but not on $(0,\infty)$, an
  infinite-dimensional vector space over $\ZZ/2\ZZ$, a non-diagonalizable matrix in
  $M_2(\CC)$, and a power series with radius of convergence $0$
classification:
  areas:
  - prelim
  topics:
  - Counterexamples
  - Differentiation
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Give an example (proof not required) of each of the following:

a) A function $f:\mathbb{R}\to\mathbb{R}$ which satisfies $f(x)=0$ for all $x\le 0$, but which is nonzero for $x>0$ and has derivatives of all orders for all $x$.

b) An infinite-dimensional vector space over the field $\mathbb{Z}/2\mathbb{Z}$.

c) A matrix in $M_2(\mathbb{C})$ which is not diagonalizable.

d) A power series $\sum_{n=0}^\infty a_n z^n \in \mathbb{C}[[z]]$ with radius of convergence $0$.
:::


::: solution
<1>1. For part (a), take
\[
f(x)=
\begin{cases}
0,&x\le0,\\
e^{-1/x},&x>0.
\end{cases}
\]
This function is $C^\infty$ on $\mathbb R$, vanishes on $(-\infty,0]$, and is nonzero for every $x>0$.
:::

<1>2. For part (b), take the polynomial ring
\[
(\mathbb Z/2\mathbb Z)[x]
\]
viewed as a vector space over $\mathbb Z/2\mathbb Z$. Its basis $1,x,x^2,\dots$ is infinite.

<1>3. For part (c), take
\[
\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\]
It is not diagonalizable over $\mathbb C$.

<1>4. For part (d), take
\[
\sum_{n=0}^\infty n!\,z^n.
\]
Its radius of convergence is $0$.
