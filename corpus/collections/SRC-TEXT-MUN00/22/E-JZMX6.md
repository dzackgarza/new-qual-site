---
schema: qual/card@1
id: E-JZMX6
kind: problem
title: Restrictions of open maps to open subspaces are open
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Exercise 5, printed p. 145; the stored
    statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 22.5, PDF p. 28. An open set U of the open
    subspace A is open in X, so p(U) is open in Y and its trace on p(A) is open there, which
    is q(U). (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $p: X \to Y$ be an open map.
Show that if $A$ is open in $X$, then the map $q: A \to p(A)$ obtained by restricting $p$ is an open map.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 22.5, PDF p. 28** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the argument is theirs.

Let $p:X\to Y$ be an open map and let $A\subset X$ be open; put $q=p\restrict_{A}:A\to p(A)$. For $U$ open in $A$, the set $U$ is open in $X$ because $A$ is open in $X$, so $p(U)$ is open in $Y$ since $p$ is an open map. And
$$
q(U)=p(U)=p(U)\cap p(A)
$$
is the trace on $p(A)$ of an open set of $Y$, hence open in the subspace $p(A)$. So $q$ is an open map.
:::
