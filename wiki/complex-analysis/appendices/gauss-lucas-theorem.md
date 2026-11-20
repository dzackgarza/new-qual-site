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

Both are instances of [[T-C7GBB]]: the zeros of $f'$ lie in the hull of the zeros of $f$, in the first case at the single hull point and in the second at an interior one.
:::

::: {.corollary}
If all zeros of a nonconstant polynomial $f$ lie in a closed half-plane $H$, then all zeros of $f^{(k)}$ lie in $H$ for every $k$ such that $f^{(k)}$ is nonconstant.

This is the half-plane form of [[T-C7GBB]], iterated: the proof is below.
:::

::: {.example title="One zero of $f''$ from three on a line"}
For $f(z) = (z-1)(z-2)(z-3) = z^3-6z^2+11z-6$ the zeros lie on the line $\RR$, and $f''(z) = 6z-12$ vanishes only at $z=2$, which is the midpoint of $1$ and $3$ and lies in the hull $[1,3]$ of the zeros.
The corollary with the half-plane $H = \theset{z : \Im z\geq0}$ gives the same thing, and the same argument applies to every $f^{(k)}$ that is nonconstant.

This is the half-plane consequence of [[T-C7GBB]] stated above, at $k=2$: its hypothesis holds for $f$ since the zeros $1,2,3$ lie on $\RR\subseteq H$, so $f''$ has its zero at $2$ in $H$, as computed.
:::

::: {.proof}
$H$ is convex, so it contains the convex hull of the zeros of $f$, and the [[T-C7GBB|Gauss--Lucas theorem]] gives the case $k=1$; induct on $k$.
:::
