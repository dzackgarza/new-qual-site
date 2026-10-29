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
For nonzero $f\in\ZZ[x]$, let $c(f)$ be the gcd of its coefficients; $f$ is $\dfn{primitive}$ if $c(f)=1$.

::: pf

::: {.pf-step #gauss}
(Gauss's lemma.) A product of primitive polynomials in $\ZZ[x]$ is primitive.

::: pf-proof
If a prime $p$ divides every coefficient of $gh$, then $\bar g\bar h=0$ in the domain $\FF_p[x]$, so $p$ divides every coefficient of $g$ or of $h$.
:::

:::

::: {.pf-step #descent}
If $f\in\ZZ[x]$ is primitive and $f=gh$ with $g,h\in\QQ[x]$, then $f=g_0h_0$ with $g_0,h_0\in\ZZ[x]$ primitive, $g_0\in\QQ^\times g$ and $h_0\in\QQ^\times h$.

::: pf-proof
Write $g=a\,g_0$ and $h=b\,h_0$ with $a,b\in\QQ^\times$ and $g_0,h_0\in\ZZ[x]$ primitive, by clearing denominators and dividing out contents. Then $f=ab\,g_0h_0$, and $g_0h_0$ is primitive by step [](#gauss){.pf-ref}. Writing $ab=r/s$ in lowest terms, $sf=r\,g_0h_0$; comparing contents gives $s=\pm r$, so $ab=\pm1$.
:::

:::

::: pf-step
A primitive $f\in\ZZ[x]$ of positive degree is irreducible in $\ZZ[x]$ if and only if it is irreducible in $\QQ[x]$. For arbitrary nonzero $f\in\ZZ[x]$, $f=c(f)f_0$ with $f_0$ primitive, and the factorizations of $f$ into nonconstant factors in $\QQ[x]$ correspond, up to rational scalars, to the factorizations of $f_0$ into primitive nonconstant factors in $\ZZ[x]$.

::: pf-proof
A factorization in $\ZZ[x]$ into nonconstant factors is one in $\QQ[x]$. Conversely, step [](#descent){.pf-ref} turns a factorization in $\QQ[x]$ into nonconstant factors into one in $\ZZ[x]$ of the same degrees. A primitive $f$ has no factorization in $\ZZ[x]$ with a constant non-unit factor. The second sentence is step [](#descent){.pf-ref} applied to $f_0$, since $f$ and $f_0$ differ by the scalar $c(f)$.
:::

:::

:::
:::
