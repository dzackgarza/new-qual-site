---
schema: qual/card@1
id: P-BKS06-8A
kind: problem
title: UC Berkeley Spring 2006 prelim 8A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $D = \{ z \in \mathbb { C } : | z | < 1 \}$ . Let $f \colon D  \mathbb { C }$ be holomorphic, and suppose that the restriction of $f$ to $D - \{ 0 \}$ is injective. Prove that $f$ is injective.
:::

::: {.solution}
Suppose on the contrary that there is $a \in D - \{ 0 \}$ such that $f ( a ) = f ( 0 )$ . Let α be the common value. Choose disjoint open disks $D _ { 0 }$ and $D _ { a }$ contained in D, centered at 0 and a, respectively. By the Open Mapping Theorem $f ( D _ { 0 } )$ and $f ( D _ { a } )$ are open subsets of C containing α. Hence $G : = f ( D _ { 0 } ) \cap f ( D _ { a } )$ is a nonempty open subset of C. Choose $\xi \in G$ with $\xi \neq \alpha$ . Then there exist $z _ { 0 } \in D _ { 0 }$ and $z _ { a } \in D _ { a }$ such that $f ( z _ { 0 } ) = f ( z _ { a } ) = \xi$ . Since $\xi \neq \alpha$ , neither $z _ { 0 }$ nor $z _ { a }$ is 0. This contradicts the injectivity of f restricted to $D - \{ 0 \}$
:::
