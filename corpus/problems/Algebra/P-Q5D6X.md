---
schema: qual/card@1
id: P-Q5D6X
kind: problem
title: Number of invertible matrices over $\ZZ/p\ZZ$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Finite Fields
  - Bases
relations: []
review: draft
---

::: {.problem}
How many invertible $n\times n$ matrices are there over $\FF_p$?
:::

::: {.solution}
An invertible matrix is equivalent to an ordered basis of the vector space $\FF_p^n$.

Choose the columns successively. The first column can be any nonzero vector:
\[
p^n-1
\]
choices. After choosing $k$ linearly independent columns, their span has $p^k$ elements, so the next column has
\[
p^n-p^k
\]
choices.

Therefore
\[
|GL_n(\FF_p)|
=
(p^n-1)(p^n-p)(p^n-p^2)\cdots(p^n-p^{n-1}).
\]
Equivalently,
\[
|GL_n(\FF_p)|
=p^{n(n-1)/2}\prod_{j=1}^n(p^j-1).
\]
:::
