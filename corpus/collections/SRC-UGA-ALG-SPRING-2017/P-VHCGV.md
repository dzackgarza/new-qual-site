---
schema: qual/card@1
id: P-VHCGV
kind: problem
title: Jordan form of the $n\times n$ matrix with $2$'s on the superdiagonal, and
  a change-of-basis matrix
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Nilpotence
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $A$ be an $n\times n$ matrix with all entries equal to $0$ except for the $n-1$ entries just above the diagonal being equal to 2.

a. What is the Jordan canonical form of $A$, viewed as a matrix in $M_n(\CC)$?

b. Find a nonzero matrix $P\in M_n(\CC)$ such that $P\inv A P$ is in Jordan canonical form.
:::

::: {.solution}
Let $e_1,\ldots,e_n$ denote the standard basis of $\mathbb C^n$, and let $J_n(0)$ be the nilpotent Jordan block with entries $1$ immediately above the diagonal.

<1>1. The Jordan canonical form of $A$ is
\[
\boxed{J_n(0)}.
\]

::: {.proof}
The matrix $A$ satisfies $Ae_1=0$ and $Ae_j=2e_{j-1}$ for $2\le j\le n$. Thus $A^n=0$ and $A^{n-1}e_n=2^{n-1}e_1\neq0$. Its minimal polynomial is therefore $x^n$. Because the exponent of $x$ in the minimal polynomial is the size of the largest nilpotent Jordan block, the Jordan form has a block of size $n$, and no other blocks can occur in an $n$-dimensional space.
:::

<1>2. An invertible change-of-basis matrix with the required property is
\[
\boxed{P=\operatorname{diag}(1,2^{-1},2^{-2},\ldots,2^{-(n-1)})}.
\]

::: {.proof}
Put $v_j=2^{-(j-1)}e_j$ for $1\le j\le n$. The vectors $v_j$ form a basis because each scalar $2^{-(j-1)}$ is nonzero. Moreover, $Av_1=0$ and for $j\ge2$,
\[
Av_j=2^{-(j-1)}(2e_{j-1})=v_{j-1}.
\]
Hence the matrix of $A$ in this basis is $J_n(0)$. Its change-of-basis matrix is precisely $P$, and consequently $P^{-1}AP=J_n(0)$.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 answer parts (a) and (b), respectively.
:::
:::
