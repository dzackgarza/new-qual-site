---
schema: qual/card@1
id: P-SPA3I
kind: problem
title: Examples of simple groups
classification:
  areas:
  - algebra
  topics:
  - Simple Groups
  - Classification
relations: []
review: draft
---

::: problem
Give examples of simple groups. Are there infinitely many?
:::

::: solution
A group is **simple** if it is nontrivial and has no normal subgroups other than $1$ and itself.

<1>1. Abelian examples:
For every prime $p$, the cyclic group
\[
C_p=\ZZ/p\ZZ
\]
is simple. Indeed, its subgroups have orders dividing $p$, so only the trivial subgroup and the whole group occur.

<1>2. Nonabelian examples:
For every $n\ge5$, the alternating group
\[
A_n
\]
is nonabelian simple.

Thus there are infinitely many simple groups even among finite groups. There are infinitely many abelian simple groups because there are infinitely many primes, and independently there are infinitely many pairwise nonisomorphic nonabelian simple groups $A_n$ for $n\ge5$.
:::
