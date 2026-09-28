---
title: Is it holomorphic?
order: 0
topics:
- Holomorphic Functions
---

# Is it holomorphic?

Four tests establish holomorphy, and each applies to a different form of input.
When the function is not holomorphic, the answer is an obstruction rather than a computation.

## Given $u$ and $v$ explicitly

**Cauchy–Riemann equations.**
Write $f(x+iy) = u(x,y) + iv(x,y)$ and check $u_x = v_y$ and $u_y = -v_x$.

The equations at a point do not imply complex differentiability there; the equations on an open set together with continuous partial derivatives imply holomorphy on that set.
In polar coordinates the equations read $u_r = \frac1r v_\theta$ and $v_r = -\frac1r u_\theta$.

Equivalently, $f$ is holomorphic exactly when $\delbar f = 0$, the Cauchy–Riemann equations written as one equation.
See [[complex-analysis/holomorphic-functions/the-cauchy-riemann-equations|The Cauchy–Riemann equations]].

## Given a power series

**Radius of convergence.**
A power series is holomorphic on the open disc of convergence, and every holomorphic function is locally given by such a series.
See [[complex-analysis/holomorphic-functions/power-series|Power series]].

## Given a limit or an integral

**Morera's theorem.**
If $f$ is continuous and $\int_{\bd T} f = 0$ for every triangle $T$, then $f$ is holomorphic.
This applies to functions without a formula to differentiate: a locally uniform limit of holomorphic functions, a series of them, or an integral depending holomorphically on a parameter.
See [[complex-analysis/cauchy-theory/morera-and-converses|Morera and converses]].

## Given a formula built from holomorphic functions

Sums, products, quotients with nonvanishing denominators, and compositions of holomorphic functions are holomorphic, and $e^z$, $\sin z$, $\cos z$, and polynomials are entire.

## Obstructions to holomorphy

::: {.example title="Holomorphic and not"}
\envlist

- $f(z) \coloneqq \abs z$ is not holomorphic.
- $f(z) \coloneqq \arg z$ is not holomorphic.
- $f(z) \coloneqq \Re z$ is not holomorphic.
- $f(z) \coloneqq \Im z$ is not holomorphic.
- $f(z) = 1/z$ is holomorphic on $\CC\smz$, and not on $\CC$.
- $f(z) = \bar z$ is real differentiable but not holomorphic:
$$
{f(z_0 + h) - f(z_0) \over h } = {\bar h \over h} = {re^{-i\theta} \over re^{i\theta}} = e^{-2i\theta},
$$
which depends on the direction $\theta$ of approach, so the limit as $h\to 0$ does not exist.

:::

The failure of holomorphy takes one of three forms.

- **Direction dependence.** The difference quotient has different limits along different rays, as for $\bar z$.
  A nonconstant real-valued function of $z$, such as $\Re z$, $\Im z$, $\abs z$, or $\arg z$, fails in this way.

- **A branch point.** $\sqrt z$ and $\log z$ have no continuous branch on any punctured neighborhood of $0$, so the obstruction is topological rather than pointwise.

::: {.example title="The square root has no holomorphic branch on the circle"}
With the branch $(e^{i\theta})^{1/2} = e^{i\theta/2}$ for $0\le\theta\le 2\pi$,
$$
\begin{aligned}
\int_{S^1} z^{1/2} \dz
&= \int_0^{2\pi} e^{i\theta/2}\, ie^{i\theta} \dtheta \\
&= i \int_0^{2\pi} e^{3i\theta/2}\dtheta \\
&= i \qty{2\over 3i} e^{3i\theta/2}\evalfrom_{0}^{2\pi} \\
&= -{4\over 3}.
\end{aligned}
$$
With the branch $e^{i\theta/2}$ for $-\pi\le\theta\le\pi$,
$$
\int_{-\pi}^{\pi} e^{i\theta/2}\, ie^{i\theta} \dtheta = {2\over 3}\qty{ e^{3\pi i/2} - e^{-3\pi i/2}} = -{4i\over 3}.
$$
Each branch is discontinuous at one point of $S^1$, and the two integrals differ.
If $g$ were a holomorphic branch of $z^{1/2}$ on a neighborhood of $S^1$, then $g' = g/(2z)$, so $h(z)\coloneqq \frac23 z\,g(z)$ would satisfy $h' = g$, and the integral of $g$ over the closed curve $S^1$ would vanish.

:::

- **The domain.** $1/z$ is holomorphic on every open set not containing $0$, so holomorphy is a statement about a function on a specified open set.

## Warnings

::: {.warnings}
$\sin z$ and $\cos z$ are unbounded on $\CC$: they are nonconstant and entire, so this follows from Liouville's theorem.
For $y\in\RR$, $\abs{\sin(iy)} = \abs{\sinh y}$.

:::

::: {.warnings}
A map whose real Jacobian is invertible at every point need not be holomorphic: $f(z) = \bar z$ has Jacobian $\operatorname{diag}(1,-1)$ and fails the Cauchy–Riemann equations.
Conversely, a holomorphic $f$ with $f'(z_0)\neq 0$ is conformal at $z_0$.

:::
