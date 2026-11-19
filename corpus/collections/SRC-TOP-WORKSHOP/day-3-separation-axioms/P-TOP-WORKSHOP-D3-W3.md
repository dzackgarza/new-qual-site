---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-W3
kind: problem
title: A space is $T_1$ if and only if the identity to the finite-complement topology is continuous
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Continuity
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
    Structured both directions into numbered steps, with the two definitions written out: T1 as the
    closedness of singletons, and continuity of the identity between the two topologies as the
    containment of one topology in the other (the inverse image of an open set under the identity is
    that set). Supplied the intermediate facts the prose used in passing, that a finite union of
    closed sets is closed and that every cofinite set is the complement of a finite set. Every macro
    used is one the preamble defines. Nothing was checked against a printed page.
---

::: {.problem}
Suppose $(X,\tau)$ is a topological space and let $(X,\tau')$ be the same set with the finite complement topology.
Then $X$ is $T_1$ if and only if $\operatorname{id}:(X,\tau)\to(X,\tau')$ is continuous.
:::

::: {.solution}

The argument is the card's own; no source text or solution set is retained for it.

Let $\tau$ be a topology on $X$ and $\tau_{f}$ the finite-complement topology on the same set, so that a set is $\tau_{f}$-open exactly when it is empty or its complement is finite.

::: pf

::: {.pf-step #criterion}
The identity $\operatorname{id}\colon(X,\tau)\to(X,\tau_{f})$ is continuous if and only if $\tau_{f}\subseteq\tau$.

::: pf-proof
For $U\in\tau_{f}$ the inverse image $\operatorname{id}^{-1}(U)$ is $U$ itself. Continuity requires every such $U$ to be $\tau$-open, which is exactly the containment $\tau_{f}\subseteq\tau$; conversely that containment makes every $\tau_{f}$-open set $\tau$-open, which is continuity.
:::

:::

::: {.pf-step #t1-singletons}
$(X,\tau)$ is $T_{1}$ if and only if every singleton is $\tau$-closed.

::: pf-proof
$(X,\tau)$ is $T_{1}$ when for each pair $x\neq y$ there is an open set containing $x$ and not $y$. If every singleton $\{y\}$ is closed then $X\setminus\{y\}$ is open and contains $x$ but not $y$, so the space is $T_{1}$. Conversely if the space is $T_{1}$ then for $y\in X$ and $x\neq y$ there is an open $U_{x}$ with $x\in U_{x}$, $y\notin U_{x}$, so $X\setminus\{y\}=\bigcup_{x\neq y}U_{x}$ is open and $\{y\}$ is closed.
:::

:::

::: {.pf-step #forward}
If $(X,\tau)$ is $T_{1}$ then the identity is continuous.

::: pf-proof
By step [](#t1-singletons){.pf-ref} every singleton is $\tau$-closed, and a finite union of closed sets is closed, so every finite subset is $\tau$-closed. Hence for every finite $F$ the set $X\setminus F$ is $\tau$-open; as $X\setminus F$ runs over the nonempty $\tau_{f}$-open sets (together with $\varnothing$), this says $\tau_{f}\subseteq\tau$, and step [](#criterion){.pf-ref} gives continuity.
:::

:::

::: {.pf-step #backward}
If the identity is continuous then $(X,\tau)$ is $T_{1}$.

::: pf-proof
Let $x\in X$. The set $X\setminus\{x\}$ is $\tau_{f}$-open, being the complement of a finite set, so by continuity and step [](#criterion){.pf-ref} it is $\tau$-open. Hence $\{x\}$ is $\tau$-closed, and by step [](#t1-singletons){.pf-ref} the space is $T_{1}$.
:::

:::

::: {.pf-step}
$(X,\tau)$ is $T_{1}$ if and only if $\operatorname{id}\colon(X,\tau)\to(X,\tau_{f})$ is continuous.

::: pf-proof
Steps [](#forward){.pf-ref} and [](#backward){.pf-ref} are the two implications.
:::

:::

:::

:::
