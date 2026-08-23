---
schema: qual/card@1
id: P-RASP22D
kind: problem
title: "Von Neumann mean ergodic theorem for unitary operators"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Ergodic Theory
  - Unitary Operators
relations: []
review: draft
solved: false
---

::: problem
Let $H$ be a Hilbert space and let $U \in L(H, H)$ be unitary, meaning $U$ is invertible and $\langle Ux, y \rangle = \langle x, U^{-1}y \rangle$ for all $x, y \in H$.

1. Let $\operatorname{Ran}(I - U)$ denote the image of $I - U$. Prove that $\operatorname{Ran}(I - U)^\perp = \operatorname{Ker}(I - U)$.

2. Set $S_n = \frac{1}{n} \sum_{j=0}^{n-1} U^j$, and let $P$ be the orthogonal projection map from $H$ to $\operatorname{Ker}(I - U)$. Prove that $S_n \to P$ in the strong operator topology. (This is von Neumann's Mean Ergodic Theorem.)
:::