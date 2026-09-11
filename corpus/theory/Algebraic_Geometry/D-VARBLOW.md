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
\[
\Bl_0 \AA^n \da \ts{ (x, \ell) \in \AA^n \times \PP^{n-1} \st x \in \ell } ,
\]
with $\pi$ the first projection.
For $X$ a variety and $p \in X$, $\Bl_p X$ is the closure of $\pi\inv(X \sm \ts{p})$ inside $\Bl_p \AA^n$ for a local embedding.
The **exceptional divisor** is $E \da \pi\inv(p) \cong \PP^{n-1}$, and the **proper transform** of a subvariety $C \subseteq X$ is the closure of $\pi\inv(C \sm \ts{p})$.
:::

::: {.proposition}
$\pi$ is an isomorphism away from $E$, hence birational, and $\Bl_p X$ is again a variety, projective over $X$.
For a surface, $E$ is a curve isomorphic to $\PP^1$, and the points of $E$ are the tangent directions at $p$.
:::

::: {.remark}
The description to give first is the moduli one: the blowup replaces $p$ by the set of directions through $p$, which is exactly what separates two branches of a curve that cross at $p$.
The nodal cubic $y^2 = x^2(x+1)$ becomes smooth after one blowup because its two branches acquire different tangent directions; the cuspidal cubic $y^2 = x^3$ needs more than one, which is the standard follow-up question.

The scheme-theoretic definition is $\Bl_Z X = \Proj \bigoplus_{d \geq 0} \mci_Z^d$ and it is worth naming, because it is the one that makes sense for a non-reduced centre and shows that $E$ is a Cartier divisor by construction.
:::
