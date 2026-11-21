---
schema: qual/card@1
id: P-TOP-WORKSHOP-D4-W3
kind: problem
title: Spaces in which every open set is compact; a Hausdorff such space is finite
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Counterexamples
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
    Structured the two parts into numbered steps and supplied the facts the argument used without
    stating them: that compact subsets of a Hausdorff space are closed, hence that every open subset
    is closed, and that a space in which every open set is closed has open arbitrary intersections,
    which is what makes each singleton open. Also recorded that the first example's topology is
    genuinely a topology and that its open sets are finite. Every macro used is one the preamble
    defines. Nothing was checked against a printed page.
---

::: {.problem}
Provide an example of a topological space where open sets are compact.
Then find an infinite set with a Hausdorff topology where open sets are compact.
:::

::: {.solution}

The argument is the card's own; no source text or solution set is retained for it.

::: pf

::: {.pf-step #finite-example}
On $X=\{0,1\}$ the Sierpiński topology $\tau=\{\varnothing,\{1\},X\}$ has only finite open sets, and every finite space is compact.

::: pf-proof
$\tau$ is a topology: it contains $\varnothing$ and $X$, and is closed under finite intersections and all unions by inspection of its three members. Its open sets are $\varnothing$, $\{1\}$ and $X$, all finite. Any open cover of a finite space has a finite subcover, since the space is the union of the (finitely many) distinct elements of the cover.
:::

:::

::: {.pf-step #closed-open}
If $X$ is Hausdorff and every open subset is compact, then every open subset is closed and arbitrary intersections of open sets are open.

::: pf-proof
A compact subset of a Hausdorff space is closed, so each open $U$ is closed, hence $X\setminus U$ is open. Then for any family $\{U_{i}\}$ of open sets,
$$
\bigcap_{i}U_{i}=X\setminus\bigcup_{i}(X\setminus U_{i}),
$$
a complement of a union of open sets, hence open.
:::

:::

::: {.pf-step #discrete}
Under these hypotheses every singleton is open, so $X$ is discrete.

::: pf-proof
$X$ is Hausdorff, hence $T_{1}$: for $y\neq x$ there is an open set containing $x$ and not $y$, so $X\setminus\{y\}$ is open. Then
$$
\{x\}=\bigcap_{y\neq x}\bigl(X\setminus\{y\}\bigr),
$$
an intersection of open sets, which is open by step [](#closed-open){.pf-ref}. All singletons open means every subset is open, that is, $X$ is discrete.
:::

:::

::: {.pf-step #finite}
If $X$ is Hausdorff, every open set is compact, and $X$ is infinite, then a contradiction follows.

::: pf-proof
$X$ is open, so it is compact by hypothesis; and by step [](#closed-open){.pf-ref} it is discrete. The cover by singletons $\{\{x\}\mid x\in X\}$ is then an open cover, and a finite subcover would exhibit $X$ as a finite union of singletons, hence finite. So $X$ infinite contradicts compactness of $X$.
:::

:::

::: {.pf-step}
A finite space with its topology gives the first example, and no infinite Hausdorff space in which every open set is compact exists.

::: pf-proof
Step [](#finite-example){.pf-ref} is the first example; step [](#finite){.pf-ref} shows that a Hausdorff space with the property is necessarily finite, so the second request has no example — the answer is that it cannot be done.
:::

:::

:::

:::
