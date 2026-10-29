---
order: 101
title: Gauss--Lucas theorem
---

# Gauss--Lucas theorem

[[T-C7GBB]]

::: {.example}
The zeros of $f'$ can lie on the boundary of the convex hull or in its interior.
For $f(z) = z^n$ the hull is $\theset{0}$, and $f'(z) = nz^{n-1}$ vanishes only at $0$.
For $f(z) = z^3 - 1$ the hull is the triangle whose vertices are the cube roots of unity, and $f'(z) = 3z^2$ vanishes only at the interior point $0$.
:::

::: {.corollary}
If all zeros of a nonconstant polynomial $f$ lie in a closed half-plane $H$, then all zeros of $f^{(k)}$ lie in $H$ for every $k$ such that $f^{(k)}$ is nonconstant.
:::

::: {.proof}
$H$ is convex, so it contains the convex hull of the zeros of $f$, and the [[T-C7GBB|Gauss--Lucas theorem]] gives the case $k=1$; induct on $k$.
:::
