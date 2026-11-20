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
$X$ is a closed subscheme of $\PP^n_k$, so it is projective over the noetherian ring $k$ and $\OO_X$ is coherent; by [@Har77, Theorem III.5.2(a)] the group $H^0(X,\OO_X)=\Gamma(X,\OO_X)$ is a finitely generated $k$-module.

It is a $k$-algebra, and it is a domain: $X$ is integral with generic point $\eta$, and evaluation at $\eta$ gives an injective map $\Gamma(X,\OO_X)\injects\OO_{X,\eta}=\kappa(\eta)$ into the function field, since the set where a section has nonzero germ is closed and a section whose germ at $\eta$ vanishes therefore vanishes everywhere.

A finite-dimensional $k$-algebra that is a domain is a field: for $a\neq0$ multiplication by $a$ is $k$-linear and injective, hence bijective, so $a$ is a unit.
So $\Gamma(X,\OO_X)$ is a finite field extension of $k$, and $k$ is algebraically closed, so $\Gamma(X,\OO_X)=k$.
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
