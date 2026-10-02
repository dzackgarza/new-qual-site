---
schema: qual/card@1
id: T-SRFRR
kind: theorem
title: Riemann--Roch for surfaces
slogan: 'Surface Riemann--Roch turns Euler characteristic into intersection theory: $\chi(\OO_X(D))-\chi(\OO_X)=\tfrac12D\cdot(D-K_X)$.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Roch
  - Surfaces
  - Intersection Theory
relations:
- kind: uses
  target: D-SRFINT
- kind: uses
  target: T-SRFADJ
review: draft
prompts:
- State Riemann--Roch for surfaces.
- What is Noether's formula?
- How do you show a divisor on a surface is effective?
---

::: {.theorem}
For a divisor $D$ on a smooth projective surface $X$,
$$
\chi(\OO_X(D)) = \chi(\OO_X) + \tfrac{1}{2} D \cdot (D - K_X) .
$$
:::

::: {.theorem title="Noether's formula"}
For a smooth projective surface,
$$
12\chi(\OO_X)=K_X^2+\deg c_2(T_X).
$$
If the ground field is $\CC$, then
$$
\deg c_2(T_X)=\chi_{\mathrm{top}}(X(\CC)).
$$
:::

::: {.remark}
The surface formula parallels the curve formula, with $\deg D$ replaced by $\tfrac{1}{2}D\cdot(D-K)$ and $1-g$ replaced by $\chi(\OO_X)$; adjunction makes these substitutions consistent.

The typical use is not to compute $\chi$ but to force a section.
Serre duality gives $h^2(D) = h^0(K-D)$, so
$$
h^0(D)
\geq
\chi(\OO_X)+\tfrac12D\cdot(D-K_X)-h^0(K_X-D).
$$
If $(K_X-D)\cdot H<0$ for an ample divisor $H$, then $K_X-D$ cannot be effective, so $h^0(K_X-D)=0$. Whenever
$$
\chi(\OO_X)+\tfrac12D\cdot(D-K_X)>0,
$$
it follows that $h^0(D)>0$, hence $D$ is linearly equivalent to an effective divisor.

For $X=\PP^2_\CC$, one has $K_X^2=9$ and $\chi_{\mathrm{top}}(X)=3$, so Noether's formula gives $\chi(\OO_X)=1$.
:::
