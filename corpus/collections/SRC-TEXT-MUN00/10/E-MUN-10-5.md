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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained Whitman solution (Exercise 10.5, printed p. 110); statement unchanged. The construction is split into the fixed well-ordering of the union, the definition of c with the uniqueness of the least element doing the work of single-valuedness, the disjoint case in which the range of c is a transversal, and the general choice-function form; the last two are separate because the book's axiom is stated for disjoint families only, so the disjoint case is what the axiom literally needs and the general form is a bonus. Pages checked against the retained PDF: the definition of well-ordering and property (1) on printed pp. 63-64, the well-ordering theorem on printed p. 65, the choice axiom on printed p. 59, the exercise on printed p. 67.

---

::: {.exercise}

Show the well-ordering theorem implies the choice axiom.

:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.5, printed p. 110** (`tmp/sources/munkres-solutions-whitman.pdf`); the construction is his, and the card adds the bookkeeping that the set obtained is exactly the form the choice axiom asserts for a disjoint family, together with the choice-function form for a general one.

Throughout, $A$ with an order relation is well-ordered when every nonempty subset of $A$ has a smallest element (definition, printed p. 63), and then every subset of $A$ is well ordered in the restricted order (property (1) of §10, printed pp. 63--64). The well-ordering theorem is the assertion that every set admits an order relation making it well ordered (§10, printed p. 65); the exercise is on printed p. 67.

::: pf

::: {.pf-step #wellorder}
Every collection $\mathcal{A}$ of nonempty sets is equipped, by the well-ordering theorem, with a fixed order that well-orders its union.

::: pf-proof
Let $U=\bigcup_{A\in\mathcal{A}}A$, which is a set by the union axiom. The well-ordering theorem gives an order relation on $U$ that well-orders it; fix such an order once and for all.

:::

:::

::: {.pf-step #choice-function}
The rule $c(A)=$ the smallest element of $A$ in the restricted order is a function on $\mathcal{A}$ with $c(A)\in A$ for every $A\in\mathcal{A}$.

::: pf-proof
Each $A\in\mathcal{A}$ is nonempty and is a subset of the well-ordered set $U$, so by property (1) it is well ordered in the restricted order and hence has a smallest element; call it $c(A)$. The smallest element of $A$ is an element of $A$, and it is unique, since if $a,a'$ were both smallest then $a\le a'$ and $a'\le a$, and an order relation is antisymmetric. So $c$ is single-valued, defined on all of $\mathcal{A}$, and $c(A)\in A$.

:::

:::

::: {.pf-step #transversal}
If the members of $\mathcal{A}$ are pairwise disjoint, the range of $c$ is a set consisting of exactly one element of each $A\in\mathcal{A}$.

::: pf-proof
Let $C=c(\mathcal{A})$. Then $C$ is contained in $\bigcup_{A\in\mathcal{A}}A$, and $c(A)\in C\cap A$ because $c(A)\in A$. If $x\in C\cap A$ then $x=c(A')$ for some $A'\in\mathcal{A}$ and $x\in A$; if $A'\neq A$ then $x\in A'\cap A=\varnothing$, a contradiction, so $A'=A$ and $x=c(A)$. Hence $C\cap A=\{c(A)\}$ for every $A\in\mathcal{A}$, which is the assertion of the choice axiom (§9, printed p. 59).

:::

:::

::: {.pf-step #general}
The choice-function form of the axiom holds for an arbitrary collection of nonempty sets.

::: pf-proof
Steps [](#wellorder){.pf-ref} and [](#choice-function){.pf-ref} apply to any collection $\mathcal{A}$ of nonempty sets, with no disjointness hypothesis: the well-ordering is imposed on $\bigcup\mathcal{A}$ whether or not the members overlap, and $c(A)$, the least element of $A$, is still an element of $A$. Hence there is a function $c$ on $\mathcal{A}$ with $c(A)\in A$ for every $A$, which is the form of the axiom used in Exercise 9.5(a).

:::

:::

:::

:::
