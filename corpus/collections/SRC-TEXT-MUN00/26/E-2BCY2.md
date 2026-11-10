---
schema: qual/card@1
id: E-2BCY2
kind: problem
title: Intersections of nested families of closed connected sets are connected
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 11, printed p. 171, with Theorem
    26.9 and Exercise 26.5; the stored theorem is printed there.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.11, PDF pp. 13-15. The intersection of a chain
    of closed connected sets is connected: a separation would be separated by disjoint open
    sets, and the chain members minus their union have the finite intersection property, so
    a point avoids both. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Theorem.
Let $X$ be a compact Hausdorff space.
Let $\mathcal{A}$ be a nonempty collection of closed connected subsets of $X$ that is simply ordered by proper inclusion.
Then

$$
Y = \bigcap_{A \in \mathcal{A}} A
$$

is connected.
[Hint: If $C \cup D$ is a separation of $Y$, choose disjoint open sets $U$ and $V$ of $X$ containing $C$ and $D$, respectively, and show that

$$
\bigcap_{A \in \mathcal{A}} (A - (U \cup V))
$$

is not empty.]
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.11, PDF pp. 13--15** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the finite-intersection argument is theirs.

**Theorem.** Let $X$ be compact Hausdorff and $\mathcal{A}$ a nonempty collection of closed connected subsets of $X$ simply ordered by proper inclusion. Then $Y=\bigcap_{A\in\mathcal{A}}A$ is connected.

*Proof.* Each $A$ is closed, so $Y$ is closed. Suppose $Y=C\cup D$ is a separation, with $C,D$ disjoint nonempty closed in $Y$ and hence in $X$; being closed subsets of the compact space $X$, they are compact, so by Exercise 26.5 there are disjoint open $U\supset C$, $V\supset D$ in $X$.

We show the family $\{A-(U\cup V)\}_{A\in\mathcal{A}}$ has the finite intersection property. For $A_{1}\subset\cdots\subset A_{n}$ in $\mathcal{A}$,
$$
\bigcap_{i\le n}\big(A_{i}-(U\cup V)\big)=A_{1}-(U\cup V),
$$
and this is nonempty: otherwise $A_{1}\subset U\cup V$, and since $A_{1}$ is connected and $U\cap V=\varnothing$ it lies in $U$ or in $V$; if $A_{1}\subset U$ then $Y\subset A_{1}\subset U$ and $D=Y\cap D\subset U\cap V=\varnothing$, a contradiction, and similarly for $V$.

The sets $A-(U\cup V)$ are closed in the compact $X$, so by Theorem 26.9 their total intersection in nonempty: there is $y\in Y$ with $y\notin U\cup V\supset C\cup D=Y$, a contradiction. Hence $Y$ is connected.
:::
