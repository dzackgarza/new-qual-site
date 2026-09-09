---
schema: qual/card@1
id: P-OIG6K
kind: problem
title: An irreducible cubic with Galois group not in $A_3$ has Galois group $S_3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Classification
  - Permutations
relations: []
review: draft
---

::: problem
Let $f\in F[x]$ be an irreducible separable cubic. If its Galois group is not contained in $A_3$, prove that its Galois group is $S_3$.
:::

::: {.solution}
Let $L$ be the splitting field and
\[
G=\operatorname{Gal}(L/F)\le S_3
\]
via the action on the three roots.

Because $f$ is irreducible, $G$ acts transitively on its roots. Hence $3$ divides $|G|$. The transitive subgroups of $S_3$ are therefore $A_3$ and $S_3$: indeed, a subgroup with order divisible by $3$ contains the unique subgroup $A_3$ of order $3$, and its order is either $3$ or $6$.

By hypothesis $G\not\subseteq A_3$, so $G\ne A_3$. Consequently
\[
G=S_3.
\]
:::
