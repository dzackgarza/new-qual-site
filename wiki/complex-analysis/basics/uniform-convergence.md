---
title: Uniform convergence
order: 55
topics:
- Uniform Convergence
- Uniform Continuity
- Compactness
- Equicontinuity
---

# Uniform convergence

Uniform continuity and uniform convergence each replace a bound that may depend on a point by one that does not: on a compact metric space for continuity, and on a fixed set for convergence of functions.
Both are what makes a limit commute with the operations of analysis — integration, differentiation, and the taking of values.

## Uniform continuity

[[D-WGYSB]]

[[T-O4UD3]]

::: {.example title="Continuity without uniform continuity"}
The function $f(x) = 1/x$ is continuous on $(0,1)$ and not uniformly continuous there: for every $\delta>0$ the points $x$ and $x/2$ of $(0,1)$ satisfy $\abs{x-x/2}<\delta$ for small $x$, while
$$
\abs{f(x)-f(x/2)} = \abs{{1\over x}-{2\over x}} = {1\over x}
$$
is arbitrarily large.
:::

## Uniform convergence

[[D-YZC3C]]

[[D-AIQG3]]

[[PR-4LISY]]

The property that uniform convergence adds to pointwise convergence is the one that survives a limit: a uniform limit of continuous functions is continuous, and a uniform limit of integrable functions is integrable with the integral of the limit equal to the limit of the integrals.
For series, the comparison test in the form of the Weierstrass $M$-test gives uniform convergence.

[[FF-IAUQG]]

::: {.example title="Uniform convergence without term-by-term differentiation"}
On $\RR$ the series $\sum_{n\geq1}\sin(n^2x)/n^2$ converges uniformly, since $\abs{\sin(n^2x)/n^2}\leq 1/n^2$ and $\sum_n 1/n^2<\infty$, while the series of derivatives $\sum_{n\geq1}\cos(n^2x)$ diverges at $x=0$.
So the identity $(f') = (\sum_n f_n)'$ needs a hypothesis on the derivatives, not only on the series.
:::

## Compactness in function spaces

A family of functions is [[D-2CCDB|equicontinuous]] when one $\delta$ serves every member of the family at every point, and that is what turns a bound into a convergent subsequence.

[[FF-XZGIY]]

For holomorphic functions the bound on compact subsets alone gives equicontinuity, by the Cauchy estimate, and the result is [[T-4ALS2|Montel's theorem]]; the pages are [[complex-analysis/conformal-maps/normal-families-and-montel|Normal families and Montel]] and [[complex-analysis/cauchy-theory/morera-and-converses#Locally uniform limits|locally uniform limits]].
