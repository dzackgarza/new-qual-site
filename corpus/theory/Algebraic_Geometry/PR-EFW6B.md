---
schema: qual/card@1
id: PR-EFW6B
kind: proposition
title: Regular functions on a projective variety are constant
slogan: 'A connected projective variety over an algebraically closed field has no nonconstant global regular functions.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Varieties
  - Regular Functions
  - Affine Schemes
relations:
- kind: uses
  target: D-CP2MH
review: draft
prompts:
- What are the global regular functions on a projective variety?
- Why is $\PP^n$ not affine?
---

::: {.proposition}
Let $X$ be a projective variety over an algebraically closed field $k$.
Then
$$
\Gamma(X,\OO_X)=k.
$$
:::

::: {.remark}
If $Y=\Spec A$ is affine, then a morphism $f\colon X\to Y$ corresponds to a $k$-algebra homomorphism
$$
A\longrightarrow\Gamma(X,\OO_X)=k.
$$
Hence $f$ factors through a $k$-point of $Y$ and is constant.

If $X$ were also affine, then
$$
X\cong\Spec\Gamma(X,\OO_X)=\Spec k.
$$
Thus every positive-dimensional projective variety is non-affine; in particular, $\PP_k^n$ is not affine for $n\geq1$.
:::
