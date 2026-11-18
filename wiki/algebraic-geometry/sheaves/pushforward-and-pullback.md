---
title: Pushforward and pullback
order: 5
topics:
- Direct Image Functor
- Inverse Image Functor
- Adjunctions
---

# Pushforward and pullback

A continuous map $f\colon X\to Y$ carries sheaves in two directions, and the two functors are the only ones available: $f_*$ pushes a sheaf forward along $f$, $f^{-1}$ pulls one back along it, and $f^*$ corrects the pullback so that it acts on $\OO_X$-modules.
The adjunction between them is the one formal statement of the chapter that is used everywhere afterwards, because it converts a statement about maps on $X$ into a statement about sections on $Y$ and back.

## The two functors

[[D-MODPULL]]

The two functors behave oppositely on stalks: the inverse image has stalk $(\inverseof{f}\mcg)_x=\mcg_{f(x)}$, which is why it is the one that can be computed pointwise, while a stalk of the direct image is a colimit over the neighbourhoods of the image point and is not the stalk of $\mcg$ anywhere.
The inverse image is exact and $f_*$ is only left exact, and the second clause is the whole reason sheaf cohomology exists; the module-theoretic pullback $f^*$ base changes the exact $f^{-1}$ and is therefore only right exact, which is why $f^*$ still has derived functors.

## Adjunction

[[D-DEFADJ]]

The pair $\inverseof{f}\dashv f_*$ is an adjunction of additive functors between abelian categories, so general facts about adjoint pairs apply without further hypotheses: the left adjoint preserves colimits and the right adjoint preserves limits ([[T-DEFRAPL]]).
That is the source of the standard computation rules for $f_*$ and $f^*$ — a pushforward of a direct sum is a direct sum, a pullback of a cokernel is the cokernel — and of the fact that $f^*$ is right exact and $f_*$ is left exact, which is all that abstract nonsense gives.

## Exactness of the two functors

[[PR-SHFPUSHEX]]

The failure of $f_*$ to be exact is measurable: its right derived functors are the higher direct images, which for a proper morphism compute the cohomology of the fibres ([[D-COHRIF]]), with the precise statement given by the base-change theorems ([[T-BASECHANGE]]).
For a closed immersion $f_*$ is exact, which is why cohomology of a closed subscheme can be computed in the ambient scheme; for a proper morphism the higher direct images are coherent and the Leray spectral sequence computes $H^*(X,\mcf)$ from them ([[T-COHLERAY]]).

## The projection formula

[[PR-SCHPROJFORM]]

The projection formula is the compatibility of the two functors with tensor: $f_*(\mcf\tensor f^*\mcg)\cong f_*\mcf\tensor\mcg$.
It is what makes pullback a map of $\OO_Y$-module categories rather than merely of abelian categories, and it is used whenever a twist is moved past a pushforward.

## Extension by zero

[[D-SHFSIX]]

Extension by zero is the functor that is left adjoint to restriction to an open set, and it exists for sheaves of abelian groups but not for quasicoherent sheaves: on $X=\AA^1_k$ with $j$ the inclusion of the complement of the origin, $j_!\OO_U$ has nonzero sections over $U$ and only zero sections over $X$, so its sections are not the localisation of its global sections and it is not quasicoherent ([[FE-MODZOO]]).
This is the sharpest illustration of what the quasicoherent condition costs: the six operations, $j_!$ and $Rf_!$ among them, live on sheaves of abelian groups and on constructible coefficients rather than on the quasicoherent ones ([[T-LADICPROPER]]).
