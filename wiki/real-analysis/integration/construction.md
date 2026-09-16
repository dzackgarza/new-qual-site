---
title: Constructing the integral
order: 10
topics:
- Lebesgue Integration
- Measure Theory
---

# Constructing the integral

Let $(X,\mathcal M,\mu)$ be a measure space.
The integral is defined first for simple functions, then for nonnegative measurable functions as a supremum over simple functions below them, and then for measurable $f$ with $\int\abs f<\infty$ as $\int f^+-\int f^-$.
Properties of the integral are proved in the same order, first for simple functions, then for nonnegative functions, then for integrable functions.

## Measurable and simple functions

A function $f\colon X\to\RR$ is measurable if $f^{-1}(B)\in\mathcal M$ for every Borel set $B$, equivalently if $\theset{f>a}\in\mathcal M$ for every $a\in\RR$.
Sums, products, countable suprema and infima, and pointwise limits of sequences of measurable functions are measurable.
A simple function is a measurable function with finitely many values, and $\int\sum_i a_i\chi_{E_i} = \sum_i a_i\mu(E_i)$ for $a_i\geq0$.

[[D-DHFN4]]

[[FD-OFT7I]] [[FD-OOCQD]]

[[PR-EWXRO]]

[[D-553MO]]

[[PR-KTKT6]]

## The Lebesgue integral

For measurable $f\geq0$, $\int f\coloneqq\sup\theset{\int\phi \st 0\leq\phi\leq f,\ \phi\text{ simple}}$.
A measurable $f$ is integrable if $\int\abs f<\infty$, and then $\int f\coloneqq\int f^+-\int f^-$ with $f^\pm\coloneqq\max(\pm f,0)$.

[[D-R4VKE]]

[[FD-Q3XHG]]

[[D-YWRVG]]

[[PR-OI5HX]]

[[PR-6OHTJ]]

[[FF-EMDBP]]

[[FF-C7GY4]] [[FF-LMANJ]]

::: {.remark}
Changing $f$ on a null set changes neither $\int f$ nor its essential supremum, so elements of $L^p$ are equivalence classes of functions equal almost everywhere.
The integrability of $x^a$ on $(0,1)$ exactly when $a>-1$ and on $(1,\infty)$ exactly when $a<-1$ is the comparison used for singularities at a point and for decay at infinity.

:::
