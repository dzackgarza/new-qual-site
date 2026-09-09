---
schema: qual/card@1
id: P-J77DY
kind: problem
title: No simple group of order $p^2 q^2$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Show that no group of order $p^2q^2$ is simple for primes $p<q$.
:::

::: {.solution}
Every group of order $p^2q^2$ has a normal Sylow subgroup, so it cannot be simple.

<1>1. Let $n_q$ be the number of Sylow $q$-subgroups. Then $n_q=1$ unless $(p,q)=(2,3)$.
::: {.proof}
Sylow gives $n_q\mid p^2$ and $n_q\equiv1\pmod q$. Hence $n_q\in\{1,p,p^2\}$, and $n_q=p$ is impossible because $1<p<q$. If $n_q=p^2$, then $q\mid p^2-1=(p-1)(p+1)$. Since $q>p$, this forces $q\mid p+1$, hence $q=p+1$. The only consecutive primes are $2$ and $3$.
:::

<1>2. In the exceptional case $|G|=36$, some Sylow subgroup is still normal.
::: {.proof}
If the Sylow $3$-subgroup is normal, we are done. Otherwise there are four Sylow $3$-subgroups, and conjugation on them gives a homomorphism $G\to S_4$. Its kernel has order divisible by $3$, hence is nontrivial and normal. If the kernel has order $9$, it is a normal Sylow $3$-subgroup. If it has order $3$, the image has order $12$ and is $A_4$; the inverse image of the normal Klein four subgroup of $A_4$ is a normal subgroup of order $12$. Its Sylow $2$-subgroup is unique (equivalently, characteristic in that preimage) and therefore normal in $G$.
:::

Thus $G$ always has a nontrivial proper normal subgroup and is not simple.
:::
