---
schema: qual/card@1
id: P-BKS04-2A
kind: problem
title: UC Berkeley Spring 2004 prelim 2A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Find a countable abelian group whose endomorphism ring has the same cardinality as the set of real numbers.
Justify your answer.
:::

::: {.solution}
Let G be a vector space of dimension $\aleph _ { 0 }$ over $\mathbb { F } _ { 2 }$ . Then G is countable, since it is a countable union of finite subspaces.
Let $v _ { 1 } , v _ { 2 } , . . .$ . be a basis.
For each $S \subseteq \{ 1 , 2 , 3 , \dots \}$ there is an endomorphism of $G$ mapping each $v _ { i }$ to $v _ { i }$ or 0 according to whether $i \in S$ Different subsets S give different endomorphisms, so # End $G \geq 2 ^ { \aleph _ { 0 } }$ . On the other hand,

$$
\# \operatorname { E n d } G \leq ( \# G ) ^ { \# G } = \aleph _ { 0 } ^ { \aleph _ { 0 } } \leq ( 2 ^ { \aleph _ { 0 } } ) ^ { \aleph _ { 0 } } = 2 ^ { \aleph _ { 0 } \aleph _ { 0 } } = 2 ^ { \aleph _ { 0 } } .
$$

Thus $\#$ End $G = 2 ^ { \aleph _ { 0 } } = \# \mathbb { R }$
:::
