---
schema: qual/card@1
id: E-LEN3V
kind: problem
title: Unions of intersecting sequences of connected subspaces
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
    Read against Munkres, Topology (2000), §23 Exercise 2, printed p. 152, with Lemma 23.2
    and Theorem 23.3; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.2, PDF pp. 1-2. The first set lies in one side
    of a would-be separation and then, inductively, so does each successive set, because
    consecutive sets meet; so the other side is empty. (tmp/sources/munkres-solutions-
    positron-ch3.pdf).
---

::: {.exercise}

Let $\theset{A_n}$ be a sequence of connected subspaces of $X$, such that $A_n \cap A_{n+1} \neq \varnothing$ for all $n$.
Show that $\bigcup A_n$ is connected.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.2, PDF pp. 1--2** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

Let $Y=\bigcup_{n}A_{n}$ with each $A_{n}$ connected and $A_{n}\cap A_{n+1}\ne\varnothing$, and suppose $Y=B\cup C$ is a separation, with $B,C$ disjoint nonempty open subsets of $Y$.

$A_{1}$ is connected and contained in $B\cup C$, so by Lemma 23.2 (printed p. 150) $A_{1}$ lies in $B$ or in $C$; assume $A_{1}\subset B$. Inductively, if $A_{n}\subset B$ then $A_{n+1}\subset B$: otherwise $A_{n+1}\subset C$, and then $A_{n}\cap A_{n+1}\subset B\cap C=\varnothing$, contradicting the hypothesis. So $A_{n}\subset B$ for every $n$ and $Y=\bigcup A_{n}\subset B$, against $C\ne\varnothing$. Hence no separation exists and $Y$ is connected.
:::
