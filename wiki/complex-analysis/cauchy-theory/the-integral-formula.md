---
title: The integral formula
order: 20
topics:
- Cauchy Integral Formula

---

# The integral formula

The values of a holomorphic function inside a curve are determined by its values on the curve.

[[T-LA2UI]]

::: {.example title="Two integrals the formula evaluates"}
For $f(z) = e^z$ and the circle $\abs z = 2$, which encloses $z_0 = 1$, the formula with $n=0$ gives
$$
\int_{\abs z=2}{e^z\over z-1}\dz = 2\pi i\,e^{1} = 2\pi i\,e.
$$
For $f(z) = \cos z$ and the circle $\abs z = 1$, the formula with $n = 2$ and $z_0 = 0$ gives
$$
\int_{\abs z=1}{\cos z\over z^{3}}\dz = {2\pi i\over 2!}\cos''(0) = {2\pi i\over 2}\cdot(-1) = -i\pi,
$$
while for $n=0,1$ the same circle gives $2\pi i\cos 0 = 2\pi i$ and $2\pi i\cos'(0) = 0$ for $\cos z/z$ and $\cos z/z^{2}$.
:::

## The mean value property

For a circle centered at the point, the integral formula gives the mean value property:

[[T-5BLYU]]

::: {.remark title="Mean value property and the maximum principle"}
The mean value property is the mechanism behind [[T-BYNL5|the maximum modulus principle]], and its analogue for a real harmonic function $u$ is behind the strict maximum principle for $u$ ([[PR-6WOTK]]).

:::

## Problems

[[E-RLHXB]] [[E-VGNUI]] [[E-3B2YA]]
[[P-AZOFF-D03]] [[P-UGA8150S21-HW3-04]]
