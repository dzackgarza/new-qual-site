---
schema: qual/card@1
id: PR-VAREM1
kind: proposition
title: The exceptional curve has self-intersection $-1$
slogan: 'Blowing up a smooth point creates $E\cong\PP^1$ with $E^2=-1$, and adds $(n-1)E$ to the canonical class.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Intersection Theory
  - Canonical Divisor
relations:
- kind: uses
  target: D-VARBLOW
review: draft
prompts:
- Why does the exceptional curve $E$ in $\Bl_p X$ satisfy $E^2 = -1$?
- What is the canonical class of a blowup?
---

::: {.proposition}
Let $X$ be a smooth projective surface over a field $k$, let $p\in X(k)$, let
$$
\pi\colon\widetilde X=\Bl_pX\longrightarrow X
$$
be the blowup, and let $E$ be its exceptional curve.
Then
$$
E \cong \PP^1_k, \qquad E^2 = -1, \qquad K_{\widetilde X} = \pi^* K_X + E .
$$
More generally, if $X$ is a smooth $n$-dimensional variety and $p\in X(k)$, then
$$
K_{\Bl_pX}=\pi^*K_X+(n-1)E.
$$
:::

::: {.proof}
For the blowup of a smooth point, the exceptional divisor is the projectivized tangent space and
$$
\OO_{\widetilde X}(E)\restrict_E\cong\OO_E(-1)
$$
[@Har77, Proposition II.8.24]. On a surface $E\cong\PP^1_k$, so
$$
E^2=\deg\OO_E(E)=\deg\OO_{\PP^1}(-1)=-1.
$$

For the canonical divisor formula, it is enough to compute near $p$. Choose étale local coordinates $x_1,\ldots,x_n$ at $p$. On the blowup chart in which the first homogeneous coordinate is nonzero, write
$$
x_1=u,\qquad x_i=u v_i\quad(2\leq i\leq n),
$$
so $E$ is given by $u=0$. Then
$$
\pi^*(dx_1\wedge\cdots\wedge dx_n)
=u^{n-1}\,du\wedge dv_2\wedge\cdots\wedge dv_n.
$$
Thus the relative canonical divisor has multiplicity $n-1$ along $E$ and no support away from $E$, giving
$$
K_{\Bl_pX}=\pi^*K_X+(n-1)E.
$$
:::

::: {.remark}
On a surface the canonical formula and the projection formula give
$$
K_{\widetilde X}^2
=(\pi^*K_X+E)^2
=K_X^2-1,
$$
because $\pi^*K_X\cdot E=0$ and $E^2=-1$.
:::
