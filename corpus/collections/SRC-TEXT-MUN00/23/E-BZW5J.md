---
schema: qual/card@1
id: E-BZW5J
kind: problem
title: Unions of connected sets meeting a common connected set
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
    Read against Munkres, Topology (2000), §23 Exercise 3, printed p. 152, with Theorem
    23.3; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.3, PDF p. 2. Each A union A_alpha is connected
    because the two parts meet, and the family of those has a common point, so the union is
    connected by Theorem 23.3 twice. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $\theset{A_\alpha}$ be a collection of connected subspaces of $X$; let $A$ be a connected subspace of $X$.
Show that if $A \cap A_\alpha \neq \varnothing$ for all $\alpha$, then $A \cup (\bigcup A_\alpha)$ is connected.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.3, PDF p. 2** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the two applications of Theorem 23.3 are theirs.

For each $\alpha$, the set $A\cup A_{\alpha}$ is connected: it is the union of the connected sets $A$ and $A_{\alpha}$, which meet because $A\cap A_{\alpha}\ne\varnothing$ (Theorem 23.3). Now $\{A\cup A_{\alpha}\}_{\alpha}$ is a collection of connected sets all containing any fixed point of $A$ (which is nonempty, since it meets each $A_{\alpha}$), so their union
$$
\bigcup_{\alpha}\big(A\cup A_{\alpha}\big)=A\cup\bigcup_{\alpha}A_{\alpha}
$$
is connected by Theorem 23.3 again.
:::
