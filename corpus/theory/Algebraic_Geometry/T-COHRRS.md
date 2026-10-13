---
schema: qual/card@1
id: T-COHRRS
kind: proposition
title: An effectivity criterion from surface Riemann--Roch
slogan: 'Surface Riemann--Roch plus Serre duality forces effectivity once the Euler characteristic is positive and $K-D$ has no sections.'
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
  target: T-SRFRR
- kind: uses
  target: D-COHEULER
- kind: related-to
  target: T-MWDVL
review: draft
prompts:
- How do you show a divisor on a surface is effective?
---

::: {.proposition}
Let $X$ be a smooth projective surface with canonical divisor $K_X$, and let $D$ be a divisor. If
$$
H^0(X,\OO_X(K_X-D))=0
$$
and
$$
\chi(\OO_X)+\frac12D\cdot(D-K_X)>0,
$$
then $H^0(X,\OO_X(D))\ne0$, so $D$ is linearly equivalent to an effective divisor.
:::

::: {.proof}
By [[T-SRFRR]],
$$
\chi(\OO_X(D))
=\chi(\OO_X)+\frac12D\cdot(D-K_X).
$$
Serre duality gives
$$
h^2(X,\OO_X(D))=h^0(X,\OO_X(K_X-D))=0.
$$
Therefore
$$
h^0(D)=\chi(\OO_X(D))+h^1(D)>0.
$$
:::

::: {.remark}
For example, if $H$ is ample and $(K_X-D)\cdot H<0$, then $K_X-D$ cannot be effective, so the first hypothesis holds. The constant term may be written
$$
\chi(\OO_X)=1-q(X)+p_g(X)
$$
using the invariants in [[D-COHEULER]]. The curve analogue is [[T-MWDVL]].
:::
