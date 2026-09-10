---
schema: qual/card@1
id: E-MUN-1-4
kind: problem
title: Negation of quantified statements about real numbers
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $A$ and $B$ be sets of real numbers.
Write the negation of each of the following statements:

(a) For every $a \in A$, it is true that $a^2 \in B$ .

(b) For at least one $a \in A$, it is true that $a^2 \in B$ .

(c) For every $a \in A$, it is true that $a^2 \notin B$ .

(d) For at least one $a \notin A$, it is true that $a^2 \in B$ .
:::

::: {.solution}
Negating a universal quantifier produces an existential quantifier and vice versa, while negating membership changes \(\in\) to \(\notin\).

(a) The negation is:
\[
\text{There exists }a\in A\text{ such that }a^2\notin B.
\]

(b) The negation is:
\[
\text{For every }a\in A,\quad a^2\notin B.
\]

(c) The negation is:
\[
\text{There exists }a\in A\text{ such that }a^2\in B.
\]

(d) The negation is:
\[
\text{For every real number }a\notin A,\quad a^2\notin B.
\]
:::
