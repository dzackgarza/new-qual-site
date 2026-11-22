---
title: What is a scheme
order: 2
topics:
- Schemes
- Affine Schemes
- Locally Ringed Spaces
---

# What is a scheme

A scheme is a locally ringed space covered by open subspaces isomorphic to spectra of rings, and the two halves of the definition answer two different questions: the space carries the points and the topology, the sheaf carries the functions and so the algebra.

[[D-AN662]]

[[D-VKR54]]

A morphism of schemes is a morphism of locally ringed spaces, which is a pair $(f,f^\sharp)$ with $f^\sharp\colon\OO_Y\to f_*\OO_X$ and the induced maps on stalks local: $(f^\sharp_p)^{-1}(\mfm_p)=\mfm_{f(p)}$ for every $p\in X$ [@Har77, §II.2] ([[D-AN662]]).
For affine schemes this recovers the anti-equivalence with rings: every morphism $\Spec B\to\Spec A$ is induced by a ring homomorphism $A\to B$ [@Har77, §II.2] ([[T-SK599]]).

## First examples

[[FE-O12TX]]

::: {.example title="Spectra of the standard rings"}
The one-point scheme $\Spec k$ has residue field $k$; $\Spec\ZZ$ is the affine scheme of the integers; $\Spec k[t]$ is the affine line; and $\Spec k[t,t^{-1}]$ is the punctured line, which is affine although it is not a closed subscheme of the line ([[D-MORIMM]]).
:::

## Recognising an affine scheme

[[T-SK599]]

By [[algebraic-geometry/cohomology/vanishing-and-duality|Serre's criterion]], a noetherian scheme $X$ is affine exactly when $H^1(X,\mci)=0$ for every coherent ideal sheaf $\mci\subseteq\OO_X$.

## Covers of an affine scheme

[[PR-SCHUNITCOVER]]

## Formal schemes

[[D-SCHFORMAL]]

## Checking a property on one affine cover

[[T-AFFCOMM]]

A property of schemes is local for the Zariski topology when it holds for $X$ exactly when it holds on the members of one affine open cover; this principle is how reducedness and the singularity classes are checked [@Har77, §II.3], while irreducibility and integrality are not of this kind: a disjoint union of two integral affine schemes is covered by integral affine opens and is not integral ([[T-AFFCOMM]]).
