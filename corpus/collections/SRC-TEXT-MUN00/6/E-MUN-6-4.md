---
schema: qual/card@1
id: E-MUN-6-4
kind: problem
title: Finite simply ordered sets have a largest element
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 6, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §6 Exercise 4, printed p. 44; both parts are
    stored as printed, including the hint to induct on the cardinality.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 6.4,
    printed pp. 76-78 (tmp/sources/munkres-solutions-whitman.pdf), both inductions on the
    cardinality: removing one element, applying the hypothesis, and comparing that
    element with the largest element of the rest. The card's (b) extends the order
    isomorphism of A' by the largest element, which is his construction. No defect found.
---

::: {.exercise}

Let $A$ be a nonempty finite simply ordered set.

(a) Show that $A$ has a largest element.
[Hint: Proceed by induction on the cardinality of $A$ .]

(b) Show that $A$ has the order type of a section of the positive integers.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 6.4, printed pp. 76--78** (`tmp/sources/munkres-solutions-whitman.pdf`); both inductions on $\cardinality{A}$ are his, as is the extension of the order isomorphism of $A-\{M\}$ by the largest element.

(a) We induct on $\cardinality{A}$. If $\cardinality{A}=1$, the unique element is the largest element.

Assume every nonempty simply ordered set of cardinality $n$ has a largest element, and let $\cardinality{A}=n+1$. Choose $a\in A$. Then $A-\{a\}$ has cardinality $n$, so by induction it has a largest element $m$. Since the order is simple, either $a<m$ or $m<a$. In the first case $m$ is largest in all of $A$; in the second case $a$ is largest. Thus every nonempty finite simply ordered set has a largest element.

(b) We again induct on $\cardinality{A}$. A one-point ordered set is order-isomorphic to $\{1\}$. Suppose the assertion holds for cardinality $n$, and let $\cardinality{A}=n+1$. By part (a), $A$ has a largest element $M$. The subset
$$
A'=A-\{M\}
$$
has cardinality $n$, so by induction there is an order-preserving bijection
$$
\phi:A'\longrightarrow\{1,\dots,n\}.
$$
Extend it by setting
$$
\Phi(M)=n+1.
$$
Since every element of $A'$ is less than $M$, $\Phi$ is an order-preserving bijection
$$
A\longrightarrow\{1,\dots,n+1\}.
$$
Hence $A$ has the order type of a section of the positive integers.
:::
