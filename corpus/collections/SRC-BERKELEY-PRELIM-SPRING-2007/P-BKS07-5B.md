---
schema: qual/card@1
id: P-BKS07-5B
kind: problem
title: UC Berkeley Spring 2007 prelim 5B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\mathbb { F } _ { q }$ denote the finite field with q elements, where q is a power of a prime.
Let $\mathrm { S L } _ { n } ( \mathbb { F } _ { q } )$ be the group of $n \times n$ matrices with entries in $\mathbb { F } _ { q }$ and determinant 1, under matrix multiplication.
Determine (with proof) a simple necessary and sufficient condition on n and q for the center of $\mathrm { S L } _ { n } ( \mathbb { F } _ { q } )$ to be trivial.
:::

::: {.solution}
Let $E _ { i j }$ denote the $n \times n$ matrix with $( i , j )$ entry equal to 1 and all other entries zero.
For $i \neq j$ , we have $I _ { n } + E _ { i j } \in \mathrm { S L } _ { n } ( \mathbb { F } _ { q } )$ . A matrix A commutes with $I _ { n } + E _ { i j }$ if and only if $E _ { i j } A = A E _ { i j }$ . The latter condition implies that $A _ { j k } = 0$ for $k \neq j$ , that $A _ { k i } = 0$ for $k \neq i ,$ and that $A _ { i i } = A _ { j j }$ . If this holds for all $i \neq j$ , then $A = x I _ { n }$ is a scalar multiple of the identity, and we have $\overset { \cdot \mathrm { ~ \tiny ~ . ~ } } { A } \in \mathrm { S L } _ { n } ( \mathbb { F } _ { q } )$ if and only if $x ^ { n } = 1$ in $\mathbb { F } _ { q }$

The multiplicative group $\mathbb { F } _ { q } ^ { \times }$ is cyclic, so the necessary and sufficient condition for $x = 1$ to be the unique solution of $x ^ { n } = 1$ in $\mathbb { F } _ { q }$ is that $q - 1$ and n are relatively prime.
:::
