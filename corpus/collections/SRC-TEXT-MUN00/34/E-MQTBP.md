---
schema: qual/card@1
id: E-MQTBP
kind: problem
title: Locally metrizable compact Hausdorff spaces are metrizable
classification:
  areas:
  - topology
  topics:
  - Metrizability
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: "Doug's World", "Munkres - Topology - Chapter
    4 Solutions" (30 August 2017), Problem 34.7, printed p. 11
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf), and dbFin, "Section 34: Problem 7 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-34-the-urysohn-metrization-theorem/problem-7-solution/
    (read 2026-11-10; kept at
    tmp/sources/dbfin/section-34-the-urysohn-metrization-theorem/problem-7-solution.txt); checked
    against Munkres, Topology (2000), Section 34 Exercise 7, printed p. 218, and its printed hint,
    with Lemma 31.1(a), Exercise 30.4 and Theorem 34.1. The proof is the card's: shrink each
    metrizable neighbourhood N_x to V_x with closure inside an open U_x inside N_x, note that the
    closure is compact metrizable hence second countable and so V_x has a countable basis, cover X
    by finitely many of them, and take the union of the countable bases. What was corrected: the
    source writes "By exercise 31.4, cl(V_x) has a countable basis", and Exercise 31.4 is about
    comparable topologies; the compact-matrizable criterion is Exercise 30.4, and the card cites it.
---

::: {.exercise}

A space $X$ is locally metrizable if each point $x$ of $X$ has a neighborhood that is metrizable in the subspace topology.
Show that a compact Hausdorff space $X$ is metrizable if it is locally metrizable.
[Hint: Show that $X$ is a finite union of open subspaces, each of which has a countable basis.]
:::

::: {.solution}
Since $X$ is compact Hausdorff, it is regular. For each $x\in X$, choose a metrizable neighborhood $N_x$. Choose an open $U_x$ with $x\in U_x\subset N_x$, and by regularity choose an open $V_x$ with
$$
x\in V_x\subset\overline{V_x}\subset U_x.
$$
The closed subspace $\overline{V_x}$ is compact and metrizable, hence second countable. Therefore the open subspace $V_x$ has a countable basis.

Compactness of $X$ gives finitely many such open sets
$$
V_{x_1},\dots,V_{x_m}
$$
covering $X$. The union of countable bases for these finitely many open subspaces is a countable basis for $X$. Since compact Hausdorff spaces are regular, the Urysohn metrization theorem now implies $X$ is metrizable.
:::
