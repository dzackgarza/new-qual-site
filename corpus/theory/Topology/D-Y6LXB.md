---
schema: qual/card@1
id: D-Y6LXB
kind: definition
title: Relative boundaries
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, $A\subseteq X$ a subspace, and $n\geq 0$, and regard the [[D-6BUWA|singular chain group]] $C_n(A)$ as a subgroup of $C_n(X)$ via the inclusion.
A \dfn{relative boundary} is a chain $\alpha\in C_n(X)$ of the form $\alpha = \del\beta + \gamma$ with $\beta \in C_{n+1}(X)$ and $\gamma \in C_n(A)$.
:::

::: {.remark}
A chain $\alpha\in C_n(X)$ is a relative boundary if and only if its image in $C_n(X,A) = C_n(X)/C_n(A)$ is a boundary for the induced boundary map.
The relative homology group $H_n(X,A)$ is isomorphic to the group of [[D-2XKM5|relative cycles]] in $C_n(X)$ modulo the subgroup of relative boundaries.
:::

::: {.concept}
[@Hat02].
:::
