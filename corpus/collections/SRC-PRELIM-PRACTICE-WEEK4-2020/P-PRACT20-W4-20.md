---
schema: qual/card@1
id: P-PRACT20-W4-20
kind: problem
title: An idempotent operator splits $V$ into its fixed space and kernel
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Linear Transformations
  - Idempotents
relations: []
review: draft
---

::: {.problem}
Assume that V is a finite dimensional vector space and $T : V \to V$ is a linear transformation such that $T ^ { 2 } = T$ . Show that each $v \in V$ can be uniquely written as $v = v _ { 1 } + v _ { 2 }$ where $T ( v _ { 1 } ) = v _ { 1 }$ and $T ( v _ { 2 } ) = 0$
:::

::: {.solution}
Since $T ^ { 2 } = T$ , T fixes members of it’s image: $T ( T ( v ) ) = T ( v ) \implies T ( T ( v ) - v ) = 0$ . This shows that for any $v \in V , T ( v ) - v \in N ( T )$ . Thus for any $v \in V$ , put $v _ { 1 } = T ( v )$ and $v _ { 2 } = v - T ( v )$ . Then $v = v _ { 1 } + v _ { 2 }$ , where $T ( v _ { 1 } ) = v _ { 1 }$ and $T ( v _ { 2 } ) = 0$ . Further, it $v = u _ { 1 } + u _ { 2 }$ is another such representation, then applying T shows that

$$
\underbrace { T ( v _ { 1 } ) } _ { = v _ { 1 } } + \underbrace { T ( v _ { 2 } ) } _ { = 0 } = \underbrace { T ( u _ { 1 } ) } _ { = u _ { 1 } } + \underbrace { T ( u _ { 2 } ) } _ { = 0 } \implies v _ { 1 } = u _ { 1 } ,
$$

whence $v _ { 1 } + v _ { 2 } = u _ { 1 } + u _ { 2 } \implies v _ { 2 } = u _ { 2 }$ . Thus the representation is unique.
[Note: a linear operator T satisfying $T ^ { 2 } = T$ is called a projection operator.]
:::
