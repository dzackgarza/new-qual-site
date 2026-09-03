---
title: Is it holomorphic?
order: 0
topics:
- Holomorphic Functions
---

# Is it holomorphic?

Four ways to answer, and they are not interchangeable: each one is cheap on a different kind of input.
There is also a fifth answer, which is that the function is not holomorphic, and then the problem wants the obstruction rather than a computation.

## You are given $u$ and $v$ explicitly

**Check the Cauchy–Riemann equations.**
Write $f(x+iy) = u(x,y) + iv(x,y)$ and check $u_x = v_y$ and $u_y = -v_x$.

The equations alone are not sufficient, and problems exploit this: CR plus *continuous* partials gives holomorphy, and CR at a single point does not.
In polar form the same test reads $u_r = \frac1r v_\theta$ and $v_r = -\frac1r u_\theta$, which is the version to use on anything written with $r$ and $\theta$.

The one-line version is the $\delbar$ test: $f$ is holomorphic exactly when $\delbar f = 0$, which is the Cauchy–Riemann equations packaged as a single equation.
See [[complex-analysis/holomorphic-functions/the-cauchy-riemann-equations|The Cauchy–Riemann equations]].

## You are given a series

**Check the radius of convergence.**
A convergent power series is holomorphic on the open disc of convergence, and holomorphic functions are exactly the ones locally given by such series.
Nothing else needs checking, which makes this the cheapest test when it applies.
See [[complex-analysis/holomorphic-functions/power-series|Power series]].

## You are given a limit or an integral

**Use Morera.**
If $f$ is continuous and $\int_{\bd T} f = 0$ for every triangle, then $f$ is holomorphic.
This is the test for a function you cannot differentiate directly: a locally uniform limit of holomorphic functions, a series of them, or a function defined by an integral depending on a parameter.
See [[complex-analysis/cauchy-theory/morera-and-converses|Morera and converses]].

## You are given a formula built from holomorphic pieces

Sums, products, quotients with nonvanishing denominators, and compositions of holomorphic functions are holomorphic, and $e^z$, $\sin z$, $\cos z$ and polynomials are entire.
Most of the time this settles the question in one line, and the interesting part of the problem is elsewhere.

## It is not holomorphic

Then say why.
The standard obstructions, and the standard examples:

:::{.example title="Holomorphic and not"}
\envlist

- $f(z) \da \abs z$ is not holomorphic.
- $f(z) \da \arg z$ is not holomorphic.
- $f(z) \da \Re z$ is not holomorphic.
- $f(z) \da \Im z$ is not holomorphic.
- $f(z) = 1/z$ is holomorphic on $\CC\smz$, and not on $\CC$.
- $f(z) = \bar z$ is not holomorphic although it is real differentiable:
\[
{f(z_0 + h) - f(z_0) \over h } = {\bar h \over h} = {re^{-i\theta} \over re^{i\theta}} = e^{-2i\theta} \converges{h\to 0}\too e^{-2i\theta}
,\]
which depends on the direction $\theta$ of approach, so the limit does not exist.

:::

Three obstructions worth naming, because a problem usually wants one of them:

- **Direction dependence.** The difference quotient has different limits along different rays, as for $\bar z$.
  Any function of $\Re z$, $\Im z$, $\abs z$ or $\arg z$ alone fails here.

- **A branch point.** $\sqrt z$ and $\log z$ have no holomorphic branch on a punctured neighborhood of $0$, so the obstruction is topological rather than pointwise.
  It shows up as a nonzero integral around a loop:

:::{.example title="Square root is not holomorphic"}
Integrating over $S^1$ gives a nonzero answer:
\[
\int_{S^1} z^{1/2} \dz
&= \int_0^{2\pi} (e^{i\theta})^{1/2} ie^{i\theta} \dtheta \\
&= i \int_0^{2\pi} e^{i3\theta \over 2}\dtheta \\
&= i \qty{2\over 3i} e^{i3\theta \over 2}\evalfrom_{0}^{2\pi} \\
&= -{4\over 3}
.\]
A different parameterization gives a different nonzero number,
\[
\int_{-\pi}^{\pi} (e^{i\theta})^{1/2} ie^{i\theta} \dtheta = {2\over 3}\qty{ e^{3\pi i \over 2} - e^{-3\pi i \over 2}} = -{4i\over 3}
,\]
which is the point: these paths do not lift to closed loops on the Riemann surface of $z\mapsto z^2$.

:::

- **The domain.** $1/z$ is holomorphic on any domain missing the origin, so "is it holomorphic" is only a question once the domain is fixed.
  A problem that does not name a domain is usually asking you to find the largest one.

## Two warnings

:::{.warnings}
$\sin z$ and $\cos z$ are **unbounded** on $\CC$.
They are nonconstant and entire, so Liouville forces it.
Real intuition is the source of more errors here than anything else in the subject.

:::

:::{.warnings}
A nonvanishing derivative does not imply holomorphy: $f(z) = \bar z$ has one, and fails the Cauchy–Riemann equations.
The implication runs the other way, holomorphic with $f'\neq 0$ implies conformal.

:::
