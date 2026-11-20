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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was checked against Munkres, *Topology* (2000), §1 Exercise 9, printed p. 15, and the two identities with their chains of membership equivalences are transcribed from the retained set: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.9, printed pp. 9--10. Each identity is one step; the quantifier step from "not for every" to "for some" is named in the second.
---

::: {.exercise}

Formulate and prove DeMorgan's laws for arbitrary unions and intersections.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.9** (`tmp/sources/munkres-solutions-whitman.pdf`); the two identities and their chains of equivalences below are his, and the statement is Munkres, *Topology* (2000), §1 Exercise 9.

::: pf

::: {.pf-step #union}
$X-\bigcup_{i\in I}A_i=\bigcap_{i\in I}(X-A_i)$.

::: pf-proof
For any $x$: $x\in X-\bigcup_iA_i$ means $x\in X$ and $x\notin\bigcup_iA_i$, that is $x\in X$ and $x\notin A_i$ for every $i$; this is $x\in X-A_i$ for every $i$, that is $x\in\bigcap_i(X-A_i)$.
:::
:::

::: {.pf-step #intersection}
$X-\bigcap_{i\in I}A_i=\bigcup_{i\in I}(X-A_i)$.

::: pf-proof
For any $x$: $x\in X-\bigcap_iA_i$ means $x\in X$ and it is not the case that $x\in A_i$ for every $i$; negating the universal quantifier gives $x\notin A_i$ for at least one $i$, so $x\in X-A_i$ for that $i$, that is $x\in\bigcup_i(X-A_i)$.
:::
:::

::: {.pf-step}
DeMorgan's laws hold for an arbitrary family of subsets of $X$: the complement of the union is the intersection of the complements, and the complement of the intersection is the union of the complements.

::: pf-proof
Steps [](#union){.pf-ref} and [](#intersection){.pf-ref} are the two identities, and each is an equivalence of membership for an arbitrary $x$, hence an equality of sets.
:::
:::

:::
:::
