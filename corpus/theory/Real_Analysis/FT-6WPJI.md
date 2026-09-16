---
schema: qual/card@1
id: FT-6WPJI
kind: theorem
title: Baire category theorem
prompts:
- State the Baire category theorem.
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Completeness
  - Metric Spaces
relations: []
review: draft
---

::: {.theorem}
If $X$ is a complete metric space or a locally compact Hausdorff space, then $X$ is a [[D-VFNTY|Baire space]].
:::

::: {.corollary}
A nonempty complete metric space is not a countable union of [[D-2MJRE|nowhere dense]] subsets.
:::

::: {.proof}
Let $X$ be a nonempty complete metric space and suppose $X=\bigcup_{k\geq1}S_k$ with each $S_k$ nowhere dense.
Each $U_k\coloneqq X\setminus\overline{S_k}$ is open, and it is dense because $\overline{S_k}$ has empty interior.
By the theorem, $\bigcap_k U_k$ is dense in $X$, hence nonempty since $X\neq\emptyset$.
But $\bigcap_k U_k\subseteq X\setminus\bigcup_k S_k=\emptyset$, a contradiction.
:::
