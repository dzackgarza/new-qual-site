---
schema: qual/card@1
id: P-BJDIE
kind: problem
title: Order of $\GL_n(\FF_q)$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Finite Fields
  - Bases
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Show that the order of the group $\mathrm{GL}_n(\mathbb{F}_q)$ of invertible $n\times n$ matrices over the field $\mathbb{F}_q$ of $q$ elements is $(q^n-1)(q^n-q)\cdots(q^n-q^{n-1})$.
:::


::: {.solution}
An invertible $n\times n$ matrix over $\FF_q$ is the same thing as an ordered basis of the vector space $\FF_q^n$, namely its ordered list of columns.

<1>1. The first column can be any nonzero vector, giving $q^n-1$ choices.
::: {.proof}
There are $q^n$ vectors in $\FF_q^n$, and only the zero vector is forbidden.
:::

<1>2. After choosing $k$ linearly independent columns, the next column has $q^n-q^k$ choices.
::: {.proof}
The span of $k$ independent vectors is a $k$-dimensional subspace, hence has $q^k$ elements. The next column must lie outside that span.
:::

<1>3. Therefore
\[
|\GL_n(\FF_q)|=(q^n-1)(q^n-q)(q^n-q^2)\cdots(q^n-q^{n-1}).
\]
::: {.proof}
Choose the columns successively and multiply the numbers of choices from <1>1 and <1>2.
:::
:::
