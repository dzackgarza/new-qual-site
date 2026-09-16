---
schema: qual/card@1
id: FT-OXN3Y
kind: theorem
title: Gauss' lemma
prompts:
- State Gauss' lemma.
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
Let $R$ be a [[D-INULL|unique factorization domain]] with [[D-OXIVT|field of fractions]] $F$, and let $p\in R[x]$.
If $p=gh$ with $g,h\in F[x]$ and $\deg g,\deg h\ge1$, then there are $g',h'\in R[x]$ with $\deg g'=\deg g$, $\deg h'=\deg h$, and $p=g'h'$.
In particular, if $p$ is [[D-BVMTZ|reducible]] in $F[x]$, then $p$ is reducible in $R[x]$.
:::

::: {.remark}
Gauss' lemma is the main step in the proof that $R[x]$ is a unique factorization domain whenever $R$ is.
By induction, $R[x_1,\ldots,x_n]$ is a unique factorization domain, and so is the polynomial ring over $R$ in any set of variables, since each polynomial involves finitely many variables.
:::
