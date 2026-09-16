---
schema: qual/card@1
id: FD-GOB47
kind: definition
title: Characteristic polynomial of a matrix
prompts:
- What is the characteristic polynomial of a matrix $A$?
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Determinants
relations: []
review: draft
---

::: {.definition}
Let $k$ be a commutative ring and $A$ an $n\times n$ matrix over $k$.
The \dfn{characteristic polynomial} of $A$ is
$$
p_A(x) \coloneqq \det(xI_n - A)\in k[x],
$$
where $I_n$ is the $n\times n$ identity matrix.
:::
