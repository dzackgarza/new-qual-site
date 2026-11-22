---
title: Harmonic functions
order: 40
topics:
- Harmonic Functions
- Subharmonic Functions
- Mean Value Property
- Poisson Kernel
- Dirichlet Problem

---

# Harmonic functions

The real and imaginary parts of a holomorphic function are harmonic, and a harmonic function equals its average over every circle and disc whose closure lies in its domain.

[[D-CFBSA]]

[[PR-JKE6C]]

[[E-SS1.EX-11]]

## The mean value property

[[PR-UWGI6]]

[[T-HMVPC]]

[[PR-6WOTK]]

::: {.example title="The mean value property for $u = x^2-y^2$"}
$u(x,y) = x^2-y^2$ is the real part of $z^2$ and hence harmonic.
On the circle of radius $r$ about $z_0 = a+ib$,
$$
u\qty(a+r\cos\theta,\ b+r\sin\theta) = (a^2-b^2) + 2ar\cos\theta - 2br\sin\theta + r^2\cos 2\theta,
$$
whose terms in $\cos\theta$, $\sin\theta$ and $\cos 2\theta$ all average to $0$ over $[0,2\pi]$; so the circular average is $a^2-b^2 = u(z_0)$, the mean value property [@SS03, ch. 3, Corollary 7.3].
At $z_0 = 1+i$, $r = 2$ both the average and $u(z_0)$ are $0$, and at $z_0 = -2+\tfrac12 i$, $r = 3/2$ both are $3.75$; the numerical averages over the circle agree.
:::

## Exercises

[[E-P2PEF]]
[[P-JHUFA11ANB]]
[[E-BEYZ5]]
[[E-B4ZSQ]]
