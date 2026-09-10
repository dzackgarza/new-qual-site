---
schema: qual/card@1
id: E-MUN-10-1
kind: problem
title: Well-ordered sets have the least upper bound property
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 10, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show that every well-ordered set has the least upper bound property.
:::

::: {.solution}
Let \(A\) be a well-ordered set, and let \(B\subset A\) be nonempty and bounded above. The set
\[
U=\{u\in A:b\le u\text{ for every }b\in B\}
\]
of upper bounds is nonempty. Since \(A\) is well-ordered, \(U\) has a smallest element \(u_0\). By definition \(u_0\) is an upper bound of \(B\), and no smaller element is an upper bound. Hence
\[
u_0=\sup B.
\]
Thus every well-ordered set has the least upper bound property.
:::
