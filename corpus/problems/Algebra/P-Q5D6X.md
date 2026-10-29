---
schema: qual/card@1
id: P-Q5D6X
kind: problem
title: Number of invertible matrices over $\FF_p$
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

::: pf

::: {.pf-step #columns}
A matrix in $\Mat_n(\FF_p)$ is invertible if and only if, for each $k=0,\ldots,n-1$, its column $c_{k+1}$ lies outside the span of $c_1,\ldots,c_k$.

::: pf-proof
A matrix is invertible exactly when its columns form a basis of $\FF_p^n$, that is, when they are linearly independent, and a list is linearly independent exactly when no vector lies in the span of the earlier ones.
:::

:::

::: pf-step
There are $\boxed{\prod_{k=0}^{n-1}(p^n-p^k)=p^{n(n-1)/2}\prod_{j=1}^n(p^j-1)}$ invertible $n\times n$ matrices over $\FF_p$.

::: pf-proof
By step [](#columns){.pf-ref}, choose the columns in order. Once $c_1,\ldots,c_k$ are chosen linearly independent, their span has $p^k$ elements, so $c_{k+1}$ has $p^n-p^k$ choices. The second form follows from $p^n-p^k=p^k(p^{n-k}-1)$ and $\sum_{k=0}^{n-1}k=n(n-1)/2$.
:::

:::

:::

:::
