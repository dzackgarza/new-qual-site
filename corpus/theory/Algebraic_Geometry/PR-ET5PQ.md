---
schema: qual/card@1
id: PR-ET5PQ
kind: proposition
title: $H^1$ classifies line bundles and extensions
slogan: '$H^1$ records gluing: units give line bundles, and $\mcf\tensor\dualof{\mcg}$ gives extensions when $\mcg$ is locally free.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Line Bundles
  - Picard Group
relations:
- kind: uses
  target: D-5PQ5W
- kind: uses
  target: D-PTIW0
review: draft
prompts:
- What is the connection between $H^1$ and line bundles?
- What does $H^1$ classify besides line bundles?
---

::: {.proposition}
Let $(X,\OO_X)$ be a ringed space.
Then $\Pic(X) \cong H^1(X, \OO_X^\times)$.
For $\OO_X$-modules $\mcf$ and $\mcg$, equivalence classes of extensions
$$
0 \to \mcf \to \mce \to \mcg \to 0
$$
are classified by $\Ext^1_{\OO_X}(\mcg,\mcf)$. If $\mcg$ is finite locally free, then
$$
\Ext^1_{\OO_X}(\mcg,\mcf)
\cong
H^1\bigl(X,\mcf\tensor_{\OO_X}\mcg^\vee\bigr).
$$
:::

::: {.remark}
A line bundle is trivial on an open cover, with transition functions
$$
g_{ij}\in\OO_X^\times(U_i\cap U_j)
$$
satisfying the Čech cocycle condition. Changing the local frames changes the cocycle by a coboundary, so tensor product of line bundles corresponds to multiplication of cocycles. This gives the canonical isomorphism $\Pic(X)\cong H^1(X,\OO_X^\times)$.

For extensions, finite local freeness gives
$$
\mathcal Hom_{\OO_X}(\mcg,\mcf)
\cong
\mcf\tensor_{\OO_X}\mcg^\vee,
$$
and the local higher $\mathcal Ext$ sheaves vanish. The local-to-global Ext spectral sequence therefore identifies the Yoneda extension group with the displayed $H^1$.

On a complex manifold the exponential sequence makes it explicit,
$$
H^1(X,\ZZ)\to H^1(X,\OO_X)\to\Pic(X)\xrightarrow{c_1}H^2(X,\ZZ)\to H^2(X,\OO_X).
$$
Thus $c_1$ records the integral cohomology class of a holomorphic line bundle, and
$$
\ker(c_1)\cong H^1(X,\OO_X)/\im H^1(X,\ZZ).
$$
:::
