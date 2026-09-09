---
schema: qual/card@1
id: E-MUN-10-4
kind: problem
title: Characterizing non-well-ordered sets via $\mathbb{Z}_{-}$
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 10, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) Let $\mathbb{Z}_{-}$ denote the set of negative integers in the usual order.
Show that a simply ordered set $A$ fails to be well-ordered if and only if it contains a subset having the same order type as $\mathbb{Z}_{-}$ .

(b) Show that if $A$ is simply ordered and every countable subset of $A$ is well-ordered, then $A$ is well-ordered.
:::

::: {.solution}
(a) If \(A\) contains a subset order-isomorphic to \(\mathbb Z_-\), then \(A\) is not well-ordered, since that subset has no smallest element.

Conversely, suppose \(A\) is not well-ordered. Then some nonempty subset \(B\subset A\) has no smallest element. Choose \(b_1\in B\). Since \(b_1\) is not smallest in \(B\), choose \(b_2\in B\) with \(b_2<b_1\). Continuing recursively, choose
\[
b_{n+1}<b_n.
\]
(The choice axiom, already available in this section of the text, justifies these successive choices.) Then
\[
\cdots<b_3<b_2<b_1,
\]
and the map
\[
-n\longmapsto b_n
\]
is an order isomorphism from \(\mathbb Z_-\) onto the subset \(\{b_n:n\ge1\}\subset A\).

(b) Suppose every countable subset of the simply ordered set \(A\) is well-ordered. If \(A\) were not well-ordered, part (a) would give a countable subset of \(A\) order-isomorphic to \(\mathbb Z_-\), which is not well-ordered. Contradiction. Hence \(A\) is well-ordered.
:::
