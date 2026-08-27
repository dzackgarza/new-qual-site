---
schema: qual/card@1
id: FF-HAMDC
kind: fact
title: Factor $x^n + a^n$
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
For $n$ odd,
$$
x^n + a^n = (x+a) \sum _{k=0}^{n-1} (-a)^k x^{n-1-k}
$$
For $n$ even this fails: $x+a$ does not divide $x^n + a^n$, since $-a$ is not a root.
:::
