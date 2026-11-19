---
schema: qual/card@1
id: T-PRMDC
kind: theorem
title: Primary decomposition in a principal ideal domain
slogan: 'In a PID every ideal is a finite intersection of primary ideals, one for each prime in the factorization of its generator.'
classification:
  areas:
  - algebra
  topics:
  - Primary Ideals
  - Principal Ideal Domains
relations: []
review: draft
---

::: {.theorem}
Let $R$ be a [[D-HTIL5|principal ideal domain]] and $I\subseteq R$ a proper nonzero ideal.
Then $I$ is a finite intersection of [[D-JGYK4|primary ideals]], namely
$$
\generators a = \bigcap_{i=1}^k \generators{p_i^{e_i}},
$$
where $a = u\,p_1^{e_1}\cdots p_k^{e_k}$ is the factorization of a generator $a$ into a unit and powers of distinct primes.
:::

::: {.proof}
A principal ideal domain is a [[D-INULL|unique factorization domain]], so $a$ has such a factorization, unique up to order and units.

Each $\generators{p_i^{e_i}}$ is primary.
If $xy \in \generators{p_i^{e_i}}$ and $x\notin \generators{p_i^{e_i}}$, then $p_i$ divides $x$ to a power smaller than $e_i$, while $p_i^{e_i}$ divides $xy$; comparing the exponent of $p_i$ on both sides gives $p_i\divides y$, hence $y^{e_i} \in \generators{p_i^{e_i}}$.

The intersection is $\generators a$: the ideal $\generators a$ lies in every $\generators{p_i^{e_i}}$, and conversely an element $b$ lying in all of them is divisible by $p_i^{e_i}$ for every $i$, hence by the product $a$, since the $p_i$ are distinct primes and $R$ is a unique factorization domain.
:::
