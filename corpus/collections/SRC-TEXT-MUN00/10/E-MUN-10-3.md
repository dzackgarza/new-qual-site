---
schema: qual/card@1
id: E-MUN-10-3
kind: problem
title: Order types of $\{1,2\} \times \mathbb{Z}_+$ and $\mathbb{Z}_+ \times \{1,2\}$
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 10, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Both $\{1,2\} \times \mathbb{Z}_{+}$ and $\mathbb{Z}_{+} \times \{1,2\}$ are well-ordered in the dictionary order.
Do they have the same order type?
:::

::: {.solution}
In dictionary order,
\[
\{1,2\}\times\mathbb Z_+
\]
has all pairs \((1,n)\) first, followed by all pairs \((2,n)\). In particular, the element \((2,1)\) has infinitely many predecessors, namely all \((1,n)\).

On the other hand,
\[
\mathbb Z_+\times\{1,2\}
\]
has the order
\[
(1,1)<(1,2)<(2,1)<(2,2)<(3,1)<(3,2)<\cdots.
\]
Every element has only finitely many predecessors.

The property of an element having infinitely many predecessors is preserved by order isomorphism. Hence these two well-ordered sets do not have the same order type. Their order types are, respectively, \(\omega+\omega\) and \(\omega\).
:::
