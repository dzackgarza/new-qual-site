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

For a circle centered at the point, the integral formula expresses $f$ at the center as the average of $f$ over the circle.

[[T-5BLYU]]

::: {.remark title="Mean value property and the maximum principle"}
The mean value property above is the mechanism behind the [[T-BYNL5|maximum modulus principle]]: a local maximum of $\abs f$ at $z_0$ makes $\abs f$ equal to $\abs{f(z_0)}$ on every small circle about $z_0$, because the average of a function bounded above by its maximum equals the maximum only when the function is constant there.
The same argument, with the mean value property of a real harmonic function $u$ in place of that of $f$, gives the strict maximum principle for $u$ ([[PR-6WOTK]]).

:::

## Problems

[[E-RLHXB]] [[E-VGNUI]] [[E-3B2YA]]
[[P-AZOFF-D03]] [[P-UGA8150S21-HW3-04]]
