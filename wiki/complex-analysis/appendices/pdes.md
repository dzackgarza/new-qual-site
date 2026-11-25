---
order: 111
title: The Dirichlet problem
---

# The Dirichlet problem

[[D-XR64P]]

::: {.proposition}
On a simply connected domain every real [[D-CFBSA|harmonic function]] is the real part of a [[D-E7A5W|holomorphic function]] [@Ahl73, ch. 4, §6.1], so on a bounded such domain a solution of a [[D-XR64P|Dirichlet problem]] can be sought among the functions $\Re g$ and $\Im g$ with $g$ holomorphic.
:::

::: {.example title="Dirichlet problem on a half-strip"}
On the half-strip $\theset{(x, y) \st 0 < x < \pi,\ y > 0}$, which is unbounded, so that the decay below is imposed in place of a boundary condition at infinity, consider the problem
$$
\begin{aligned}
\laplacian T &= 0, & T(0, y) &= T(\pi, y) = 0 \text{ for all } y > 0, \\
T(x, 0) &= \sin(x), & T(x, y) &\to 0 \text{ as } y\to\infty.
\end{aligned}
$$
The function
$$
T(x ,y) = e^{-y} \sin(x) = \Im\qty{e^{iz}} = \Re\qty{-ie^{iz}}, \qquad z = x+iy,
$$
is harmonic on $\RR^2$ as the imaginary part of the entire function $e^{iz}$, and it satisfies each boundary condition.
:::
