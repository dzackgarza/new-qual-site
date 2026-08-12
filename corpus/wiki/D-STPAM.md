---
schema: qual/card@1
id: D-STPAM
kind: definition
title: "Exact Sequence"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

::: {.definition title="Exact Sequence"}
A sequence of module morphisms
\[
\cdots \to A_{n+1} \mapsvia{d_{n+1}} A_n \mapsvia{d_n} A_{n-1} \to \cdots
\]
is **exact at $A_n$** iff $\im d_{n+1} = \ker d_n$, and **exact** iff it is exact at every term.
A chain complex only requires $\im d_{n+1}\subseteq \ker d_n$, so exactness is exactly the vanishing of its homology.
:::

::: {.concept}
See Hatcher, p. 113.
:::
