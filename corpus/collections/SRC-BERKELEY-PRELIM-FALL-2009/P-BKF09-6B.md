---
schema: qual/card@1
id: P-BKF09-6B
kind: problem
title: The numerical range of a normal matrix is a convex polygon
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\langle z,w\rangle=\sum z_i\bar{w}_i$ be the Hermitian dot product on $\CC^n$, and let $A$ be a *normal* linear operator on $\CC^n$, i.e. $A^*A=AA^*$ where $A^*=\bar{A}^t$ is Hermitian adjoint to $A$. Prove that the set of complex numbers
$$
\Lambda_A\coloneqq\{\langle Az,z\rangle\mid z\in\CC^n,\ \langle z,z\rangle=1\}
$$
is a convex polygon.
:::

::: {.solution}
According to the orthogonal diagonalization theorem, a normal operator has an Hermitian orthonormal basis of eigenvectors.
In such a basis, $\langle Az,z\rangle=\sum\lambda_i\abs{z_i}^2$, where $\lambda_i$ are the eigenvalues of $A$, while $\langle z,z\rangle=1$ becomes $\sum\abs{z_i}^2=1$.
This shows that $\Lambda_A$ coincides with the convex hull of the finite set $\lambda_1,\ldots,\lambda_n$ of eigenvalues of $A$.
:::
