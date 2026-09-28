---
schema: qual/card@1
id: D-2TZAI
kind: definition
title: Topology via open sets and closed sets
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
relations: []
review: draft
---

::: {.definition}
Let $X$ be a set.
A \dfn{topology} on $X$ is a collection $\tau$ of subsets of $X$ such that

- $\emptyset \in \tau$ and $X\in \tau$;

- $\Union_{i\in I} U_i \in \tau$ for every family $(U_i)_{i\in I}$ of elements of $\tau$;

- $U_1\intersect \cdots \intersect U_n \in \tau$ for all $n\geq 1$ and $U_1, \ldots, U_n\in\tau$.

The pair $(X, \tau)$ is a \dfn{topological space}, the elements of $\tau$ are its \dfn{open sets}, and a subset $F\subseteq X$ is \dfn{closed} if $X\sm F$ is open.
:::

::: {.remark}
By De Morgan's laws, a collection $\mathcal F$ of subsets of $X$ is the collection of closed sets of a topology on $X$ if and only if $\emptyset, X\in\mathcal F$, $\mathcal F$ is closed under arbitrary intersections, and $\mathcal F$ is closed under finite unions; the topology is then $\ts{X\sm F \st F\in\mathcal F}$.
:::
