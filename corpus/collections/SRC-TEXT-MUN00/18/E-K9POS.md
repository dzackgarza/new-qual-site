---
schema: qual/card@1
id: E-K9POS
kind: problem
title: Continuous images of limit points
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Limit Points
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 2, printed p. 111, with the
    definitions of limit point and of continuity in §17 and §18; the stored statement is the
    printed question.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 18.2, PDF p. 11. The counterexample is a constant
    map on X = R, continuous by Theorem 18.2, whose image has one point and so has no limit
    points. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Suppose that $f: X \to Y$ is continuous.
If $x$ is a limit point of the subset $A$ of $X$, is it necessarily true that $f(x)$ is a limit point of $f(A)$?
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 18.2, PDF p. 11** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the counterexample is theirs. Whitman, printed p. 179, gives the same one.

**No.** Let $X=\RR$ with the usual topology, $Y$ any space with a point $y_{0}$, and $f:X\to Y$ the constant map $f(x)=y_{0}$; $f$ is continuous (Munkres, Theorem 18.2(a)). Take $A=X$, so that every real number is a limit point of $A$. But $f(A)=\{y_{0}\}$, and a neighbourhood of $f(x)=y_{0}$ meets $f(A)$ only in $y_{0}$ itself; so $f(x)$ is not a limit point of $f(A)$.

Continuity preserves the property of being in the closure (Theorem 18.1: $f(\overline{A})\subset\overline{f(A)}$) but not the property of being a limit point.
:::
