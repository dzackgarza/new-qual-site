---
schema: qual/card@1
id: P-ALGS05C
kind: problem
title: "Eigenpair of algebraic and geometric multiplicity one yields a complementary block form"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: problem
Assume that $(\lambda, x)$ is an eigenpair of $A \in \mathbb{C}^{n \times n}$ such that $\operatorname{am}(\lambda) = \operatorname{gm}(\lambda) = 1$.
Prove that there exists a nonsingular matrix $(x \quad X)$ with inverse $(y \quad Y)^*$ such that
\[
\begin{pmatrix} y^* \\ Y^* \end{pmatrix} A \begin{pmatrix} x & X \end{pmatrix} = \begin{pmatrix} \lambda & 0 \\ 0 & M \end{pmatrix}.
\]
:::
