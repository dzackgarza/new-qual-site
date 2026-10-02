---
schema: qual/card@1
id: T-COHRRS
kind: theorem
title: Riemann--Roch for surfaces
slogan: 'On a surface, Riemann--Roch replaces degree by $\frac12D\cdot(D-K)$; with Serre duality, positivity turns Euler characteristic into sections.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Roch
  - Surfaces
  - Intersection Theory
relations:
- kind: uses
  target: T-COHSD
- kind: uses
  target: D-COHEULER
- kind: related-to
  target: T-MWDVL
review: draft
prompts:
- State Riemann--Roch for a surface.
- How do you show a divisor on a surface is effective?
---

::: {.theorem title="Riemann--Roch for surfaces"}
Let $X$ be a smooth projective surface with canonical divisor $K$, and $D$ any divisor.
Then
$$
\chi\qty{\OO_X(D)} = \chi\qty{\OO_X} + \frac{1}{2} D \cdot (D - K) .
$$
:::

::: {.remark}
For the curve analogue see [[T-MWDVL]]. On a surface,
$$
\chi(\OO_X)=1-q(X)+p_g(X)
$$
with the invariants defined in [[D-COHEULER]].

Serre duality turns $h^2(D)$ into $h^0(K-D)$, so
$$
h^0(D) \geq \chi(\OO_X) + \tfrac{1}{2} D\cdot(D-K) - h^0(K - D) ,
$$
because $h^1(D)\geq0$. If $h^0(K-D)=0$ and
$$
\chi(\OO_X)+\tfrac12D\cdot(D-K)>0,
$$
then $h^0(D)>0$, so $D$ is linearly equivalent to an effective divisor.
:::
