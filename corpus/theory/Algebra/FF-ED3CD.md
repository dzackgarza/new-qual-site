---
schema: qual/card@1
id: FF-ED3CD
kind: fact
title: Factorization of $x^n - a^n$
prompts:
- How does $x^n - a^n$ factor?
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Factorization
relations: []
review: draft
---

::: {.fact}
Let $R$ be a commutative ring, let $a\in R$, and let $n\ge1$.
In $R[x]$,
$$
x^n-a^n=(x-a)\sum_{k=0}^{n-1}a^kx^{n-1-k}.
$$
:::

::: {.proof}
Expanding,
$$
(x-a)\sum_{k=0}^{n-1}a^kx^{n-1-k}=\sum_{k=0}^{n-1}a^kx^{n-k}-\sum_{k=1}^{n}a^kx^{n-k},
$$
and the two sums cancel except for the terms $x^n$ and $-a^n$.
:::
