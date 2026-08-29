---
schema: qual/card@1
id: P-E2CRQ
kind: problem
title: The union of intersecting connected sets is connected
classification:
  areas:
  - complex-analysis
  topics:
  - Connectedness
  - Point-Set Topology
relations: []
review: draft
---

::: {.problem}
Suppose $A, B\subseteq \RR^n$ are connected and not disjoint.
Prove that $A\union B$ is also connected.
:::

::: {.solution}
Use that $X$ is connected iff $\Hom_{\Top}(X, S^0) = \ts{c_{-1}, c_1}$, i.e. every continuous map from $X\to \ts{-1, 1}$ is a constant map $x \mapsvia{c_{-1}} -1$ or $x \mapsvia{c_1} 1$.
Let $f: A\union B \to S^0$ be arbitrary, and let $f_1 \da \ro{f}{A}$ and $f_2 \da \ro{f}{B}$.
By connectedness of $A$, $f_1$ is a constant map, as is $f_2$.
On the intersection, for $x\in A \intersect B \neq \emptyset$, we have $f_1(x) = f_2(x)$ since $x\in A$ and $x\in B$.
So $f_1$ and $f_2$ are constant functions that must map to the *same* constant, so $f$ is constant and this $A\union B$ is connected.
:::
