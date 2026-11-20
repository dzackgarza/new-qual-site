---
schema: qual/card@1
id: E-QGR6H
kind: problem
title: Compact unions of closed metrizable subspaces are metrizable
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
    4 Solutions" (30 August 2017), Problem 34.9 with its Proposition 7, printed pp. 11-12
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf), and dbFin, "Section 34: Problem 9 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-34-the-urysohn-metrization-theorem/problem-9-solution/
    (read 2026-11-10; kept at
    tmp/sources/dbfin/section-34-the-urysohn-metrization-theorem/problem-9-solution.txt); checked
    against Munkres, Topology (2000), Section 34 Exercise 9, printed p. 218, and its printed hint,
    with Exercise 30.4. The card builds the countable family of the hint -- lifts of the bases of the
    two closed subspaces together with X - X_1 and X - X_2 -- and checks that its finite
    intersections form a basis, by taking for each i either the lifted basis element through x or the
    complement of X_i. What was corrected: Doug's World writes the cover at the end as B = B_1 cup B_2
    cup (X_1 - X_2) cup (X_2 - X_1) and then proves separateness in two cases, introducing a
    "B = B_1 cap B_2" that its own definition does not contain; the card takes the whole family of
    finite intersections, which is the hint's construction.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf` with
    seven steps, each carrying a `pf-proof`, and answers Munkres, Topology, §34 Exercise 9. Cited by
    number only: Exercise 30.4 (a compact metrizable space has a countable basis), Theorem 32.3
    (every compact Hausdorff space is normal) and Theorem 34.1 (Urysohn metrization). The
    transcription is from "Doug's World", Munkres -- Topology -- Chapter 4 Solutions, Problem 34.9,
    and dbFin, Section 34: Problem 9 Solution, with the hint's family of finite intersections in
    place of Doug's World's two-case separateness argument. Checked: that a countable family has
    countably many finite subsets, that the chosen member of the family meets $X_i$ inside
    $U\cap X_i$ in both cases, and that a point of the intersection lies in $X_i$ for some $i$ and
    hence in $U$.
---

::: {.exercise}

Let $X$ be a compact Hausdorff space that is the union of the closed subspaces $X_1$ and $X_2$.
If $X_1$ and $X_2$ are metrizable, show that $X$ is metrizable.
[Hint: Construct a countable collection $\mathcal{A}$ of open sets of $X$ whose intersections with $X_i$ form a basis for $X_i$, for $i = 1, 2$. Assume $X_1 - X_2$ and $X_2 - X_1$ belong to $\mathcal{A}$. Let $\mathcal{B}$ consist of finite intersections of elements of $\mathcal{A}$.]
:::

::: {.solution}

The construction is the hint's, and the argument follows "Doug's World", *Munkres -- Topology -- Chapter 4 Solutions*, Problem 34.9, and dbFin, *Section 34: Problem 9 Solution*, read in the retained texts `tmp/sources/munkres-solutions-dougsworld-ch4.pdf` and `tmp/sources/dbfin/section-34-the-urysohn-metrization-theorem/problem-9-solution.txt`. What the card takes from neither is the family of finite intersections, which is the hint's own construction and avoids the two-case separateness argument of Doug's World.

::: pf

::: {.pf-step #compact-bases}
Each $X_i$ is compact and has a countable basis $\mathcal B_i$.

::: pf-proof
$X_i$ is closed in the compact space $X$, hence compact. A compact metrizable space has a countable basis (Munkres, Exercise 30.4), and $X_i$ is metrizable by hypothesis, so $\mathcal B_i$ exists.
:::

:::

::: {.pf-step #lifts}
For each $B\in\mathcal B_i$ choose an open set $\widetilde B\subseteq X$ with $\widetilde B\cap X_i=B$, and let $\mathcal A$ be the collection of all these lifts together with $X-X_1$ and $X-X_2$. Then $\mathcal A$ is a countable collection of open subsets of $X$.

::: pf-proof
$B$ is open in the subspace $X_i$, so $B=O\cap X_i$ for some open $O\subseteq X$, and $O$ serves as $\widetilde B$. Each $\mathcal B_i$ is countable, so the lifts form a countable family, and adding the two open sets $X-X_i$ keeps it countable.
:::

:::

::: {.pf-step #finite-intersections}
The collection $\mathcal C$ of all finite intersections of members of $\mathcal A$ is countable.

::: pf-proof
A countable set has only countably many finite subsets, and the map sending a finite subset to its intersection is a surjection of a countable set onto $\mathcal C$; explicitly, $\mathcal C$ is the union over $n$ of the images of the $n$-fold intersections, countably many countable sets.
:::

:::

::: {.pf-step #separating-member}
Let $x\in U$ with $U\subseteq X$ open. For each $i$ there is a member $A_i\in\mathcal A$ containing $x$ and satisfying $A_i\cap X_i\subseteq U\cap X_i$.

::: pf-proof
If $x\in X_i$, then $U\cap X_i$ is an open neighbourhood of $x$ in $X_i$, so there is $B_i\in\mathcal B_i$ with $x\in B_i\subseteq U\cap X_i$; its lift $\widetilde B_i\in\mathcal A$ contains $x$ and satisfies $\widetilde B_i\cap X_i=B_i\subseteq U\cap X_i$. If $x\notin X_i$, take $A_i=X-X_i$: it contains $x$ and meets $X_i$ in no point, so $A_i\cap X_i=\varnothing\subseteq U\cap X_i$.
:::

:::

::: {.pf-step #intersection-inside}
The intersection $C$ of the members $A_1,A_2$ of step [](#separating-member){.pf-ref} contains $x$ and satisfies $C\subseteq U$.

::: pf-proof
Both members contain $x$, so $x\in C$. Let $c\in C$. Since $X=X_1\cup X_2$, the point $c$ lies in some $X_i$; then $c\in C\cap X_i\subseteq A_i\cap X_i\subseteq U\cap X_i\subseteq U$. So $C\subseteq U$.
:::

:::

::: {.pf-step #basis}
$\mathcal C$ is a countable basis for $X$.

::: pf-proof
$\mathcal C$ consists of open sets, being finite intersections of open sets, and it is countable by step [](#finite-intersections){.pf-ref}. Given $x\in U$ with $U$ open, step [](#intersection-inside){.pf-ref} produces $C\in\mathcal C$ with $x\in C\subseteq U$, which is the basis criterion.
:::

:::

::: {.pf-step #metrizable}
$X$ is metrizable.

::: pf-proof
$X$ is compact Hausdorff by hypothesis, hence normal (Munkres, Theorem 32.3) and therefore regular. With the countable basis of step [](#basis){.pf-ref}, the Urysohn metrization theorem (Munkres, Theorem 34.1) gives a metric on $X$ inducing its topology.
:::

:::

:::

:::
