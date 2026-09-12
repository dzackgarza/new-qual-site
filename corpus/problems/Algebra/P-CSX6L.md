---
schema: qual/card@1
id: P-CSX6L
kind: problem
title: Conjugacy classes in $S_n$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Permutations
  - Partitions
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
Talk about conjugacy classes in the symmetric group $S_n$.
:::


::: {.solution}
<1>1. Two permutations in $S_n$ are conjugate if and only if they have the same cycle type.
::: {.proof}
If
\[
\sigma=(a_{11}\ \cdots\ a_{1r_1})\cdots(a_{k1}\ \cdots\ a_{kr_k}),
\]
then for any $g\in S_n$,
\[
g\sigma g^{-1}=(g(a_{11})\ \cdots\ g(a_{1r_1}))\cdots(g(a_{k1})\ \cdots\ g(a_{kr_k})),
\]
so conjugation preserves cycle lengths.

Conversely, if two permutations have the same multiset of cycle lengths, choose a bijection sending the entries of each cycle of the first permutation, in cyclic order, to the entries of a cycle of the same length in the second. Extending these bijections over all cycles gives $g\in S_n$ conjugating one permutation to the other.
:::

<1>2. Hence conjugacy classes in $S_n$ are indexed by partitions of $n$.
::: {.proof}
The cycle lengths of a permutation form a partition
\[
n=1^{m_1}2^{m_2}\cdots n^{m_n},
\qquad
\sum_i i m_i=n.
\]
By <1>1, this partition determines the conjugacy class and every partition occurs as a cycle type.
:::

<1>3. If a permutation has cycle type $1^{m_1}2^{m_2}\cdots n^{m_n}$, then its conjugacy class has size
\[
\frac{n!}{\prod_{i=1}^n i^{m_i}m_i!}.
\]
::: {.proof}
Its centralizer has order
\[
\prod_{i=1}^n i^{m_i}m_i!.
\]
Indeed, for each length $i$, one may independently rotate each of the $m_i$ cycles in $i^{m_i}$ ways and permute those equal-length cycles in $m_i!$ ways. Orbit-stabilizer for the conjugation action then gives the stated class size.
:::
:::
