---
schema: qual/card@1
id: P-BKF09-2B
kind: problem
title: Real matrices with $P^TP=P$ are orthogonal projections $A(A^TA)^{-1}A^T$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $P$ be a square matrix over $\RR$ such that $P^TP=P$.
Prove that there exists a matrix $A$ such that $A^TA$ is invertible and $P=A(A^TA)^{-1}A^T$.
:::

::: {.solution}
For any matrix $A$ with linearly independent columns, $A^TA$ is invertible, and $A(A^TA)^{-1}A^T$ is the matrix of the orthogonal projection on the column space of $A$. (Indeed, the null space of $A^T$ is the orthogonal complement to the column space of $A$, and for every $x$ from the column space of $A$ we have $x=Az$ for some $z$, and hence $A(A^TA)^{-1}A^Tx=Az=x$.)
Taking $A$ to be a matrix whose columns are a basis of the column space of $P$, we have only to prove that $P$ is the matrix of an orthogonal projection (necessarily onto its own column space).
In other words, we must show that $x-Px$ is orthogonal to $Py$ for all vectors $x,y$. But $(x-Px)^TPy=x^T(P-P^TP)y=0$ by the hypothesis.
(Another way: $P^TP=P$ implies that $P^T=(P^TP)^T=P^TP=P$, i.e. $P$ is a self-adjoint idempotent: $P^2=P$.)
:::
