---
schema: qual/card@1
id: T-JEZZY
kind: theorem
title: Gauss's lemma
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

::: {.theorem}
Let $R$ be a [[D-INULL|unique factorization domain]] with [[D-OXIVT|field of fractions]] $F$, and let $p\in R[x]$ be [[D-4VC6X|primitive]].
Then $p$ is irreducible in $R[x]$ if and only if $p$ is [[D-BVMTZ|irreducible]] in $F[x]$.

More precisely, if $p=AB$ with $A,B\in F[x]$ nonconstant, then there exist $r,s\in F^\times$ with $rs=1$ such that $rA,sB\in R[x]$, so $p=(rA)(sB)$ is a factorization of $p$ in $R[x]$ into nonconstant polynomials.
:::

::: {.example}
Every monic polynomial in $R[x]$ is primitive, since its leading coefficient $1$ is a unit; so a monic $p\in\ZZ[x]$ is irreducible in $\ZZ[x]$ if and only if it is irreducible in $\QQ[x]$.
:::
