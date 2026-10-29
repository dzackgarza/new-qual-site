---
title: The integral formula
order: 20
topics:
- Cauchy Integral Formula

---

# The integral formula

The values of a holomorphic function inside a curve are determined by its values on the curve.

[[T-LA2UI]]

## The mean value property

For a circle centered at the point, the integral formula expresses $f$ at the center as the average of $f$ over the circle.

[[T-5BLYU]]

::: {.remark title="Mean value property and the maximum principle"}
If $\abs f$ has a local maximum at $z_0$, then for small $r$
$$
\abs{f(z_0)} \leq \frac{1}{2\pi}\int_0^{2\pi}\abs{f(z_0+re^{i\theta})}\dtheta \leq \abs{f(z_0)}
,$$
and since $\abs f$ is continuous, $\abs f = \abs{f(z_0)}$ on every small circle about $z_0$.
This is the argument for the [[complex-analysis/cauchy-theory/maximum-modulus-and-open-mapping|maximum modulus principle]], and the same argument, with the mean value property of a real harmonic function $u$ in place of that of $f$, proves the maximum principle for $u$.

:::

## Problems

[[E-RLHXB]] [[E-VGNUI]] [[E-3B2YA]]
[[E-5AKU5]] [[E-AZSMO]]
