---
schema: qual/card@1
id: E-MUN-3-13
kind: problem
title: The least upper bound property implies the greatest lower bound property
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
    Read against Munkres, Topology (2000), §3 Exercise 13, printed p. 29; the exercise
    prints the theorem "if an ordered set A has the least upper bound property, then it
    has the greatest lower bound property" and asks for the proof. The stored statement
    matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.13,
    printed p. 35 (tmp/sources/munkres-solutions-whitman.pdf). His proof through the set
    B_0 of lower bounds is the one below.
---

::: {.exercise}

Prove the following:

Theorem. If an ordered set $A$ has the least upper bound property, then it has the greatest lower bound property.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.13, printed p. 35** (`tmp/sources/munkres-solutions-whitman.pdf`); the argument through the set of lower bounds is his.

Let $A$ have the least upper bound property, let $A_0\subset A$ be nonempty and bounded below, and let
$$
B_0=\{x\in A\mid x \text{ is a lower bound of } A_0\},
$$
which is nonempty by hypothesis. Choose $a\in A_0$; then every $x\in B_0$ satisfies $x\le a$, so $a$ is an upper bound of $B_0$. Hence $B_0$ is nonempty and bounded above, and has a least upper bound $c=\sup B_0$.

*$c$ is a lower bound of $A_0$.* Let $x\in A_0$. Every $y\in B_0$ satisfies $y\le x$, so $x$ is an upper bound of $B_0$; since $c$ is the least one, $c\le x$.

*$c$ is the greatest lower bound.* If $y$ is any lower bound of $A_0$ then $y\in B_0$, so $y\le c$ because $c$ is an upper bound of $B_0$.

Hence every nonempty bounded-below subset of $A$ has a greatest lower bound, so $A$ has the greatest lower bound property.
:::
