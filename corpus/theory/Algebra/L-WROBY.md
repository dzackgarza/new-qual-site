---
schema: qual/card@1
id: L-WROBY
kind: lemma
title: A group of order $pq$ with $p<q$ has a normal Sylow $q$-subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Classification
relations: []
review: draft
---

::: {.lemma}
Let $p<q$ be primes and let $G$ be a group with $\abs G=pq$.
Then $G$ has a [[D-EKE4Q|normal subgroup]] of order $q$.
:::

::: {.proof}
Let $n_q$ be the number of Sylow $q$-subgroups of $G$.
By [[FT-ZENUU|Sylow's third theorem]], $n_q\equiv1\pmod q$ and $n_q\divides p$.
The divisors of $p$ are $1$ and $p$, and $1<p<q$ gives $p\not\equiv1\pmod q$, so $n_q=1$ and $G$ has a unique Sylow $q$-subgroup $Q$.
For every $g\in G$, the conjugate $gQg^{-1}$ is again a Sylow $q$-subgroup, so $gQg^{-1}=Q$.
Therefore $Q\trianglelefteq G$, and $\abs Q=q$.
:::
