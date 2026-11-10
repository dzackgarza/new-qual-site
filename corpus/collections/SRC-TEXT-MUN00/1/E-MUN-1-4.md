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
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §1 Exercise 4, printed p. 14; the four
    statements (a)-(d) are stored as printed, including (d)'s quantifier over real
    numbers a not in A.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 1.4,
    printed pp. 6-7 (tmp/sources/munkres-solutions-whitman.pdf). His four negations are
    the card's four; the sentence naming the rule (a universal quantifier becomes an
    existential one and conversely) is his remark that these are the basic logical
    negations. No defect found.
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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.4, printed pp. 6--7** (`tmp/sources/munkres-solutions-whitman.pdf`); the four negations are his, and his remark that these are the basic logical negations using existential quantifiers is the rule stated first below.

Negating a universal quantifier produces an existential quantifier and vice versa, while negating membership changes $\in$ to $\notin$.

(a) The negation is:
$$
\text{There exists }a\in A\text{ such that }a^2\notin B.
$$

(b) The negation is:
$$
\text{For every }a\in A,\quad a^2\notin B.
$$

(c) The negation is:
$$
\text{There exists }a\in A\text{ such that }a^2\in B.
$$

(d) The negation is:
$$
\text{For every real number }a\notin A,\quad a^2\notin B.
$$
:::
