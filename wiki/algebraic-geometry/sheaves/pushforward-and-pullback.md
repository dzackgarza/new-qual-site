---
title: Pushforward and pullback
order: 5
topics:
- Direct Image Functor
- Inverse Image Functor
- Adjunctions
---

# Pushforward and pullback

A continuous map $f\colon X\to Y$ carries sheaves in two directions: $f_*$ pushes a sheaf forward along $f$, $f^{-1}$ pulls one back along it, and $f^*$ corrects the pullback so that it acts on $\OO_X$-modules.
These are the two functors that every continuous map has. Extension by zero $j_!$ along an open immersion, its derived proper-support functor $Rf_!$, and the dualizing functor $f^!$ exist under hypotheses on $f$ or on the coefficients, and they are treated where those hypotheses are in force ([[D-SHFSIX]], [[T-LADICPROPER]]).

## The two functors

[[D-MODPULL]]

The two functors behave oppositely on stalks: the inverse image has stalk $(\inverseof{f}\mcg)_x=\mcg_{f(x)}$, which is why it is the one that can be computed pointwise, while a stalk of the direct image is a colimit over the neighbourhoods of the image point and is not the stalk of $\mcg$ anywhere.
The inverse image is exact and $f_*$ is only left exact: for $f\colon X\to\Spec k$ the direct image $f_*$ is $\Gamma(X,-)$, so the failure of exactness of $f_*$ is what the higher direct images measure ([[D-COHRIF]]).
The module-theoretic pullback $f^*$ base changes the exact $f^{-1}$ along $\inverseof f\OO_Y\to\OO_X$, hence is only right exact, and has left derived functors ([[D-MODPULL]]).

## Adjunction

[[D-DEFADJ]]

The pair $\inverseof{f}\dashv f_*$ is an adjunction of additive functors between abelian categories, so general facts about adjoint pairs apply without further hypotheses: the left adjoint preserves colimits and the right adjoint preserves limits ([[T-DEFRAPL]]).
So $f^{-1}$ preserves colimits and $f_*$ preserves limits, and the same adjunction gives the computation rules for $f_*$ and $f^*$: a pushforward of a direct sum is a direct sum, and a pullback of a cokernel is the cokernel ([[T-DEFRAPL]]).

## Exactness of the two functors

[[PR-SHFPUSHEX]]

For a closed immersion $f_*$ is exact, so the cohomology of a closed subscheme can be computed in the ambient scheme.
For a proper morphism $f$ and a coherent $\mcf$ the higher direct images $R^if_*\mcf$ are coherent, and the base-change theorems compare $(R^if_*\mcf)\otimes\kappa(y)$ with $H^i(X_y,\mcf_y)$ over points $y\in Y$ ([[T-BASECHANGE]]); the Leray spectral sequence computes $H^*(X,\mcf)$ from the higher direct images ([[T-COHLERAY]]).

## The projection formula

[[PR-SCHPROJFORM]]

The projection formula is the compatibility of the two functors with tensor: $f_*(\mcf\tensor f^*\mcg)\cong f_*\mcf\tensor\mcg$.
It is what makes pullback a map of $\OO_Y$-module categories rather than merely of abelian categories, and it is used whenever a twist is moved past a pushforward.

## Extension by zero

[[D-SHFSIX]]

Extension by zero is the functor that is left adjoint to restriction to an open set, and it exists for sheaves of abelian groups but not for quasicoherent sheaves: on $X=\AA^1_k$ with $j$ the inclusion of the complement of the origin, $j_!\OO_U$ has nonzero sections over $U$ and only zero sections over $X$, so its sections are not the localisation of its global sections and it is not quasicoherent ([[FE-MODZOO]]).
The functors $j_!$ and $Rf_!$ therefore act on sheaves of abelian groups, or on constructible coefficients, rather than on quasicoherent sheaves ([[T-LADICPROPER]]).
