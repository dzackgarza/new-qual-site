---
schema: qual/card@1
id: PR-LF7SW
kind: proposition
title: "Properties of Outer Measure"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
:::{.proposition title="Properties of Outer Measure"}
\envlist

1. Monotonicity: $E\subseteq F \implies m_*(E) \leq m_*(F)$.
2. Countable Subadditivity: $m_*(\union E_{i}) \leq \sum m_*(E_{i})$.
3. Approximation: For all $E$ there exists a $G \supseteq E$ such that $m_*(G) \leq m_*(E) + \varepsilon$.
4. Disjoint[^1] Additivity: $m_*(A \disjoint B) = m_*(A) + m_*(B)$. 

:::

[^1]: This holds for outer measure **iff** $\mathrm{dist}(A, B) > 0$.
