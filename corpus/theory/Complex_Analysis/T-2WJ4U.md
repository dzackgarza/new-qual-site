---
schema: qual/card@1
id: T-2WJ4U
kind: theorem
title: Hadamard factorization
classification:
  areas:
  - complex-analysis
  topics:
  - Weierstrass Factorization
  - Entire Functions
  - Zeros
relations: []
review: draft
---

::: {.theorem}
For an integer $p\ge0$, let $E_p$ be the canonical factor
$$
E_0(z)=1-z,\qquad E_p(z)=(1-z)\exp\Big(z+\frac{z^2}{2}+\cdots+\frac{z^p}{p}\Big)\quad(p\ge1).
$$
Let $f$ be an entire function of order $\rho<\infty$, where
$$
\rho\coloneqq\inf\ts{\sigma\ge0\st\text{there is }R>0\text{ with }\abs{f(z)}\le e^{\abs z^\sigma}\text{ for all }\abs z>R},
$$
and let $p\coloneqq\lfloor\rho\rfloor$.
Suppose $f$ is not identically zero, has a [[D-65VIK|zero]] of order $m\ge0$ at $0$, and let $(z_k)_{k\ge1}$ be its nonzero zeros, repeated with multiplicity.
Then there is a polynomial $g$ of degree at most $p$ such that
$$
f(z)=z^me^{g(z)}\prod_{k\ge1}E_p\Big(\frac{z}{z_k}\Big),
$$
where the product converges uniformly on compact subsets of $\CC$.
:::
