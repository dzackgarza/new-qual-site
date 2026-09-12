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

::: problem
Let $A$ be an $n\times n$ matrix with all entries equal to $0$ except for the $n-1$ entries just above the diagonal being equal to 2.

a. What is the Jordan canonical form of $A$, viewed as a matrix in $M_n(\CC)$?

b. Find a nonzero matrix $P\in M_n(\CC)$ such that $P\inv A P$ is in Jordan canonical form.
:::

::: solution
Let $J_n(0)$ denote the nilpotent Jordan block with $1$'s on the superdiagonal. Then $A=2J_n(0)$. Since $A^{n-1}\ne0$ and $A^n=0$, its minimal polynomial is $x^n$; hence its Jordan form consists of one block, namely $J_n(0)$.

For the standard basis $e_1,\ldots,e_n$, set
\[
v_j=2^{-(j-1)}e_j\qquad(1\le j\le n).
\]
Then $Av_1=0$ and, for $j\ge2$,
\[
Av_j=2^{-(j-1)}(2e_{j-1})=v_{j-1}.
\]
Thus in the ordered basis $(v_1,\ldots,v_n)$ the matrix is $J_n(0)$. Taking
\[
P=\operatorname{diag}(1,2^{-1},2^{-2},\ldots,2^{-(n-1)})
\]
gives $P^{-1}AP=J_n(0)$.
:::
