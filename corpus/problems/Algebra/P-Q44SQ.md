---
schema: qual/card@1
id: P-Q44SQ
kind: problem
title: Subgroups of order 5 in $S_5$ are transitive
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Subgroups
  - Group Actions
relations: []
review: draft
---

::: problem
Show that every subgroup of order $5$ in $S_5$ acts transitively on $\{1,2,3,4,5\}$.
:::

::: {.solution}
Let $H\le S_5$ have order $5$. Then $H$ is cyclic, say
\[
H=\langle\sigma\rangle
\]
with $\sigma\ne e$. Since $\sigma$ has order $5$, its cycle decomposition in $S_5$ must consist of a single $5$-cycle. Therefore the orbit of any point under $\langle\sigma\rangle$ has size $5$ and is the whole set.

Hence $H$ is transitive.
:::
