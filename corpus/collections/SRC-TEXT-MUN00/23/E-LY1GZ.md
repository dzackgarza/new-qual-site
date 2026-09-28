---
schema: qual/card@1
id: E-LY1GZ
kind: problem
title: Connected sets crossing a set and its complement meet the boundary
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Boundary
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Let $A \subset X$.
Show that if $C$ is a connected subspace of $X$ that intersects both $A$ and $X - A$, then $C$ intersects $\operatorname{Bd} A$.
:::

::: {.solution}
<1>1. $X-\operatorname{Bd}A=\operatorname{Int}A\cup\operatorname{Int}(X-A)$, a union of disjoint open sets.

::: {.proof}
A point outside $\operatorname{Bd}A=\overline A\cap\overline{X-A}$ lies outside $\overline{X-A}=X-\operatorname{Int}A$ or outside $\overline A=X-\operatorname{Int}(X-A)$.
Conversely $\operatorname{Int}A$ misses $\overline{X-A}$ and $\operatorname{Int}(X-A)$ misses $\overline A$.
The two interiors lie in the disjoint sets $A$ and $X-A$.
:::

<1>2. Q.E.D.

::: {.proof}
Suppose $C\cap\operatorname{Bd}A=\varnothing$.
By step <1>1, $C$ is the union of the disjoint relatively open sets $C\cap\operatorname{Int}A$ and $C\cap\operatorname{Int}(X-A)$, so one of them is empty because $C$ is connected.
If $C\cap\operatorname{Int}A=\varnothing$, then $C\subseteq X-A$, contradicting $C\cap A\ne\varnothing$; if $C\cap\operatorname{Int}(X-A)=\varnothing$, then $C\subseteq A$, contradicting $C\cap(X-A)\ne\varnothing$.
:::
:::
