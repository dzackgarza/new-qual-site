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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was checked against Munkres, *Topology* (2000), §10 Exercise 1, printed p. 66, and the argument is transcribed from the retained set: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.1, printed p. 108. Checked: the set of upper bounds is a nonempty subset of a well-ordered set, so it has a least element, which is the least upper bound.
---

::: {.exercise}

Show that every well-ordered set has the least upper bound property.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.1** (`tmp/sources/munkres-solutions-whitman.pdf`); the argument below is his. The statement is Munkres, *Topology* (2000), §10 Exercise 1.

::: pf

::: {.pf-step #bounds}
For a nonempty $B\subset A$ bounded above in a well-ordered set $A$, the set $C\coloneqq\{u\in A\st u\ge b\text{ for every }b\in B\}$ is nonempty.

::: pf-proof
The hypothesis that $B$ is bounded above says exactly that some $u\in A$ satisfies $u\ge b$ for every $b\in B$, and each such $u$ lies in $C$.
:::
:::

::: {.pf-step #least}
$C$ has a smallest element $c$.

::: pf-proof
$C$ is a nonempty subset of the well-ordered set $A$, and every nonempty subset of a well-ordered set has a least element.
:::
:::

::: {.pf-step #lub}
$c$ is an upper bound of $B$ and $c\le u$ for every upper bound $u$ of $B$.

::: pf-proof
As an element of $C$, $c$ satisfies $c\ge b$ for every $b\in B$, so it bounds $B$ above. If $u$ is any upper bound of $B$ then $u\in C$, and $c$ is the least element of $C$, so $c\le u$.
:::
:::

::: {.pf-step}
Every well-ordered set has the least upper bound property.

::: pf-proof
Steps [](#bounds){.pf-ref}, [](#least){.pf-ref} and [](#lub){.pf-ref} produce, for an arbitrary nonempty subset bounded above, a least upper bound in $A$; that is the least upper bound property.
:::
:::

:::
:::
