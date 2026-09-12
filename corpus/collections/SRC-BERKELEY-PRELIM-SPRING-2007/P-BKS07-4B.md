---
schema: qual/card@1
id: P-BKS07-4B
kind: problem
title: UC Berkeley Spring 2007 prelim 4B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let E be the C-vector space of entire functions.
Let V be a nonzero finite-dimensional C-subspace of E with the property that $f \in V$ implies $f ^ { \prime } \in V$ . Prove that V contains a function that is everywhere nonzero.
:::

::: {.solution}
The map $T \colon V \to V$ sending f to $f ^ { \prime }$ is a linear transformation.
Since V is a C-vector space, there exists an eigenvalue $\lambda \in \mathbb { C }$ . Let $f \in V$ be a corresponding (nonzero) eigenvector.
Then $f ^ { \prime } = \lambda f$ , so $f ( z ) = c e ^ { \lambda z }$ for some $c \in \mathbb { C } ^ { \times }$ . This function is everywhere nonzero.
:::
