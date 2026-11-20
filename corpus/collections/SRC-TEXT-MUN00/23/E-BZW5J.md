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

The argument is **"positron0802"**, *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.3 (`tmp/sources/munkres-solutions-positron-ch3.pdf`); its two applications of Theorem 23.3 are the ones below, and the statement was checked against Munkres, *Topology* (2000), §23 Exercise 3, with Theorem 23.3 on printed p. 150.

::: pf

::: {.pf-step #pairs-connected}
For every $\alpha$ the set $A\cup A_{\alpha}$ is connected.

::: pf-proof
$A$ and $A_{\alpha}$ are connected subspaces of $X$ and $A\cap A_{\alpha}\neq\varnothing$ by hypothesis, so $A\cup A_{\alpha}$ is a union of connected subspaces with a common point and is connected by Theorem 23.3.
:::

:::

::: {.pf-step #common-point}
$A\neq\varnothing$, and every set $A\cup A_{\alpha}$ contains each point of $A$.

::: pf-proof
The collection $\theset{A_{\alpha}}$ is assumed nonempty for the intersections $A\cap A_{\alpha}$ to be formed; picking an $\alpha$ and a point of $A\cap A_{\alpha}$ exhibits a point of $A$. Every set $A\cup A_{\alpha}$ contains $A$ as a subset, hence contains any fixed point $a_{0}\in A$.
:::

:::

::: {.pf-step #union-identity}
$\bigcup_{\alpha}(A\cup A_{\alpha})=A\cup\bigcup_{\alpha}A_{\alpha}$.

::: pf-proof
A point of the left side lies in $A$ or in some $A_{\alpha}$, hence in the right side; a point of the right side lies in $A$, and then in every $A\cup A_{\alpha}$, or in some $A_{\alpha}$ and then in that $A\cup A_{\alpha}$, so it lies on the left.
:::

:::

::: pf-step
Therefore $A\cup\bigcup_{\alpha}A_{\alpha}$ is connected.

::: pf-proof
By steps [](#pairs-connected){.pf-ref} and [](#common-point){.pf-ref} it is, up to the rewriting of step [](#union-identity){.pf-ref}, a union of connected subspaces of $X$ that all contain the point $a_{0}$, so Theorem 23.3 makes it connected.
:::

:::

:::

:::
