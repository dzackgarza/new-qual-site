---
schema: qual/card@1
id: E-LY1GZ
kind: problem
title: Connected sets crossing a set and its complement meet the boundary
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Boundary
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §23 Exercise 6, printed p. 152, with the
    definition of boundary in Exercise 17.19 and Lemma 23.1; the stored statement is the
    printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.6, PDF p. 2. If a connected set meeting both A
    and its complement missed the boundary, its two traces would be a separation, since
    neither would contain a limit point of the other. (tmp/sources/munkres-solutions-
    positron-ch3.pdf).
---

::: {.exercise}

Let $A \subset X$.
Show that if $C$ is a connected subspace of $X$ that intersects both $A$ and $X - A$, then $C$ intersects $\operatorname{Bd} A$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.6, PDF p. 2** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

Let $C$ be connected and let $A\subset X$ be such that $C\cap A\ne\varnothing\ne C\cap(X-A)$; put $P=C\cap A$ and $Q=C\cap(X-A)$, two nonempty disjoint sets with union $C$. Suppose $C\cap\operatorname{Bd}A=\varnothing$. Since $\operatorname{Bd}A=\overline{A}\cap\overline{X-A}$, this says no point of $C$ lies in both closures.

Then neither $P$ nor $Q$ contains a limit point of the other: a point $x\in Q$ that is a limit point of $P$ lies in $C$, in $\overline{A}$ (as a limit point of $P\subset A$) and in $Q\subset X-A\subset\overline{X-A}$, hence in $C\cap\operatorname{Bd}A$, contrary to the supposition; symmetrically for $Q$'s limit points in $P$. By Lemma 23.1 the pair $P,Q$ is then a separation of $C$, contradicting the connectedness of $C$. Hence $C\cap\operatorname{Bd}A\ne\varnothing$.
:::
