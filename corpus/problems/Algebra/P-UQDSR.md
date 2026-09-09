---
schema: qual/card@1
id: P-UQDSR
kind: problem
title: A $k$-cycle as a product of transpositions
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
---

::: problem
Show directly that every $k$-cycle is a product of transpositions, and determine the minimum number of transpositions needed.
:::

::: solution
For a $k$-cycle
\[
\sigma=(a_1\ a_2\ \cdots\ a_k),
\]
one has
\[
\sigma
=(a_1\ a_k)(a_1\ a_{k-1})\cdots(a_1\ a_2),
\]
where products are composed from right to left. Thus every $k$-cycle is a product of $k-1$ transpositions.

This number is minimal. Multiplying a permutation by a transposition changes the number of cycles in its disjoint-cycle decomposition, counting fixed points, by exactly $1$: it either joins two cycles or splits one cycle into two.

The identity on the support $\{a_1,\ldots,a_k\}$ has $k$ cycles, while a $k$-cycle has one cycle. Therefore at least
\[
k-1
\]
transpositions are required to pass from the identity to a $k$-cycle.

Hence the minimum number is exactly
\[
\boxed{k-1}.
\]
:::
