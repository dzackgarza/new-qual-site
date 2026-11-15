---
schema: qual/card@1
id: E-KWBI9
kind: problem
title: Connected $T_1$ spaces have positive dimension
classification:
  areas:
  - topology
  topics:
  - Dimension
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), §50 Exercise 2, printed p. 315, with the definition of dimension by
    order of refinements and the $T_1$ axiom. The argument: for distinct a, b the two open sets X - {a} and
    X - {b} cover X; a refinement of order 1 has pairwise disjoint members, none of them all of X, so splitting
    it at one member separates X, contradicting connectedness. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located proves Munkres §50 Exercise 2 (printed p. 315),
    and the card's own argument stands: the two-set cover by the complements of two distinct points refines to
    a cover of order at most 1 only if that cover separates the space. Murayama's selection has no Chapter 8,
    dbFin has no chapter-8 page, the ten GitHub repositories of Munkres solutions listed in COMPLAINTS.md stop
    before §36, and the AoPS post *Topology by Munkres Chapter 8 | Day 18*
    (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with its formulas lost. The
    Stack Exchange queries of this pass are in the COMPLAINTS.md entry for §43--§50; none of them returned this
    exercise. Nothing needed correction.
---

::: {.exercise}

Show that any connected $T_1$ space having more than one point has dimension at least 1.
:::

::: {.solution}
Suppose, toward a contradiction, that $\dim X=0$. Choose distinct points $a,b\in X$. Since $X$ is $T_1$,
$$
U=X-\{a\},\qquad V=X-\{b\}
$$
are open and cover $X$. Dimension zero gives an open cover $\mathcal W$ refining $\{U,V\}$ and having order at most $1$. Hence distinct members of $\mathcal W$ are disjoint.

No single member of $\mathcal W$ can equal $X$, since each is contained in either $U$ or $V$, both proper. Therefore $\mathcal W$ has at least two nonempty members. Taking one member $W_0$ and the union of all the others gives two disjoint nonempty open sets whose union is $X$, contradicting connectedness. Thus $\dim X\ge1$.
:::
