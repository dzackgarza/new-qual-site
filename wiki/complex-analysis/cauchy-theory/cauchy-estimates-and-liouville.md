---
title: Cauchy estimates and Liouville
order: 30
topics:
- Cauchy Estimates
- Growth Estimates
- Derivative Estimates
- Liouville's Theorem
---

# Cauchy estimates and Liouville

The integral formula bounds the derivatives of a holomorphic function by the values of the function on a circle, and that single estimate forces every entire function of controlled growth to be a polynomial.

## The estimates

[[T-22RQZ]]

The estimate is the one inequality in the subject that converts a bound on $\abs f$ over a set into a bound on the derivatives at an interior point, so it is the first thing to try when a hypothesis is a bound and the conclusion is about a derivative.
Taking $r\to\infty$ in a bound that does not depend on $r$ is what produces rigidity: the derivative vanishes, and the function is constant.

::: {.example title="Growth of an entire function and its derivatives"}
For $f(z) = e^z$ and $z_0 = 0$, Cauchy's inequality on $\DD_R(0)$ gives $\abs{f^{(n)}(0)}\leq n!/R^n$ for every $R>0$, hence $\abs{f^{(n)}(0)}\leq n!$, with equality at $R\to\infty$ only in the limit; the coefficient $\abs{a_n} = 1/n!$ is recovered exactly.
For $f(z) = 1/(1-z)$ on $\DD$ and $z_0 = 0$, the same inequality on $\DD_r(0)$ with $r<1$ gives $\abs{f^{(n)}(0)}\leq n!/(1-r)r^n$, and the best choice of $r = n/(n+1)$ recovers $\abs{f^{(n)}(0)} = n!$.
:::

## Liouville

[[T-QHIHJ]]

Liouville's theorem is the case $n=0$ of the growth bound, and its standard consequence is that a bounded entire function is constant, so a nonconstant entire function is unbounded on every unbounded set.

[[C-BKYF7]]

Other theorems whose conclusion is that a holomorphic function is constant are collected on [[complex-analysis/cauchy-theory/theorems-that-give-a-constant|Theorems that give a constant]], and the proofs of the fundamental theorem of algebra that run through Liouville's theorem are on [[complex-analysis/appendices/appendix-fta-proofs|the fundamental theorem of algebra]].

## Problems

[[E-SS2.EX-15]]
[[E-BPSOU]]
[[E-4NGIV]]
[[E-IPIKC]]
[[E-GQMTN]]
[[P-57CAX]]
[[P-BERK81S-17]]
[[P-8CA13]]
[[E-U2X4C]]
[[E-JLGWE]]
[[P-EMCA9]]
