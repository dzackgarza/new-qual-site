---
schema: qual/card@1
id: E-HAT-4.D-10
kind: problem
title: "Eigenvalues of quaternionic matrices"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
---

Fill in the details of the following argument to show that every $n \times n$ matrix $A$ with entries in $\mathbb{H}$ has an eigenvalue in $\mathbb{H}$.
For $t \in [0, 1]$ and $\lambda \in S^3 \subset \mathbb{H}$, consider the matrix $t\lambda I + (1-t)A$.
If $A$ has no eigenvalues, this is invertible for all $t$.
Thus the map $S^3 \to GL_n(\mathbb{H})$, $\lambda \mapsto \lambda I$, is nullhomotopic.
But by the preceding problem and Exercise 10(b) in §3.C, this map represents $n$ times a generator of $\pi_3 GL_n(\mathbb{H})$.
