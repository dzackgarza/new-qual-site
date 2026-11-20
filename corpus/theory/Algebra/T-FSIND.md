---
schema: qual/card@1
id: T-FSIND
kind: theorem
title: The Frobenius--Schur indicator
slogan: '$\nu(\chi)$ is $1$, $0$, or $-1$: real, non-real, or quaternionic'
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Real Representations
relations: []
review: draft
---

::: {.theorem}
Let $G$ be a finite group and $\chi$ an irreducible character of $G$ over $\CC$.
The Frobenius--Schur indicator
$$
\nu(\chi)\coloneqq\frac{1}{\size G}\sum_{g\in G}\chi(g^2)
$$
takes the value $1$ when $\chi$ is the character of a representation realizable over $\RR$, the value $0$ when $\chi$ is not real-valued, and the value $-1$ otherwise, in which case the representation is quaternionic.
:::
