---
schema: qual/card@1
id: E-GD2KF
kind: problem
title: Refining a topology refines the subspace topologies
classification:
  areas:
  - topology
  topics:
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §16 Exercise 2, printed p. 92; the stored
    statement is the printed question.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 16.2, printed pp.
    149-150. The answer and both examples are his: a finer topology gives a finer subspace
    topology, because V = Y cap U with U open in the coarser one; but strictness can be
    lost, as on X = {a,b,c} with Y = {a,b}, where {c} distinguishes the topologies on X and
    does not meet Y, while {b} does distinguish the subspace topologies.
    (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

If $\mathcal{T}$ and $\mathcal{T}'$ are topologies on $X$ and $\mathcal{T}'$ is strictly finer than $\mathcal{T}$, what can you say about the corresponding subspace topologies on the subset $Y$ of $X$?
:::

::: {.solution}

The argument is **Dan Whitman**, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 16.2 (`tmp/sources/munkres-solutions-whitman.pdf`); the claim and both examples are his, with the two checks that each displayed family is a topology added here, and the statement was checked against Munkres, *Topology* (2000), §16 Exercise 2.

Throughout, $\mathcal{T}$ and $\mathcal{T}'$ are topologies on $X$ with $\mathcal{T}\subsetneq\mathcal{T}'$, the subset $Y\subset X$ carries the two subspace topologies
$$
\mathcal{T}_{Y}\coloneqq\theset{Y\cap U\mid U\in\mathcal{T}},\qquad
\mathcal{T}_{Y}'\coloneqq\theset{Y\cap U\mid U\in\mathcal{T}'},
$$
and a topology is finer than another when it contains it.

::: pf

::: {.pf-step #finer}
$\mathcal{T}_{Y}'$ is finer than $\mathcal{T}_{Y}$.

::: pf-proof
If $V\in\mathcal{T}_{Y}$ then $V=Y\cap U$ with $U\in\mathcal{T}$, and $\mathcal{T}\subset\mathcal{T}'$ gives $U\in\mathcal{T}'$, so $V=Y\cap U\in\mathcal{T}_{Y}'$.
:::

:::

::: {.pf-step #first-example}
There are $X$, $Y$ and $\mathcal{T}\subsetneq\mathcal{T}'$ for which $\mathcal{T}_{Y}=\mathcal{T}_{Y}'$.

:::: pf-proof

::: {.pf-step #first-topologies}
With $X=\theset{a,b,c}$, $Y=\theset{a,b}$, $\mathcal{T}=\theset{\varnothing,X,\theset{a,b}}$ and $\mathcal{T}'=\theset{\varnothing,X,\theset{a,b},\theset{c}}$, both families are topologies on $X$ and $\mathcal{T}\subsetneq\mathcal{T}'$.

::: pf-proof
Each family contains $\varnothing$ and $X$. In $\mathcal{T}$ the only unions and intersections to check are $\theset{a,b}\cup\varnothing=\theset{a,b}$ and $\theset{a,b}\cap X=\theset{a,b}$. In $\mathcal{T}'$ the new open set $\theset{c}$ satisfies $\theset{c}\cup\theset{a,b}=X$, $\theset{c}\cap X=\theset{c}$ and $\theset{c}\cap\theset{a,b}=\varnothing$, so the family is closed under finite unions and intersections; $\mathcal{T}'\supsetneq\mathcal{T}$ because $\theset{c}\notin\mathcal{T}$.
:::

:::

::: {.pf-step #first-subspace}
$\mathcal{T}_{Y}=\theset{\varnothing,Y}=\mathcal{T}_{Y}'$.

::: pf-proof
Intersecting the members of $\mathcal{T}$ with $Y$ gives $\varnothing$, $Y\cap X=Y$ and $Y\cap\theset{a,b}=Y$, so $\mathcal{T}_{Y}=\theset{\varnothing,Y}$; intersecting the members of $\mathcal{T}'$ with $Y$ gives in addition $Y\cap\theset{c}=\varnothing$, so $\mathcal{T}_{Y}'=\theset{\varnothing,Y}$ as well.
:::

:::

::::

:::

::: {.pf-step #second-example}
There are $X$, $Y$ and $\mathcal{T}\subsetneq\mathcal{T}'$ for which $\mathcal{T}_{Y}\subsetneq\mathcal{T}_{Y}'$.

:::: pf-proof

::: {.pf-step #second-topologies}
With $X=\theset{a,b,c}$ and $Y=\theset{a,b}$ but now $\mathcal{T}'=\theset{\varnothing,X,\theset{a,b},\theset{b}}$, the family $\mathcal{T}'$ is a topology on $X$ strictly finer than $\mathcal{T}$.

::: pf-proof
The new member $\theset{b}$ satisfies $\theset{b}\cup\theset{a,b}=\theset{a,b}$, $\theset{b}\cap\theset{a,b}=\theset{b}$ and $\theset{b}\cap X=\theset{b}$, so $\mathcal{T}'$ is closed under finite unions and intersections and contains $\varnothing$ and $X$; it strictly contains $\mathcal{T}$ because $\theset{b}\notin\mathcal{T}$.
:::

:::

::: {.pf-step #second-subspace}
$\mathcal{T}_{Y}=\theset{\varnothing,Y}$ and $\mathcal{T}_{Y}'=\theset{\varnothing,Y,\theset{b}}$, so $\mathcal{T}_{Y}\subsetneq\mathcal{T}_{Y}'$.

::: pf-proof
The first equality was computed in step [](#first-subspace){.pf-ref} and does not involve $\mathcal{T}'$. For the second, $Y\cap X=Y$, $Y\cap\theset{a,b}=Y$, $Y\cap\theset{b}=\theset{b}$ and $Y\cap\varnothing=\varnothing$; the three distinct sets obtained are exactly the members listed, so $\theset{b}\in\mathcal{T}_{Y}'-\mathcal{T}_{Y}$.
:::

:::

::::

:::

::: pf-step
The only conclusion available is that $\mathcal{T}_{Y}'$ is finer than $\mathcal{T}_{Y}$.

::: pf-proof
Step [](#finer){.pf-ref} proves the inclusion $\mathcal{T}_{Y}\subset\mathcal{T}_{Y}'$ for every $Y$ and every strictly finer $\mathcal{T}'$. Step [](#first-example){.pf-ref} exhibits a case where the inclusion is an equality and step [](#second-example){.pf-ref} a case where it is strict, so neither strictness nor equality follows from the hypotheses, and no sharper statement than $\mathcal{T}_{Y}\subset\mathcal{T}_{Y}'$ holds in general.
:::

:::

:::

:::
