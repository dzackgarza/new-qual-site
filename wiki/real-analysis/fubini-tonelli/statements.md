---
title: The statements
order: 10
topics:
- Measure Theory
---

# The statements

Let $(X,\mathcal M,\mu)$ and $(Y,\mathcal N,\nu)$ be $\sigma$-finite measure spaces with product measure $\mu\times\nu$ on $\mathcal M\otimes\mathcal N$.
Tonelli's and Fubini's theorems both equate $\int_{X\times Y} f\,d(\mu\times\nu)$ with the two iterated integrals; Tonelli's theorem assumes $f\geq0$ and Fubini's theorem assumes $f\in L^1(\mu\times\nu)$.
[[real-analysis/fubini-tonelli/which-one-applies|Which one applies?]] compares the hypotheses.

## Tonelli: nonnegative measurable functions

For $f\geq0$ measurable on $X\times Y$, the iterated integrals and the integral over $X\times Y$ are equal as elements of $[0,\infty]$.
For a double sequence $a_{mn}\geq0$ (counting measure on $\NN\times\NN$), this gives $\sum_m\sum_n a_{mn} = \sum_n\sum_m a_{mn}$.

[[T-6PRW3]]

[[FT-4JRQX]]

## Fubini: integrable functions

For $f\in L^1(\mu\times\nu)$, the sections $f(x,\wait)$ are in $L^1(\nu)$ for $\mu$-almost every $x$, the function $x\mapsto\int_Y f(x,y)\,d\nu(y)$ is in $L^1(\mu)$, and the iterated integrals are finite and equal to $\int_{X\times Y} f\,d(\mu\times\nu)$; the same holds with the roles of $X$ and $Y$ exchanged.

[[T-4GPEF]]

[[T-X7XZX]]

[[FT-H6AWV]] [[FT-VHK2H]]

## Other interchanges

For nonnegative terms, sums and integrals commute by the monotone convergence theorem, or by Tonelli's theorem with counting measure.
Differentiating under the integral sign requires a domination hypothesis on the derivative.

[[PR-V4MOK]]

[[PR-JW3QE]]

[[E-WXIRH]]
