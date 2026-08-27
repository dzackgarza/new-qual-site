---
schema: qual/card@1
id: FT-52GNK
kind: theorem
title: Urysohn's Lemma
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Continuity
relations: []
review: draft
---

::: {.theorem}
A space $X$ is normal iff for every pair of **disjoint** closed sets $U, V \subseteq X$ there is a continuous $f: X\to [0,1]$ with $\ro f U = 0$ and $\ro f V = 1$.
:::

::: {.remark}
Munkres, *Topology*, §33, Theorem 33.1. Disjointness is needed: without it take $U = V$ nonempty and no such $f$ exists.

This card previously closed with "Equivalently, a topological space is separable and metrizable iff it is regular, Hausdorff, and second-countable". That is the **Urysohn metrization theorem**, Munkres §34, Theorem 34.1 — a different theorem with a different conclusion, not an equivalent form of the lemma. The lemma is what metrization is proved *from*.
:::
