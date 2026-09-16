---
schema: qual/card@1
id: D-2PNEG
kind: definition
title: Free and properly discontinuous group actions
classification:
  areas:
  - topology
  topics:
  - Group Actions
  - Covering Spaces
relations: []
review: draft
---

::: {.definition}
Let $G$ be a group acting on a topological space $X$ by homeomorphisms, $G\actson X$.

- The action is \dfn{free} if $g(x) = x$ for some $x\in X$ implies $g = e$.

- The action is \dfn{properly discontinuous} if every $x\in X$ has a [[D-JMRPA|neighborhood]] $U$ such that for all $g_1, g_2\in G$, $g_1(U) \intersect g_2(U) \neq \emptyset$ implies $g_1 = g_2$.
:::

::: {.remark}
A properly discontinuous action in this sense is free.
Other sources call an action properly discontinuous under the weaker condition that every $x\in X$ has a neighborhood $U$ with $U \intersect g(U) \neq \emptyset$ for only finitely many $g\in G$.
An action satisfying the condition in the definition is called a covering space action in [@Hat02, §1.3, p. 72].
:::
