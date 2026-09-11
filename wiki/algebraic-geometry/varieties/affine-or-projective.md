---
title: Affine or projective
order: 2
topics:
- Projective Varieties
- Affine Schemes
- Segre Embedding
---

# Affine or projective

Three of the questions in the bank are the same question: given a variety by a presentation, decide which of the two categories it belongs to.
The exchange is short, so the useful thing is a test that terminates, not a definition.

[[D-CP2MH]]

## Is it projective?

Exhibit a closed embedding into some $\PP^N$.
Two constructions cover almost every case that is asked.

[[PR-VA4S3]]

The other is the $d$-uple Veronese, which re-embeds $\PP^n$ so that degree-$d$ hypersurfaces become hyperplane sections.
It converts a statement about a hypersurface of high degree into a statement about a hyperplane, and it is used below for exactly that.

## Is it affine?

The obstruction is a function count.

[[PR-EFW6B]]

So a variety with a complete curve inside it is not affine, and this settles $\PP^n$, $\PP^m \times \PP^n$, and every projective variety of positive dimension in one stroke.
In the other direction the affine examples are produced by inverting something.

[[PR-WZGOQ]]

## The two answers together

$\PP^1 \times \PP^1$ is projective by Segre and not affine by the function count.
The complement of a hypersurface in $\PP^2$ is affine, and it is not projective, because it is a proper open subset of an irreducible projective surface.
Neither answer needs cohomology.

Serre's cohomological criterion — $X$ Noetherian is affine exactly when $H^1(X, \mcF) = 0$ for every quasicoherent $\mcF$ — is the version that generalises, and it is in [[algebraic-geometry/cohomology/index|cohomology]].
It is worth knowing which of the two an examiner is asking for: a request to *decide* a case wants the function count, and a request to *prove a criterion* wants Serre.
