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
---

::: {.exercise}

Let $A$ be a nonempty finite simply ordered set.

(a) Show that $A$ has a largest element.
[Hint: Proceed by induction on the cardinality of $A$ .]

(b) Show that $A$ has the order type of a section of the positive integers.
:::

::: {.solution}
(a) We induct on \(|A|\). If \(|A|=1\), the unique element is the largest element.

Assume every nonempty simply ordered set of cardinality \(n\) has a largest element, and let \(|A|=n+1\). Choose \(a\in A\). Then \(A-\{a\}\) has cardinality \(n\), so by induction it has a largest element \(m\). Since the order is simple, either \(a<m\) or \(m<a\). In the first case \(m\) is largest in all of \(A\); in the second case \(a\) is largest. Thus every nonempty finite simply ordered set has a largest element.

(b) We again induct on \(|A|\). A one-point ordered set is order-isomorphic to \(\{1\}\). Suppose the assertion holds for cardinality \(n\), and let \(|A|=n+1\). By part (a), \(A\) has a largest element \(M\). The subset
\[
A'=A-\{M\}
\]
has cardinality \(n\), so by induction there is an order-preserving bijection
\[
\phi:A'\longrightarrow\{1,\dots,n\}.
\]
Extend it by setting
\[
\Phi(M)=n+1.
\]
Since every element of \(A'\) is less than \(M\), \(\Phi\) is an order-preserving bijection
\[
A\longrightarrow\{1,\dots,n+1\}.
\]
Hence \(A\) has the order type of a section of the positive integers.
:::
