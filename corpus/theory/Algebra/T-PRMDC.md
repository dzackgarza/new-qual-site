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
where $a = u\,p_1^{e_1}\cdots p_k^{e_k}$ is the factorization of a generator $a$ into a unit and powers of distinct primes [@Hun74, chapter III, §3, Exercise 5(b)--(d)].
:::

::: {.remark}
Part (b) of that exercise identifies the primary ideals of a principal ideal domain as the ideals $\generators{p^n}$ with $p$ prime, together with the zero ideal, part (c) says that for distinct primes $p_1,\ldots,p_k$ the product $\generators{p_1^{e_1}}\cdots\generators{p_k^{e_k}}$ equals the intersection $\bigcap_i\generators{p_i^{e_i}}$, and part (d) says that every proper ideal is an intersection of finitely many primary ideals, unique up to order.
:::
