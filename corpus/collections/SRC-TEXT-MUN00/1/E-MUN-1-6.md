---
schema: qual/card@1
id: E-MUN-1-6
kind: problem
title: Contrapositives of quantified subset statements
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Write the contrapositive of each of the statements of Exercise 5.
:::

::: {.solution}
The contrapositive of an implication \(P\Rightarrow Q\) is \(\neg Q\Rightarrow\neg P\). Applying this to Exercise 5 gives:

(a)
\[
\bigl(x\notin A\text{ for every }A\in\mathcal A\bigr)
\Longrightarrow
x\notin\bigcup_{A\in\mathcal A}A.
\]

(b)
\[
\bigl(x\notin A\text{ for at least one }A\in\mathcal A\bigr)
\Longrightarrow
x\notin\bigcup_{A\in\mathcal A}A.
\]

(c)
\[
\bigl(x\notin A\text{ for every }A\in\mathcal A\bigr)
\Longrightarrow
x\notin\bigcap_{A\in\mathcal A}A.
\]

(d)
\[
\bigl(x\notin A\text{ for at least one }A\in\mathcal A\bigr)
\Longrightarrow
x\notin\bigcap_{A\in\mathcal A}A.
\]
As expected, (a), (c), and (d) are true and (b) is false, since a statement and its contrapositive have the same truth value.
:::
