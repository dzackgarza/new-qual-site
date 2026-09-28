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
The \dfn{blowup} of $\AA^n$ at the origin is
$$
\Bl_0 \AA^n \da \ts{ (x, \ell) \in \AA^n \times \PP^{n-1} \st x \in \ell } ,
$$
with $\pi$ the first projection.
For $X\subseteq\AA^n$ a closed subvariety through $p=0$, $\Bl_p X$ is the closure of $\pi\inv(X \sm \ts{p})$ inside $\Bl_0 \AA^n$; for a variety $X$ and $p\in X$, it is defined through an affine neighbourhood of $p$ embedded in some $\AA^n$.
The \dfn{exceptional divisor} is $E \da \pi\inv(p)\cap\Bl_pX$, and the \dfn{proper transform} of a subvariety $C \subseteq X$ is the closure of $\pi\inv(C \sm \ts{p})$.
:::

::: {.proposition}
$\pi$ is an isomorphism away from $E$, hence birational, and $\Bl_p X$ is again a variety, projective over $X$.
The exceptional divisor $E\subseteq\PP^{n-1}$ is the projectivization of the tangent cone of $X$ at $p$.
If $p$ is a smooth point of $X$ and $\dim X=d$, then $E\cong\PP^{d-1}$ is the space of tangent directions at $p$; for $X=\AA^n$, $E\cong\PP^{n-1}$.
:::

::: {.remark}
Since $E$ parametrizes tangent directions at $p$, the proper transforms of two smooth branches through $p$ with distinct tangent lines are disjoint over $p$.
The nodal cubic $y^2 = x^2(x+1)$ has two branches at the origin with tangent lines $y=\pm x$, and its proper transform after one blowup is smooth.
The cuspidal cubic $y^2 = x^3$ has proper transform $y_1^2 = x$ in the chart $y = xy_1$, which is smooth and tangent to $E$; two further blowups make the total transform a divisor with normal crossings.

The scheme-theoretic definition $\Bl_Z X = \Proj \bigoplus_{d \geq 0} \mci_Z^d$ also applies to non-reduced centers and makes the exceptional divisor Cartier by construction.
:::
