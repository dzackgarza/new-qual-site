---
schema: qual/card@1
id: FF-2AKVH
kind: fact
title: Factorization of $x^n + y^n$ for odd $n$
prompts:
- When does $x + y$ divide $x^n + y^n$, and what is the factorization?
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
Let $n\ge1$.
If $n$ is odd, then in $\ZZ[x,y]$
$$
x^n+y^n=(x+y)\sum_{k=0}^{n-1}(-1)^kx^{n-1-k}y^k .
$$
If $n$ is even, then $x+y$ does not divide $x^n+y^n$ in $\ZZ[x,y]$.
:::

::: {.proof}
For odd $n$, $(-y)^n=-y^n$, so substituting $a=-y$ in $x^n-a^n=(x-a)\sum_{k=0}^{n-1}a^kx^{n-1-k}$ ([[FF-ED3CD]]) gives the factorization.

Since $x+y$ is monic in $x$ over $\ZZ[y]$, division by $x+y$ in $(\ZZ[y])[x]$ shows that $x+y$ divides $f\in\ZZ[x,y]$ if and only if $f(-y,y)=0$.
For even $n$, $(-y)^n+y^n=2y^n\ne0$.
:::
