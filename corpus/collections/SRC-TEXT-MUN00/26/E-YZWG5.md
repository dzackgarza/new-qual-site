---
schema: qual/card@1
id: E-YZWG5
kind: problem
title: Separating disjoint compact sets in a Hausdorff space
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 5, printed p. 171, with Lemma 26.4;
    the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.5, PDF pp. 12-13. Lemma 26.4 at each point of A
    gives disjoint open sets, and finitely many of them cover the compact A; the union of
    the one side and the intersection of the other are disjoint open sets around A and B.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained positron0802 solution (Chapter 3, Exercise 26.5, PDF pp. 12-13); statement unchanged. The disjointness argument is its own step and now says explicitly that the point of U lies in some U_{x_i} and that V is contained in that same V_{x_i}, which is what the contradiction needs; the passage from the open cover of the subspace A to the finite subcover is written out. Pages checked against the retained PDF: Lemma 26.4 on printed p. 166, the topology axioms on printed p. 76, the subspace topology on printed p. 89, the exercise on printed p. 171.

---

::: {.exercise}

Let $A$ and $B$ be disjoint compact subspaces of the Hausdorff space $X$.
Show that there exist disjoint open sets $U$ and $V$ containing $A$ and $B$, respectively.

:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.5, PDF pp. 12--13** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

Throughout, $X$ is a Hausdorff space, $A,B\subset X$ are compact and disjoint, and Lemma 26.4 says that if $Y$ is a compact subspace of the Hausdorff space $X$ and $x_0\in X-Y$, then there are disjoint open sets containing $x_0$ and $Y$ respectively; the exercise is on printed p. 171.

::: pf

::: {.pf-step #separation-at-a-point}
For each $x\in A$ there are disjoint open sets $U_x$ and $V_x$ of $X$ with $x\in U_x$ and $B\subset V_x$.

::: pf-proof
$x\in A$ and $A\cap B=\varnothing$ give $x\notin B$; and $B$ is a compact subspace of the Hausdorff space $X$. So Lemma 26.4 applies with $Y=B$ and $x_0=x$, and supplies disjoint open $U_x\ni x$ and $V_x\supset B$.

:::

:::

::: {.pf-step #finite-subcover}
Finitely many of the sets $U_x$ cover $A$.

::: pf-proof
The family $\{U_x\}_{x\in A}$ is a cover of $A$ by sets open in $X$, since $x\in U_x$ for each $x$; their traces on $A$ form an open cover of the subspace $A$ (printed p. 89). As $A$ is compact, finitely many of those traces cover $A$, say for $x_1,\dots,x_n\in A$; then $A\subset U_{x_1}\cup\cdots\cup U_{x_n}$.

:::

:::

::: {.pf-step #the-sets}
$U=U_{x_1}\cup\cdots\cup U_{x_n}$ and $V=V_{x_1}\cap\cdots\cap V_{x_n}$ are open, contain $A$ and $B$ respectively, and are disjoint.

::: pf-proof
$U$ is a finite union of open sets and $V$ a finite intersection, so both are open (a topology is closed under finite unions and intersections, printed p. 76). $U$ contains $A$ by step [](#finite-subcover){.pf-ref}. Each $V_{x_i}$ contains $B$, so $V$ does too. If $c\in U\cap V$, then $c\in U_{x_i}$ for some $i$ while $c\in V\subset V_{x_i}$; but $U_{x_i}\cap V_{x_i}=\varnothing$ by step [](#separation-at-a-point){.pf-ref}, a contradiction. Hence $U\cap V=\varnothing$.

:::

:::

:::

:::
