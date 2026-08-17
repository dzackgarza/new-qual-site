---
schema: qual/card@1
id: E-TUKVC
kind: exercise
title: Entire functions with a vanishing Taylor coefficient at every point are polynomials
classification:
  areas:
  - complex-analysis
  topics:
  - power-series
  - entire-functions
  - polynomials
  - identity-theorem
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Suppose $f$ is analytic, defined on all of $\CC$, and for each $z_0 \in \CC$ there is at least one coefficient in the expansion $f(z) = \sum_{n=0}^\infty c_n(z-z_0)^n$ is zero.
Prove that $f$ is a polynomial.

> Hint: use the fact that $c_n n! = f^{(n)}(z_0)$ and use a countability argument.
:::

::: {.solution}
Write $Z_n \da \ts{z\in \CC \st f^{(n)}(z) = 0 }$, then by hypothesis $\Union_{n\geq 0} Z_n = \CC$.
A version of the Baire category theorem is that if $X$ is a complete metric space and $X$ is a countable union of closed sets, then at least one such set has a nonempty interior.
Thus some $Z_n$ has an interior point $z_0$, and as a result there is some disc $\DD_\eps(z_0)$ on which $f^{(n)}(z_0) \equiv 0$.
This implies that $f^{(k)}(z_0) \equiv 0$ on $\DD_\eps(z_0)$ for every $k\geq n$, so $f$ is a polynomial of degree at most $n$.
:::
