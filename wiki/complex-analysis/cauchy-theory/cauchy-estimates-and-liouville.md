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

::: {.example title="How sharp the estimate is"}
For $f(z) = e^z$, $z_0 = 0$, and $\DD_R(0)$, the maximum of $\abs f$ on the circle is $e^R$, so Cauchy's inequality reads
$$
\abs{f^{(n)}(0)}\leq {n!\,e^R\over R^n}\qquad\text{for every } R>0.
$$
The right-hand side is smallest at $R = n$, where it is $n!(e/n)^n$: $e = 2.718\ldots$ for $n=1$ and $5.699\ldots$ for $n=5$, against the true value $\abs{f^{(n)}(0)} = 1$ taken from the series $e^z = \sum_k z^k/k!$.
So the estimate is right in its dependence on $n$ up to a factor growing like $(e/n)^n$, and the exact coefficients come from the series, not from the estimate.

For $f(z) = 1/(1-z)$ on $\DD$, $z_0 = 0$, and $r<1$, the maximum on $\abs z = r$ is $1/(1-r)$, so
$$
\abs{f^{(n)}(0)}\leq {n!\over (1-r)\,r^n},
$$
which is smallest at $r = n/(n+1)$ and there equals $n!(n+1)^{n+1}/n^n$: $4$ for $n=1$ and $1791.59\ldots$ for $n=5$, against the true value $n!$.
The estimate is therefore sharp in order and not in constant.
:::

## Liouville

[[T-QHIHJ]]

Liouville's theorem is the case $n=0$ of the growth bound, and its standard consequence is that a bounded entire function is constant, so a nonconstant entire function is unbounded on every unbounded set.
It is also what rules out $\CC$ in the uniformization of plane domains, which is stated with the Riemann mapping theorem ([[C-BKYF7]]).

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
