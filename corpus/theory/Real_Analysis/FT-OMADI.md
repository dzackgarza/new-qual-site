---
schema: qual/card@1
id: FT-OMADI
kind: theorem
title: Continuity of measure from below and from above
prompts:
- State continuity of measure from above and from below.
classification:
  areas:
  - real-analysis
  topics:
  - Continuity of Measure
  - Measure Theory
relations: []
review: draft
---

::: {.theorem}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space and let $(E_i)_{i\geq1}$ be a sequence in $\mcm$.

1. **From below.** If $E_1\subseteq E_2\subseteq\cdots$ and $E=\bigcup_{i\geq1} E_i$, then $\mu(E_i) \to \mu(E)$.

2. **From above.** If $E_1\supseteq E_2\supseteq\cdots$, $E=\bigcap_{i\geq1} E_i$, and $\mu(E_1) < \infty$, then $\mu(E_i) \to \mu(E)$.
:::
