---
schema: qual/card@1
id: P-APAS21A
kind: problem
title: Schur form; deflating a simple eigenpair and the angle between $x$ and $y$
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Linear Algebra
relations: []
review: draft
solved: false
---

::: problem
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex components, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

(a) State, but do not prove, the Schur decomposition theorem for a matrix $A \in M_n$.

(b) Let $(\lambda, x)$ be a simple eigenpair of $A \in M_n$ with $x^H x = 1$. Prove that there exists a nonsingular matrix $\begin{pmatrix} x & X \end{pmatrix}$ with inverse $\begin{pmatrix} y & Y \end{pmatrix}^H$ such that
\[
\begin{pmatrix} y^H \\ Y^H \end{pmatrix}
A
\begin{pmatrix} x & X \end{pmatrix}
=
\begin{pmatrix} \lambda & 0 \\ 0 & M \end{pmatrix}.
\]

(c) Hence prove that the angle $\theta$ between $x$ and $y$ satisfies $\sec \theta = \|y\|_2$.
:::
