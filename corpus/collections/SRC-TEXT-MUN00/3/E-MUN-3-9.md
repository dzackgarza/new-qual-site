---
schema: qual/card@1
id: E-MUN-3-9
kind: problem
title: The dictionary order is an order relation
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Exercise 9, printed p. 29. The dictionary
    order is defined earlier in §3: a_1 x b_1 < a_2 x b_2 if a_1 <_A a_2, or a_1 = a_2
    and b_1 <_B b_2; the book says that checking it is an order relation involves
    several cases and leaves it to the exercises. The card states the definition so that
    the exercise stands alone.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.9,
    printed pp. 27-28 (tmp/sources/munkres-solutions-whitman.pdf). The two-by-two case
    analysis in each property is his.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was checked against Munkres, *Topology* (2000), §3 Exercise 9, printed p. 29, and the case analysis is transcribed from the retained set: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.9, printed pp. 27--28. The three steps are exactly the three properties in the book's definition of an order relation.
---

::: {.exercise}

Check that the dictionary order is an order relation: for sets $A$ and $B$ with order relations $<_A$ and $<_B$, define $a_1\times b_1 < a_2\times b_2$ if $a_1 <_A a_2$, or if $a_1 = a_2$ and $b_1 <_B b_2$, and show that this is an order relation on $A\times B$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.9, printed pp. 27--28** (`tmp/sources/munkres-solutions-whitman.pdf`); the case analysis below is his, and the statement is Munkres, *Topology* (2000), §3 Exercise 9.

::: pf

::: {.pf-step #comparability}
For distinct points $a_1\times b_1\neq a_2\times b_2$, either $a_1\times b_1<a_2\times b_2$ or $a_2\times b_2<a_1\times b_1$.

::: pf-proof
If $a_1\neq a_2$, then $<_A$ being an order relation gives $a_1<_Aa_2$ or $a_2<_Aa_1$, and the corresponding point is smaller by the first clause of the definition. If $a_1=a_2$, then $b_1\neq b_2$, so $b_1<_Bb_2$ or $b_2<_Bb_1$, and the corresponding point is smaller by the second clause.
:::
:::

::: {.pf-step #nonreflexive}
Never $a\times b<a\times b$.

::: pf-proof
Here $a=a$, so the first clause fails and the second would require $b<_Bb$, which an order relation forbids.
:::
:::

::: {.pf-step #transitive}
If $a_1\times b_1<a_2\times b_2$ and $a_2\times b_2<a_3\times b_3$, then $a_1\times b_1<a_3\times b_3$.

::: pf-proof
Suppose first $a_1<_Aa_2$. Then either $a_2<_Aa_3$, giving $a_1<_Aa_3$ by transitivity of $<_A$, or $a_2=a_3$ with $b_2<_Bb_3$, giving $a_1<_Aa_3$. Suppose instead $a_1=a_2$ with $b_1<_Bb_2$. Then either $a_2<_Aa_3$, giving $a_1<_Aa_3$, or $a_2=a_3$ with $b_2<_Bb_3$, giving $a_1=a_3$ and $b_1<_Bb_3$ by transitivity of $<_B$. In each case $a_1\times b_1<a_3\times b_3$.
:::
:::

::: {.pf-step}
The dictionary order is an order relation on $A\times B$.

::: pf-proof
Steps [](#comparability){.pf-ref}, [](#nonreflexive){.pf-ref} and [](#transitive){.pf-ref} are comparability, nonreflexivity and transitivity, which is the book's definition of an order relation.
:::
:::

:::
:::
