---
title: Constructing the integral
order: 10
problems:
  topics:
  - Lebesgue Integration
  - Measure Theory
---

# Constructing the integral

The construction is deliberately monotone.
First choose the class of measurable functions, which is closed under the pointwise operations used in limits.
Then define the integral on simple functions, extend it to nonnegative measurable functions by approximation from below, and finally pass to signed functions by positive and negative parts.
Every later convergence theorem is built to respect this order.

## Measurable and simple functions

Measurability is the condition that inverse images of Borel sets stay measurable; in practice it is enough to check sublevel sets and use closure under sums, products, countable suprema and infima, and sequential pointwise limits.
Simple functions are the finite-valued measurable functions, so their integrals reduce to finite sums of values times measures of level sets.

[[D-DHFN4]]

[[FD-OFT7I]] [[FD-OOCQD]]

[[PR-EWXRO]]

[[D-553MO]]

[[PR-KTKT6]]

## The Lebesgue integral

For $f\ge0$, define $\int f$ as the supremum of the integrals of simple $0\le\phi\le f$.
For general measurable $f$, write $f=f^+-f^-$ and require the two parts not to produce the indeterminate form $\infty-\infty$.
Integrability is the finite case $\int |f|<\infty$.

[[D-R4VKE]]

[[FD-Q3XHG]]

[[D-YWRVG]]

[[PR-OI5HX]]

[[T-YSMII]]

[[FF-EMDBP]]

[[FF-C7GY4]] [[FF-LMANJ]]

The essential supremum ignores null-set changes, matching the convention that functions equal almost everywhere represent the same $L^p$ element.
The power tests on $(0,1)$ and $(1,\infty)$ are the model local-singularity and tail calculations: they reduce many integrability questions to comparing an exponent with the critical value $-1$.

::: {.remark title="The three-step definition"}
Simple functions, then nonnegative measurable functions as a supremum over simple ones below, then general $f$ as $f^+ - f^-$.
Every property of the integral is proved in the same three steps, which is why so many proofs in this chapter open by reducing to the nonnegative case.
:::
