---
schema: qual/card@1
id: E-MUN-1-9
kind: problem
title: DeMorgan's laws for arbitrary unions and intersections
classification:
  areas:
  - topology
  topics:
  - Fundamental Concepts
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Formulate and prove DeMorgan's laws for arbitrary unions and intersections.
:::

::: {.solution}
Fix a set \(X\) and a family \(\{A_i\}_{i\in I}\) of subsets of \(X\). The arbitrary DeMorgan laws are
\[
X-\bigcup_{i\in I}A_i
=
\bigcap_{i\in I}(X-A_i)
\]
and
\[
X-\bigcap_{i\in I}A_i
=
\bigcup_{i\in I}(X-A_i).
\]

For the first identity,
\[
\begin{aligned}
x\in X-\bigcup_iA_i
&\iff x\in X\text{ and }x\notin A_i\text{ for every }i\\
&\iff x\in X-A_i\text{ for every }i\\
&\iff x\in\bigcap_i(X-A_i).
\end{aligned}
\]
For the second,
\[
\begin{aligned}
x\in X-\bigcap_iA_i
&\iff x\in X\text{ and it is not true that }x\in A_i\text{ for every }i\\
&\iff x\in X\text{ and }x\notin A_i\text{ for at least one }i\\
&\iff x\in\bigcup_i(X-A_i).
\end{aligned}
\]
Thus both identities hold for arbitrary indexed families.
:::
