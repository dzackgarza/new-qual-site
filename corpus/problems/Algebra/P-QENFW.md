---
schema: qual/card@1
id: P-QENFW
kind: problem
title: Symmetric polynomials
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
  - Polynomials
relations: []
review: draft
---

::: problem
What are symmetric polynomials? State their fundamental structure theorem.
:::

::: {.solution}
A polynomial
\[
f(x_1,\dots,x_n)\in R[x_1,\dots,x_n]
\]
is **symmetric** if
\[
f(x_{\sigma(1)},\dots,x_{\sigma(n)})=f(x_1,\dots,x_n)
\]
for every permutation $\sigma\in S_n$.

The basic examples are the elementary symmetric polynomials
\[
e_k=\sum_{1\le i_1<\cdots<i_k\le n}x_{i_1}\cdots x_{i_k},
\qquad 1\le k\le n.
\]

The fundamental theorem of symmetric polynomials says that every symmetric polynomial $f$ can be written uniquely as a polynomial in
\[
e_1,\dots,e_n.
\]
Equivalently,
\[
R[x_1,\dots,x_n]^{S_n}=R[e_1,\dots,e_n].
\]
Thus the ring of symmetric polynomials is itself a polynomial ring on the elementary symmetric functions.
:::
