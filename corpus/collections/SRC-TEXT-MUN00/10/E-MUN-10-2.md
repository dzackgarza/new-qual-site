---
schema: qual/card@1
id: E-MUN-10-2
kind: problem
title: Immediate successors in well-ordered sets
classification:
  areas:
  - topology
  topics:
  - Well-Ordered Sets
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §10 Exercise 2, printed p. 67; both parts are
    stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 10.2, printed p. 108.
    (a) is his: the set of elements above a is nonempty because a is not the largest, and
    its smallest element has nothing strictly between it and a. (b) is his example Z with
    the usual order, in which n+1 is an immediate successor of n, while the negative
    integers have no smallest element.
---

::: {.exercise}

(a) Show that in a well-ordered set, every element except the largest (if one exists) has an immediate successor.

(b) Find a set in which every element has an immediate successor that is not well-ordered.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.2, printed p. 108** (`tmp/sources/munkres-solutions-whitman.pdf`); both parts are his.

(a) Let $A$ be well ordered by $<$ and let $a\in A$ be an element that is not the largest. Then some $x\in A$ satisfies $a<x$, so
$$
X=\{y\in A\mid a<y\}
$$
is a nonempty subset of $A$ and has a smallest element $b$. Since $b\in X$ we have $a<b$. If $z\in A$ satisfied $a<z<b$, then $z\in X$ and $z<b$, contradicting the minimality of $b$ in $X$. Hence there is no element of $A$ strictly between $a$ and $b$: the element $b$ is an immediate successor of $a$.

(b) Take $A=\ZZ$ with the usual order. For every $n\in\ZZ$ the integer $n+1$ satisfies $n<n+1$, and there is no integer strictly between $n$ and $n+1$, so $n+1$ is an immediate successor of $n$; thus every element of $\ZZ$ has an immediate successor. But $\ZZ$ is not well ordered: the set $\ZZ_{-}$ of negative integers is a nonempty subset of $\ZZ$ with no smallest element.
:::
