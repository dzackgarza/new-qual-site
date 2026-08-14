---
schema: qual/card@1
id: FT-J7RQV
kind: theorem
title: 'Urysohn''s Lemma'
classification:
  areas:
  - topology
  topics:
  - separation-axioms
  - continuity
relations:
- kind: variant-of
  target: FT-52GNK
review: draft
---

::: {.theorem title="Urysohn's Lemma"}
A space $X$ is normal iff for every pair of **disjoint** closed sets $U, V \subseteq X$ there is a continuous $f: X\to [0,1]$ with $\ro f U = 0$ and $\ro f V = 1$.
:::

::: {.remark}
Munkres, *Topology*, §33, Theorem 33.1, which states it for disjoint closed $A, B$ and any closed interval $[a,b]$.

Disjointness is not decoration: without it take $U = V$ nonempty and no such $f$ exists.
:::
