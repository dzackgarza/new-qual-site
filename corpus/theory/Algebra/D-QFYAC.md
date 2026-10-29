---
schema: qual/card@1
id: D-QFYAC
kind: definition
title: Characteristic polynomial
prompts:
- What is the characteristic polynomial of a matrix $A$?
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Determinants
  - Matrices
relations: []
review: draft
---

::: {.definition}
Let $R$ be a commutative [[D-GURUB|ring]] and $A\in\Mat_{n\times n}(R)$.
The \dfn{characteristic polynomial} of $A$ is
$$
\chi_A(x) \coloneqq \det(xI - A)\in R[x].
$$
:::

::: {.remark}
$\chi_A$ is monic of degree $n$.
Some texts define the characteristic polynomial as $\det(A-xI)=(-1)^n\chi_A(x)$.
:::
