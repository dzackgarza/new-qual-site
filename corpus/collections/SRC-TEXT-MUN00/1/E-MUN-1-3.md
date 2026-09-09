---
schema: qual/card@1
id: E-MUN-1-3
kind: problem
title: Contrapositive, converse, and truth of conditional statements
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) Write the contrapositive and converse of the following statement: "If $x < 0$, then $x^2 - x > 0$," and determine which (if any) of the three statements are true.

(b) Do the same for the statement "If $x > 0$, then $x^2 - x > 0$ ."
:::

::: {.solution}
(a) The original statement is
\[
x<0\Longrightarrow x^2-x>0.
\]
Its contrapositive is
\[
x^2-x\le0\Longrightarrow x\ge0,
\]
and its converse is
\[
x^2-x>0\Longrightarrow x<0.
\]
The original statement is true because if \(x<0\), then both \(x\) and \(x-1\) are negative, so
\[
x^2-x=x(x-1)>0.
\]
Its contrapositive is therefore also true. The converse is false: \(x=2\) satisfies \(x^2-x>0\) but not \(x<0\).

(b) The original statement is
\[
x>0\Longrightarrow x^2-x>0.
\]
Its contrapositive is
\[
x^2-x\le0\Longrightarrow x\le0,
\]
and its converse is
\[
x^2-x>0\Longrightarrow x>0.
\]
All three are false. Taking \(x=\tfrac12\) disproves both the original statement and its contrapositive since
\[
x^2-x=-\tfrac14\le0
\]
while \(x>0\). Taking \(x=-1\) disproves the converse since \(x^2-x=2>0\) but \(x\not>0\).
:::
