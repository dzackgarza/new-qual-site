---
schema: qual/card@1
id: PR-SCHINT
kind: proposition
title: Affine computation of scheme-theoretic intersections
slogan: 'For closed subschemes of an affine scheme, scheme-theoretic intersection is computed by adding defining ideals.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fibre Products
  - Subschemes
  - Intersection Theory
relations:
- kind: uses
  target: D-SCHFIBRES
- kind: uses
  target: D-SCHSUB
review: draft
prompts:
- How do you compute a scheme-theoretic intersection inside an affine scheme?
---

::: {.proposition}
Let $Y=\Spec R$ and let
$$
X_i=\Spec(R/J_i)\hookrightarrow Y
$$
be closed subschemes. Their [[D-SCHFIBRES|scheme-theoretic intersection]] has coordinate ring
$$
(R/J_1)\tensor_R(R/J_2)
\cong
R/(J_1+J_2).
$$
Hence
$$
X_1\times_YX_2\cong\Spec R/(J_1+J_2).
$$
:::

::: {.proof}
Tensor the exact sequence
$$
J_1\longrightarrow R\longrightarrow R/J_1\longrightarrow0
$$
with $R/J_2$. Right exactness gives
$$
J_1\tensor_RR/J_2
\longrightarrow
R/J_2
\longrightarrow
(R/J_1)\tensor_R(R/J_2)
\longrightarrow0.
$$
The image of the first map is $(J_1+J_2)/J_2$, so the cokernel is $R/(J_1+J_2)$.
:::

::: {.example title="Contact of order $m$"}
In $\AA_k^2=\Spec k[x,y]$, let
$$
C=V(y-x^m),\qquad L=V(y),\qquad m\geq2.
$$
Both defining ideals are prime, but
$$
C\cap L
\cong
\Spec k[x,y]/(y-x^m,y)
\cong
\Spec k[x]/(x^m),
$$
a single point of length $m$. Thus the sum of two radical ideals need not be radical, and the nonreduced intersection records the order of tangency.
:::
