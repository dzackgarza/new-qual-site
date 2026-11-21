---
schema: qual/card@1
id: E-EE4EE
kind: problem
title: Interior, isolated, and limit points
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}
- What is an interior point?
  An isolated point?
  A limit point?
:::

::: {.solution}

No retained solution set covers this question, and the collection carries no provenance: the three definitions are the card's own statement of the standard ones, and each is followed by the one-line equivalence that makes it usable.

Let $X$ be a topological space and $A\subseteq X$.

::: pf

::: {.pf-step #interior}
$x\in A$ is an interior point of $A$ when some open $U$ satisfies $x\in U\subseteq A$; equivalently, when $x\in\operatorname{Int}A$, the union of all open subsets of $A$.

::: pf-proof
If $x\in U\subseteq A$ with $U$ open, then $U$ is one of the sets whose union is $\operatorname{Int}A$, so $x\in\operatorname{Int}A$. Conversely $\operatorname{Int}A$ is itself open, being a union of open sets, and it is contained in $A$, so $x\in\operatorname{Int}A$ exhibits the required $U=\operatorname{Int}A$.
:::

:::

::: {.pf-step #isolated}
$x\in A$ is an isolated point of $A$ when some open $U$ satisfies $U\cap A=\{x\}$; equivalently, when $\{x\}$ is open in the subspace $A$.

::: pf-proof
The open sets of the subspace $A$ are exactly the sets $U\cap A$ with $U$ open in $X$; so $U\cap A=\{x\}$ for some open $U$ exactly when $\{x\}$ is open in $A$. Note that this concerns the subspace $A$: an isolated point of $A$ need not be isolated in $X$.
:::

:::

::: {.pf-step #limit}
$x\in X$ is a limit point of $A$ when every open $U\ni x$ satisfies $\big(U\setminus\{x\}\big)\cap A\ne\varnothing$; equivalently, when $x\in\overline{A\setminus\{x\}}$.

::: pf-proof
A point lies in the closure of a set $S$ exactly when every open set containing it meets $S$; applying this to $S=A\setminus\{x\}$ gives the equivalence, and note that the point $x$ itself is allowed to lie outside $A$.
:::

:::

::: {.pf-qed}
The three notions are steps [](#interior){.pf-ref}, [](#isolated){.pf-ref} and [](#limit){.pf-ref}, each with the formulation in terms of $\operatorname{Int}$, of the subspace topology on $A$, and of closure.
:::

:::

:::
