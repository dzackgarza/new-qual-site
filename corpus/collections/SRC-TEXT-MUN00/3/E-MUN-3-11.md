---
schema: qual/card@1
id: E-MUN-3-11
kind: problem
title: Uniqueness of the immediate predecessor, the immediate successor and the extreme elements
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
    Read against Munkres, Topology (2000), §3 Exercise 11, printed p. 29. The card uses
    the book's definitions: the open interval (a,b) is {x : a < x < b}, and a is the
    immediate predecessor of b, b the immediate successor of a, when that interval is
    empty.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.11,
    printed p. 31 (tmp/sources/munkres-solutions-whitman.pdf). His argument for the
    successor - two candidates are comparable, and the smaller lies in the open interval
    above the larger - is the one below, and the smallest and largest elements follow from
    the same comparison. The card also states the equivalence a < b iff not b <= a that
    he proves first.
---

::: {.exercise}

Show that an element in an ordered set has at most one immediate successor and at most one immediate predecessor. Show that a subset of an ordered set has at most one smallest element and at most one largest element.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.11, printed p. 31** (`tmp/sources/munkres-solutions-whitman.pdf`); the arguments below are his.

Let $<$ be an order relation on $A$. We use the equivalence
$$
a<b \iff \text{not } (b\le a),
$$
which holds because $a<b$ and $b\le a$ would give either $a<a$ (if $b=a$) or $a<a$ by transitivity (if $b<a$), both excluded by nonreflexivity, and conversely if not $b\le a$ then $a\ne b$, so $a<b$ or $b<a$ by comparability, and only $a<b$ remains.

*Immediate successor.* Let $b_1\ne b_2$ both be immediate successors of $a$, so $a<b_1$, $a<b_2$ and the open intervals $(a,b_1)$ and $(a,b_2)$ are empty. The two are comparable; say $b_1<b_2$. Then $a<b_1<b_2$, so $b_1\in(a,b_2)$, contradicting that interval being empty. Hence $b_1=b_2$.

*Immediate predecessor.* The same argument with the order reversed: two candidates $a_1<a_2$ for the immediate predecessor of $b$ satisfy $a_1<a_2<b$, so $a_2\in(a_1,b)$ while $(a_1,b)$ is empty.

*Smallest element.* Let $a_1,a_2$ be smallest elements of $A_0\subset A$ and suppose $a_1\ne a_2$. They are comparable; say $a_1<a_2$. Then not $a_2\le a_1$, although $a_1\in A_0$, so $a_2$ is not a smallest element of $A_0$: a contradiction. Hence $a_1=a_2$.

*Largest element.* The same argument with the order reversed: if $a_1<a_2$ are both largest, then $a_2\le a_1$ would have to hold because $a_1\in A_0$, contradicting $a_1<a_2$.
:::
