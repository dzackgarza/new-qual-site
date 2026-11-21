---
schema: qual/card@1
id: E-R65PW
kind: problem
title: Finite unions of compact subspaces are compact
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 3, printed p. 171, with Theorem
    26.1; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.3, PDF p. 12. A finite subcover of each compact
    piece, collected over the finitely many pieces, is a finite subcover of the union.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that the trace of an open cover on each compact
    piece has a finite subcover and that a finite union of the finitely many subcollections
    covers the union. positron0802, Chapter 3 Exercise 26.3, PDF p. 12. The printed
    statement needed no repair.
---

::: {.exercise}

Show that a finite union of compact subspaces of $X$ is compact.
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.3** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

::: pf

::: {.pf-step #subcovers}
Let $Y_{1},\dots,Y_{n}$ be compact subspaces of $X$ and $\mathcal{A}$ a cover of $Y=\bigcup_{i=1}^{n}Y_{i}$ by sets open in $X$. For each $i$ there is a finite subcollection $\mathcal{A}_{i}\subset\mathcal{A}$ covering $Y_{i}$.

::: pf-proof
Fix $i$. Each member of $\mathcal{A}$ is open in $X$, so its trace on $Y_{i}$ is open in the subspace $Y_{i}$, and those traces cover $Y_{i}$ because $\mathcal{A}$ covers $Y_{i}\subset Y$. The space $Y_{i}$ is compact, so finitely many of the traces cover it, say those of the members of a finite subcollection $\mathcal{A}_{i}\subset\mathcal{A}$; then $\mathcal{A}_{i}$ covers $Y_{i}$.
:::

:::

::: {.pf-step #finite}
$\bigcup_{i=1}^{n}\mathcal{A}_{i}$ is a finite subcollection of $\mathcal{A}$ covering $Y$.

::: pf-proof
It is a union of finitely many finite collections, hence finite, and its members are members of $\mathcal{A}$. A point of $Y$ lies in some $Y_{i}$, hence in a member of $\mathcal{A}_{i}\subset\bigcup_{j}\mathcal{A}_{j}$.
:::

:::

::: {.pf-step}
$Y$ is compact.

::: pf-proof
An arbitrary cover of $Y$ by open sets of $X$ has, by steps [](#subcovers){.pf-ref} and [](#finite){.pf-ref}, a finite subcollection covering $Y$; that is the definition of compactness of the subspace $Y$.
:::

:::

:::
:::
