---
schema: qual/card@1
id: E-MUN-7-7
kind: problem
title: Equal cardinality of $\{0,1\}^{\omega}$ subsets
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show that the sets D and E of Exercise 5 have the same cardinality.
:::

::: {.solution}
Recall
\[
D=(\mathbb Z_+)^\omega,
\qquad
E=\{0,1\}^\omega.
\]
There is an injection \(E\to D\) given by
\[
(x_n)\mapsto(x_n+1).
\]

For the reverse direction, encode \(a=(a_1,a_2,\ldots)\in D\) by the binary sequence
\[
\underbrace{11\cdots1}_{a_1}0\,
\underbrace{11\cdots1}_{a_2}0\,
\underbrace{11\cdots1}_{a_3}0\cdots.
\]
Because every \(a_i\ge1\), this sequence contains infinitely many separator zeros, and the lengths of the successive blocks of ones uniquely recover \(a_1,a_2,\ldots\). Thus this encoding is injective \(D\to E\).

By Schroeder--Bernstein,
\[
\boxed{|D|=|E|}.
\]
:::
