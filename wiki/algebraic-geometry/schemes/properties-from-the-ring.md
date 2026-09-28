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

A scheme is integral exactly when it is reduced and irreducible: on an affine open $\Spec A$, a reduced ring whose nilradical is prime has $(0)$ prime.
"Noetherian" for a scheme means a finite cover by spectra of Noetherian rings, which is strictly stronger than the topological Noetherian condition of [[algebraic-geometry/varieties/the-dictionary|the dictionary]]: $\Spec k[x_1,x_2,\ldots]/(x_1,x_2,\ldots)^2$ is a one-point space, and its ring is not noetherian.

## Generic points

An irreducible closed subset $Z$ of a scheme has a unique generic point $\eta_Z$, with $\overline{\{\eta_Z\}}=Z$.
For $X$ integral the generic point $\eta$ has residue field $k(X)$, the function field, and a rational map is a morphism defined on some neighbourhood of $\eta$.

For $X$ integral and $\mcf$ coherent, $\mcf_\eta$ is a finite-dimensional $k(X)$-vector space, so $\mcf$ is locally free on a dense open subset of $X$.
A property that holds on an open subset of an irreducible scheme $X$ holds on a dense open subset exactly when it holds at $\eta$.

## Singularity classes

[[D-SCHCMGOR]]
