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

::: {.proof}
$X$ is a closed subscheme of $\PP^n_k$, so it is projective over the noetherian ring $k$ and $\OO_X$ is coherent; by [@Har77, Theorem III.5.2(a)] the $k$-module
$$
\Gamma(X,\OO_X)=H^0(X,\OO_X)
$$
is finitely generated, hence finite dimensional over $k$.

**$\Gamma(X,\OO_X)$ is reduced.**
The map $\Gamma(X,\OO_X)\to\prod_{x\in X}\OO_{X,x}$ is injective, a section being zero exactly when all of its germs are, and each $\OO_{X,x}$ is reduced because $X$ is; so $\Gamma(X,\OO_X)$ has no nonzero nilpotent.
A finite-dimensional reduced commutative $k$-algebra is a product of finitely many finite field extensions of $k$, and $k$ is algebraically closed, so each factor is $k$ and
$$
\Gamma(X,\OO_X)\cong k^m
$$
for some $m\geq1$.

**$m=1$.**
An idempotent $e\in\Gamma(X,\OO_X)$ has $e_x\in\theset{0,1}$ at every $x$, since $\OO_{X,x}$ is a local ring; the sets $\theset{x:e_x=1}=\theset{x:(e-1)_x=0}$ and $\theset{x:e_x=0}$ are therefore complementary and both open, and $X$ is connected because it is integral. So one of them is empty and $e\in\theset{0,1}$: the ring $k^m$ has no idempotent other than $0$ and $1$, hence $m=1$ and $\Gamma(X,\OO_X)=k$.
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
