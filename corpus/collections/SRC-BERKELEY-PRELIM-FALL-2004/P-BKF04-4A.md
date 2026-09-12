---
schema: qual/card@1
id: P-BKF04-4A
kind: problem
title: UC Berkeley Fall 2004 prelim 4A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let A be an $n \times n$ matrix with complex entries. Prove that A is diagonalizable if and only if the following is true: Whenever f is a polynomial with complex coefficients such that $f ( A )$ is nilpotent, we have $f ( A ) = 0$ . (A matrix A is nilpotent if $A ^ { m } = 0$ for some $m \geq 1 . )$ )
:::

::: {.solution}
First suppose that A is diagonalizable. If C is an invertible $n \times n$ matrix, then $f ( C A C ^ { - 1 } ) = C f ( A ) { \bar { C } } ^ { - 1 }$ , so both sides of the “if and only $\mathrm { i f } ^ { \dag }$ are unchanged by conjugation. Thus we may assume A is diagonal. Then $f ( A )$ is diagonal for any $f .$ Hence if $f ( A )$ is nilpotent, then $f ( A ) = 0$

Now suppose, conversely, that A is such that $f ( A ) = 0$ whenever $f ( A )$ is nilpotent. Let $f ( x )$ be the product of $( x - \lambda )$ where λ runs through the distinct eigenvalues of A. Then the characteristic polynomial $c ( x )$ of A divides some power of $f ( x )$ , but $c ( A ) = 0$ (Cayley-Hamilton Theorem), so some power of $f ( A )$ is 0. By hypothesis, $f ( A ) = 0$ . Thus the minimal polynomial of A has distinct zeros, so A is diagonalizable.
:::
