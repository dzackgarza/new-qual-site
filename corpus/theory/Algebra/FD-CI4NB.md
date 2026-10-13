---
schema: qual/card@1
id: FD-CI4NB
kind: definition
title: Polynomial ring $R[x]$
prompts:
- What is the polynomial ring $R[x]$?
- What are the elements of the polynomial ring $R[x]$?
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Rings
relations:
- kind: related-to
  target: FD-24RNF
review: draft
---

::: {.definition}
Let $R$ be a commutative [[D-GURUB|ring]].
The \dfn{polynomial ring} in the variable $x$ over $R$ is
$$
R[x] \coloneqq \theset{\sum_{i=0}^n a_ix^i \st n\in \ZZ_{\geq 0},\ a_0,\ldots,a_n\in R},
$$
where two polynomials are equal when their coefficients of $x^i$ agree for every $i\geq0$, with missing coefficients taken to be $0$.
Addition is coefficientwise, and multiplication is $\bigl(\sum_i a_ix^i\bigr)\bigl(\sum_j b_jx^j\bigr)=\sum_k\bigl(\sum_{i+j=k}a_ib_j\bigr)x^k$.
:::
