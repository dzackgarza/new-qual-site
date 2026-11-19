---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2A-HW1
kind: problem
title: The separation axioms $T_0$ through $T_4$
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
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
    Restructured into a structured proof under #2. The item asks for definitions, so the steps state
    the axioms and their names and justify the standard chain of implications $T_4\Rightarrow T_3
    \Rightarrow T_2\Rightarrow T_1\Rightarrow T_0$: normality separates a point from a closed set,
    regularity with $T_1$ separates points, Hausdorff gives $T_1$, and $T_1$ gives $T_0$. Added: that
    chain of implications and the note that the words regular and normal carry $T_1$ under this
    convention, which is what the second question asks. No defect found in the statement. The
    collection's provenance is the worksheet, so no retained solution set bears on the item.
---

::: {.problem}
What are the properties $T_0$--$T_4$?
What other names are there for $T_2$--$T_4$?
:::

::: {.solution}
This item asks for definitions; the statements below are the standard separation axioms as the workshop's text states them, and the collection's provenance is the worksheet itself, so no retained solution set bears on it.

::: pf

::: {.pf-step #axioms}
The axioms $T_0$--$T_4$ are the following conditions on a topological space $X$.

::: pf-proof
$T_0$: for any two distinct points $x,y$, at least one of them has an open neighbourhood not containing the other. $T_1$: for any two distinct points $x,y$, each has an open neighbourhood not containing the other, equivalently every singleton is closed. $T_2$: any two distinct points have disjoint open neighbourhoods. $T_3$: $X$ is $T_1$ and regular, that is, for $x\notin F$ with $F$ closed there are disjoint open sets containing $x$ and $F$. $T_4$: $X$ is $T_1$ and normal, that is, two disjoint closed sets have disjoint open neighbourhoods.
:::

:::

::: {.pf-step #implications}
$T_4\Rightarrow T_3\Rightarrow T_2\Rightarrow T_1\Rightarrow T_0$.

::: pf-proof
A normal space is regular: the point $x$ not in the closed set $F$ gives two disjoint closed sets $\{x\}$ and $F$, which normality separates. A regular $T_1$ space is Hausdorff: for $x\ne y$ the singleton $\{y\}$ is closed and does not contain $x$, so regularity separates $x$ from $\{y\}$. A Hausdorff space is $T_1$: given $x\ne y$, a neighbourhood of $x$ missing $y$ exists by disjointness, and symmetrically. A $T_1$ space is $T_0$ by forgetting one of the two neighbourhoods. The implications are strict in general, since the corresponding counterexamples separate the classes.
:::

:::

::: {.pf-step}
The names of $T_2$, $T_3$, $T_4$ are Hausdorff, regular and normal.

::: pf-proof
$T_2$ is the Hausdorff axiom. $T_3$ is regularity together with $T_1$, and $T_4$ is normality together with $T_1$; under this convention the words regular and normal include the $T_1$ condition, which is the point of the question. A space satisfying the separation clause of $T_3$ without $T_1$ is called regular in the weaker sense, and similarly for normal.
:::

:::

:::
:::
