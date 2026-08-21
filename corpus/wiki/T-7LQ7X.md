---
schema: qual/card@1
id: T-7LQ7X
kind: theorem
title: Properties of measures
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

:::{.theorem title="Properties of measures"}
Let $(X, \mcm, \mu)$ be a measure space.
Then

1. Monotonicity: $E \subseteq F \implies \mu(E) \leq \mu(F)$.
2. Countable subadditivity: If $ts{E_k}_{k\geq 1}$ is a countable collection, 
\[
\mu\qty{\Union_{k\geq 1} E_k} \leq \sum_{k\geq 1} \mu(E_k)
.\]
:::
