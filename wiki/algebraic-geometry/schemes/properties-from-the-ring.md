---
title: Properties from the ring
order: 2
topics:
- Schemes
- Integral Schemes
- Generic Points
---

# Properties from the ring

A scheme is reduced, or locally noetherian, exactly when the rings of one affine open cover are reduced, or noetherian.

[[PR-6TCSJ]]

A scheme is integral exactly when it is reduced and irreducible: on an affine open $\Spec A$, a zero nilradical that is prime says that $(0)$ is prime.
A scheme is noetherian when it has a finite cover by spectra of noetherian rings.
This is strictly stronger than the topological noetherian condition of [[algebraic-geometry/varieties/the-dictionary|the dictionary]]: a scheme with noetherian underlying space need not have noetherian rings of functions.

## Generic points

An irreducible closed subset $Z$ of a scheme has a unique generic point $\eta_Z$, with $\overline{\{\eta_Z\}}=Z$.
For $X$ integral the generic point $\eta$ has residue field $k(X)$, the function field, and a rational map is a morphism defined on some neighbourhood of $\eta$.

For $X$ integral and $\mcf$ coherent, $\mcf_\eta$ is a finite-dimensional $k(X)$-vector space, so $\mcf$ is locally free on a dense open subset of $X$.
In an irreducible scheme $X$ every nonempty open subset is dense and contains $\eta$, so a property whose locus is open holds on a dense open subset exactly when it holds at $\eta$.

## Singularity classes

[[D-SCHCMGOR]]
