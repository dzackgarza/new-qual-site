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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the four negations, which is what Queue D asks for on this card. Each part is a step whose justification is the quantifier rule stated as a step of its own; the rule and the statement's four clauses were re-read against Munkres, Topology (2000), §1 Exercise 4, printed p. 14, and against Dan Whitman's set, Exercise 1.4, printed pp. 6-7, where the exercise begins on p. 6 and his four negations stand on p. 7. Nothing in the mathematics changed: the four negations and the citation are the card's own already, and no statement repair was needed. For (c) and (d) the card now says why the double negation leaves the affirmative inner statement, which the prose left to the reader.
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
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.4, printed pp. 6--7** (`tmp/sources/munkres-solutions-whitman.pdf`); the four negations are his, and his remark that these are the basic logical negations is step [](#quantifier-negation){.pf-ref}. The statement is Munkres, *Topology*, 2nd ed. (2000), §1 Exercise 4, printed p. 14.

::: pf

::: {.pf-step #quantifier-negation}
For a statement $P(a)$ about real numbers, the negation of "for every $a\in A$, $P(a)$" is "there is $a\in A$ with $\lnot P(a)$", and the negation of "there is $a\in A$ with $P(a)$" is "for every $a\in A$, $\lnot P(a)$"; and the negation of $a^2\in B$ is $a^2\notin B$.

::: pf-proof
The two quantifier rules are $\lnot\forall a\,P(a)\Longleftrightarrow\exists a\,\lnot P(a)$ and $\lnot\exists a\,P(a)\Longleftrightarrow\forall a\,\lnot P(a)$, read for $a$ ranging over $A$, and $\notin$ is by definition the negation of $\in$.
:::

:::

::: {.pf-step #part-a}
(a) The negation is: there exists $a\in A$ such that $a^2\notin B$.

::: pf-proof
Statement (a) is "for every $a\in A$, $a^2\in B$". With $P(a)$ the statement $a^2\in B$, the first rule of step [](#quantifier-negation){.pf-ref} gives the negation.
:::

:::

::: {.pf-step #part-b}
(b) The negation is: for every $a\in A$, $a^2\notin B$.

::: pf-proof
Statement (b) is "there is $a\in A$ with $a^2\in B$", so the second rule of step [](#quantifier-negation){.pf-ref} applies.
:::

:::

::: {.pf-step #part-c}
(c) The negation is: there exists $a\in A$ such that $a^2\in B$.

::: pf-proof
Statement (c) is "for every $a\in A$, $a^2\notin B$, that is, for every $a\in A$ it is false that $a^2\in B$. Negating it twice by the first rule of step [](#quantifier-negation){.pf-ref} leaves an existential statement whose inner statement is the negation of $a^2\notin B$, namely $a^2\in B$.
:::

:::

::: {.pf-step #part-d}
(d) The negation is: for every real number $a\notin A$, $a^2\notin B$.

::: pf-proof
Statement (d) is "there is $a\notin A$ with $a^2\in B$", a bounded existential statement over the set $\RR-A$, so the second rule of step [](#quantifier-negation){.pf-ref} gives "for every $a\notin A$, not $a^2\in B$", which is the claim. This is the last part, and the four negations are (a)--(d).
:::

:::

:::
:::
