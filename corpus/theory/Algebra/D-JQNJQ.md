---
schema: qual/card@1
id: D-JQNJQ
kind: definition
title: Elementary divisor decomposition
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Abelian Groups
  - Classification
relations: []
review: draft
---

::: {.definition}
Let $G$ be a finitely generated abelian group, and for $n\geq 1$ let $C_n$ denote the cyclic group of order $n$.
An \dfn{elementary divisor decomposition} of $G$ is an isomorphism
$$
G \cong \ZZ^r \times \prod_{k=1}^m C_{p_k^{e_k}}
$$
with $r,m\geq 0$, primes $p_1,\ldots,p_m$ that need not be distinct, and exponents $e_1,\ldots,e_m\geq 1$.
The prime powers $p_1^{e_1},\ldots,p_m^{e_m}$ are the \dfn{elementary divisors} of $G$.
:::

::: {.theorem}
Every finitely generated abelian group $G$ has an elementary divisor decomposition.
The integer $r$ and the list $p_1^{e_1},\ldots,p_m^{e_m}$, up to reordering, are uniquely determined by $G$.
:::
