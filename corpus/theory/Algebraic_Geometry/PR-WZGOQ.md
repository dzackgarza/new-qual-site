---
schema: qual/card@1
id: PR-WZGOQ
kind: proposition
title: Hypersurface complements are affine
slogan: 'A hypersurface complement is affine: localize by its equation in affine space, or use Veronese to make it a hyperplane complement projectively.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Hypersurfaces
  - Veronese Embedding
relations:
- kind: uses
  target: D-BIVAU
review: draft
prompts:
- Is the complement of a hypersurface in $\AA^n$ affine?
- Is the complement of a hypersurface in $\PP^n$ affine?
---

::: {.proposition}
Let $k$ be a field.

1. If $f\in k[x_1,\ldots,x_n]$, then
$$
\AA_k^n\sm V(f)=D_f\cong\Spec k[x_1,\ldots,x_n]_f.
$$

2. If $f\in k[x_0,\ldots,x_n]$ is a nonzero homogeneous polynomial of degree $d\geq1$, then
$$
\PP_k^n\sm V_+(f)
$$
is affine.
:::

::: {.proof}
For the affine statement,
$$
k[x_1,\ldots,x_n]_f
\cong
k[x_1,\ldots,x_n,y]/(yf-1),
$$
so $D_f$ is isomorphic to the closed subscheme
$$
V(yf-1)\subseteq\AA_k^{n+1}.
$$

For the projective statement, let
$$
\nu_d\colon\PP_k^n\hookrightarrow\PP_k^N,
\qquad
N=\binom{n+d}{d}-1,
$$
be the $d$-uple Veronese embedding. The degree-$d$ polynomial $f$ is a linear form in the Veronese coordinates, so there is a hyperplane $H_f\subseteq\PP_k^N$ such that
$$
\nu_d^{-1}(H_f)=V_+(f).
$$
Hence
$$
\PP_k^n\sm V_+(f)
\cong
\nu_d(\PP_k^n)\cap(\PP_k^N\sm H_f).
$$
The Veronese image is closed in $\PP_k^N$, while $\PP_k^N\sm H_f\cong\AA_k^N$. Therefore the displayed intersection is closed in an affine scheme and is affine.
:::

::: {.remark}
In the projective case the complement can also be described as the distinguished open $D_+(f)$ in $\Proj k[x_0,\ldots,x_n]$, whose coordinate ring is the degree-zero part of the homogeneous localization:
$$
\Gamma(D_+(f),\OO)=\bigl(k[x_0,\ldots,x_n]_f\bigr)_0.
$$
:::
