---
schema: qual/card@1
id: E-MUN-6-7
kind: problem
title: Finiteness of function sets between finite sets
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 6, Exercise 7; the stored statement matches.
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
    Read against Munkres, Topology (2000), §6 Exercise 7, printed p. 44; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 6.7,
    printed pp. 79-80 (tmp/sources/munkres-solutions-whitman.pdf). His bijection
    B^A -> B^n is g -> g o f^{-1} for a fixed bijection f : A -> {1,...,n}, which is the
    card's n-tuple correspondence; he treats the case A empty separately, as the card
    does. No defect found.
---

::: {.exercise}

If $A$ and $B$ are finite, show that the set of all functions $f: A \to B$ is finite.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 6.7, printed pp. 79--80** (`tmp/sources/munkres-solutions-whitman.pdf`); his bijection $B^A\to B^n$, $g\mapsto g\circ f^{-1}$, is the $n$-tuple correspondence below, and he separates the case $A=\varnothing$ as the card does.

Let $\cardinality{A}=n$ and $\cardinality{B}=m$. After choosing a bijection
$$
A\cong\{1,\dots,n\},
$$
a function $f:A\to B$ is uniquely determined by the $n$-tuple
$$
(f(1),\dots,f(n))\in B^n.
$$
Thus the set $B^A$ of all functions $A\to B$ is in bijection with $B^n$. A finite cartesian product of finite sets is finite, so $B^n$, and hence $B^A$, is finite.

More precisely, when $n,m>0$,
$$
\cardinality{B^A}=m^n.
$$
If $A=\varnothing$, there is exactly one function $A\to B$; if $B=\varnothing$ and $A\ne\varnothing$, there are none. These cases are finite as well.
:::
