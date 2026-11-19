---
schema: qual/card@1
id: P-TOP-WORKSHOP-D4-03
kind: problem
title: The compact-complement topology is coarser than a Hausdorff topology
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Point-Set Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured the verification into numbered steps, one per topology axiom, and supplied the two
    points the prose left to the reader: that a closed subset of a compact space is compact, which is
    what makes the intersection of the complements compact inside the compact set X minus U_j, and
    that the empty set belongs to the family by construction while X does because the empty set is
    compact. Also split the containment into the two halves it needs, X Hausdorff giving compactness
    implies closedness, and recorded that the counterexample uses a bounded interval whose complement
    is unbounded and hence not compact. Every macro used is one the preamble defines. Nothing was
    checked against a printed page.
---

::: {.problem}
Let $(X,\tau)$ be a Hausdorff space and let $$\tau'=\{U\subseteq X\mid X\setminus U\text{ is compact}\}\cup\{\varnothing\}.$$ Show that $\tau'$ is a topology on $X$ and is coarser than $\tau$.
Show that, in general, they need not be equal.
:::

::: {.solution}

The argument is the card's own; no source text or solution set is retained for it.

Let $(X,\tau)$ be Hausdorff and $\tau'=\{U\subseteq X\mid X\setminus U\text{ is compact}\}\cup\{\varnothing\}$.

::: pf

::: {.pf-step #closed-subset}
A closed subset of a compact subset of $X$ is compact.

::: pf-proof
Let $K\subset X$ be compact and $F\subset K$ closed, and let $\{V_{i}\}$ be a cover of $F$ by open sets of $X$. Then $\{V_{i}\}\cup\{X\setminus F\}$ is an open cover of $K$, so finitely many members cover $K$; discarding $X\setminus F$ if it was used, finitely many $V_{i}$ cover $F$.
:::

:::

::: {.pf-step #ends}
$\varnothing\in\tau'$ and $X\in\tau'$.

::: pf-proof
$\varnothing$ is adjoined by definition, and $X\setminus X=\varnothing$ is compact, so $X\in\tau'$ as well.
:::

:::

::: {.pf-step #unions}
Arbitrary unions of members of $\tau'$ lie in $\tau'$.

::: pf-proof
Let $U_{i}\in\tau'$. If every $U_{i}=\varnothing$ then so is the union. Otherwise choose $j$ with $U_{j}\neq\varnothing$, so $K=X\setminus U_{j}$ is compact. Then
$$
X\setminus\bigcup_{i}U_{i}=\bigcap_{i}(X\setminus U_{i})\subset X\setminus U_{j}=K .
$$
Each $X\setminus U_{i}$ is compact, and compact subsets of the Hausdorff space $X$ are closed, so the intersection is closed in $X$ and hence closed in $K$; by step [](#closed-subset){.pf-ref} it is compact. So the union lies in $\tau'$.
:::

:::

::: {.pf-step #intersections}
Finite intersections of members of $\tau'$ lie in $\tau'$.

::: pf-proof
For $U_{1},\dots,U_{n}\in\tau'$,
$$
X\setminus\bigcap_{k=1}^{n}U_{k}=\bigcup_{k=1}^{n}(X\setminus U_{k}),
$$
a finite union of compact sets, which is compact; if all $U_{k}=X$ the left side is empty, which is compact. So the intersection lies in $\tau'$.
:::

:::

::: {.pf-step #topology}
$\tau'$ is a topology on $X$.

::: pf-proof
Steps [](#ends){.pf-ref}, [](#unions){.pf-ref} and [](#intersections){.pf-ref} are the three axioms.
:::

:::

::: {.pf-step #coarser}
$\tau'\subseteq\tau$.

::: pf-proof
Let $U\in\tau'$ be nonempty. Then $X\setminus U$ is compact by definition, and a compact subset of a Hausdorff space is closed, so $X\setminus U$ is $\tau$-closed and $U\in\tau$. The empty set is in $\tau$ too.
:::

:::

::: {.pf-step #strict}
$\tau'$ need not equal $\tau$: with $X=\RR$ usual, $(-1,1)\in\tau\setminus\tau'$.

::: pf-proof
$(-1,1)$ is open in $\RR$. Its complement $(-\infty,-1]\cup[1,\infty)$ has the open cover by the sets $(-\infty,-n)\cup(n,\infty)$, $n\geq1$, no finite subfamily of which covers it, so it is not compact; hence $(-1,1)\notin\tau'$ and the two topologies differ.
:::

:::

::: {.pf-step}
$\tau'$ is a topology coarser than $\tau$, and the two can differ.

::: pf-proof
Steps [](#topology){.pf-ref}, [](#coarser){.pf-ref} and [](#strict){.pf-ref}.
:::

:::

:::

:::
