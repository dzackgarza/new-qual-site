---
schema: qual/card@1
id: P-BKF04-4A
kind: problem
title: $A$ is diagonalizable iff every nilpotent $f(A)$ is zero
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $A$ be an $n\times n$ matrix with complex entries. Prove that $A$ is diagonalizable if and only if the following is true: Whenever $f$ is a polynomial with complex coefficients such that $f(A)$ is nilpotent, we have $f(A)=0$. (A matrix $A$ is nilpotent if $A^m=0$ for some $m\geq1$.)
:::

::: {.solution}
First suppose that $A$ is diagonalizable. If $C$ is an invertible $n\times n$ matrix, then $f(CAC^{-1})=Cf(A)C^{-1}$, so both diagonalizability and the stated property are unchanged by conjugation. Thus we may assume $A$ is diagonal. Then $f(A)$ is diagonal for every $f$, and a nilpotent diagonal matrix is $0$. Hence if $f(A)$ is nilpotent, then $f(A)=0$.

Conversely, suppose that $f(A)=0$ whenever $f(A)$ is nilpotent. Let $f(x)=\prod_\lambda(x-\lambda)$, where $\lambda$ runs through the distinct eigenvalues of $A$. The characteristic polynomial $c(x)$ of $A$ divides some power $f(x)^k$, and $c(A)=0$ by the Cayley--Hamilton theorem, so $f(A)^k=0$. By hypothesis, $f(A)=0$. Thus the minimal polynomial of $A$ divides $f$ and has distinct roots, so $A$ is diagonalizable.
:::
