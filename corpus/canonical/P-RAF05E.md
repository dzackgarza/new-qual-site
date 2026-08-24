---
schema: qual/card@1
id: P-RAF05E
kind: problem
title: "Dense sequence with Gram matrix approaching identity implies weak convergence to zero"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Weak Convergence
  - Gram Matrix
relations: []
review: draft
solved: false
---

::: problem
Let $H$ be a Hilbert space.
Suppose that there is a sequence $\{x_j\}$ in $H$ such that the finite linear combinations of the $x_j$ are dense in $H$ and
$$
|\langle x_j, x_k \rangle| \leq 1/2^{|j-k|} \quad \forall j, k \in \mathbb{N}.
$$
Prove that $x_j \to 0$ weakly.
:::
