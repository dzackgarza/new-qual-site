---
schema: qual/card@1
id: P-SWIZT
kind: problem
title: When conjugacy classes of $S_n$ split in $A_n$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Permutations
relations: []
review: draft
---

::: {.problem}
When does an $S_n$-conjugacy class contained in $A_n$ split into two $A_n$-conjugacy classes?
:::

::: {.solution}
An $S_n$-conjugacy class contained in $A_n$ splits into two $A_n$-classes exactly when its cycle type consists of **distinct odd parts**.

Let $\sigma\in A_n$. Since $A_n\normal S_n$ has index $2$, the $S_n$-class of $\sigma$ either stays one $A_n$-class or splits into two equal $A_n$-classes. By orbit--stabilizer,
\[
|\operatorname{Cl}_{S_n}(\sigma)|=[S_n:C_{S_n}(\sigma)],
\qquad
|\operatorname{Cl}_{A_n}(\sigma)|=[A_n:C_{A_n}(\sigma)].
\]
The $S_n$-class splits exactly when
\[
C_{S_n}(\sigma)\subseteq A_n.
\]

Now inspect the centralizer from the cycle decomposition of $\sigma$.

If an even cycle occurs, that cycle itself is an odd permutation lying in $C_{S_n}(\sigma)$, so no splitting occurs.

If two cycles have the same odd length, there is a permutation interchanging those two cycles position-by-position. This centralizes $\sigma$ and is a product of an odd number of transpositions, hence is odd. Again no splitting occurs.

Conversely, suppose all cycle lengths are odd and pairwise distinct. Then every element of the centralizer must preserve each cycle support separately, because there are no equal-length cycles to permute. On each support it is a power of that odd cycle. Every power of an odd cycle is even. Hence every element of $C_{S_n}(\sigma)$ is even, so
\[
C_{S_n}(\sigma)\subseteq A_n.
\]
Therefore the class splits exactly for cycle types with distinct odd parts.
:::
