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
---

::: {.exercise}

Check that the dictionary order is an order relation: for sets $A$ and $B$ with order relations $<_A$ and $<_B$, define $a_1\times b_1 < a_2\times b_2$ if $a_1 <_A a_2$, or if $a_1 = a_2$ and $b_1 <_B b_2$, and show that this is an order relation on $A\times B$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.9, printed pp. 27--28** (`tmp/sources/munkres-solutions-whitman.pdf`); the case analysis below is his.

*Comparability.* Let $a_1\times b_1$ and $a_2\times b_2$ be distinct. If $a_1\ne a_2$ then, $<_A$ being an order relation, $a_1<_A a_2$ or $a_2<_A a_1$, and the corresponding point is smaller. If $a_1=a_2$ then $b_1\ne b_2$, so $b_1<_B b_2$ or $b_2<_B b_1$, and again the corresponding point is smaller.

*Nonreflexivity.* If $a\times b<a\times b$ then, since $a=a$, we would need $b<_B b$, which is false.

*Transitivity.* Suppose $a_1\times b_1<a_2\times b_2$ and $a_2\times b_2<a_3\times b_3$. If $a_1<_A a_2$, then either $a_2<_A a_3$, whence $a_1<_A a_3$ by transitivity, or $a_2=a_3$ with $b_2<_B b_3$, whence $a_1<_A a_3$. If instead $a_1=a_2$ with $b_1<_B b_2$, then either $a_2<_A a_3$, whence $a_1<_A a_3$, or $a_2=a_3$ with $b_2<_B b_3$, whence $a_1=a_3$ and $b_1<_B b_3$. In every case $a_1\times b_1<a_3\times b_3$.
:::
