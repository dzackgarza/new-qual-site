---
schema: qual/card@1
id: P-RAF24C
kind: problem
title: First-countable TVS with sequential Cauchy completeness is net-complete
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Continuity
relations: []
review: draft
solved: false
---

::: problem
Let $X$ be a topological vector space. A net (or, less generally, a sequence) $\langle x_\alpha \rangle_{\alpha \in A}$ in $X$ is *Cauchy* if the net of pairwise differences $\langle x_\alpha - x_\beta \rangle_{(\alpha,\beta) \in A \times A}$, with $A \times A$ directed by the rule $(\alpha, \beta) \preceq (\alpha', \beta') \Leftrightarrow (\alpha \preceq \alpha' \text{ and } \beta \preceq \beta')$, converges to $0 \in X$. Prove that if $X$ is first countable and every Cauchy sequence in $X$ converges, then every Cauchy net in $X$ converges.
:::
