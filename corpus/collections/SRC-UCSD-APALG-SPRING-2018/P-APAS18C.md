---
schema: qual/card@1
id: P-APAS18C
kind: problem
title: Cauchy–Schwarz form $|x^*y|^2\leq(x^*Px)(y^*P^{-1}y)$ for positive definite $P$
classification:
  areas:
  - applied-algebra
  topics:
  - Positive Definite Matrices
  - Inner Product Spaces
relations: []
review: draft
---

::: problem
Let $P\in\mathbb{C}^{n\times n}$ be a positive definite Hermitian matrix.
Show that
\[
|x^*y|^2\leq(x^*Px)(y^*P^{-1}y)
\]
for all $x,y\in\mathbb{C}^n$.
:::

::: solution
Because \(P\) is Hermitian positive definite, its positive definite square root \(P^{1/2}\) exists and is invertible. Write
\[
x^*y=(P^{1/2}x)^*(P^{-1/2}y).
\]
Applying the ordinary Cauchy--Schwarz inequality in \(\mathbb C^n\),
\[
|x^*y|^2
\le \|P^{1/2}x\|_2^2\,\|P^{-1/2}y\|_2^2.
\]
Now
\[
\|P^{1/2}x\|_2^2=x^*Px,
\qquad
\|P^{-1/2}y\|_2^2=y^*P^{-1}y.
\]
Hence
\[
|x^*y|^2\le (x^*Px)(y^*P^{-1}y).
\]
:::
