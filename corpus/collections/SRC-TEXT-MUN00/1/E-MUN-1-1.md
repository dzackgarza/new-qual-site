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
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §1 Exercise 1, printed p. 14: "Check the
    distributive laws for the union and intersection and DeMorgan's laws." The stored
    statement matches; the exercise asks for no more than that.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 1.1,
    printed pp. 1-2 of that manual (tmp/sources/munkres-solutions-whitman.pdf), which
    proves all four laws by chains of membership equivalences. The card's argument is
    that one, expanded: each distributive law and each DeMorgan law is derived from the
    propositional equivalence distributing "and" over "or" and from the definition of
    set difference, and the universe-relative form is stated at the end. Nothing was
    weakened; no defect found.
---

::: {.exercise}

Check the distributive laws for $\cup$ and $\cap$ and DeMorgan's laws.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.1, printed pp. 1--2** (`tmp/sources/munkres-solutions-whitman.pdf`), which derives all four laws as chains of logical equivalences between membership statements. The argument below is his, expanded so that each step names the equivalence it uses.

For any element $x$, membership in a union corresponds to logical "or" and membership in an intersection corresponds to logical "and". Hence
$$
\begin{aligned}
x\in A\cap(B\cup C)
&\iff x\in A\ \text{and}\ (x\in B\ \text{or}\ x\in C)\\
&\iff (x\in A\cap B)\ \text{or}\ (x\in A\cap C)\\
&\iff x\in (A\cap B)\cup(A\cap C),
\end{aligned}
$$
so
$$
A\cap(B\cup C)=(A\cap B)\cup(A\cap C).
$$
Similarly,
$$
A\cup(B\cap C)=(A\cup B)\cap(A\cup C).
$$
These are the two distributive laws.

For DeMorgan's laws,
$$
\begin{aligned}
x\in A-(B\cup C)
&\iff x\in A,\ x\notin B,\ x\notin C\\
&\iff x\in(A-B)\cap(A-C),
\end{aligned}
$$
so
$$
A-(B\cup C)=(A-B)\cap(A-C).
$$
Likewise,
$$
A-(B\cap C)=(A-B)\cup(A-C).
$$
Equivalently, relative to a fixed universe $U$,
$$
(B\cup C)^c=B^c\cap C^c,
\qquad
(B\cap C)^c=B^c\cup C^c.
$$
:::
