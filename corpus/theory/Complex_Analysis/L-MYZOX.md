---
schema: qual/card@1
id: L-MYZOX
kind: lemma
title: Abel's test for power series on the unit circle
slogan: 'Monotone coefficients tending to zero force convergence at every boundary point except $1$.'
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Power Series
relations: []
review: draft
---

::: {.lemma}
Let $(c_k)_{k\ge0}$ be a nonincreasing sequence of nonnegative real numbers with $c_k\to0$, and let $f(z)\coloneqq\sum_{k\ge0}c_kz^k$.
Then the series $f(z)$ converges for every $z$ with $\abs{z}=1$ and $z\neq1$.

This is [@Rud76, ch. 3, Theorem 3.44], which concludes convergence at every point of $\abs z=1$ except possibly $z=1$ for a series of radius of convergence $1$ with $c_0\ge c_1\ge\cdots$ and $c_k\to0$. The hypothesis of radius $1$ is not needed for the boundary statement and is not assumed above: boundedness of $c_k$ already puts the radius at least $1$, and the argument for the boundary points is the bound on the partial sums of $z^k$ together with [@Rud76, ch. 3, Theorem 3.42].
:::
