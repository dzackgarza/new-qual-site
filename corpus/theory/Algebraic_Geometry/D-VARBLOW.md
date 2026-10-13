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
\Bl_0 \AA^n \coloneqq \theset{ (x, \ell) \in \AA^n \times \PP^{n-1} \st x \in \ell } ,
$$
with $\pi$ the first projection.
For a variety $X$ and a closed point $p\in X$ with ideal sheaf $\mci_p$, the intrinsic definition is
$$
\Bl_pX
\coloneqq
\Proj_X\bigoplus_{d\ge0}\mci_p^d,
$$
as in [[D-SCHBLOWUP]].
The \dfn{exceptional divisor} is $E\coloneqq\pi^{-1}(p)$, and its fibre over $p$ is
$$
E
\cong
\Proj\operatorname{gr}_{\mfm_p}\OO_{X,p},
$$
the projectivized tangent cone.
The \dfn{proper transform} of a subvariety $C\subseteq X$ is the closure of $\pi^{-1}(C\sm\theset{p})$.
:::

::: {.proposition}
$\pi$ is an isomorphism away from $E$, hence birational, and $\Bl_p X$ is again a variety, projective over $X$.
If $X$ is smooth of dimension $n$ at $p$, then
$$
E\cong\PP^{n-1}_{\kappa(p)},
$$
the projective space of one-dimensional quotients of the tangent space at $p$.
In particular, for a smooth surface $E\cong\PP^1_{\kappa(p)}$.
:::

::: {.remark}
Since $E$ parametrizes tangent directions at $p$, the proper transforms of two smooth branches through $p$ with distinct tangent lines are disjoint over $p$.
The nodal cubic $y^2 = x^2(x+1)$ has two branches at the origin with tangent lines $y=\pm x$, and its proper transform after one blowup is smooth.
The cuspidal cubic $y^2 = x^3$ has proper transform $y_1^2 = x$ in the chart $y = xy_1$, which is smooth and tangent to $E$; two further blowups make the total transform a divisor with normal crossings.

The scheme-theoretic definition $\Bl_Z X = \Proj \bigoplus_{d \geq 0} \mci_Z^d$ also applies to non-reduced centers and makes the exceptional divisor Cartier by construction.
:::
