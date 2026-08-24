---
schema: qual/card@1
id: P-APAF06A
kind: problem
title: Eigenpair of algebraic and geometric multiplicity one yields a complementary block form
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: problem
Assume that $(\lambda, x)$ is an eigenpair of $A \in M_n$ such that $am(\lambda) = gm(\lambda) = 1$.
Prove that there exists a nonsingular matrix $(x \quad X)$ with inverse $(y \quad Y)^*$ such that
\[
\begin{pmatrix} y^* \\ Y^* \end{pmatrix} A (x \quad X) = \begin{pmatrix} \lambda & 0 \\ 0 & M \end{pmatrix}.
\]
:::
