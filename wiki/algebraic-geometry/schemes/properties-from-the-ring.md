---
title: Properties from the ring
order: 2
topics:
- Schemes
- Integral Schemes
- Generic Points
---

# Properties from the ring

Every local property of a scheme is a property of a ring, and the affine case carries the whole dictionary.

[[PR-6TCSJ]]

Two of these are asked as a pair.
"Integral" is reduced plus irreducible, and the proof is one line in the table: no nilpotents and a prime nilradical say that $(0)$ is prime.
"Noetherian" for a scheme means a finite cover by spectra of Noetherian rings, which is strictly stronger than the topological Noetherian condition of [[algebraic-geometry/varieties/the-dictionary|the dictionary]] — a topologically Noetherian scheme need not have Noetherian rings of functions, and this is the gap the weakening question in Serre's criterion probes.

## Generic points

An irreducible closed subset of a scheme has a unique generic point, and this is the technical device that replaces "a general point of $X$" as a figure of speech.
For $X$ integral the generic point $\eta$ has residue field $k(X)$, the function field, and a rational map is a morphism defined on some neighbourhood of $\eta$.

The practical consequence is that generic statements become statements at a point: a coherent sheaf is locally free at $\eta$ always, and generic flatness, generic smoothness and generic reducedness are all the observation that a condition open on the base holds at $\eta$ exactly when it holds on a dense open.

## Singularity classes

[[D-SCHCMGOR]]
