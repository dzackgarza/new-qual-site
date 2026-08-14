---
schema: qual/card@1
id: D-QYLPH
kind: definition
title: "Measures on measurable spaces"
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
relations: []
review: draft
---
:::{.definition title="Measures on measurable spaces"}
If $(X, \mcm)$ is a measurable space, then a **measure** is a function $\mu: \mcm \to [0,\infty]$ such that 

1. $\mu(\emptyset) = 0$.
2. Countable additivity: if $\ts{E_k}_{k\geq 1}$ is a countable union of disjoint sets in $X$, then 
\[
\mu\qty{\disjoint_{k\geq 1} E_k} = \sum_{k\geq 1} \mu(E_k)
.\]

If (2) only holds for finitely indexed sums, we say $\mu$ is **$\sigma\dash$additive**.
:::
