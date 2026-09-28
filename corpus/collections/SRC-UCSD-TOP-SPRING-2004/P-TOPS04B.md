---
schema: qual/card@1
id: P-TOPS04B
kind: problem
title: "Euler characteristic multiplies by degree for covering spaces"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Euler Characteristic
relations: []
review: draft
---

::: {.problem}
Let $E \to B$ be a $d$-sheeted covering map.
Prove that the Euler characteristic satisfies $\chi(E) = d \cdot \chi(B)$ if $B$ is a finite CW-complex.
:::

::: {.solution}
<1>1. Lift a finite CW structure on $B$ through the covering map $p:E\to B$.
::: {.proof}
Over each open cell $e^k\subset B$, the covering is trivial because $e^k$ is contractible. Thus $p^{-1}(e^k)$ is a disjoint union of $d$ open cells, each mapped homeomorphically onto $e^k$.
:::

<1>2. If $c_k(B)$ denotes the number of $k$-cells of $B$, then
$$
c_k(E)=d\,c_k(B).
$$
::: {.proof}
Each cell has exactly $d$ lifts in a $d$-sheeted covering.
:::

<1>3. Therefore
$$
\chi(E)=\sum_k(-1)^kc_k(E)
=d\sum_k(-1)^kc_k(B)
=d\chi(B).
$$
::: {.proof}
Substitute <1>2 into the cellular formula for Euler characteristic.
:::
:::
