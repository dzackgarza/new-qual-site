---
title: The residue theorem
order: 10
topics:
- Residue Theorem

---

# The residue theorem

## The integral of $z^k$ over the unit circle

::: {.fact title="Integral of $z^k$ over $S^1$"}
For $k\in\ZZ$ and $\gamma(\theta) = e^{i\theta}$, $\theta\in[0,2\pi]$,
$$
\int_\gamma z^k \dz =
\begin{cases}
2\pi i & k=-1,\\
0 & \text{else}.
\end{cases}
$$
The case $k=-1$ is the index of the circle about the origin, $n(\gamma,0)=\frac{1}{2\pi i}\int_\gamma\dz/z=1$, which is [[D-PJ7JM|the winding number]], and [@Ahl73, ch. 4, §2.1, Lemma 2] computes it as $2\pi i$.
:::

::: {.example title="The computation"}
$$
\int_\gamma z^k \dz = \int_0^{2\pi} e^{ik\theta} ie^{i\theta} \dtheta = i\int_0^{2\pi} e^{i(k+1)\theta} \dtheta,
$$
which is $2\pi i$ for $k=-1$ and $0$ otherwise.
:::

[[T-HRPNO]]

::: {.example title="A closed integral computed by residues"}
On the circle $\abs z = 3$ the integrand
$$
f(z) = {z^2+1\over z(z-1)(z+2)}
$$
has all three of its [[D-AUD6K|poles]] inside, with residues
$$
\Res_{z=0}f = {1\over (0-1)(0+2)} = -\frac12,\qquad
\Res_{z=1}f = {2\over 1\cdot 3} = \frac23,\qquad
\Res_{z=-2}f = {5\over (-2)(-3)} = \frac56,
$$
whose sum is $1$, so the integral is $2\pi i$, which is also what the parametrization returns.
The circle $\abs z = 2$ would not do: it passes through the pole at $z = -2$.
:::

Real integrals are evaluated by writing them as limits of closed contour integrals; the contours are on [[complex-analysis/residues-and-contours/which-contour-do-i-close|Which contour do I close?]].
