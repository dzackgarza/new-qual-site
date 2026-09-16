---
schema: qual/card@1
id: FD-SZKGS
kind: definition
title: Polynomial ring $K[x]$
prompts:
- What are the elements of the polynomial algebra $K[x]$?
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Rings
relations:
- kind: variant-of
  target: FD-CI4NB
- kind: variant-of
  target: FD-24RNF
review: draft
---

::: {.definition}
Let $K$ be a commutative [[D-GURUB|ring]].
The \dfn{polynomial ring} in the variable $x$ over $K$ is
$$
K[x] \coloneqq \theset{\sum_{i=0}^n a_ix^i \st n\in \ZZ^{\geq 0},\ a_0,\ldots,a_n\in K},
$$
where two polynomials are equal when their coefficients of $x^i$ agree for every $i\geq0$, with missing coefficients taken to be $0$.
Addition is coefficientwise, and multiplication is $\bigl(\sum_i a_ix^i\bigr)\bigl(\sum_j b_jx^j\bigr)=\sum_k\bigl(\sum_{i+j=k}a_ib_j\bigr)x^k$.
:::
