---
schema: qual/card@1
id: P-CASP23B
kind: problem
title: "Product of distances from a point on T to given points is at least one"
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Principle
  - Polynomials
  - Unit Circle
relations: []
review: draft
---

::: problem
Let $z_1, \ldots, z_n$ be points on $\mathbb{T}$.
Prove that there is $z_0 \in \mathbb{T}$ such that the product of the distances from $z_0$ to each of the given points is at least one.
:::

::: solution
Consider the polynomial
\[
p(z)=\prod_{j=1}^n(z-z_j).
\]
Since every $|z_j|=1$,
\[
|p(0)|=\prod_{j=1}^n|z_j|=1.
\]
By the maximum modulus principle applied on the closed unit disk,
\[
1=|p(0)|\le \max_{|z|=1}|p(z)|.
\]
Choose $z_0\in\mathbb T$ where this maximum is attained. Then
\[
\prod_{j=1}^n|z_0-z_j|=|p(z_0)|\ge1,
\]
as required.
:::
