---
schema: qual/card@1
id: E-VXB5V
kind: problem
title: Discrete spaces have dimension zero
classification:
  areas:
  - topology
  topics:
  - Dimension
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
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The source claim needs a nonempty space when the empty space has dimension -1.'
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), §50 Exercise 1, printed p. 315, with the definitions of order and
    of topological dimension on printed p. 304: the cover by singletons refines any open cover and has order 1.
    What was corrected: the stored statement had narrowed the exercise to nonempty discrete spaces; it now
    states the exercise as printed, and the solution says why the nonempty case is what the book's definition of
    order can speak about, the empty collection having no point to count.
---

::: {.exercise}

Show that any discrete space has dimension 0.
:::

::: {.solution}
The book's definition of order presupposes a point lying in the elements counted, so the statement is read for a nonempty space $X$: for the empty space there is no dimension in this sense. Let $\mathcal U$ be an open cover of a nonempty discrete space $X$. The family of singletons
$$
\mathcal V=\{\{x\}:x\in X\}
$$
is an open cover refining $\mathcal U$: for each $x$, choose $U_x\in\mathcal U$ containing $x$, and then $\{x\}\subset U_x$. No point belongs to more than one member of $\mathcal V$, so $\mathcal V$ has order $1$. Thus $\dim X\le0$. For a nonempty space the dimension cannot be less than $0$, hence $\dim X=0$. (The empty space has the conventional dimension $-1$.)
:::
