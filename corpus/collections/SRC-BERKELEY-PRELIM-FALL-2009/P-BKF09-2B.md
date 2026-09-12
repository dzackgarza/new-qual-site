---
schema: qual/card@1
id: P-BKF09-2B
kind: problem
title: Berkeley Fall 2009 prelim problem 2B
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let P be a square matrix over R such that $P ^ { T } P = P$. Prove that there exists a matrix A such that$A ^ { T } A$is invertible and$P = A ( A ^ { T } A ) ^ { - 1 } A ^ { T }$
:::

::: {.solution}
For any matrix A with linearly independent columns, $A ^ { T } A$is invertible, and$A ( A ^ { T } A ) ^ { - 1 } A ^ { T }$is the matrix of the orthogonal projection on the column space of A. (Indeed, the null space of$A ^ { T }$is the orthogonal complement to the column space of A, and for every x from the column space of A we have$x = A z$for some z, an hence$A ( A ^ { T } A ) ^ { - 1 } A ^ { T } x = A z = x . )$Taking A to be a matrix whose columns are a basis of the column space of$P ,$we have only to prove that P is the matrix of an orthogonal projection (necessarily onto its own column space). In other words, we must show that$x - P x$is orthogonal to$P y$for all vectors x, y. But$( x - P x ) ^ { T } P y = x ^ { T } ( P - P ^ { T } P ) y = 0$by the hypothesis. (Another way:$P ^ { T } P = P$implies that$P ^ { T } = ( { P } ^ { T } P ) ^ { T } = { P } ^ { T } P = P .$, i.e. P is a self-adjoint idempotent:$P ^ { 2 } = P . )$
:::
