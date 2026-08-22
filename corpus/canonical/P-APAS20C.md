---
schema: qual/card@1
id: P-APAS20C
kind: problem
title: Positive definiteness of $\phi-t\psi$ via the smallest eigenvalue of $\psi^{-1/2}\phi\psi^{-1/2}$
classification:
  areas:
  - applied-algebra
  topics:
  - Positive Definite Matrices
  - Hermitian Matrices
relations: []
review: draft
solved: false
---

::: problem
Let $V$ be an inner product space of dimension $n$, and $\phi,\psi\colon V\to V$ two positive definite Hermitian maps.
You may use without proof that $\psi$ has a unique positive definite square root $\psi^{1/2}$, and that $\psi$ and $\psi^{1/2}$ are non-singular.

Let $t\in\mathbb{R}$ be a real number.
Prove that $\phi-t\psi$ is positive definite if and only if $t<\lambda_n(\theta)$ (i.e., the smallest eigenvalue of $\theta$) where $\theta=\psi^{-1/2}\phi\psi^{-1/2}$.
:::
