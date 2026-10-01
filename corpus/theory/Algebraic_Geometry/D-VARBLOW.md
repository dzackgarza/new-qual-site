---
schema: qual/card@1
id: D-VARBLOW
kind: definition
title: The blowup of a variety at a point
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Exceptional Divisors
  - Birational Geometry
relations:
- kind: related-to
  target: D-0SYCY
review: draft
prompts:
- What is a blowup?
- What is the exceptional divisor, and what is a proper transform?
---

::: {.definition title="Blowup"}
The blowup of $\AA^n$ at the origin is
$$
\Bl_0 \AA^n \da \ts{ (x, \ell) \in \AA^n \times \PP^{n-1} \st x \in \ell } ,
$$
with $\pi$ the first projection.
For a variety $X$ and a closed point $p\in X$ with ideal sheaf $\mci_p$, the intrinsic definition is
$$
\Bl_pX
\coloneqq
\Proj_X\bigoplus_{d\ge0}\mci_p^d,
$$
as in [[D-SCHBLOWUP]].
The \dfn{exceptional divisor} is $E\da\pi^{-1}(p)$, and its fibre over $p$ is
$$
E
\cong
\Proj\operatorname{gr}_{\mfm_p}\OO_{X,p},
$$
the projectivized tangent cone.
The **proper transform** of a subvariety $C\subseteq X$ is the closure of $\pi^{-1}(C\sm\ts{p})$.
:::

::: {.proposition}
$\pi$ is an isomorphism away from $E$, hence birational, and $\Bl_p X$ is again a variety, projective over $X$.
If $X$ is smooth of dimension $n$ at $p$, then
$$
E\cong\PP^{n-1}_{\kappa(p)},
$$
the projective space of one-dimensional quotients of the tangent space at $p$.
In particular, for a smooth surface $E\cong\PP^1$.
:::

::: {.remark}
Geometrically, the blowup replaces $p$ by the set of directions through $p$, which separates branches of a curve with distinct tangent directions.
The nodal cubic $y^2 = x^2(x+1)$ becomes smooth after one blowup because its two branches acquire different tangent directions, while the cuspidal cubic $y^2 = x^3$ requires further resolution.

The scheme-theoretic definition $\Bl_Z X = \Proj \bigoplus_{d \geq 0} \mci_Z^d$ also applies to non-reduced centers and makes the exceptional divisor Cartier by construction.
:::
