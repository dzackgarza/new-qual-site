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

## The estimate

[[T-22RQZ]]

The hypothesis to check first is $\overline{\DD_R(z_0)}\subseteq\Omega$: the estimate concerns a closed disc contained in the domain, and the constant is the supremum of $\abs f$ on its boundary circle, which for nonconstant $f$ is also the supremum over the closed disc ([[T-BYNL5]]).

The inequality converts a bound on $\abs f$ over a set into a bound on the derivatives at an interior point, at the price of the factor $n!/R^n$ for $n$ derivatives. Read at the centre of the circle it bounds the Taylor coefficients of $f$ there, in the form the card records as its variation.

## Liouville

[[T-QHIHJ]]

The hypothesis is a bound on $\abs f$ over all of $\CC$, and a one-sided bound on $\Re f$ is enough as well ([[P-57CAX]]). Liouville's theorem is also what rules out $\CC$ among the domains of [[complex-analysis/conformal-maps/the-riemann-mapping-theorem|the Riemann mapping theorem]]: a [[D-TM4TE|biholomorphism]] $\CC\to\DD$ would be a bounded nonconstant entire function, while [[T-4MDS6|the theorem]] is stated for a nonempty simply connected $\Omega\subsetneq\CC$.

Theorems whose conclusion is that a holomorphic function is constant are collected on [[complex-analysis/cauchy-theory/theorems-that-give-a-constant|Theorems that give a constant]], and the routes to the fundamental theorem of algebra that run through Liouville's theorem are on [[complex-analysis/appendices/appendix-fta-proofs|the fundamental theorem of algebra]].

## Polynomial growth

[[T-PG7ZK]]

The bound is a supremum on a circle, about one centre and with one pair of constants for every radius; because $f$ is entire, every such closed disc lies in the domain, and no hypothesis about $f$ away from those circles is needed. The degree in the conclusion is attained: $f(z)=z^k$ satisfies the hypothesis with $A=1$ and $B=0$ and is a polynomial of degree exactly $k$.

## Sharpness

::: {.example title="How sharp the estimate is"}
For $f(z) = e^z$, $z_0 = 0$, and $\DD_R(0)$, the maximum of $\abs f$ on the circle is $e^R$, so Cauchy's inequality reads
$$
\abs{f^{(n)}(0)}\leq {n!\,e^R\over R^n}\qquad\text{for every } R>0.
$$
The right-hand side is smallest at $R = n$, where it is $n!(e/n)^n$: $e = 2.718\ldots$ for $n=1$ and $5.699\ldots$ for $n=5$, against the true value $\abs{f^{(n)}(0)} = 1$ taken from the series $e^z = \sum_k z^k/k!$.
So the bound at its best radius is $\sqrt{2\pi n}$ times the true value, by Stirling's formula: the estimate is right in its order in $n$, and the exact coefficients come from the series, not from the estimate.

For $f(z) = 1/(1-z)$ on $\DD$, $z_0 = 0$, and $r<1$, the maximum on $\abs z = r$ is $1/(1-r)$, so
$$
\abs{f^{(n)}(0)}\leq {n!\over (1-r)\,r^n},
$$
which is smallest at $r = n/(n+1)$ and there equals $n!(n+1)^{n+1}/n^n$: $4$ for $n=1$ and $1791.59\ldots$ for $n=5$, against the true value $n!$.
The estimate is therefore sharp in order and not in constant.
:::

## Problems

### Polynomial growth

The estimate at order $n+1$ kills every coefficient past the $n$th when $\abs f$ is $\bigo{\abs z^n}$; these questions ask for the degree, for the constant, or for the contradiction.

[[E-BPSOU]] [[E-IPIKC]] [[E-JLGWE]] [[P-57CAX]]

### A lower bound on $\abs f$

A lower bound on $\abs f$ at large $\abs z$ is an upper bound on $\abs{1/f}$, so the estimate is applied to $1/f$ and the conclusion is again that $f$ is constant.

[[E-U2X4C]] [[E-GQMTN]] [[E-3ZHRE]] [[E-27X7K]]

### A bound that comes from elsewhere

The hypothesis need not be a numerical bound: a bound by another entire function, or a periodicity that makes a continuous function bounded, gives the same conclusion.

[[P-BERK81S-17]] [[P-8CA13]] [[E-4NGIV]]
