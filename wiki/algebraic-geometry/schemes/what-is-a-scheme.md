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

A morphism of schemes is a morphism of locally ringed spaces, which is a pair $(f,f^\sharp)$ with $f^\sharp\colon\OO_Y\to f_*\OO_X$ and the induced maps on stalks local: $(f^\sharp_p)^{-1}(\mfm_p)=\mfm_{f(p)}$ for every $p\in X$ [@Har77, §II.2, p. 72] ([[D-AN662]]).
For affine schemes this recovers the anti-equivalence with rings: every morphism $\Spec B\to\Spec A$ is induced by a ring homomorphism $A\to B$ [@Har77, §II.2, p. 73] ([[T-SK599]]).

## First examples

[[FE-O12TX]]

The spectra of the standard rings give the first list: $\Spec k$, the one-point scheme with residue field $k$; $\Spec\ZZ$; $\Spec k[t]$, the affine line; and $\Spec k[t,t^{-1}]$, the punctured line, which is affine although it is not a closed subscheme of the line.

## Recognising an affine scheme

[[T-SK599]]

By [[algebraic-geometry/cohomology/vanishing-and-duality|Serre's criterion]], a noetherian scheme $X$ is affine exactly when $H^1(X,\mci)=0$ for every coherent ideal sheaf $\mci\subseteq\OO_X$.

## Covers of an affine scheme

[[PR-SCHUNITCOVER]]

## Formal schemes

[[D-SCHFORMAL]]

## Checking a property on one affine cover

[[T-AFFCOMM]]

A property of schemes is local for the Zariski topology when it holds for $X$ exactly when it holds on the members of one affine open cover; the cards above apply that principle to reducedness, integrality and the singularity classes [@Har77, §II.3, pp. 82--85].
