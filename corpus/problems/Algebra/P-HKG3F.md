---
schema: qual/card@1
id: P-HKG3F
kind: problem
title: Groups of order 14
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Normal Subgroups
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
Classify groups of order 14. Why is there a group of order 7? Are all index-2 subgroups normal?
:::


::: {.solution}
Let $|G|=14=2\cdot7$.

<1>1. There is a unique subgroup $N$ of order $7$, and it is normal.
::: {.proof}
Sylow gives
\[
n_7\mid2,
\qquad
n_7\equiv1\pmod7.
\]
Hence $n_7=1$. The subgroup exists by Sylow's first theorem and is cyclic because it has prime order.
:::

<1>2. Every subgroup of index $2$ in any group is normal.
::: {.proof}
If $H\le G$ has index $2$, there are exactly two left cosets and two right cosets. Both decompositions contain $H$ itself, so the unique remaining left coset equals the unique remaining right coset. Hence $gH=Hg$ for every $g$, so $H\trianglelefteq G$.
:::

<1>3. Let $P$ be a Sylow $2$-subgroup. Then
\[
G\cong C_7\rtimes C_2.
\]
::: {.proof}
The subgroup $N\cong C_7$ is normal, $P\cong C_2$, and $N\cap P=1$. Their product has order $14$, so it is all of $G$.
:::

<1>4. There are exactly two isomorphism types of groups of order $14$.
::: {.proof}
The action in the semidirect product is a homomorphism
\[
C_2\to\operatorname{Aut}(C_7)\cong C_6.
\]
There are two possibilities for the image: trivial, or the unique subgroup of order $2$.

The trivial action gives
\[
C_7\times C_2\cong C_{14}.
\]
The nontrivial action is inversion on $C_7$ and gives the dihedral group of order $14$.
:::

Thus the groups of order $14$ are exactly $C_{14}$ and the dihedral group $D_{14}$ (often denoted $D_7$ when the subscript records the polygon rather than the group order).
:::
