---
schema: qual/card@1
id: P-SIGK5
kind: problem
title: Jordan forms of a $5\times 5$ matrix with characteristic polynomial $(x-3)^5$
  and minimal polynomial $(x-3)^2$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Minimal and Characteristic Polynomials
relations: []
review: draft
---

::: {.problem}
Let $T$ be a $5\times 5$ complex matrix with characteristic polynomial $\chi(x) = (x-3)^5$ and minimal polynomial $m(x) = (x-3)^2$.
Determine all possible Jordan forms of $T$.
:::

::: {.solution}
The characteristic polynomial shows that the only eigenvalue is $3$, with
algebraic multiplicity $5$. Hence every Jordan block is a Jordan block for the
eigenvalue $3$, and the sum of the block sizes is $5$.

For a fixed eigenvalue, the exponent of $(x-3)$ in the minimal polynomial is
the size of the largest Jordan block. Since
\[
m_T(x)=(x-3)^2,
\]
the largest block has size exactly $2$. Therefore every block has size $1$ or
$2$, and at least one block has size $2$.

The only partitions of $5$ with parts in $\{1,2\}$ and at least one part $2$
are
\[
5=2+2+1
\qquad\text{and}\qquad
5=2+1+1+1.
\]
Thus, up to permutation of Jordan blocks, the only possible Jordan forms are
\[
\boxed{J_2(3)\oplus J_2(3)\oplus[3]}
\]
and
\[
\boxed{J_2(3)\oplus[3]\oplus[3]\oplus[3]},
\]
where
\[
J_2(3)=\begin{pmatrix}3&1\\0&3\end{pmatrix}.
\]
Both forms have characteristic polynomial $(x-3)^5$ and minimal polynomial
$(x-3)^2$, so both occur.
:::
