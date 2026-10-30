---
title: The argument principle
order: 10
topics:
- Argument Principle
- Winding Number
---

# The argument principle

## The logarithmic derivative

[[D-IA5FS]]

::: {.fact}
Every zero of a meromorphic $f$ is a simple pole of $\logd f$ whose residue is its multiplicity.

:::

::: {.remark}
For a nonzero rational function $f\in\CC(x)$ and $p\in\CC$, the residue of the logarithmic derivative at $p$ is the valuation $v_p(f)$ of $f$ at the prime ideal $\generators{x-p} \subseteq \CC[x]$:
$$
d \qty{ \log(f) } = {f'\over f}\dz \implies \Res_{z=p}(d \log(f) ) = v_p(f)
.$$

:::

## The statement

[[D-PJ7JM]]

[[T-JXDQT]]

## The index version

[[T-52HK6]]

::: {.example title="Using the index version"}
Let $f(z) = z^2 + z = z(z+1)$.

- $\gamma_1 \coloneqq \theset{\abs z = 2}$ encloses 2 zeros and no poles, so $f\circ \gamma_1$ winds twice about the origin counterclockwise.
- $\gamma_2 \coloneqq \theset{\abs z = {1\over 2}}$ encloses 1 zero and no poles, so $f\circ \gamma_2$ winds once.

:::

::: {.remark title="Tracking the argument by hand"}
The winding number is the total change of a continuous branch of $\arg$ along the image curve, divided by $2\pi$, and it is additive over sub-curves.
For a curve in $\HH$ from a point of $(0,\infty)$ to a point of $(-\infty,0)$, a continuous branch of $\arg$ with values in $[0,\pi]$ changes by $\pi$.

![An image curve f(gamma(t)) in the upper half-plane runs from f(gamma(a)) on the positive real axis to f(gamma(b)) on the negative real axis, looping as it goes; arg f(gamma(t)) is the angle of the segment from 0 to the current point.](../../../../assets/assets/figures/2021-12-10_18-06-04.png)

:::

## Counting solutions of $f(z) = w$

::: {.remark}
The integral
$$
F(w) \coloneqq {1\over 2\pi i} \oint_{\bd \Omega} {f'(z) \over f(z) - w} \dz
$$
is $\frac{1}{2\pi i}\oint_{\bd\Omega} \logd g_w(z)\dz$ for $g_w(z) \coloneqq f(z) - w$, so for holomorphic $f$ it counts the solutions of $f(z) = w$ in $\Omega$ with multiplicity.
It is a continuous function of $w$ on each connected component of $\CC\sm f(\bd\Omega)$ and takes values in $\ZZ$, hence is constant on each component.

A solution of $f(z) = a$ of multiplicity $m \geq 2$ is a zero of $f'$.

:::

## Exercises

[[E-PWVJS]]
[[E-UVNVV]]
