---
order: 111
---

# The Dirichlet problem

[[D-XR64P]]

::: {.remark}
In a Dirichlet problem the values of the function on the boundary are prescribed; in a Neumann problem its normal derivative on the boundary is prescribed.
On a simply connected domain every real harmonic function is the real part of a holomorphic function, so solutions can be sought among the functions $\Re g$ and $\Im g$ with $g$ holomorphic.
:::

::: {.example title="Dirichlet problem on a half-strip"}
On the half-strip $\ts{(x, y) \st 0 < x < \pi,\ y > 0}$, consider the problem
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
