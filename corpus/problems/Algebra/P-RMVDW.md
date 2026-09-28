---
schema: qual/card@1
id: P-RMVDW
kind: problem
title: 'Gauss''s lemma: factorisation in $\QQ[x]$ versus $\ZZ[x]$'
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Polynomials
  - Irreducibility Criteria
relations: []
review: draft
---

::: {.problem}
What does factorization over $\QQ[x]$ say about factorization over $\ZZ[x]$?
:::

::: {.solution}
For $f\in\ZZ[x]$, let $\operatorname{cont}(f)$ be the gcd of its coefficients. A polynomial is **primitive** if its content is $1$.

Gauss's lemma says that the product of primitive polynomials in $\ZZ[x]$ is primitive. Consequently, if a primitive polynomial $f\in\ZZ[x]$ factors in $\QQ[x]$,
\[
f=gh,\qquad g,h\in\QQ[x],
\]
with both factors nonconstant, then after clearing denominators and dividing out contents one obtains a factorization
\[
f=g_0h_0
\]
with nonconstant primitive $g_0,h_0\in\ZZ[x]$.

Therefore a primitive polynomial in $\ZZ[x]$ is irreducible in $\ZZ[x]$ if and only if it is irreducible in $\QQ[x]$.

For arbitrary $f\in\ZZ[x]$, write
\[
f=c(f)f_0
\]
with $f_0$ primitive. The nonconstant factorization theory of $f$ over $\QQ[x]$ is exactly that of its primitive part $f_0$ over $\ZZ[x]$; only the integer content changes.
:::
