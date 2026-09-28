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
Let $\langle z , w \rangle = \sum z _ { i } { \bar { w } } _ { i }$be the Hermitian dot product on$\mathbb { C } ^ { n }$, and let A be a normal linear operator on Cn, i.e.$A ^ { * } A = A A ^ { * }$where$A ^ { * } = \bar { A } ^ { t }$is Hermitian adjoint to A. Prove that the set of complex numbers$$\Lambda _ { A } : = \{ \langle A z , z \rangle \mid z \in \mathbb { C } ^ { n } , \langle z , z \rangle = 1 \}$$

is a convex polygon.
:::

::: {.solution}
According to the orthogonal diagonalization theorem, a normal operator has an Hermitian orthonormal basis of eigenvectors.
In such a basis, $\langle A z , z \rangle = \sum \lambda _ { i } | z _ { i } | ^ { 2 }$, where$\lambda _ { i }$are the eigenvalues of A, while$\langle z , z \rangle = 1$becomes$\sum | z _ { i } | ^ { 2 } = 1$This shows that$\Lambda _ { A }$coincides with the convex hull of the finite set$\lambda _ { 1 } , \ldots , \lambda _ { n }$ of eigenvalues of A.
:::
