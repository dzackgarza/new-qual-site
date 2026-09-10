---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS4A-HW2
kind: problem
title: A $\Delta$-complex structure and homology of $S^1$
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Give a $\Delta$-complex structure for $S^1$, and use that to compute the homology groups for $S^1$.
:::

::: {.solution}
Give \(S^1\) the \(\Delta\)-complex structure with one vertex \(v\) and one \(1\)-simplex \(e\) whose two endpoints are both identified with \(v\). Then
\[
0\longrightarrow C_1\cong\mathbb Z
\xrightarrow{\partial_1}
C_0\cong\mathbb Z
\longrightarrow0.
\]
Since both endpoints of \(e\) are \(v\),
\[
\partial_1e=v-v=0.
\]
Therefore
\[
H_1(S^1)\cong\ker\partial_1\cong\mathbb Z,
\qquad
H_0(S^1)\cong C_0/\operatorname{im}\partial_1\cong\mathbb Z,
\]
and \(H_n(S^1)=0\) for \(n\ge2\).
:::
