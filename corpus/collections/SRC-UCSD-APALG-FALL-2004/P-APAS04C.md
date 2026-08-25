---
schema: qual/card@1
id: P-APAS04C
kind: problem
title: Pseudo-inverse gives the minimal $2$-norm least-squares solution
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
  - Linear Algebra
  - Norms
relations: []
review: draft
---

::: problem
Let $\hat{x}$ be a least squares solution to $Ax=b$, where $A\in M_{m,n}$ and $m\ge n$.
Let $A^\dagger$ be the pseudo-inverse of $A$.
Use the Singular Value Decomposition to show that $\tilde{x}=A^\dagger b$ is the min $2$-norm least squares solution to $Ax=b$, i.e., show

(a) $\tilde{x}$ is a least squares solution,

(b) if $\hat{x}$ is a least square solution then $\|\hat{x}\|_2\ge\|\tilde{x}\|_2$, and

(c) $\tilde{x}$ is unique.

(Notation: $M_{m,n}$ denotes the set of $m\times n$ complex matrices.)
:::
