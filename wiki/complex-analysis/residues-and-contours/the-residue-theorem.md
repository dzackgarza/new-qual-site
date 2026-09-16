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

For a Laurent series with finitely many negative terms converging on a neighborhood of $S^1$, the convergence is uniform on $S^1$, so term-by-term integration keeps only the coefficient of $z\inv$:
$$
\int_\gamma \sum_{k \geq -M} c_k z^k = \sum_{k \geq -M} \int_\gamma c_k z^k = 2\pi i c_{-1}
.$$

The coefficient $c_{-1}$ of the Laurent series at a singularity is its residue, and the residue theorem sums these contributions over the singularities enclosed by a curve, weighted by winding numbers.

[[T-HRPNO]]

::: {.remark title="Residues of $1$-forms"}
The residue is an invariant of the $1$-form $f\dz$ rather than of the function $f$: if $z = \varphi(w)$ with $\varphi$ biholomorphic near $w_0$ and $\varphi(w_0)=p$, then $\Res_{w=w_0} f(\varphi(w))\varphi'(w) = \Res_{z=p} f(z)$, while $\Res_{w=w_0} f(\varphi(w))$ is in general different.
The notation $\Res_{z=p}(f)$ abbreviates $\Res_{z=p}(f\dz)$.

:::

Real integrals are evaluated by writing them as limits of closed contour integrals; the contours are on [[complex-analysis/residues-and-contours/which-contour-do-i-close|Which contour do I close?]].
