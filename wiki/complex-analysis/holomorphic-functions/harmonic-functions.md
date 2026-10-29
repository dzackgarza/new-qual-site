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

The real and imaginary parts of a holomorphic function are harmonic, and a harmonic function equals its average over every circle and disc in its domain.

[[D-CFBSA]]

[[PR-JKE6C]]

[[E-TZJKN]]

## The mean value property

[[PR-UWGI6]]

::: {.proof}
Define
$$
F(r) \coloneqq {1\over 2\pi r} \oint_{\bd \DD_r(z_0)} u\,ds = {1\over 2\pi} \int_{[-\pi, \pi]} u(z_0 + re^{it} ) \dt
,$$
and differentiate:
$$
\begin{aligned}
F'(r)
&= {1\over 2 \pi} \int_{[-\pi, \pi]} \cos(t) u_x(z_0 +re^{it} ) + \sin(t) u_y(z_0 + re^{it}) \dt \\
&= {1\over 2\pi r} \oint_{\bd \DD_r(z_0)}\qty{x-x_0\over r} u_x(x, y) + \qty{y-y_0\over r}u_y(x, y) \,ds \\
&= {1\over 2\pi r} \oint_{\bd \DD_r(z_0)} \dd{u}{n} \,ds \qquad n = \thevector{{x-x_0\over r}, {y-y_0\over r}} \\
&= {1\over 2\pi r} \iint_{\DD_r(z_0)} \laplacian u \dx \dy \\
&= 0
\end{aligned},$$
where $n$ is the outward unit normal, using Green's theorem and $\laplacian u = 0$.
So $F$ is constant, and letting $r\to 0$,
$$
F(r) = {1\over 2\pi} \int_{[-\pi, \pi]} u(z_0 + re^{it}) \dt \too u(z_0)
.$$
Multiplying $u(z_0) = F(s)$ by $s$ and integrating over $0\leq s\leq r$ gives $\frac{r^2}{2}u(z_0) = \frac{1}{2\pi}\iint_{\DD_r(z_0)} u \dx\dy$ in polar coordinates, which is the area mean.

:::

::: {.remark title="Converse"}
A continuous $u$ satisfying the mean value property on every disc in its domain is harmonic, so the mean value property characterizes harmonic functions among continuous functions.
The mean value property gives the [[PR-6WOTK|strict maximum principle]]: a real harmonic function on a connected open set that attains its maximum is constant, by the argument on [[complex-analysis/cauchy-theory/maximum-modulus-and-open-mapping|Maximum modulus and open mapping]].

:::

## Exercises

[[E-P2PEF]]
[[P-JHUFA11ANB]]
[[E-BEYZ5]]
[[E-B4ZSQ]]
