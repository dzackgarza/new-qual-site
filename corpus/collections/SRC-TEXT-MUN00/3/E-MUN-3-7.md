---
schema: qual/card@1
id: E-MUN-3-7
kind: problem
title: The restriction of an order relation is an order relation
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
    Read against Munkres, Topology (2000), §3 Exercise 7, printed p. 29; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.7,
    printed pp. 26-27 (tmp/sources/munkres-solutions-whitman.pdf). The restriction here
    is < cap (A_0 x A_0), the same definition as in Exercise 2, and the three checks are
    his.
---

::: {.exercise}

Show that the restriction of an order relation is an order relation.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.7, printed pp. 26--27** (`tmp/sources/munkres-solutions-whitman.pdf`); the three checks below are his.

Let $<$ be an order relation on $A$ and let $A_0\subset A$; put $\prec\;=\;<\cap\,(A_0\times A_0)$, which is a relation on $A_0$.

*Comparability.* Let $x,y\in A_0$ be distinct. Since $x,y\in A$ and $<$ is an order relation, either $x<y$ or $y<x$; say $x<y$. Then $(x,y)\in A_0\times A_0$ as well, so $x\prec y$.

*Nonreflexivity.* Let $x\in A_0$. Since $x\in A$ and $<$ is nonreflexive, not $x<x$; hence $(x,x)\notin\,<$, so $(x,x)\notin\;\prec$.

*Transitivity.* Let $x\prec y$ and $y\prec z$. Then $x<y$ and $y<z$, so $x<z$ by transitivity of $<$, and $(x,z)\in A_0\times A_0$; hence $x\prec z$.

So $\prec$ is an order relation on $A_0$.
:::
