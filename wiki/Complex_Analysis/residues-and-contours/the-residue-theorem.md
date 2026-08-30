---
title: The residue theorem
order: 10
problems:
  topics:
  - Residue Theorem
  - Residue Formula
---

# The residue theorem

## The one integral everything reduces to

Every residue statement descends from a single computation on the circle.

:::{.fact title="Integrating $z^k$ around $S^1$ powers residues"}
\[
\int_\gamma z^k \dz = \int_0^{2\pi} e^{ik\theta} ie^{i\theta} \dtheta = i\int_0^{2\pi} e^{i(k+1)\theta} \dtheta
=
\begin{cases}
2\pi i & k=-1
\\
0 & \text{else}.
\end{cases}
\]

:::

Every power except $z\inv$ integrates to zero, so integrating a Laurent series term by term keeps exactly one coefficient:
\[
\int_\gamma \sum_{k \geq -M} c_k z^k = \sum_{k \geq -M} \int_\gamma c_k z^k = 2\pi i c_{-1}
.\]

That coefficient is the definition of the residue, and the theorem is the statement that this survives being summed over the singularities a curve encloses.

[[T-HRPNO]]

## What the residue is an invariant of

:::{.warnings}
A pedantic warning: $\Res_{z=p}(f)$ should really be $\Res_{z=p}(f\dz)$, since it is an invariant of the $1\dash$form and not of $f$ itself.
We freely abuse notation.

:::

## Where the theorem is used

The residue theorem converts a closed contour integral into a finite sum.
Turning a *real* integral into a closed contour integral is the other half, and which curve to close is decided on [[Complex_Analysis/residues-and-contours/which-contour-do-i-close|Which contour do I close?]].
