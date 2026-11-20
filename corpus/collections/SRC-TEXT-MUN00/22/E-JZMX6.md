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

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 22.5** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the argument is theirs, with the two uses of openness separated below.

Let $p:X\to Y$ be an open map, let $A$ be open in $X$, and put $q=p\restriction_{A}:A\to p(A)$.

::: pf

::: {.pf-step #open-in-X}
If $U$ is open in the subspace $A$, then $U$ is open in $X$.

::: pf-proof
$U=A\cap V$ for some open $V$ of $X$; since $A$ is open in $X$, the intersection $A\cap V$ is open in $X$.
:::

:::

::: {.pf-step #image-open}
$p(U)$ is open in $Y$.

::: pf-proof
$U$ is open in $X$ by step [](#open-in-X){.pf-ref}, and $p$ is an open map.
:::

:::

::: {.pf-step #trace}
$q(U)=p(U)\cap p(A)$.

::: pf-proof
For $U\subseteq A$ one has $q(U)=p(U)$, because $q$ agrees with $p$ on $A$ and $U$ lies in $A$; and $p(U)\subseteq p(A)$, so $p(U)\cap p(A)=p(U)$.
:::

:::

::: {.pf-qed}
For every $U$ open in $A$ the set $q(U)=p(U)\cap p(A)$ is, by steps [](#image-open){.pf-ref} and [](#trace){.pf-ref}, the trace on $p(A)$ of an open set of $Y$, hence open in the subspace $p(A)$. So $q$ is an open map.
:::

:::

:::
