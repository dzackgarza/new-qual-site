---
schema: qual/card@1
id: E-MUN-10-5
kind: problem
title: Well-ordering theorem implies the axiom of choice
classification:
  areas:
  - topology
  topics:
  - Well-Ordered Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 10, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show the well-ordering theorem implies the choice axiom.
:::

::: {.solution}
Let \(\mathcal A\) be a collection of nonempty sets. Put
\[
U=\bigcup_{A\in\mathcal A}A.
\]
By the well-ordering theorem, choose a well-order \(<\) on \(U\). For each \(A\in\mathcal A\), the subset \(A\) is nonempty, so it has a unique \(<\)-smallest element. Define
\[
c(A)=\min_{<}A.
\]
Then \(c(A)\in A\) for every \(A\in\mathcal A\). Thus \(c\) is a choice function on \(\mathcal A\), proving the axiom of choice.
:::
