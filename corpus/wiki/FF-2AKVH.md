---
schema: qual/card@1
id: FF-2AKVH
kind: fact
title: Factor $x^n + y^n$
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Factorization
relations:
- kind: variant-of
  target: FF-UC7SQ
review: draft
---

::: {.fact}
For $n$ odd,
$$
x^n + y^n = (x+y)\left(x^{n-1} + x^{n-2}(-y) + \cdots + (-y)^{n-1}\right)
$$
For $n$ even this fails: $x+y$ does not divide $x^n + y^n$.
:::
