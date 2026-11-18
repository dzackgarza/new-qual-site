---
schema: qual/card@1
id: E-5GHY2
kind: problem
title: Projections with compact factor are closed maps
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 7, printed p. 171, with the tube
    lemma; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.7, PDF p. 13. A point outside the image gives a
    slice disjoint from the closed set, and the tube lemma produces a neighbourhood of it
    disjoint from the image. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that if $Y$ is compact, then the projection $\pi_1: X \times Y \to X$ is a closed map.
:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.7, PDF p. 13** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the tube-lemma argument is theirs, with the two inclusions separated below.

Let $Y$ be compact and let $C\subseteq X\times Y$ be closed.

::: pf

::: {.pf-step #open-slice}
For $x_{0}\notin\pi_{1}(C)$ the set $N=(X\times Y)\setminus C$ is open in $X\times Y$ and contains the slice $\{x_{0}\}\times Y$.

::: pf-proof
$N$ is the complement of a closed set, hence open. If $(x_{0},y)\in C$ for some $y$, then $x_{0}=\pi_{1}(x_{0},y)\in\pi_{1}(C)$, contrary to hypothesis; so no point of the slice lies in $C$.
:::

:::

::: {.pf-step #tube}
There is a neighbourhood $W$ of $x_{0}$ in $X$ with $W\times Y\subseteq N$.

::: pf-proof
$Y$ is compact, so the tube lemma (Lemma 26.8, printed p. 168) applies to the open set $N$ containing the slice $\{x_{0}\}\times Y$ and yields a neighbourhood $W$ of $x_{0}$ with $W\times Y\subseteq N$.
:::

:::

::: {.pf-step #miss}
$W\cap\pi_{1}(C)=\varnothing$.

::: pf-proof
If $x\in W$ and $x=\pi_{1}(x,y)$ for some $(x,y)\in C$, then $(x,y)\in W\times Y\subseteq N$ by step [](#tube){.pf-ref}, while $(x,y)\in C$; but $N$ is the complement of $C$, a contradiction.
:::

:::

::: {.pf-qed}
Every point of $X\setminus\pi_{1}(C)$ has a neighbourhood $W$ inside it by steps [](#open-slice){.pf-ref} and [](#miss){.pf-ref}, so $\pi_{1}(C)$ is closed. As $C$ was an arbitrary closed subset of $X\times Y$, the projection $\pi_{1}$ is a closed map.
:::

:::

:::
