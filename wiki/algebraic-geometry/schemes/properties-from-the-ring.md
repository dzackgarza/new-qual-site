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

A scheme is integral exactly when it is reduced and irreducible [@Har77, Proposition II.3.1].
A scheme is noetherian when it has a finite cover by spectra of noetherian rings.
This is strictly stronger than the topological noetherian condition: $\underlyingspace{\Spec A}$ is a noetherian topological space when $A$ is noetherian, and can be noetherian when $A$ is not [@Har77, Exercise II.2.13] ([[PR-6TCSJ]]).

## Generic points

An irreducible closed subset $Z$ of a scheme has a unique generic point $\eta_Z$, with $\overline{\{\eta_Z\}}=Z$ [@Har77, Exercise II.2.9], since irreducible closed subsets of $\Spec A$ correspond to prime ideals ([[D-SCHPTS]], [[D-SCHDIM]]).
For $X$ integral the generic point $\eta$ has residue field $k(X)$, the function field, and a rational map is a morphism defined on some neighbourhood of $\eta$.

For $X$ noetherian integral and $\mcf$ coherent, $\mcf_\eta$ is a free $k(X)$-module, so $\mcf$ is locally free on a dense open subset of $X$ [@Har77, Exercise II.5.7(a)].
In an irreducible scheme $X$ every nonempty open subset is dense and contains $\eta$, so a property whose locus is open holds on a dense open subset exactly when it holds at $\eta$.

## Singularity classes

[[D-SCHCMGOR]]
