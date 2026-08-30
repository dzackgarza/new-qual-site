---
title: Harmonic functions
order: 40
problems:
  topics:
  - Harmonic Functions
  - Subharmonic Functions
  - Mean Value Property
  - Mean-Value Property
  - Poisson Kernel
  - Dirichlet Problem
---

# Harmonic functions

The real and imaginary parts of a holomorphic function, characterized by the Laplacian and by an averaging property.

[[D-CFBSA]]

[[PR-JKE6C]]

[[PR-K57J6]]

:::{.proof}
\envlist

- By the Cauchy–Riemann equations,
\[
u_x = v_y && u_y = -v_x
.\]

- Differentiate in $x$:
\[
u_{xx} = v_{yx} && u_{yx} = -v_{xx}
.\]
- Differentiate in $y$:
\[
u_{xy} = v_{yy} && u_{yy} = -v_{xy}
.\]
- By Clairaut's theorem the mixed partials agree, so
\[
u_{xx} + u_{yy} = 0, \qquad v_{xx} + v_{yy} = 0
.\]

:::

## The mean value property

[[PR-UWGI6]]

:::{.proof}
Define
\[
F(r) \da {1\over 2\pi r} \oint_{\DD_r(z_0)} u\ds = {1\over 2\pi} \int_{[-\pi, \pi]} u(z_0 + re^{it} ) \dt
,\]
and differentiate:
\[
F'(r)
&= {1\over 2 \pi} \int_{[-\pi, \pi]} \cos(t) u_x(z_0 +re^{it} ) + \sin(t) u_y(z_0 + re^{it}) \dt \\
&= {1\over 2\pi r} \oint_{\bd \DD_r(z_0)}\qty{x-x_0\over r} u_x(x, y) + \qty{y-y_0\over r}u_y(x, y) \ds \\
&= {1\over 2\pi r} \oint_{\bd \DD_r(z_0)} \dd{u}{w} \ds \qquad w = \tv{{x-x_0\over r}, {y-y_0\over r}} \\
&= {1\over 2\pi r} \iint_{\DD_r(z_0)} \laplacian u \dx \dy \\
&= 0
,\]
using Green's theorem and $\laplacian u = 0$.
So $F$ is constant, and letting $r\to 0$,
\[
F(r) = {1\over 2\pi} \int_{[-\pi, \pi]} u(z_0 + re^{it}) \dt \too u(z_0)
.\]

:::

:::{.remark title="The converse, which is the useful direction"}
A continuous $u$ satisfying the mean value property on every disc is automatically harmonic.
That is what makes the property a *characterization* rather than a corollary, and it is why harmonic functions inherit the maximum principle from [[Complex_Analysis/cauchy-theory/maximum-modulus-and-open-mapping|the same argument]] that gives it for holomorphic ones: the proof there uses only the averaging identity.

:::

## Exercises

[[E-P2PEF]]
[[E-TZJKN]]
[[E-I6W47]]
[[E-BEYZ5]]
[[E-B4ZSQ]]
