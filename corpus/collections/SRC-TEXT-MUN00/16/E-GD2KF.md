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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 16.2, printed pp. 149--150** (`tmp/sources/munkres-solutions-whitman.pdf`); the answer, both examples and the conclusion are his.

Let $\mathcal{T}_{Y}=\{Y\cap U\mid U\in\mathcal{T}\}$ and $\mathcal{T}_{Y}'=\{Y\cap U\mid U\in\mathcal{T}'\}$ be the subspace topologies on $Y$. Then $\mathcal{T}_{Y}'$ is finer than $\mathcal{T}_{Y}$: if $V\in\mathcal{T}_{Y}$ then $V=Y\cap U$ with $U\in\mathcal{T}\subset\mathcal{T}'$, so $V\in\mathcal{T}_{Y}'$.

Strictness, however, is not inherited. Take $X=\{a,b,c\}$ and $Y=\{a,b\}$, with
$$
\mathcal{T}=\{\varnothing,X,\{a,b\}\},\qquad \mathcal{T}'=\{\varnothing,X,\{a,b\},\{c\}\}.
$$
Then $\mathcal{T}'$ is strictly finer than $\mathcal{T}$, while $\mathcal{T}_{Y}=\{\varnothing,Y\}=\mathcal{T}_{Y}'$, so the subspace topologies coincide. With instead
$$
\mathcal{T}'=\{\varnothing,X,\{a,b\},\{b\}\}
$$
and the same $\mathcal{T}$, one gets $\mathcal{T}_{Y}=\{\varnothing,Y\}$ but $\mathcal{T}_{Y}'=\{\varnothing,Y,\{b\}\}$, which is strictly finer.

So the only thing that can be said is that $\mathcal{T}_{Y}'$ is finer than $\mathcal{T}_{Y}$; whether it is strictly finer depends on $Y$ and on the two topologies, and both outcomes occur.
:::
