---
schema: qual/card@1
id: P-BKF16-9A
kind: problem
title: Order of $\operatorname{GL}_n(\mathbb F_p)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2016 solution packet: an
    invertible matrix is exactly an ordered basis written as its columns.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the dimension and cardinality of each successive column span
    and every factor in the product.
---

::: {.problem}
Let p be a prime number, $\mathbb { F } _ { p }$ be the finite field of $p$ elements, and ${ \mathrm { G L } } _ { n } ( \mathbb { F } _ { p } )$ be the finite group of all invertible $n \times n$ matrices with coefficients in $\mathbb { F } _ { p } .$ . Find the order of ${ \mathrm { G L } } _ { n } ( \mathbb { F } _ { p } )$
:::

::: {.solution}
Let
$$
V=\FF_p^n.
$$

<1>1. An $n\times n$ matrix over $\FF_p$ is invertible if and only if
its columns form an ordered basis of $V$.

::: {.proof}
A square matrix is invertible exactly when its columns are linearly
independent. An independent family of $n$ vectors in the
$n$-dimensional space $V$ is a basis, and conversely every basis gives
an invertible matrix by using its vectors as columns.
:::

<1>2. The first column of an invertible matrix has
$$
p^n-1
$$
possible values.

::: {.proof}
The first column may be any nonzero vector of $V$. The vector space
$V$ has $p^n$ elements, exactly one of which is zero.
:::

<1>3. After linearly independent columns
$$
v_1,\ldots,v_j
$$
have been chosen, with $0\le j<n$, there are
$$
p^n-p^j
$$
choices for the next column.

::: {.proof}
The span
$$
\operatorname{span}\{v_1,\ldots,v_j\}
$$
has dimension $j$, hence contains $p^j$ vectors. The next column must
lie outside this span, leaving
$$
p^n-p^j
$$
choices.
:::

<1>4. Therefore
$$
\boxed{
\left|\operatorname{GL}_n(\FF_p)\right|
=
\prod_{j=0}^{n-1}(p^n-p^j)
=
(p^n-1)(p^n-p)\cdots(p^n-p^{n-1}).
}
$$

::: {.proof}
By step <1>1, count ordered bases column by column. Step <1>2 gives
the first factor and step <1>3 gives each remaining factor.
Multiplying the numbers of choices gives the displayed product.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested group order.
:::
:::
