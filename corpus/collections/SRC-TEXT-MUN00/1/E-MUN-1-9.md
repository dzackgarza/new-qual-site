---
schema: qual/card@1
id: E-MUN-1-9
kind: problem
title: DeMorgan's laws for arbitrary unions and intersections
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 9; the stored statement matches.
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
    Read against Munkres, Topology (2000), §1 Exercise 9, printed p. 15; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 1.9,
    printed pp. 9-10 (tmp/sources/munkres-solutions-whitman.pdf). Both laws are his,
    including the step that turns "not (x in B for every B)" into "x not in B for at
    least one B", which is where the argument uses that the collection is nonempty; the
    card states the family as {A_i} indexed by I and his as a collection B.
---

::: {.exercise}

Formulate and prove DeMorgan's laws for arbitrary unions and intersections.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.9, printed pp. 9--10** (`tmp/sources/munkres-solutions-whitman.pdf`); the two identities and their chains of equivalences below are his.

Fix a set $X$ and a family $\{A_i\}_{i\in I}$ of subsets of $X$. The arbitrary DeMorgan laws are
$$
X-\bigcup_{i\in I}A_i
=
\bigcap_{i\in I}(X-A_i)
$$
and
$$
X-\bigcap_{i\in I}A_i
=
\bigcup_{i\in I}(X-A_i).
$$

For the first identity,
$$
\begin{aligned}
x\in X-\bigcup_iA_i
&\iff x\in X\text{ and }x\notin A_i\text{ for every }i\\
&\iff x\in X-A_i\text{ for every }i\\
&\iff x\in\bigcap_i(X-A_i).
\end{aligned}
$$
For the second,
$$
\begin{aligned}
x\in X-\bigcap_iA_i
&\iff x\in X\text{ and it is not true that }x\in A_i\text{ for every }i\\
&\iff x\in X\text{ and }x\notin A_i\text{ for at least one }i\\
&\iff x\in\bigcup_i(X-A_i).
\end{aligned}
$$
:::
