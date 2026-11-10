---
schema: qual/card@1
id: E-Y0QAW
kind: problem
title: Quotients of locally connected spaces are locally connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §25 Exercise 8, printed p. 162, with Theorem 25.3
    and the hint; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 25.8, PDF p. 10. The preimage of a component of an
    open set is a union of components of the preimage of the open set, hence open, hence the
    component is open in the quotient. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $p: X \to Y$ be a quotient map.
Show that if $X$ is locally connected, then $Y$ is locally connected.
[Hint: If $C$ is a component of the open set $U$ of $Y$, show that $p^{-1}(C)$ is a union of components of $p^{-1}(U)$.]
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 25.8, PDF p. 10** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument follows the hint.

Let $p:X\to Y$ be a quotient map with $X$ locally connected, let $U$ be open in $Y$ and $C$ a component of $U$. We show $C$ is open, which gives the result by Theorem 25.3.

If $D$ is a component of $p^{-1}(U)$ meeting $p^{-1}(C)$, then $p(D)$ is connected and meets $C$, so $p(D)\subset C$ and $D\subset p^{-1}(C)$. Thus $p^{-1}(C)$ is a union of components of the open set $p^{-1}(U)$; since $X$ is locally connected those components are open in $X$ (Theorem 25.3), so $p^{-1}(C)$ is open in $X$. As $p$ is a quotient map, $C$ is open in $Y$.
:::
