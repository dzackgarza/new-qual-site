---
schema: qual/card@1
id: FF-UC7SQ
kind: fact
title: Factorization of $x^n - y^n$
prompts:
- How does $x^n - y^n$ factor?
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
For $n\ge1$, in $\ZZ[x,y]$,
$$
x^n-y^n=(x-y)\qty{x^{n-1}+x^{n-2}y+\cdots+xy^{n-2}+y^{n-1}}=(x-y)\sum_{k=0}^{n-1}x^{n-1-k}y^k.
$$
:::

::: {.proof}
This is [[FF-ED3CD]] over the commutative ring $R=\ZZ[y]$ with $a=y$.
:::
