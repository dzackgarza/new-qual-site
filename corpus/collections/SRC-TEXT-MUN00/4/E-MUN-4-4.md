---
schema: qual/card@1
id: E-MUN-4-4
kind: problem
title: Largest element of finite subsets of $\{1, \ldots, n\}$
classification:
  areas:
  - topology
  topics:
  - Integers and Real Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) Prove by induction that given $n \in \mathbb{Z}_+$, every nonempty subset of $\{1, \ldots, n\}$ has a largest element.

(b) Explain why you cannot conclude from (a) that every nonempty subset of $\mathbb{Z}_{+}$ has a largest element.
:::

::: {.solution}
(a) Let \(P(n)\) be the assertion that every nonempty subset of \(\{1,\dots,n\}\) has a largest element.

For \(n=1\), the only nonempty subset is \(\{1\}\), whose largest element is \(1\).

Assume \(P(n)\), and let \(A\subset\{1,\dots,n+1\}\) be nonempty. If \(n+1\in A\), then \(n+1\) is the largest element of \(A\). If \(n+1\notin A\), then
\[
A\subset\{1,\dots,n\},
\]
so \(A\) has a largest element by the inductive hypothesis. Thus \(P(n+1)\) holds. By induction, \(P(n)\) holds for every \(n\in\mathbb Z_+\).

(b) Part (a) concerns subsets contained in one *fixed finite initial segment* \(\{1,\dots,n\}\). A general nonempty subset of \(\mathbb Z_+\) need not be bounded above and hence need not lie in any such segment. For example, \(\mathbb Z_+\) itself has no largest element, since \(m+1\in\mathbb Z_+\) and \(m+1>m\) for every \(m\in\mathbb Z_+\).
:::
