---
schema: qual/card@1
id: E-MUN-6-2
kind: problem
title: Subsets of finite sets are finite
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 6, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show that if $B$ is not finite and $B \subset A$, then $A$ is not finite.
:::

::: {.solution}
Suppose, toward a contradiction, that \(A\) were finite. Every subset of a finite set is finite: if \(|A|=n\), identify \(A\) with \(\{1,\dots,n\}\); then the image of \(B\) is a subset of this finite set and hence is finite, so \(B\) is finite as well. This contradicts the hypothesis that \(B\) is not finite.

Therefore
\[
B\subset A\text{ and }B\text{ infinite}\quad\Longrightarrow\quad A\text{ infinite}.
\]
Equivalently, this is the contrapositive of the statement that every subset of a finite set is finite.
:::
