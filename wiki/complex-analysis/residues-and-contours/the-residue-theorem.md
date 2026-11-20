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
\int_\gamma z^k \dz = \int_0^{2\pi} e^{ik\theta} ie^{i\theta} \dtheta = i\int_0^{2\pi} e^{i(k+1)\theta} \dtheta
=
\begin{cases}
2\pi i & k=-1
\\
0 & \text{else}.
\end{cases}
$$

:::

For a Laurent series with finitely many negative terms converging on a neighborhood of $S^1$, the convergence is uniform on $S^1$, so term-by-term integration keeps only the coefficient of $\inverseof{z}$:
$$
\int_\gamma \sum_{k \geq -M} c_k z^k = \sum_{k \geq -M} \int_\gamma c_k z^k = 2\pi i c_{-1}
.$$

The uniform convergence on the compact circle is [@Ahl73, ch. 5, §1.1, Weierstrass's Theorem], which states that a series of analytic functions converging uniformly on every compact subset of a region has an analytic sum and may be differentiated term by term; the same uniform convergence justifies integrating term by term, and each integral in the display is the computation of the block above.

The coefficient $c_{-1}$ of the Laurent series at a singularity is the [[D-C3JIU|residue]], and the residue theorem sums these contributions over the singularities enclosed by a curve, weighted by [[D-PJ7JM|winding numbers]].
Write $\Res_{z=p}f$ for $\Res_{z=p}(f\dz)$.

[[T-HRPNO]]

::: {.example title="A closed integral computed by residues"}
On the circle $\abs z = 3$ the integrand
$$
f(z) = {z^2+1\over z(z-1)(z+2)}
$$
has all three of its poles inside, with residues
$$
\Res_{z=0}f = {1\over (0-1)(0+2)} = -\frac12,\qquad
\Res_{z=1}f = {2\over 1\cdot 3} = \frac23,\qquad
\Res_{z=-2}f = {5\over (-2)(-3)} = \frac56,
$$
whose sum is $1$, so the integral is $2\pi i$, which is also what the parametrization returns.
The circle $\abs z = 2$ would not do: it passes through the pole at $z = -2$.
:::

::: {.remark title="Residues of $1$-forms"}
The residue is an invariant of the $1$-form $f\dz$ rather than of the function $f$: if $z = \varphi(w)$ with $\varphi$ biholomorphic near $w_0$ and $\varphi(w_0)=p$, then $\Res_{w=w_0} f(\varphi(w))\varphi'(w) = \Res_{z=p} f(z)$, while $\Res_{w=w_0} f(\varphi(w))$ is in general different.

:::

Real integrals are evaluated by writing them as limits of closed contour integrals; the contours are on [[complex-analysis/residues-and-contours/which-contour-do-i-close|Which contour do I close?]].
