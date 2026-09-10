---
schema: qual/card@1
id: P-TOP-WORKSHOP-D4-W1
kind: problem
title: A neighborhood characterization of closure (workshop warm-up)
classification:
  areas:
  - topology
  topics:
  - Closure
  - Point-Set Topology
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
For a set $A\subset X$, $\overline A$ is defined to be the intersection of all closed sets containing $A$.
Using this definition, show: $x\in\overline A$ if and only if every open set $U$ containing $x$ intersects $A$.
:::

::: {.solution}
Suppose first that \(x\in\overline A\). If some open set \(U\ni x\) were disjoint from \(A\), then \(X\setminus U\) would be a closed set containing \(A\) but not \(x\). This contradicts the definition of \(\overline A\) as the intersection of all closed sets containing \(A\). Hence every open neighborhood of \(x\) meets \(A\).

Conversely, suppose every open neighborhood of \(x\) meets \(A\). If \(x\notin\overline A\), then by the defining intersection there is a closed set \(F\supseteq A\) with \(x\notin F\). Its complement \(X\setminus F\) is an open neighborhood of \(x\) disjoint from \(A\), contradiction. Therefore \(x\in\overline A\).
:::
