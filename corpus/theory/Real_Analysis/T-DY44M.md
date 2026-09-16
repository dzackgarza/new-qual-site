---
schema: qual/card@1
id: T-DY44M
kind: theorem
title: $\RR$ is a Baire space
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Metric Spaces
  - Completeness
relations: []
review: draft
---

::: {.theorem}
$\RR$ is a [[D-VFNTY|Baire space]].
Consequently, $\RR$ is not a countable union of [[D-2MJRE|nowhere dense]] subsets of $\RR$.
:::

::: {.proof}
The first statement is the Baire category theorem for the [[D-G5N6I|complete]] metric space $\RR$.
Suppose $\RR=\bigcup_{k\geq1}N_k$ with each $N_k$ nowhere dense.
Then each $U_k\coloneqq\RR\setminus\overline{N_k}$ is open and [[D-KJBAK|dense]], because $\overline{N_k}$ has empty interior, but $\bigcap_{k\geq1}U_k\subseteq\RR\setminus\bigcup_{k\geq1}N_k=\emptyset$ is not dense, contradicting the first statement.
:::
