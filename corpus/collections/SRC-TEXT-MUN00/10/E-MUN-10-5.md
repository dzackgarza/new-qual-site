---
schema: qual/card@1
id: E-MUN-10-5
kind: problem
title: Well-ordering theorem implies the axiom of choice
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
    Read against Munkres, Topology (2000), §10 Exercise 5, printed p. 67, and the statement
    of the choice axiom in §9 printed p. 59; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 10.5, printed p. 110.
    The construction is his: well-order the union of the family, and let c(A) be the least
    element of A in the restricted order, which exists because a subset of a well-ordered
    set is well ordered (§10, printed p. 64). The card adds the bookkeeping that this is
    exactly the choice axiom for a disjoint family and the choice-function form of Exercise
    9.5(a) for a general one.
---

::: {.exercise}

Show the well-ordering theorem implies the choice axiom.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.5, printed p. 110** (`tmp/sources/munkres-solutions-whitman.pdf`); the construction is his.

Let $\mathcal{A}$ be a collection of nonempty sets and let $U=\bigcup_{A\in\mathcal{A}}A$. By the well-ordering theorem there is an order relation on $U$ that well-orders it, and we fix one. Each $A\in\mathcal{A}$ is a nonempty subset of the well-ordered set $U$, so by property (1) of §10 every subset of a well-ordered set is well ordered in the restricted order, $A$ has a smallest element in the restricted order; call it $c(A)$.

This defines a function
$$
c:\mathcal{A}\longrightarrow U,\qquad A\longmapsto c(A)\in A,
$$
that is, a choice function on $\mathcal{A}$: it picks exactly one element out of each member of the family. Its range is a set consisting of exactly one element from each element of $\mathcal{A}$, which is the assertion of the choice axiom for a family of pairwise disjoint nonempty sets; and because $c$ is defined on an arbitrary collection of nonempty sets, it also gives the choice-function form of the axiom (Exercise 9.5(a)) without assuming the members of $\mathcal{A}$ to be disjoint.
:::
