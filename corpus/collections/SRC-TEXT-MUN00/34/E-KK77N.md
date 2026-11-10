---
schema: qual/card@1
id: E-KK77N
kind: problem
title: Locally metrizable regular Lindelof spaces are metrizable
classification:
  areas:
  - topology
  topics:
  - Metrizability
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Doug's World", "Munkres - Topology - Chapter 4
    Solutions" (30 August 2017), Problem 34.8, printed p. 12
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf), and dbFin, "Section 34: Problem 8 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-34-the-urysohn-metrization-theorem/problem-8-solution/
    (read 2026-11-10; kept at
    tmp/sources/dbfin/section-34-the-urysohn-metrization-theorem/problem-8-solution.txt); checked
    against Munkres, Topology (2000), Section 34 Exercise 8, printed p. 218, Exercise 30.9 and
    Exercise 30.5(b). The argument is the card's, and it answers the printed question about where
    regularity is used: to shrink a metrizable neighbourhood to one whose closure is closed in the
    Lindelof space, hence Lindelof and metrizable, hence second countable. What was corrected: the
    source writes "Since a closed subspace of a Lindeof space is Lindeof, cl(V_x) is Lindeof" and
    then "Since V_x is a subspace of U_x, it is metrizable. By exercise 30.5(b), cl(V_x) is second
    countable", applying 30.5(b) to the open subspace V_x where the argument gives it for the closed
    one, and then citing Theorem 30.2 for the passage to V_x; the card keeps the two steps separate.
---

::: {.exercise}

Show that a regular Lindelöf space is metrizable if it is locally metrizable.
[Hint: A closed subspace of a Lindelöf space is Lindelöf.] Regularity is essential; where do you use it in the proof?
:::

::: {.solution}
Let $x\in X$. Choose a metrizable neighborhood $N_x$ of $x$, and choose an open set $U_x$ with
$$
x\in U_x\subset N_x.
$$
Regularity is used now: choose an open $V_x$ such that
$$
x\in V_x\subset\overline{V_x}\subset U_x.
$$
The subspace $\overline{V_x}$ is closed in Lindelöf $X$, hence Lindelöf. It is also a subspace of the metrizable space $N_x$, so it is metrizable. Every Lindelöf metric space is second countable; therefore $\overline{V_x}$, and hence its open subspace $V_x$, has a countable basis.

The family $\{V_x:x\in X\}$ is an open cover of Lindelöf $X$. Choose a countable subcover
$$
V_{x_1},V_{x_2},\dots.
$$
For each $i$, let $\mathcal B_i$ be a countable basis for $V_{x_i}$. Since the $V_{x_i}$ are open in $X$,
$$
\mathcal B=\bigcup_{i=1}^\infty\mathcal B_i
$$
is a countable basis for $X$. The space $X$ is regular and second countable, so the Urysohn metrization theorem implies $X$ is metrizable.

The essential use of regularity was the shrinking
$$
x\in V_x\subset\overline{V_x}\subset U_x,
$$
which makes $\overline{V_x}$ a closed Lindelöf subspace while keeping it inside a metrizable neighborhood.
:::
