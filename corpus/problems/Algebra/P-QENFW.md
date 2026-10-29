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

::: {.problem}
What are symmetric polynomials? State their fundamental structure theorem.
:::

::: {.solution}
Let $R$ be a commutative ring. A polynomial $f\in R[x_1,\ldots,x_n]$ is symmetric if
$$f(x_{\sigma(1)},\ldots,x_{\sigma(n)})=f(x_1,\ldots,x_n)\quad\text{for every }\sigma\in S_n,$$
that is, if $f$ lies in the invariant ring $R[x_1,\ldots,x_n]^{S_n}$. The elementary symmetric polynomials are
$$e_k=\sum_{1\le i_1<\cdots<i_k\le n}x_{i_1}\cdots x_{i_k},\qquad 1\le k\le n.$$

::: pf

::: pf-step
(Fundamental theorem of symmetric polynomials.) Every symmetric polynomial is a polynomial in $e_1,\ldots,e_n$ in exactly one way:
$$\boxed{R[x_1,\ldots,x_n]^{S_n}=R[e_1,\ldots,e_n]},$$
and $e_1,\ldots,e_n$ are algebraically independent over $R$, so this ring is a polynomial ring in them.

::: pf-proof
This is the standard theorem, proved by induction on the leading monomial in the lexicographic order: if the leading monomial of a symmetric $f$ is $c\,x_1^{a_1}\cdots x_n^{a_n}$, then $a_1\ge\cdots\ge a_n$, and $f-c\,e_1^{a_1-a_2}\cdots e_{n-1}^{a_{n-1}-a_n}e_n^{a_n}$ is symmetric with a smaller leading monomial.
:::

:::

:::

:::
