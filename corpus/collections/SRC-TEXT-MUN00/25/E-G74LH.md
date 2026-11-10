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
---

::: {.exercise}

Let $X$ be locally path connected.
Show that every connected open set in $X$ is path connected.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 25.4, PDF p. 9** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the three-line argument is theirs.

Let $X$ be locally path connected and let $U$ be a connected open subset. By Theorem 25.4 each path component of the open set $U$ is open in $X$, hence open in $U$; being a path component it is also closed in $U$. So each path component of $U$ is a nonempty set both open and closed in the connected space $U$, and therefore equals $U$. Hence $U$ is path connected.
:::
