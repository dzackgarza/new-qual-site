---
schema: qual/card@1
id: P-RASP17C
kind: problem
title: "Diagonal operators on Hilbert space: boundedness and compactness criterion"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Compact Operators
  - Orthonormal Bases
relations: []
review: draft
---

::: problem
Let $(H, \langle \cdot | \cdot \rangle)$ be a Hilbert space, $\{e_n\}_{n=1}^\infty$ and $\{u_n\}_{n=1}^\infty$ be orthonormal bases for $H$, and $\{\lambda_n\}_{n=1}^\infty \subset \mathbb{C}$ with $M := \sup_n |\lambda_n| < \infty$.

1. Show $Th := \sum_{n=1}^\infty \lambda_n \langle h | e_n \rangle u_n$ exists in $H$ for all $h \in H$.

2. Show $\|T\|_{op} \leq M < \infty$, where $\|T\|_{op}$ is the operator norm of $T$.

3. Show $T$ is a compact operator if $\lim_{n \to \infty} \lambda_n = 0$.
:::
