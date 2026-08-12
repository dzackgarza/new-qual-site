---
schema: qual/card@1
id: T-FBMYQ
kind: theorem
title: "Excision: Todo"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

::: {.theorem title="Excision"}
Given subspaces $Z \subseteq A \subseteq X$ with $\cl_X(Z) \subseteq A\interior$, the inclusion of pairs induces isomorphisms
\[
H_n(X\sm Z,\, A\sm Z) \mapsvia{\sim} H_n(X, A) \qquad \text{for all } n
.\]
Equivalently, for subspaces $A, B\subseteq X$ with $X = A\interior \union B\interior$, the inclusion $(B, A\intersect B)\injects (X, A)$ induces isomorphisms $H_n(B, A\intersect B)\mapsvia{\sim} H_n(X,A)$ for all $n$.
The two forms are related by $B = X\sm Z$.
:::

::: {.concept}
See Hatcher, §2.1, Theorem 2.20, p. 119.
:::
