---
schema: qual/card@1
id: E-OW8A0
kind: problem
title: The subspace metric
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $A \subset X$.
If $d$ is a metric for the topology of $X$, show that $d \mid A \times A$ is a metric for the subspace topology on $A$.
:::

::: {.solution}
The restriction $d_A=d|_{A\times A}$ is plainly a metric on $A$. For $a\in A$ and $r>0$, its open ball is
\[
B_{d_A}(a,r)=\{x\in A:d(a,x)<r\}=A\cap B_d(a,r).
\]
Thus every $d_A$-ball is open in the subspace topology. Conversely, if $U=A\cap V$ is subspace-open and $a\in U$, choose $r>0$ with
\[
B_d(a,r)\subseteq V.
\]
Then
\[
B_{d_A}(a,r)=A\cap B_d(a,r)\subseteq U.
\]
Hence the metric topology of $d_A$ is exactly the subspace topology.
:::
