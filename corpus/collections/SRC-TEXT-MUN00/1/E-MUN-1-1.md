---
schema: qual/card@1
id: E-MUN-1-1
kind: problem
title: Distributive laws and DeMorgan's laws for sets
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Check the distributive laws for $\cup$ and $\cap$ and DeMorgan's laws.
:::

::: {.solution}
For any element \(x\), membership in a union corresponds to logical ``or'' and membership in an intersection corresponds to logical ``and''. Hence
\[
\begin{aligned}
x\in A\cap(B\cup C)
&\iff x\in A\ \text{and}\ (x\in B\ \text{or}\ x\in C)\\
&\iff (x\in A\cap B)\ \text{or}\ (x\in A\cap C)\\
&\iff x\in (A\cap B)\cup(A\cap C),
\end{aligned}
\]
so
\[
A\cap(B\cup C)=(A\cap B)\cup(A\cap C).
\]
Similarly,
\[
A\cup(B\cap C)=(A\cup B)\cap(A\cup C).
\]
These are the two distributive laws.

For DeMorgan's laws,
\[
\begin{aligned}
x\in A-(B\cup C)
&\iff x\in A,\ x\notin B,\ x\notin C\\
&\iff x\in(A-B)\cap(A-C),
\end{aligned}
\]
so
\[
A-(B\cup C)=(A-B)\cap(A-C).
\]
Likewise,
\[
A-(B\cap C)=(A-B)\cup(A-C).
\]
Equivalently, relative to a fixed universe \(U\),
\[
(B\cup C)^c=B^c\cap C^c,
\qquad
(B\cap C)^c=B^c\cup C^c.
\]
:::
