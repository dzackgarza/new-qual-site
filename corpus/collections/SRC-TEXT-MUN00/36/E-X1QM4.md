---
schema: qual/card@1
id: E-X1QM4
kind: problem
title: Compact locally euclidean Hausdorff spaces are manifolds
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: "Doug's World", "Munkres - Topology - Chapter
    4 Solutions" (30 August 2017), Problem 36.3 with Proposition 8, printed pp. 13-14
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf), and dbFin, "Section 36: Problem 3 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-36-imbeddings-of-manifolds/problem-3-solution/
    (read 2026-11-10; kept at
    tmp/sources/dbfin/section-36-imbeddings-of-manifolds/problem-3-solution.txt); checked against
    Munkres, Topology (2000), Section 36 Exercise 3, printed p. 227, Exercise 30.4 and Theorem 30.2.
    The card's proof is the direct one: each point has an open neighbourhood that is an open subspace
    of a Euclidean open set, hence second countable, and compactness gives finitely many of them whose
    countable bases together form a countable basis. The sources reach the same conclusion differently
    -- dbFin through Exercise 2 and second countability of a subspace of a Euclidean space, Doug's
    World by showing X is a finite union of closed metrizable subspaces, hence metrizable, and then
    citing Exercise 30.4; no correction to the mathematics was needed.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that an open neighbourhood of a point is an
    open subspace homeomorphic to an open subset of R^m and is second countable, that
    finitely many of them cover the compact space, and that the union of their countable
    bases is a basis for X by Lemma 13.2. The argument is the card's own; no retained set is
    cited. Munkres §36 Exercise 1, printed p. 228. The printed statement needed no repair.
---

::: {.exercise}

Let $X$ be a Hausdorff space such that each point of $X$ has a neighborhood that is homeomorphic with an open subset of $\RR^m$.
Show that if $X$ is compact, then $X$ is an $m$-manifold.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It is checked against Munkres §36 Exercise 1, printed p. 228, with the definitions of an $m$-manifold and of second countability.

::: pf

::: {.pf-step #local}
For each $x\in X$ there is an open set $V_{x}$ with $x\in V_{x}\subset X$ second countable and homeomorphic to an open subset of $\RR^{m}$.

::: pf-proof
By hypothesis there is a neighbourhood $U_{x}$ of $x$ homeomorphic to an open subset of $\RR^{m}$; a neighbourhood of $x$ contains an open set $V_{x}$ with $x\in V_{x}\subset U_{x}$, and $V_{x}$ is then an open subspace of $U_{x}$, hence homeomorphic to an open subset of an open subset of $\RR^{m}$, that is to an open subset of $\RR^{m}$. An open subset of $\RR^{m}$ is second countable, since the balls with rational centres and rational radii form a countable basis for $\RR^{m}$ (§20) and their intersections with an open set form a countable basis for it.
:::

:::

::: {.pf-step #finite}
Finitely many of the sets $V_{x}$ cover $X$.

::: pf-proof
The family $\{V_{x}\mid x\in X\}$ is an open cover of $X$, which is compact, so it has a finite subcover $V_{x_{1}},\dots,V_{x_{r}}$.
:::

:::

::: {.pf-step #basis}
The union of countable bases of the finitely many $V_{x_{i}}$ is a countable basis for $X$.

::: pf-proof
Choose a countable basis $\mathcal{B}_{i}$ for the open subspace $V_{x_{i}}$ and put $\mathcal{B}=\bigcup_{i=1}^{r}\mathcal{B}_{i}$, a countable union of countable sets and hence countable. Each member of $\mathcal{B}$ is open in $V_{x_{i}}$, hence open in $X$ because $V_{x_{i}}$ is open in $X$. If $x\in W$ with $W$ open in $X$, choose $i$ with $x\in V_{x_{i}}$; then $W\cap V_{x_{i}}$ is a neighbourhood of $x$ in the subspace $V_{x_{i}}$, so it contains a member $B\in\mathcal{B}_{i}$ with $x\in B$, and $x\in B\subset W$. So $\mathcal{B}$ is a basis for $X$ (Lemma 13.2) and $X$ is second countable.
:::

:::

::: {.pf-step}
$X$ is an $m$-manifold.

::: pf-proof
An $m$-manifold is a second countable Hausdorff space each of whose points has a neighbourhood homeomorphic to an open subset of $\RR^{m}$. Hausdorffness is the hypothesis, the local condition is the hypothesis through step [](#local){.pf-ref}, and second countability is step [](#basis){.pf-ref}.
:::

:::

:::
:::
