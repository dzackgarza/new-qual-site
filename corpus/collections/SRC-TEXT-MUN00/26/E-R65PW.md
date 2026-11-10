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
---

::: {.exercise}

Show that a finite union of compact subspaces of $X$ is compact.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.3, PDF p. 12** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

Let $Y_{1},\dots,Y_{n}$ be compact subspaces of $X$ and $\mathcal{A}$ a cover of $Y=\bigcup_{i\le n}Y_{i}$ by sets open in $X$. For each $i$, $\mathcal{A}$ covers the compact space $Y_{i}$, so it has a finite subcollection $\mathcal{A}_{i}$ covering $Y_{i}$ (Theorem 26.1). Then $\bigcup_{i\le n}\mathcal{A}_{i}$ is a finite subcollection of $\mathcal{A}$ covering $Y$, so $Y$ is compact by Theorem 26.1.
:::
