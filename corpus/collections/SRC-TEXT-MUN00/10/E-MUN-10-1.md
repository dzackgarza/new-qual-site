---
schema: qual/card@1
id: E-MUN-10-1
kind: problem
title: Well-ordered sets have the least upper bound property
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
    Read against Munkres, Topology (2000), §10 Exercise 1, printed p. 67; the stored
    statement is the printed sentence, and the definitions it uses are those of §10 printed
    p. 62 and of the least upper bound property in §10.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 10.1, printed p. 108
    (tmp/sources/munkres-solutions-whitman.pdf). The content is his: the set of upper bounds
    of B is a nonempty subset of the well-ordered A, and its smallest element is the least
    upper bound of B. Nothing else is used.
---

::: {.exercise}

Show that every well-ordered set has the least upper bound property.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.1, printed p. 108** (`tmp/sources/munkres-solutions-whitman.pdf`); the argument below is his.

Let $A$ be a well-ordered set, and let $B\subset A$ be nonempty and bounded above in $A$. Put
$$
C=\{u\in A\mid u\ge b \text{ for every } b\in B\},
$$
the set of upper bounds of $B$ in $A$. By hypothesis $C\ne\varnothing$. Since $C$ is a nonempty subset of the well-ordered set $A$, it has a smallest element $c$. As an element of $C$, $c$ is an upper bound of $B$; and if $u$ is any upper bound of $B$ then $u\in C$, so $c\le u$. Hence $c$ is the least upper bound of $B$ in $A$. As $B$ was an arbitrary nonempty subset of $A$ bounded above, $A$ has the least upper bound property.
:::
