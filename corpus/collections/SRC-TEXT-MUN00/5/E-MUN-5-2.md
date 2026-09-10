---
schema: qual/card@1
id: E-MUN-5-2
kind: problem
title: Associativity of finite and infinite Cartesian products
classification:
  areas:
  - topology
  topics:
  - Cartesian Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 5, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) Show that if $n > 1$ there is bijective correspondence of

$$
A _ {1} \times \dots \times A _ {n} \quad \text { with } \quad (A _ {1} \times \dots \times A _ {n - 1}) \times A _ {n}.
$$

(b) Given the indexed family $\{A_{1}, A_{2}, \ldots\}$, let $B_{i} = A_{2i-1} \times A_{2i}$ for each positive integer $i$ . Show there is bijective correspondence of $A_{1} \times A_{2} \times \cdots$ with $B_{1} \times B_{2} \times \cdots$ .
:::

::: {.solution}
(a) Define
\[
\Phi:A_1\times\cdots\times A_n
\longrightarrow
(A_1\times\cdots\times A_{n-1})\times A_n
\]
by
\[
\Phi(a_1,\dots,a_n)=((a_1,\dots,a_{n-1}),a_n).
\]
Its inverse is
\[
((a_1,\dots,a_{n-1}),a_n)\longmapsto(a_1,\dots,a_n),
\]
so \(\Phi\) is bijective.

(b) For \(B_i=A_{2i-1}\times A_{2i}\), define
\[
\Psi(a_1,a_2,a_3,a_4,\dots)
=((a_1,a_2),(a_3,a_4),\dots).
\]
This maps \(\prod_{j\ge1}A_j\) into \(\prod_{i\ge1}B_i\). Its inverse simply flattens the sequence of ordered pairs:
\[
((b_1,b_2),(b_3,b_4),\dots)
\longmapsto
(b_1,b_2,b_3,b_4,\dots).
\]
Thus the two infinite products are in bijective correspondence.
:::
