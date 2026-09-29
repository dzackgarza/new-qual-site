---
schema: qual/card@1
id: P-TOPS23C
kind: problem
title: "Kernel of F_2 to S_3 sending generators to transpositions"
classification:
  areas:
  - topology
  topics:
  - Free Groups
  - Covering Spaces
  - Symmetric Groups
relations: []
review: draft
---

::: {.problem}
Let $F_2 = \langle a, b \rangle$ be the free group on $2$ letters and let $S_3$ be the symmetric group.
Let $K$ be the kernel of the homomorphism $F_2 \to S_3$ given by sending $a \mapsto (12)$, $b \mapsto (23)$.
To which well-known group is $K$ isomorphic?
:::

::: {.solution}

::: pf

::: pf-step
The map $F_2\to S_3$ is surjective.

::: pf-proof
The transpositions $(12)$ and $(23)$ generate $S_3$.
:::

:::

::: pf-step
Therefore its kernel $K$ has index $6$ in the rank-$2$ free group $F_2$.

::: pf-proof
By the first isomorphism theorem, $F_2/K\cong S_3$, which has six elements.
:::

:::

::: {.pf-step #nielsen-schreier-rank}
Nielsen--Schreier gives
$$\operatorname{rank}K=1+6(2-1)=7.$$

::: pf-proof
An index-$d$ subgroup of a free group of rank $r$ is free of rank $1+d(r-1)$.
:::

:::

::: pf-step
Hence
$$\boxed{K\cong F_7.}$$

::: pf-proof
Every subgroup of a free group is free, and step [](#nielsen-schreier-rank){.pf-ref} determines its rank.
:::

:::

:::

:::
