---
schema: qual/card@1
id: E-IP1R7
kind: problem
title: The plane minus countably many points is path connected
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
    Read against Munkres, Topology (2000), §24 Exercise 9, printed p. 158, with the hint;
    the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.9, PDF p. 6. Through each point pass
    uncountably many lines and only countably many meet the countable set, so two lines
    avoiding it and meeting each other join the two points inside the complement.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Assume that $\RR$ is uncountable.
Show that if $A$ is a countable subset of $\RR^2$, then $\RR^2 - A$ is path connected.
[Hint: How many lines are there passing through a given point of $\RR^2$?]
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.9, PDF p. 6** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the two-line argument is theirs.

Let $A\subset\RR^{2}$ be countable and let $x,y\in\RR^{2}-A$.

Through $x$ pass uncountably many lines (one for each direction), and each line meets $A$ in at most as many points as $A$ has, so only countably many of them meet $A$; choose a line $L$ through $x$ with $L\cap A=\varnothing$. Similarly choose a line $M$ through $y$ with $M\cap A=\varnothing$ and $M$ not parallel to $L$, so that $L\cap M$ is a single point $z$; then $z\notin A$ since $z\in L$.

Now $L\cong\RR$ and $M\cong\RR$ are path connected, and $L\cup M$ is path connected because the two meet in $z$ (Exercise 24.8(d)); since $x,y\in L\cup M\subset\RR^{2}-A$, the points $x$ and $y$ are joined by a path in $\RR^{2}-A$. As $x,y$ were arbitrary, $\RR^{2}-A$ is path connected.
:::
