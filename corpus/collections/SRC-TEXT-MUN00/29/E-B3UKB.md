---
schema: qual/card@1
id: E-B3UKB
kind: problem
title: Compact closure neighborhoods in locally compact Hausdorff spaces
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
    Read against Munkres, Topology (2000), §29 Exercise 10, printed p. 186, with Lemma 26.4
    and Theorem 26.2; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.10, PDF p. 23. The complement in a compact
    neighbourhood of the intersection with the given neighbourhood is compact, an open set
    avoiding it and meeting the neighbourhood has closure inside the given neighbourhood.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that if $X$ is a Hausdorff space that is locally compact at the point $x$, then for each neighborhood $U$ of $x$, there is a neighborhood $V$ of $x$ such that $\overline{V}$ is compact and $\overline{V} \subset U$.
:::

::: {.solution}

The construction is that of **"positron0802"**, *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.10, PDF p. 23 (`tmp/sources/munkres-solutions-positron-ch3.pdf`), with one step of it repaired: that solution says "$U\cap W$ is open in $X$, hence in $C$", which is false in general, since $W$ is only a neighbourhood of $x$ and need not be open. The proof below chooses an open set inside $U$ and an open set inside $W$, so that the subset of $C$ whose compactness is used really is closed in $C$. The statement was checked against Munkres, *Topology* (2000), §29 Exercise 10, printed p. 186, with the definition of local compactness on printed p. 182, Theorem 26.2 and Theorem 26.3 on printed p. 165, and Lemma 26.4 on printed p. 166.

::: pf

::: {.pf-step #open-neighbourhoods}
There are open sets $O$ and $W$ with $x\in O\subset U$ and $x\in W\subset C$ for a compact subspace $C$ of $X$.

::: pf-proof
$U$ is a neighbourhood of $x$, so some open $O$ satisfies $x\in O\subset U$. Local compactness at $x$ (printed p. 182) gives a compact subspace $C$ of $X$ containing a neighbourhood of $x$, so some open $W$ satisfies $x\in W\subset C$.
:::

:::

::: {.pf-step #C-closed}
$C$ is closed in the Hausdorff space $X$.

::: pf-proof
$C$ is a compact subspace of the Hausdorff space $X$, so it is closed by Theorem 26.3 (printed p. 165).
:::

:::

::: {.pf-step #complement-compact}
$C-O$ is a compact subspace of $X$ and $x\notin C-O$.

::: pf-proof
$O$ is open in $X$, so $X-O$ is closed and $C-O=C\cap(X-O)$ is closed in the subspace $C$; a closed subspace of a compact space is compact by Theorem 26.2 (printed p. 165). Since $x\in O$, the point $x$ is not in $C-O$.
:::

:::

::: {.pf-step #separation}
There are disjoint sets $V_{1}$ and $V_{2}$, open in $X$, with $x\in V_{1}$ and $C-O\subset V_{2}$.

::: pf-proof
$C-O$ is a compact subspace of the Hausdorff space $X$ and $x$ is a point outside it by step [](#complement-compact){.pf-ref}; Lemma 26.4 (printed p. 166) supplies disjoint open sets containing $x$ and $C-O$ respectively.
:::

:::

::: {.pf-step #the-neighbourhood}
$V\coloneqq V_{1}\cap O\cap W$ is an open neighbourhood of $x$ with $V\subset C$, so $\overline{V}\subset C$.

::: pf-proof
$V$ is an intersection of sets open in $X$ and contains $x$, since $x$ lies in all three. A point of $V$ lies in $W\subset C$, so $V\subset C$; since $C$ is closed by step [](#C-closed){.pf-ref}, the closure of $V$ lies in the closure of $C$, which is $C$.
:::

:::

::: {.pf-step #closure-misses}
$\overline{V}\cap(C-O)=\varnothing$.

::: pf-proof
$V\subset V_{1}$ and $X-V_{2}$ is closed, so $\overline{V}\subset X-V_{2}$, using $V_{1}\subset X-V_{2}$ from the disjointness in step [](#separation){.pf-ref}. As $C-O\subset V_{2}$, a point of $\overline{V}$ cannot lie in $C-O$.
:::

:::

::: pf-step
Therefore $\overline{V}\subset U$ and $\overline{V}$ is compact, so $V$ is the required neighbourhood of $x$.

::: pf-proof
By steps [](#the-neighbourhood){.pf-ref} and [](#closure-misses){.pf-ref} the set $\overline{V}$ is contained in $C$ and meets neither $C-O$; since a point of $C$ outside $C-O$ lies in $O$, this gives $\overline{V}\subset O\subset U$. And $\overline{V}$ is a closed subset of the compact space $C$ by step [](#the-neighbourhood){.pf-ref}, hence compact by Theorem 26.2 (printed p. 165); $\overline{V}$ is closed in $X$ as a closure, so closed in $C$.
:::

:::

:::

:::
