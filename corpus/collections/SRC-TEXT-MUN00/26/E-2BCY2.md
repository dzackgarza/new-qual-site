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

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.11, PDF pp. 13--15** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the finite-intersection argument is theirs, and its use of the hint is the book's.

Let $X$ be compact Hausdorff, let $\mathcal{A}$ be a nonempty collection of closed connected subsets of $X$ simply ordered by proper inclusion, and put $Y=\bigcap_{A\in\mathcal{A}}A$.

::: pf

::: {.pf-step #closed}
$Y$ is closed in $X$, and if $Y=C\cup D$ is a separation then $C$ and $D$ are disjoint nonempty compact subsets of $X$.

::: pf-proof
$Y$ is an intersection of closed sets, hence closed. A separation writes $Y$ as a union of two disjoint nonempty sets $C$, $D$ each closed in $Y$; since $Y$ is closed in $X$, a set closed in $Y$ is closed in $X$ (Theorem 17.3, printed p. 95: the closed subsets of a subspace are its intersections with closed sets of the ambient space, and intersecting a closed set with $Y$ keeps it closed). Closed subsets of the compact space $X$ are compact (Theorem 26.2, printed p. 165).
:::

:::

::: {.pf-step #separate}
There are disjoint open sets $U\supseteq C$ and $V\supseteq D$ of $X$.

::: pf-proof
$C$ and $D$ are disjoint compact subspaces of the Hausdorff space $X$, so Exercise 26.5 (printed p. 167) supplies such $U$ and $V$.
:::

:::

::: {.pf-step #fip}
The family $\theset{A\setminus(U\cup V)}_{A\in\mathcal{A}}$ consists of closed subsets of $X$ and has the finite intersection property.

:::: {.pf-proof}

::: {.pf-step #fip-closed}
Each $A\setminus(U\cup V)=A\cap(X\setminus U)\cap(X\setminus V)$ is closed in $X$, and each $A$ is nonempty.

::: pf-proof
$A$ is closed and $X\setminus U$, $X\setminus V$ are closed, so the intersection is closed. As $C\ne\varnothing$ we have $Y\ne\varnothing$, and $Y\subseteq A$, so $A\ne\varnothing$.
:::

:::

::: {.pf-step #fip-finite}
Every finite intersection $\bigcap_{i\le n}\big(A_{i}\setminus(U\cup V)\big)$ is nonempty.

::: pf-proof
By hypothesis the $A_{i}$ are simply ordered by proper inclusion, so after relabelling $A_{1}\subseteq A_{2}\subseteq\cdots\subseteq A_{n}$ and the intersection is $A_{1}\setminus(U\cup V)$. If it were empty, then $A_{1}\subseteq U\cup V$, and $A_{1}=(A_{1}\cap U)\cup(A_{1}\cap V)$ is a union of two disjoint sets open in the connected space $A_{1}$, which is nonempty by step [](#fip-closed){.pf-ref}; so one of them is empty, that is $A_{1}\subseteq U$ or $A_{1}\subseteq V$. In the first case $D=Y\cap D\subseteq A_{1}\cap D\subseteq U\cap V=\varnothing$, contradicting $D\ne\varnothing$; in the second, $C\subseteq A_{1}\cap C\subseteq U\cap V=\varnothing$, contradicting $C\ne\varnothing$. So the intersection is nonempty.
:::

:::

::::

:::

::: {.pf-step #contradiction}
$\bigcap_{A\in\mathcal{A}}\big(A\setminus(U\cup V)\big)\ne\varnothing$, which is impossible.

::: pf-proof
By step [](#fip){.pf-ref} the family is a collection of closed subsets of the compact space $X$ with the finite intersection property, so its total intersection is nonempty (Theorem 26.9, printed p. 169). A point $y$ of it lies in every $A\in\mathcal{A}$, hence in $Y$, and lies in $X\setminus(U\cup V)$, so $y\notin C\cup D=Y$: a contradiction.
:::

:::

::: {.pf-qed}
No separation of $Y$ exists, so $Y$ is connected.
:::

:::

:::
