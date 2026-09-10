---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS1B-HW1
kind: problem
title: Define a topology on a set (warm-up)
classification:
  areas:
  - topology
  topics:
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
What is a topology on a set?
:::

::: {.solution}
A topology on a set \(X\) is a collection \(\tau\subseteq\mathcal P(X)\) such that:

1. \(\varnothing\in\tau\) and \(X\in\tau\);
2. if \(\{U_\alpha\}_{\alpha\in A}\subseteq\tau\), then \(\bigcup_{\alpha\in A}U_\alpha\in\tau\);
3. if \(U_1,\dots,U_n\in\tau\), then \(U_1\cap\cdots\cap U_n\in\tau\).

The members of \(\tau\) are called the open subsets of \(X\), and the pair \((X,\tau)\) is a topological space.
:::
