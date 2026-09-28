---
title: Affine or projective
order: 2
topics:
- Projective Varieties
- Affine Schemes
- Segre Embedding
---

# Affine or projective

[[D-CP2MH]]

## Is it projective?

Projectivity is established by exhibiting a closed embedding into some $\PP^N$.

[[PR-VA4S3]]

The $d$-uple Veronese embedding $\nu_d\colon\PP^n\to\PP^{\binom{n+d}{d}-1}$ sends each degree-$d$ hypersurface $V(f)$ to a hyperplane section of $\nu_d(\PP^n)$.
So $\PP^n\setminus V(f)$ is isomorphic to $\nu_d(\PP^n)$ minus a hyperplane section, a closed subvariety of $\AA^{\binom{n+d}{d}-1}$, and is affine.

## Is it affine?

[[PR-EFW6B]]

A closed subvariety of an affine variety is affine, and a complete connected affine variety is a point, so a variety containing a complete curve is not affine.
In particular $\PP^n$, $\PP^m \times \PP^n$, and every projective variety of positive dimension are not affine.

[[PR-WZGOQ]]

## Is it complete?

[[D-VARCOMP]]

Projective implies complete and not conversely, so the three classes nest: projective inside complete inside separated of finite type.

## Examples

$\PP^1 \times \PP^1$ is projective by the Segre embedding and not affine because it contains the complete curve $\PP^1\times\{p\}$.
The complement of a curve in $\PP^2$ is affine by the Veronese argument, and it is not projective, because it is a proper open subset of an irreducible projective surface.

[[algebraic-geometry/cohomology/vanishing-and-duality|Serre's criterion]] characterizes affineness cohomologically: a noetherian scheme $X$ is affine exactly when $H^1(X,\mcf)=0$ for every quasicoherent $\mcf$.
