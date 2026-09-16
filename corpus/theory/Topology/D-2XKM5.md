---
schema: qual/card@1
id: D-2XKM5
kind: definition
title: Relative cycle
classification:
  areas:
  - topology
  topics:
  - Homology
  - Homological Algebra
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space and $A\subseteq X$ a subspace, and regard the [[D-6BUWA|singular chain group]] $C_n(A)$ as a subgroup of $C_n(X)$ via the inclusion.
The group of \dfn{relative chains} is $C_n(X,A) \coloneqq C_n(X)/C_n(A)$.
A \dfn{relative cycle} is a chain $\alpha \in C_n(X)$ with $\del_n \alpha \in C_{n-1}(A)$.
:::

::: {.remark}
A chain $\alpha\in C_n(X)$ is a relative cycle if and only if its image in $C_n(X,A)$ is a cycle for the boundary map induced by $\del_n$.
:::

::: {.concept}
[@Hat02].
:::
