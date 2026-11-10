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
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §1 Exercise 6, printed p. 14; the stored
    statement matches, and the reference to Exercise 5 is to the four statements stored
    on E-MUN-1-5.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 1.6,
    printed p. 8 (tmp/sources/munkres-solutions-whitman.pdf). His four contrapositives
    agree with the card's, and the observation that a statement and its contrapositive
    have the same truth value, used to read the truth values off Exercise 5, is his.
---

::: {.exercise}

Write the contrapositive of each of the statements of Exercise 5.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.6, printed p. 8** (`tmp/sources/munkres-solutions-whitman.pdf`); the four contrapositives below are his.

The contrapositive of an implication $P\Rightarrow Q$ is $\neg Q\Rightarrow\neg P$. Applying this to the statements of [[E-MUN-1-5]] gives:

(a)
$$
\bigl(x\notin A\text{ for every }A\in\mathcal A\bigr)
\Longrightarrow
x\notin\bigcup_{A\in\mathcal A}A.
$$

(b)
$$
\bigl(x\notin A\text{ for at least one }A\in\mathcal A\bigr)
\Longrightarrow
x\notin\bigcup_{A\in\mathcal A}A.
$$

(c)
$$
\bigl(x\notin A\text{ for every }A\in\mathcal A\bigr)
\Longrightarrow
x\notin\bigcap_{A\in\mathcal A}A.
$$

(d)
$$
\bigl(x\notin A\text{ for at least one }A\in\mathcal A\bigr)
\Longrightarrow
x\notin\bigcap_{A\in\mathcal A}A.
$$
A statement and its contrapositive have the same truth value, so by [[E-MUN-1-5]], (a), (c), and (d) are true and (b) is false.
:::
