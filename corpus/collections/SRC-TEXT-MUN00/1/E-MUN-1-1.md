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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was already checked against Munkres, *Topology* (2000), §1 Exercise 1, printed p. 14, and the four laws are transcribed from the retained set's chains of equivalences: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.1, printed pp. 1--2. Each step is one of his equivalences, with the propositional law it uses named. Not proved here: any form of the laws for an arbitrary index set, which the exercise does not ask for.
---

::: {.exercise}

Check the distributive laws for $\cup$ and $\cap$ and DeMorgan's laws.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.1** (`tmp/sources/munkres-solutions-whitman.pdf`), which derives all four laws as chains of logical equivalences between membership statements; the statement is Munkres, *Topology* (2000), §1 Exercise 1. The steps transcribe his argument, naming the propositional law each equivalence uses.

::: pf

::: {.pf-step #distributive-one}
$A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$.

::: pf-proof
For any $x$: $x\in A\cap(B\cup C)$ means $x\in A$ and ($x\in B$ or $x\in C$), which distributes to ($x\in A$ and $x\in B$) or ($x\in A$ and $x\in C$), that is $x\in(A\cap B)\cup(A\cap C)$. Membership in a union is "or" and in an intersection "and", so the two sets have the same elements.
:::
:::

::: {.pf-step #distributive-two}
$A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$.

::: pf-proof
For any $x$: $x\in A\cup(B\cap C)$ means $x\in A$ or ($x\in B$ and $x\in C$), which distributes to ($x\in A$ or $x\in B$) and ($x\in A$ or $x\in C$), that is $x\in(A\cup B)\cap(A\cup C)$.
:::
:::

::: {.pf-step #demorgan-one}
$A-(B\cup C)=(A-B)\cap(A-C)$.

::: pf-proof
For any $x$: $x\in A-(B\cup C)$ means $x\in A$ and not ($x\in B$ or $x\in C$); by DeMorgan's law for propositions this is $x\in A$ and $x\notin B$ and $x\notin C$, equivalently ($x\in A$ and $x\notin B$) and ($x\in A$ and $x\notin C$), which is $x\in(A-B)\cap(A-C)$.
:::
:::

::: {.pf-step #demorgan-two}
$A-(B\cap C)=(A-B)\cup(A-C)$.

::: pf-proof
For any $x$: $x\in A-(B\cap C)$ means $x\in A$ and not ($x\in B$ and $x\in C$), equivalently $x\in A$ and ($x\notin B$ or $x\notin C$), which distributes to ($x\in A$ and $x\notin B$) or ($x\in A$ and $x\notin C$), that is $x\in(A-B)\cup(A-C)$.
:::
:::

::: {.pf-step}
The distributive laws for $\cup$ and $\cap$ are steps [](#distributive-one){.pf-ref} and [](#distributive-two){.pf-ref}, and DeMorgan's laws are steps [](#demorgan-one){.pf-ref} and [](#demorgan-two){.pf-ref}.

::: pf-proof
The four identities proved are the two distributive laws and the two DeMorgan laws for a pair of sets, which is what the exercise asks to check.
:::
:::

:::
:::
