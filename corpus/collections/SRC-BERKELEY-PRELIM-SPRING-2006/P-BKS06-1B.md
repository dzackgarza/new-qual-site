---
schema: qual/card@1
id: P-BKS06-1B
kind: problem
title: UC Berkeley Spring 2006 prelim 1B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $A _ { 1 } \supseteq A _ { 2 } \supseteq \cdots$ · be compact connected subsets of $\mathbb { R } ^ { n }$ . Show that the set $A = \cap A _ { m }$ is connected.
:::

::: {.solution}
The intersection A is nonempty, since otherwise $\left\{ A _ { 1 } - A _ { m } \right\}$ is a covering of $A _ { 1 }$ (by sets open in $A _ { 1 } )$ with no finite subcover.

Suppose that A is not connected.
Then there exist sets $B _ { 0 } , C _ { 0 }$ open in A such that $B _ { 0 } \cup C _ { 0 } = A$ and $B _ { 0 } \cap C _ { 0 } = \varnothing$ . Then $B _ { 0 } , C _ { 0 }$ are also closed in A, which (as an intersection of closed sets) is closed in Rn, so $B _ { 0 } , C _ { 0 }$ are closed in $\mathbb { R } ^ { n }$ . Hence we can find disjoint sets $B , C$ open in $A _ { 1 }$ such that $B _ { 0 } \subseteq B , C _ { 0 } \subseteq C .$ : for instance, we could let B be the set of points in $A _ { 1 }$ that are strictly closer to $B _ { 0 }$ than to $C _ { 0 }$ , and vice versa for C.

Since $A = B _ { 0 } \cup C _ { 0 } \subseteq B \cup C$ , the sets $B , C _ { i }$ , and $A _ { 1 } - A _ { m }$ for $m \geq 1$ form a cover of $A _ { 1 }$ by sets open in $A _ { 1 } ;$ thus there is a finite subcover consisting of $B , C .$ , and $A _ { 1 } - A _ { m }$ for $m = 1 , \ldots , r .$ . So r is such that $A _ { r } \subseteq B \cup C$ Since $B , C$ are open, disjoint, and $B \cap A _ { r } \supseteq B _ { 0 } \cap A \neq \emptyset$ and $C \cap A _ { r } \supseteq C _ { 0 } \cap A \neq \emptyset$ , we have that $A _ { r }$ is not connected, a contradiction.
:::
