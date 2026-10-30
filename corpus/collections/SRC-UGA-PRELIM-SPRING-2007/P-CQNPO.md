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

(a) A function $f:\RR\to\RR$ which satisfies $f(x)=0$ for all $x\le 0$, but which is nonzero for $x>0$ and has derivatives of all orders for all $x$.

(b) An infinite-dimensional vector space over the field $\ZZ/2\ZZ$.

(c) A matrix in $M_2(\CC)$ which is not diagonalizable.

(d) A power series $\sum_{n=0}^\infty a_n z^n \in \CC[[z]]$ with radius of convergence $0$.
:::

::: {.solution}

::: pf

::: pf-step
For part (a), take
$$
f(x)=
\begin{cases}
0,&x\le0,\\
e^{-1/x},&x>0.
\end{cases}
$$
This function is $C^\infty$ on $\RR$, vanishes on $(-\infty,0]$, and is nonzero for every $x>0$.

:::

::: pf-step
For part (b), take the polynomial ring
$$
(\ZZ/2\ZZ)[x]
$$
viewed as a vector space over $\ZZ/2\ZZ$. Its basis $1,x,x^2,\dots$ is infinite.

:::

::: pf-step
For part (c), take
$$
\begin{pmatrix}0&1\\0&0\end{pmatrix}.
$$
It is not diagonalizable over $\CC$.

:::

::: pf-step
For part (d), take
$$
\sum_{n=0}^\infty n!\,z^n.
$$
Its radius of convergence is $0$.

:::

:::

:::
