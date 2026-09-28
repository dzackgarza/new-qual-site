---
order: 101
---

# Gauss--Lucas theorem

[[T-C7GBB]]

::: {.theorem title="Gauss--Lucas"}
If $f$ is a nonconstant polynomial with zeros $a_1, \ldots, a_n$, listed with multiplicity, then every zero of $f'$ lies in the convex hull $\operatorname{conv}\ts{a_1, \ldots, a_n}$.
:::

::: {.proof}
Let $f'(w) = 0$ and suppose $w \notin \operatorname{conv}\ts{a_1, \ldots, a_n}$; in particular $f(w)\neq 0$.
A point outside a compact convex set is strictly separated from it by a line, so after a rotation $z\mapsto e^{i\phi}z$ of the plane, which changes neither the hypotheses nor the conclusion, $\Re(a_k) < \Re(w)$ for every $k$.
Writing $f(z) = c\prod_{k=1}^n (z-a_k)$,
$$
\frac{f'(w)}{f(w)} = \sum_{k=1}^n \frac{1}{w - a_k},
$$
and $\Re\qty{\frac{1}{w-a_k}} = \frac{\Re(w-a_k)}{\abs{w-a_k}^2} > 0$ for each $k$.
So $\Re\qty{f'(w)/f(w)} > 0$, contradicting $f'(w) = 0$.
:::

::: {.example}
The zeros of $f'$ can lie on the boundary of the convex hull or in its interior.
For $f(z) = z^n$ the hull is $\ts{0}$, and $f'(z) = nz^{n-1}$ vanishes only at $0$.
For $f(z) = z^3 - 1$ the hull is the triangle whose vertices are the cube roots of unity, and $f'(z) = 3z^2$ vanishes only at the interior point $0$.
:::

::: {.corollary}
If all zeros of a nonconstant polynomial $f$ lie in a closed half-plane $H$, then all zeros of $f^{(k)}$ lie in $H$ for every $k$ such that $f^{(k)}$ is nonconstant.
:::

::: {.proof}
$H$ is convex, so it contains the convex hull of the zeros of $f$, and the theorem gives the case $k=1$; induct on $k$.
:::
