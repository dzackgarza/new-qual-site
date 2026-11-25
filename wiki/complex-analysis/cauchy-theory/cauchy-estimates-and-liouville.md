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

The bound is a supremum on a circle, about one centre and with one pair of constants for every radius; because $f$ is entire, every such closed disc lies in the domain, and no hypothesis about $f$ away from those circles is needed. The degree in the conclusion is attained: $f(z)=z^k$ satisfies the hypothesis with $A=B=1$, both positive as the statement requires, because $R^k\le R^k+1$ for every $R>0$, and it is a polynomial of degree exactly $k$.

## The bound at the best radius

::: {.example title="The optimized bound against the true value"}
For $f(z) = e^z$, $z_0 = 0$, and $\DD_R(0)$, the maximum of $\abs f$ on the circle is $e^R$, so Cauchy's inequality reads
$$
\abs{f^{(n)}(0)}\leq {n!\,e^R\over R^n}\qquad\text{for every } R>0.
$$
For $n\geq1$ the right-hand side is smallest at $R = n$, where it is $n!(e/n)^n$: $e = 2.718\ldots$ for $n=1$ and $5.699\ldots$ for $n=5$, against the true value $\abs{f^{(n)}(0)} = 1$ taken from the series $e^z = \sum_k z^k/k!$. (At $n=0$ there is no minimizing radius: the bound $e^R$ increases in $R$ on $R>0$.)
So at the best admissible radius the bound is $n!(e/n)^n$ times the true value, and Stirling's formula gives only
$$
n!\left(\frac en\right)^n \sim \sqrt{2\pi n},
$$
so that ratio grows without bound in $n$. The estimate is therefore not sharp even up to a constant factor, and the exact coefficients come from the series, not from the estimate.

For $f(z) = 1/(1-z)$ on $\DD$, $z_0 = 0$, and $r<1$, the maximum on $\abs z = r$ is $1/(1-r)$, so
$$
\abs{f^{(n)}(0)}\leq {n!\over (1-r)\,r^n},
$$
which for $n\geq1$ is smallest at $r = n/(n+1)$ and there equals $n!(n+1)^{n+1}/n^n$: $4$ for $n=1$ and $1791.59\ldots$ for $n=5$, against the true value $n!$. (At $n=0$ the bound $1/(1-r)$ increases in $r$ on $0<r<1$, so again there is no minimizing radius.) The ratio of the bound to the true value is then $(n+1)^{n+1}/n^n$, and
$$
\frac{(n+1)^{n+1}}{n^n} \sim e(n+1)
$$
is unbounded in $n$ as well.
:::

## Problems

### Polynomial growth

The estimate at order $n+1$ kills every coefficient past the $n$th when $\abs f$ is $\bigo{\abs z^n}$; these questions ask for the degree, for the constant, or for the contradiction.

[[E-BPSOU]] [[E-IPIKC]] [[E-JLGWE]] [[P-57CAX]]

### A lower bound on $\abs f$

A lower bound $\abs f\ge c>0$ over all of $\CC$ makes $1/f$ entire and bounded by $1/c$, so [[T-QHIHJ|Liouville's theorem]] applies to $1/f$; [[E-U2X4C]], [[E-GQMTN]] and [[E-3ZHRE]] are of that shape. A bound only for large $\abs z$ does not have that effect: it says nothing about $\abs f$ near $0$, so $1/f$ need not be entire, and $f(z)=z$ has $\abs{f(z)}\ge R$ on $\abs z\ge R$ without being constant.

[[E-27X7K]] bounds $\abs f$ below on every large circle rather than at a point, through a finite positive limit $\tilde m$ of $m(r)=\min_{\abs z=r}\abs{f(z)}$, and its route is the behaviour of $g(w)=f(1/w)$ at $0$ rather than Liouville applied to $1/f$. Positivity of $\tilde m$ gives $\abs{g(w)}\ge\tilde m/2$ on a punctured disc, and [[T-C5VEI|Casorati--Weierstrass]] then rules out an essential singularity of $g$ at $0$, because its conclusion puts values of $g$ arbitrarily close to $0$ in every punctured neighbourhood; finiteness of $\tilde m$ excludes a pole. The singularity at $0$ is then removable, $f$ is bounded, and Liouville's theorem makes it constant.

[[E-U2X4C]] [[E-GQMTN]] [[E-3ZHRE]] [[E-27X7K]]

### A bound that comes from elsewhere

The hypothesis need not be a numerical bound: a bound by another entire function, or a periodicity that makes a continuous function bounded, gives the same conclusion.

[[P-BERK81S-17]] [[P-8CA13]] [[E-4NGIV]]
