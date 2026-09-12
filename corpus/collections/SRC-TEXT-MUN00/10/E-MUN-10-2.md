---
schema: qual/card@1
id: E-MUN-10-2
kind: problem
title: Immediate successors in well-ordered sets
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 10, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) Show that in a well-ordered set, every element except the largest (if one exists) has an immediate successor.

(b) Find a set in which every element has an immediate successor that is not well-ordered.
:::

::: {.solution}
(a) Let \(a\) be an element of the well-ordered set \(A\) that is not largest. Then
\[
B=\{x\in A:a<x\}
\]
is nonempty. Let \(s\) be its smallest element. Then \(a<s\), and there is no \(x\) with
\[
a<x<s,
\]
for such an \(x\) would belong to \(B\) and be smaller than \(s\). Hence \(s\) is the immediate successor of \(a\).

(b) The integers \(\mathbb Z\) with their usual order are not well-ordered, since \(\mathbb Z\) itself has no smallest element. Nevertheless every \(n\in\mathbb Z\) has the immediate successor \(n+1\).
:::
