---
schema: qual/card@1
id: E-G74LH
kind: problem
title: Connected open sets in locally path connected spaces
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §25 Exercise 4, printed p. 162, with Theorem 25.3
    and Theorem 25.4; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 25.4, PDF p. 9. Path components of the open set
    are open by Theorem 25.4 and closed, so each connected open set is one path component.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained positron0802 solution (Chapter 3,
    Exercise 25.4, PDF p. 9). Checked against the book: §25 Exercise 4 as printed (p. 162);
    the definition of local path connectedness and Theorem 25.4 (printed p. 161), which is
    the only theorem used. Repair: the retained text, and this card's earlier prose, went
    from "each path component of U is open in U" to "both open and closed in U" without
    saying why a path component is closed, and that is false for an arbitrary space (a path
    component of the topologist's sine curve is not closed). The step is now supplied: the
    path components partition U, so the complement of one of them is the union of the
    others, which is open because each of them is. No repair to the printed statement.
---

::: {.exercise}

Let $X$ be locally path connected.
Show that every connected open set in $X$ is path connected.
:::

::: {.solution}
The argument is the retained published solution, **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 25.4** (`tmp/sources/munkres-solutions-positron-ch3.pdf`), restructured into steps; one step of it is supplied, where that text passes from "each path component of $U$ is open in $U$" to "thus each path component is both open and closed in $U$" without saying why a path component is closed, which is false in general.

Throughout, $X$ is locally path connected: at each point and for each neighbourhood $U$ of it there is a path-connected neighbourhood contained in $U$ (§25), and $U$ is an open connected subset of $X$.

::: pf

::: {.pf-step #open}
Each path component of $U$ is open in $U$.

::: pf-proof
Theorem 25.4 states that $X$ is locally path connected if and only if for every open set $V$ of $X$ each path component of $V$ is open in $X$. Applying it to the open set $U$ gives that a path component $P$ of $U$ is open in $X$, and a set open in $X$ and contained in $U$ is open in the subspace $U$.
:::

:::

::: {.pf-step #closed}
Each path component of $U$ is closed in $U$.

::: pf-proof
The path components of $U$ are the equivalence classes of the relation "joined by a path in $U$", so they are nonempty, pairwise disjoint, and cover $U$. Hence the complement in $U$ of a path component $P$ is the union of all the other path components, and each of those is open in $U$ by step [](#open){.pf-ref}; a union of open sets is open, so the complement of $P$ is open in $U$ and $P$ is closed in $U$. What is used here is that every path component of $U$ is open, not merely that $P$ is a path component: a path component of an arbitrary space need not be closed.
:::

:::

::: {.pf-step}
$U$ is path connected.

::: pf-proof
Every point of $U$ lies in a path component of $U$, and by steps [](#open){.pf-ref} and [](#closed){.pf-ref} each path component is a nonempty subset of $U$ that is both open and closed in $U$. A separation of $U$ is a pair of disjoint nonempty open sets covering $U$, so a space is connected exactly when its only subset that is both open and closed is the empty set or the whole space; $U$ is connected by hypothesis, so its only nonempty open and closed subset is $U$ itself. Hence $U$ has a single path component, namely $U$, and any two points of $U$ are joined by a path in $U$: thus $U$ is path connected.
:::

:::

:::
:::
