---
title: Affine or projective
order: 2
topics:
- Projective Varieties
- Affine Schemes
- Segre Embedding
---

# Affine or projective

Many presentations reduce to deciding whether a variety is affine, projective, or complete.
The useful criteria below turn those classifications into concrete computations.

[[D-CP2MH]]

## Is it projective?

Projectivity is established by exhibiting a closed embedding into some $\PP^N$.
Two constructions cover many standard cases.

[[PR-VA4S3]]

The other is the $d$-uple Veronese, which re-embeds $\PP^n$ so that degree-$d$ hypersurfaces become hyperplane sections.
It converts a statement about a hypersurface of high degree into a statement about a hyperplane, and it is used below for exactly that.

## Is it affine?

The obstruction is a function count.

[[PR-EFW6B]]

So a variety with a complete curve inside it is not affine, and this settles $\PP^n$, $\PP^m \times \PP^n$, and every projective variety of positive dimension in one stroke.
In the other direction the affine examples are produced by inverting something.

[[PR-WZGOQ]]

## Is it complete?

[[D-VARCOMP]]

Projective implies complete and not conversely, so the three classes nest: projective inside complete inside separated of finite type.
In many examples completeness follows immediately from projectivity.

## The two answers together

$\PP^1 \times \PP^1$ is projective by Segre and not affine by the function count.
The complement of a hypersurface in $\PP^2$ is affine, and it is not projective, because it is a proper open subset of an irreducible projective surface.
Neither answer needs cohomology.

Serre's cohomological criterion — $X$ Noetherian is affine exactly when $H^1(X, \mcf) = 0$ for every quasicoherent $\mcf$ — is developed in [[algebraic-geometry/cohomology/index|cohomology]]. Function counts decide many concrete cases, while Serre's theorem supplies a general criterion.
