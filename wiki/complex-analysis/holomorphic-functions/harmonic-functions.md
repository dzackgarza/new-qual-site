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

[[PR-K57J6]]

::: {.proof}
\envlist

- By the Cauchy–Riemann equations,
$$
\begin{aligned}
u_x = v_y && u_y = -v_x
\end{aligned}.$$

- Differentiate in $x$:
$$
\begin{aligned}
u_{xx} = v_{yx} && u_{yx} = -v_{xx}
\end{aligned}.$$
- Differentiate in $y$:
$$
\begin{aligned}
u_{xy} = v_{yy} && u_{yy} = -v_{xy}
\end{aligned}.$$
- A holomorphic function is analytic, so $u$ and $v$ are $C^\infty$, and by Clairaut's theorem the mixed partials agree. Hence
$$
u_{xx} + u_{yy} = 0, \qquad v_{xx} + v_{yy} = 0
.$$

:::

## The mean value property

[[PR-UWGI6]]

::: {.proof}
Define
$$
F(r) \coloneqq {1\over 2\pi r} \oint_{\bd \DD_r(z_0)} u\ds = {1\over 2\pi} \int_{[-\pi, \pi]} u(z_0 + re^{it} ) \dt
,$$
and differentiate:
$$
\begin{aligned}
F'(r)
&= {1\over 2 \pi} \int_{[-\pi, \pi]} \cos(t) u_x(z_0 +re^{it} ) + \sin(t) u_y(z_0 + re^{it}) \dt \\
&= {1\over 2\pi r} \oint_{\bd \DD_r(z_0)}\qty{x-x_0\over r} u_x(x, y) + \qty{y-y_0\over r}u_y(x, y) \ds \\
&= {1\over 2\pi r} \oint_{\bd \DD_r(z_0)} \dd{u}{n} \ds \qquad n = \tv{{x-x_0\over r}, {y-y_0\over r}} \\
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
The proof of the maximum principle on [[complex-analysis/cauchy-theory/maximum-modulus-and-open-mapping|Maximum modulus and open mapping]] uses only the mean value property, so it applies to harmonic functions as well.

:::

## Exercises

[[E-P2PEF]]
[[E-TZJKN]]
[[E-I6W47]]
[[E-BEYZ5]]
[[E-B4ZSQ]]
