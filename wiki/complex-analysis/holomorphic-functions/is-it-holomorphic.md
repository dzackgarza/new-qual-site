---
title: Is it holomorphic?
order: 0
topics:
- Holomorphic Functions
---

# Is it holomorphic?

The test depends on how the function is given: by its real and imaginary parts, by a series, by a limit or an integral, or by a formula.

## Given $u$ and $v$ explicitly

Write $f(x+iy) = u(x,y)+iv(x,y)$ and check $u_x = v_y$ and $u_y = -v_x$.
If $u$ and $v$ are continuously differentiable on an open set and satisfy the equations there, then $f$ is [[D-E7A5W|holomorphic]] on that set and $f' = u_x+iv_x$ ([[PR-JKE6C]]); conversely a complex differentiable $f$ satisfies them ([[PR-37QA5]]).
In polar coordinates the equations read $u_r = \frac1r v_\theta$ and $v_r = -\frac1r u_\theta$.

At a single point the equations are weaker than complex differentiability: $f(x+iy)\coloneqq\sqrt{\abs{xy}}$ satisfies them at $0$, and along $y=x$ its difference quotient at $0$ is $\abs x/\bigl((1+i)x\bigr)$, which has no limit as $x\to 0$.
For a real differentiable $f$ the pair of equations is the single equation $\delbar f = 0$ ([[PR-TVPCM]], [[D-OAFF5|Wirtinger operators]]).
The equations and their consequences are on [[complex-analysis/holomorphic-functions/the-cauchy-riemann-equations|The Cauchy--Riemann equations]].

## Given a power series

A power series is holomorphic on the open disc of convergence, and every holomorphic function is locally the sum of such a series ([[T-GROTS]]).
See [[complex-analysis/holomorphic-functions/power-series|Power series]].

## Given a limit or an integral

[[T-LHSMY|Morera's theorem]]: a continuous $f$ whose integral over every triangle in an open set vanishes is holomorphic there.
It applies to functions with no formula to differentiate: a locally uniform limit of holomorphic functions ([[C-TODSQ]]), a series of them, or an integral depending holomorphically on a parameter.
See [[complex-analysis/cauchy-theory/morera-and-converses|Morera and converses]].

## Given a formula built from holomorphic functions

Sums, products, quotients with nonvanishing denominators, and compositions of holomorphic functions are holomorphic, and $e^z$, $\sin z$, $\cos z$, and the polynomials are entire [@SS03, ch. 1].

## Obstructions to holomorphy

::: {.example title="A real-valued function of $z$"}
The functions $\Re z$, $\Im z$, $\abs z$, and $\arg z$ are not holomorphic on any open set.
For a nonconstant real-valued $u$ the Cauchy--Riemann equations would force $u_x = u_y = 0$, and a continuously differentiable $u$ with vanishing gradient on a domain is constant.
:::

::: {.example title="Direction dependence"}
For $f(z) = \bar z$ the difference quotient is
$$
{f(z_0+h) - f(z_0)\over h} = {\bar h\over h} = {re^{-i\theta}\over re^{i\theta}} = e^{-2i\theta},
$$
which depends on the direction $\theta$ of approach, so the limit as $h\to 0$ does not exist, although $\bar z$ is real differentiable everywhere.
:::

::: {.example title="A branch point"}
The functions $\sqrt z$ and $\Log z$ have no continuous branch on any punctured neighborhood of $0$, so the obstruction is topological rather than pointwise.
:::

::: {.example title="The square root has no holomorphic branch on the circle"}
With the branch $(e^{i\theta})^{1/2} = e^{i\theta/2}$ for $0\leq\theta\leq 2\pi$,
$$
\begin{aligned}
\int_{S^1} z^{1/2}\dz
&= \int_0^{2\pi} e^{i\theta/2}\, ie^{i\theta}\dtheta \\
&= i\int_0^{2\pi} e^{3i\theta/2}\dtheta \\
&= i\qty{2\over 3i} e^{3i\theta/2}\evalfrom_{0}^{2\pi} \\
&= -{4\over 3}.
\end{aligned}
$$
With the branch $e^{i\theta/2}$ for $-\pi\leq\theta\leq\pi$,
$$
\int_{-\pi}^{\pi} e^{i\theta/2}\, ie^{i\theta}\dtheta = {2\over 3}\qty{e^{3\pi i/2} - e^{-3\pi i/2}} = -{4i\over 3}.
$$
Each branch is discontinuous at one point of $S^1$, and the two integrals differ.
If $g$ were a holomorphic branch of $z^{1/2}$ on a neighborhood of $S^1$, then $g' = g/(2z)$, so $h(z)\coloneqq\frac23 z\,g(z)$ would satisfy $h' = g$, and the integral of $g$ over the closed curve $S^1$ would vanish.
:::

::: {.example title="The domain matters"}
The function $1/z$ is holomorphic on every open set that does not contain $0$, and on no open set that does, so holomorphy is a statement about a function on a specified open set.
:::

## Warnings

::: {.warnings}
$\sin z$ and $\cos z$ are unbounded on $\CC$: they are nonconstant and entire, so this follows from [[T-QHIHJ|Liouville's theorem]].
For $y\in\RR$, $\abs{\sin(iy)} = \abs{\sinh y}$.
:::

::: {.warnings}
A map whose real Jacobian is invertible at every point need not be holomorphic: $f(z) = \bar z$ has Jacobian $\operatorname{diag}(1,-1)$ and fails the Cauchy--Riemann equations.
Conversely, a holomorphic $f$ with $f'(z_0)\neq 0$ is [[D-TM4TE|conformal]] at $z_0$.
:::
