---
schema: qual/card@1
id: PR-CRVHYPCI
kind: proposition
title: Hyperelliptic curves are not projective complete intersections
slogan: 'For a smooth complete-intersection curve of genus at least $2$, adjunction makes the canonical bundle very ample, so the curve cannot be hyperelliptic.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hyperelliptic Curves
  - Complete Intersections
  - Canonical Divisor
relations:
- kind: uses
  target: D-CRVHYP
- kind: related-to
  target: FE-CRVLOWG
review: draft
prompts:
- Can a hyperelliptic curve be a complete intersection in $\PP^n$?
- What is the canonical sheaf of a complete intersection curve, and why does that settle the question?
- Which canonical curves are complete intersections?
---

::: {.proposition}
Let $k$ be an algebraically closed field and let $C \subseteq \PP^n_k$ be a smooth curve of genus $g \geq 2$ which is a complete intersection of hypersurfaces of degrees $d_1,\ldots,d_{n-1}$.
Then $C$ is not hyperelliptic.
:::

::: {.remark}
Adjunction on the complete intersection gives
$$
\omega_C \cong \OO_C(a), \qquad a = \sum_{i=1}^{n-1} d_i - n - 1 ,
$$
and, with $d\coloneqq\prod_{i=1}^{n-1}d_i$, one has $\deg\OO_C(1)=d>0$.
So $2g-2 = ad$, and the hypothesis $g \geq 2$ forces $a \geq 1$.
For $a\geq1$, the line bundle $\OO_{\PP^n}(a)$ is very ample, and its restriction $\OO_C(a)\cong\omega_C$ is very ample. Hence the canonical map embeds $C$. By [[D-CRVHYP]], a hyperelliptic curve of genus at least $2$ has a degree-two canonical map onto a rational normal curve, so $C$ cannot be hyperelliptic.
:::

::: {.remark title="Canonical complete intersections"}
Suppose the canonical embedding of a non-hyperelliptic curve of genus $g\geq3$ is a complete intersection in $\PP^{g-1}$ of hypersurfaces of degrees $d_1,\ldots,d_{g-2}$. Since the canonical curve is nondegenerate, $d_i\geq2$. Adjunction gives
$$
\omega_C\cong\OO_C\left(\sum_{i=1}^{g-2}d_i-g\right).
$$
Because the canonical embedding has $\omega_C\cong\OO_C(1)$,
$$
\sum_{i=1}^{g-2}d_i=g+1.
$$
The inequality $2(g-2)\leq g+1$ forces $g\leq5$. The possible multidegrees are therefore
$$
g=3:\ (4),\qquad g=4:\ (2,3),\qquad g=5:\ (2,2,2).
$$
Thus any canonical curve that is a complete intersection has one of these three multidegrees: a plane quartic, a quadric--cubic intersection in $\PP^3$, or an intersection of three quadrics in $\PP^4$.
:::
