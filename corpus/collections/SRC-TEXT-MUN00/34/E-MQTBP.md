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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, and the two retained sets are now cited in the
    solution section rather than only here: Doug's World, Problem 34.7, printed p. 11 (whose
    footer reads Page 11, the page carrying 34.5 through 34.7), and the dbFin page by URL
    and date read. Pages checked one by one against the book: §34 Exercise 7 on printed
    p. 218; Theorem 34.1 (Urysohn metrization) on printed p. 215; Exercise 30.4, "every
    compact metrizable space has a countable basis", on printed p. 194 — the criterion both
    sources need where they cite "Exercise 31.4", which is about comparable topologies;
    Lemma 31.1(a) on printed p. 196 for the shrinking x in V_x inside closure(V_x) inside
    U; Lemma 26.1 on printed p. 164 for the finite subcover; Theorem 26.2 on printed p. 165
    for a closed subspace of a compact space being compact. One trap recorded: the
    regularity of a compact Hausdorff space is Theorem 32.3, printed p. 202, not
    Theorem 26.3, which is the different statement that a compact subspace of a Hausdorff
    space is closed. Steps now written out that the prose asserted: that the closure of the
    piece is metrizable because it lies in the metrizable neighbourhood, and that V_x, being
    open in that closure, is second countable with a countable basis; and the basis
    criterion for the finite union of the countable bases, verified at a point. No repair to
    the statement.
---

::: {.exercise}

A space $X$ is locally metrizable if each point $x$ of $X$ has a neighborhood that is metrizable in the subspace topology.
Show that a compact Hausdorff space $X$ is metrizable if it is locally metrizable.
[Hint: Show that $X$ is a finite union of open subspaces, each of which has a countable basis.]
:::

::: {.solution}
The argument is the retained published solution, **"Doug's World", *Munkres -- Topology -- Chapter 4 Solutions* (30 August 2017), Problem 34.7, printed p. 11** (`tmp/sources/munkres-solutions-dougsworld-ch4.pdf`), with the same proof at **dbFin, "Section 34: Problem 7 Solution"**, https://dbfin.com/topology/munkres/chapter-4/section-34-the-urysohn-metrization-theorem/problem-7-solution/ (read 2026-11-10); it is restructured into steps below. Both sources cite "Exercise 31.4" for the second countability of the closed metrizable piece, and Exercise 31.4 is about comparable topologies; the criterion they need is Exercise 30.4, which is what is cited here.

Throughout, $X$ is compact Hausdorff and locally metrizable, and the exercise is §34 Exercise 7. Two facts about subspaces are used repeatedly: an open subspace of a second-countable space is second countable, and a subspace of a metrizable space is metrizable.

::: pf

::: {.pf-step #regular}
$X$ is regular.

::: pf-proof
Every compact Hausdorff space is normal (Theorem 32.3), and its proof records the preceding step, that such a space is regular; for the form used below, regularity says that for a point $x$ and a neighbourhood $U$ of $x$ there is an open $V$ with $x\in V\subset\closure V\subset U$ (Lemma 31.1(a)).
:::

:::

::: {.pf-step #shrinking}
For each $x\in X$ there are a metrizable neighbourhood $N_x$ of $x$ and an open $V_x$ with
$$
x\in V_x\subset\closure{V_x}\subset U_x\subset N_x .
$$

::: pf-proof
Local metrizability gives a neighbourhood $N_x$ of $x$ that is metrizable in the subspace topology, and a neighbourhood contains an open set $U_x$ containing $x$; then step [](#regular){.pf-ref} with $U_x$ gives the open $V_x$ with $x\in V_x\subset\closure{V_x}\subset U_x$. Since $U_x\subset N_x$, the closure of $V_x$ lies in $N_x$.
:::

:::

::: {.pf-step #piece-basis}
Each $V_x$ has a countable basis.

::: pf-proof
$\closure{V_x}$ is closed in the compact space $X$, hence compact (Theorem 26.2), and it is metrizable because it is a subspace of the metrizable space $N_x$. A compact metrizable space has a countable basis (Exercise 30.4), and $\closure{V_x}$ is second countable. The set $V_x$ is open in $X$, so $V_x=V_x\cap\closure{V_x}$ is open in the subspace $\closure{V_x}$, and a subspace of a second-countable space is second countable; a countable basis of $V_x$ as a subspace consists of sets open in $V_x$.
:::

:::

::: {.pf-step #finite-cover}
Finitely many of the $V_x$ cover $X$.

::: pf-proof
The family $\{V_x\}_{x\in X}$ is an open cover of $X$, and $X$ is compact, so finitely many members $V_{x_1},\ldots,V_{x_m}$ cover $X$ (Lemma 26.1).
:::

:::

::: {.pf-step #countable-basis}
$X$ has a countable basis.

::: pf-proof
For each $i$ let $\mathcal{B}_i$ be a countable basis of the open subspace $V_{x_i}$, and let $\mathcal{B}=\bigcup_{i=1}^m\mathcal{B}_i$. Each member of $\mathcal{B}_i$ is open in $V_{x_i}$ and $V_{x_i}$ is open in $X$, so each member of $\mathcal{B}$ is open in $X$; and $\mathcal{B}$ is a finite union of countable sets, hence countable. It is a basis: if $x\in X$ and $O$ is an open neighbourhood of $x$, step [](#finite-cover){.pf-ref} gives $i$ with $x\in V_{x_i}$, then $O\cap V_{x_i}$ is a neighbourhood of $x$ in the subspace $V_{x_i}$, so there is $B\in\mathcal{B}_i$ with $x\in B\subset O\cap V_{x_i}\subset O$.
:::

:::

::: {.pf-step}
$X$ is metrizable.

::: pf-proof
$X$ is regular by step [](#regular){.pf-ref} and has a countable basis by step [](#countable-basis){.pf-ref}; the Urysohn metrization theorem (Theorem 34.1) states that every regular space with a countable basis is metrizable.
:::

:::

:::
:::
