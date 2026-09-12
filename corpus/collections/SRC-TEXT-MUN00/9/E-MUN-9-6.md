---
schema: qual/card@1
id: E-MUN-9-6
kind: problem
title: Paradoxes of the set of all sets
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 9, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Most of the famous paradoxes of naive set theory are associated in some way or other with the concept of the "set of all sets."
None of the rules we have given for forming sets allows us to consider such a set.
And for good reason—the concept itself is self-contradictory.
For suppose that $\mathcal{A}$ denotes the "set of all sets."

(a) Show that $\mathcal{P}(\mathcal{A})\subset \mathcal{A}$ ; derive a contradiction.

(b) (Russell's paradox.)
Let $\mathcal{B}$ be the subset of $\mathcal{A}$ consisting of all sets that are not elements of themselves;

$$
\mathcal {B} = \{A \mid A \in \mathcal {A} \text { and } A \notin A \}.
$$

(Of course, there may be no set $A$ such that $A \in A$ ; if such is the case, then $\mathcal{B} = \mathcal{A}$ .) Is $\mathcal{B}$ an element of itself or not?
:::

::: {.solution}
(a) Suppose \(\mathcal A\) were the set of all sets. Every subset of \(\mathcal A\) is itself a set, hence by the defining property of \(\mathcal A\) it is an element of \(\mathcal A\). Therefore
\[
\mathcal P(\mathcal A)\subset\mathcal A.
\]
The inclusion map would be an injection
\[
\mathcal P(\mathcal A)\hookrightarrow\mathcal A,
\]
contradicting Cantor's theorem, which says there is no injection from the power set of a set into the set itself. Hence a set of all sets cannot exist.

(b) Define
\[
\mathcal B=\{A\in\mathcal A:A\notin A\}.
\]
Since \(\mathcal A\) is assumed to contain every set, \(\mathcal B\in\mathcal A\). Ask whether \(\mathcal B\in\mathcal B\). By definition,
\[
\mathcal B\in\mathcal B
\iff
\mathcal B\notin\mathcal B,
\]
a contradiction in either case. This is Russell's paradox and independently shows that the supposed set \(\mathcal A\) cannot exist.
:::
