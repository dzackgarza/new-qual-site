---
schema: qual/card@1
id: E-MUN-1-7
kind: problem
title: Expressing sets using union, intersection, and difference
classification:
  areas:
  - topology
  topics:
  - Fundamental Concepts
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Given sets $A, B$, and $C$, express each of the following sets in terms of $A, B$, and $C$, using the symbols $\cup, \cap,$ and $-$ .

$$
D = \{x \mid x \in A \text { and } (x \in B \text { or } x \in C) \},
$$

$$
E = \{x \mid (x \in A \text { and } x \in B) \text { or } x \in C \},
$$

$$
F = \{x \mid x \in A \text { and } (x \in B \Rightarrow x \in C) \}.
$$
:::

::: {.solution}
Directly translating the logical connectives gives
\[
D=A\cap(B\cup C)
\]
and
\[
E=(A\cap B)\cup C.
\]
For \(F\), use
\[
(x\in B\Rightarrow x\in C)
\iff (x\notin B\text{ or }x\in C).
\]
Thus, among points of \(A\), the only points excluded are those lying in \(B-C\). Therefore
\[
\boxed{F=A-(B-C).}
\]
Equivalently,
\[
F=(A-B)\cup(A\cap C).
\]
:::
