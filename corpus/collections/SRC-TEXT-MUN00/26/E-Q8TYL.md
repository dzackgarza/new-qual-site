---
schema: qual/card@1
id: E-Q8TYL
kind: problem
title: Compactness under comparable topologies
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 1, printed p. 170, with Theorem 26.2
    and Theorem 26.3; both parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.1, PDF p. 12. Compactness passes from a finer
    to a coarser topology; conversely two comparable compact Hausdorff topologies coincide,
    since a set closed in the finer one is compact and hence closed in the coarser.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, and one repair of substance: the earlier counterexample
    for the converse of part (a) was the two-point set with the indiscrete and the discrete
    topologies, which does not work, because every space with finitely many points is
    compact under any topology (Example 3, printed p. 164) -- the book's own example
    contradicts it. The counterexample is now the real line with the finite complement
    topology, compact by the finite-complement argument (Exercise 26.2(a), printed p. 170),
    against the discrete topology on the same set, which is finer and not compact since the
    family of singletons has no finite subcover. Citations: the exercise on printed p. 170,
    Theorem 26.2 and Theorem 26.3 on printed p. 165. Part (a) is now stated for subsets,
    which is what part (b) needs; and part (b)'s disjunction is drawn explicitly, the proof
    of the comparable case being step [](#equal){.pf-ref}, so that the incomparable case is
    not left implicit.
---

::: {.exercise}

(a) Let $\mathcal{T}$ and $\mathcal{T}'$ be two topologies on the set $X$; suppose that $\mathcal{T}' \supset \mathcal{T}$.
What does compactness of $X$ under one of these topologies imply about compactness under the other?

(b) Show that if $X$ is compact Hausdorff under both $\mathcal{T}$ and $\mathcal{T}'$, then either $\mathcal{T}$ and $\mathcal{T}'$ are equal or they are not comparable.
:::

::: {.solution}
The argument is the retained published solution, **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.1, PDF p. 12** (`tmp/sources/munkres-solutions-positron-ch3.pdf`), restructured into steps; its counterexample for the converse in part (a) is replaced, the one given there being false.

Throughout, $\mathcal{T}\subset\mathcal{T}'$ are topologies on a set $X$; a subset is called $\mathcal{T}$-compact when it is compact as a subspace of $(X,\mathcal{T})$. The exercise is §26 Exercise 1 (printed p. 170).

::: pf

::: {.pf-step #coarser}
(a) If $(X,\mathcal{T}')$ is compact then $(X,\mathcal{T})$ is compact; more generally a $\mathcal{T}'$-compact subset of $X$ is $\mathcal{T}$-compact.

::: pf-proof
Let $Y\subset X$ be $\mathcal{T}'$-compact and let $\{U_\alpha\}$ be a cover of $Y$ by $\mathcal{T}$-open sets. Every $\mathcal{T}$-open set is $\mathcal{T}'$-open because $\mathcal{T}\subset\mathcal{T}'$, so this is a cover of $Y$ by $\mathcal{T}'$-open sets and, $Y$ being $\mathcal{T}'$-compact, finitely many of the $U_\alpha$ cover $Y$. Hence $Y$ is $\mathcal{T}$-compact, and with $Y=X$ the first assertion follows.
:::

:::

::: {.pf-step #converse-fails}
(a) The converse fails: compactness of $(X,\mathcal{T})$ does not give compactness of $(X,\mathcal{T}')$.

::: pf-proof
Take $X=\RR$ with $\mathcal{T}$ the finite complement topology, which is compact: given an open cover, one member of it has finite complement and the finitely many remaining points are covered by finitely many further members (Exercise 26.2(a), printed p. 170), and take $\mathcal{T}'$ the discrete topology, which contains $\mathcal{T}$ because every subset is discrete-open. The family of singletons is an open cover of $\RR$ in the discrete topology with no finite subcover, since $\RR$ is infinite, so $(\RR,\mathcal{T}')$ is not compact. A finite set would not serve as an example: every space with finitely many points is compact (Example 3, printed p. 164), under any topology.
:::

:::

::: {.pf-step #equal}
(b) If $\mathcal{T}\subset\mathcal{T}'$ and $X$ is compact Hausdorff under both, then $\mathcal{T}=\mathcal{T}'$.

::: pf-proof

::: {.pf-step #closed}
Every $\mathcal{T}'$-closed subset of $X$ is $\mathcal{T}$-closed.

::: pf-proof
Let $B$ be $\mathcal{T}'$-closed. Then $B$ is a closed subspace of the compact space $(X,\mathcal{T}')$, hence $\mathcal{T}'$-compact (Theorem 26.2, printed p. 165), hence $\mathcal{T}$-compact by step [](#coarser){.pf-ref}; and a compact subspace of the Hausdorff space $(X,\mathcal{T})$ is $\mathcal{T}$-closed (Theorem 26.3, printed p. 165).
:::

:::

::: {.pf-step #topologies}
$\mathcal{T}'\subset\mathcal{T}$.

::: pf-proof
Let $A\in\mathcal{T}'$; then $B=X-A$ is $\mathcal{T}'$-closed, hence $\mathcal{T}$-closed by step [](#closed){.pf-ref}, so $A=X-B$ is $\mathcal{T}$-open. With $\mathcal{T}\subset\mathcal{T}'$ this gives $\mathcal{T}=\mathcal{T}'$.
:::

:::

:::

:::

::: {.pf-step}
(b) If $X$ is compact Hausdorff under both $\mathcal{T}$ and $\mathcal{T}'$, then either the topologies are equal or they are not comparable.

::: pf-proof
If they are comparable, one of the two containments holds, and step [](#equal){.pf-ref} applied to the pair in that order gives equality. Hence either the two topologies are equal, or neither contains the other, that is they are not comparable.
:::

:::

:::
:::
