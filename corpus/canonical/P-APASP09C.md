---
schema: qual/card@1
id: P-APASP09C
kind: problem
title: "The Moore–Penrose pseudo-inverse gives the minimum-norm least-squares solution"
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: problem
Let $\tilde{x}$ be a least squares solution to $Ax = b$, where $A$ is $m \times n$ and $m \geq n$.
Let $A^\dagger$ be the pseudo-inverse of $A$.
Use the Singular Value Decomposition to show that $\tilde{x} = A^\dagger b$ is the minimum 2-norm least squares solution to $Ax = b$, i.e.\ show

(a) $\tilde{x}$ is a least squares solution,

(b) if $\hat{x}$ is a least squares solution then $\|\hat{x}\|_2 \geq \|\tilde{x}\|_2$, and

(c) $\tilde{x}$ is unique.
:::
