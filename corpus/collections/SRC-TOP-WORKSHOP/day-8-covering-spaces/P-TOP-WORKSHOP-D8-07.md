---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-07
kind: problem
title: Covering maps are open maps
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Continuity
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
(Purdue Jan ’07) Let $p:E\to B$ be a covering map.
Prove that $p$ takes open sets to open sets.
:::

::: {.solution}
Let \(O\subset E\) be open. For each \(e\in O\), choose an evenly covered neighborhood \(U_e\) of \(p(e)\), and let \(V_e\) be the sheet over \(U_e\) containing \(e\). Then
\[
O\cap V_e
\]
is open in \(V_e\), and the restriction \(p|_{V_e}:V_e\to U_e\) is a homeomorphism. Hence
\[
p(O\cap V_e)
\]
is open in \(U_e\), and therefore open in \(B\). Finally,
\[
p(O)=\bigcup_{e\in O}p(O\cap V_e),
\]
a union of open subsets of \(B\). Thus \(p\) is an open map.
:::
