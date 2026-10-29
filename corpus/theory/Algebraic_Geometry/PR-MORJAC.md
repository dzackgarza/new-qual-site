---
schema: qual/card@1
id: PR-MORJAC
kind: proposition
title: The Jacobian criterion for smoothness
slogan: 'For an affine variety over an algebraically closed field, the Jacobian computes the tangent-space dimension; smoothness means tangent dimension equals local dimension.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Smooth Morphisms
  - Jacobian Criterion
  - Singularities
relations:
- kind: uses
  target: D-MORSM
review: draft
prompts:
- State the Jacobian criterion.
- How do you check in practice that a variety is smooth at a point?
---

::: {.proposition title="Jacobian criterion"}
Let $k$ be an algebraically closed field, let
$$
X=\Spec k[x_1,\ldots,x_n]/I\subseteq\AA_k^n
$$
be an affine variety, and choose generators $I=(f_1,\ldots,f_m)$. For a closed point $p\in X$, let
$$
J(p)=\qty{\frac{\partial f_i}{\partial x_j}(p)}_{1\leq i\leq m,\ 1\leq j\leq n}.
$$
Then
$$
\dim_k T_pX=n-\rank J(p).
$$
The point $p$ is smooth exactly when
$$
\rank J(p)=n-\dim\OO_{X,p}.
$$
In particular, if $X$ has pure dimension $d$, then $p$ is smooth exactly when $\rank J(p)=n-d$.
:::

::: {.remark}
The conormal sequence at $p$ gives
$$
(I/I^2)\tensor_{\OO_{X,p}}\kappa(p)
\longrightarrow
\mfm_{\AA^n,p}/\mfm_{\AA^n,p}^2
\longrightarrow
\mfm_{X,p}/\mfm_{X,p}^2
\longrightarrow0.
$$
In the coordinate bases, the first map is represented by the rows of $J(p)$, which gives the tangent-space dimension formula.

Over an algebraically closed field, smoothness at a closed point is equivalent to regularity of the local ring. Thus the criterion compares
$$
\dim_k\mfm_{X,p}/\mfm_{X,p}^2
$$
with $\dim\OO_{X,p}$.

The generators must generate the scheme-theoretic defining ideal. Replacing an equation by a power can leave its set-theoretic zero locus unchanged while changing its Jacobian; for example, $V(x)=V(x^2)$ as subsets of affine space, but $x^2$ has zero differential along that locus.
:::
