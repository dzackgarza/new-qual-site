---
schema: qual/card@1
id: D-2HXLN
kind: definition
title: Hyperbolic metric on the disc
prompts:
- What is the hyperbolic length of a curve in the unit disc?
- What is the hyperbolic distance on the disc?
classification:
  areas:
  - complex-analysis
  topics:
  - Hyperbolic Metric
  - Hyperbolic Geometry
relations: []
review: draft
---

::: {.definition}
For a piecewise $C^1$ curve $\gamma\colon[a,b]\to\DD$ its \dfn{hyperbolic length} is
$$
\length_{\DD}(\gamma)\coloneqq\int_\gamma\frac{\abs{\dz}}{1-\abs z^2}=\int_a^b\frac{\abs{\gamma'(t)}}{1-\abs{\gamma(t)}^2}\dt,
$$
and the \dfn{hyperbolic distance} between $z,w\in\DD$ is
$$
d_{\DD}(z,w)\coloneqq\inf_\gamma\length_{\DD}(\gamma),
$$
the infimum over piecewise $C^1$ curves in $\DD$ from $z$ to $w$.
The \dfn{hyperbolic metric} is the family $\rho_{\DD}(z)\abs{\dz}$ with $\rho_{\DD}(z) = (1-\abs z^2)^{-1}$.
:::

::: {.remark}
The geodesics are the circle arcs and diameters meeting $\bd\DD$ orthogonally, and the hyperbolic distance is realised by exactly one such arc through two distinct points (C. McMullen, *Advanced Complex Analysis*, §2, the paragraph "Geodesics" following Theorem 2.21).
It is invariant under the automorphisms of $\DD$: the [[D-MFPYG|Blaschke factors]] satisfy $\abs{\psi_a'(z)}/(1-\abs{\psi_a(z)}^2) = (1-\abs z^2)^{-1}$, and the invariance under every automorphism is [@SS03, ch. 8, Problem 3(b)], where this distance and the metric $\abs{\dz}^2/(1-\abs z^2)^2$ are defined.
Parts (c) and (d) of that problem give $d_{\DD}(0,s) = \frac12\log\frac{1+s}{1-s}$ for $s\in[0,1)$, and part (e) the formula for two arbitrary points, which tends to $\infty$ as $s\to1$, so the metric is complete.
:::
