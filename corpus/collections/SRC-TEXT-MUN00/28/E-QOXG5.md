---
schema: qual/card@1
id: E-QOXG5
kind: problem
title: Countable compactness equals limit point compactness for T1 spaces
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
    Read against Munkres, Topology (2000), §28 Exercise 4, printed p. 181, with the
    definition of countable compactness printed there and Exercise 17.15; the stored
    statement and hint are printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 28.4, PDF pp. 18-19. Countable compactness gives
    limit point compactness with no separation hypothesis, and the converse uses T1 to
    isolate the limit point from finitely many chosen points. (tmp/sources/munkres-
    solutions-positron-ch3.pdf).
---

::: {.exercise}

A space $X$ is said to be countably compact if every countable open covering of $X$ contains a finite subcollection that covers $X$.
Show that for a $T_1$ space $X$, countable compactness is equivalent to limit point compactness.
[Hint: If no finite subcollection of $U_n$ covers $X$, choose $x_n \notin U_1 \cup \dots \cup U_n$, for each $n$.]
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 28.4, PDF pp. 18--19** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both directions are theirs, following the hint.

*Countably compact implies limit point compact.* First note that a closed subset $Y$ of a countably compact space is countably compact: a countable open cover of $Y$, together with $X-Y$, covers $X$, and a finite subcover restricts to one of $Y$. Now let $A\subset X$ be infinite and $B\subset A$ a countably infinite subset with no limit point; then $B$ is closed, hence countably compact, yet the neighbourhoods $U_{b}$ of its points meeting $B$ only in $b$ give a countable cover with no finite subcover — a contradiction. So $A$ has a limit point. (The $T_{1}$ hypothesis is not used in this direction.)

*Limit point compact and $T_{1}$ implies countably compact.* Suppose $\{U_{n}\}$ is a countable open cover with no finite subcover and choose $x_{n}\notin U_{1}\cup\cdots\cup U_{n}$. The infinite set $A=\{x_{n}\}$ has a limit point $y$, lying in some $U_{1}\cup\cdots\cup U_{N}$; since $X$ is $T_{1}$ each $x_{i}$, $i\le N$, has a neighbourhood $V_{i}$ omitting $y$ (Exercise 17.15), and then $\big(V_{1}\cap\cdots\cap V_{N}\big)\cap\big(U_{1}\cup\cdots\cup U_{N}\big)$ is a neighbourhood of $y$ meeting $A$ in nothing, a contradiction.
:::
