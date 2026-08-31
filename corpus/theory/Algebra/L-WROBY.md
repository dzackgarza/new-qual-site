---
schema: qual/card@1
id: L-WROBY
kind: lemma
title: $pq$ groups have normals the size of the biggest prime
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
If $\size G = pq$ with $p<q$ distinct primes, then $G$ has a normal subgroup of size $q$.
:::

::: {.proof}
Let $n_q$ be the number of Sylow $q$-subgroups of $G$.
By Sylow's third theorem, $n_q \equiv 1 \pmod q$ and $n_q \divides p$.
Since $p < q$, the only divisor of $p$ that is congruent to $1$ modulo $q$ is $1$ itself (the divisors of $p$ are $1$ and $p$, and $p < q$ means $p \not\equiv 1 \pmod q$).
Hence $n_q = 1$, so $G$ has a unique Sylow $q$-subgroup $Q$.
A unique Sylow subgroup is normal: for any $g \in G$, the conjugate $gQg^{-1}$ is again a Sylow $q$-subgroup, and by uniqueness $gQg^{-1} = Q$.
Therefore $Q \trianglelefteq G$, and $|Q| = q$.
:::
