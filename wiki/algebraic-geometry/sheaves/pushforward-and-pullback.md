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
Every continuous map has the adjoint pair $\inverseof{f}\dashv f_*$. Extension by zero $j_!$ along an open immersion, its derived proper-support functor $Rf_!$, and the dualizing functor $f^!$ exist under hypotheses on $f$ or on the coefficients, and they are treated where those hypotheses are in force ([[D-SHFSIX]], [[T-LADICPROPER]]).

## The two functors

[[D-MODPULL]]

The two functors behave oppositely on stalks: the inverse image has stalk $(\inverseof{f}\mcg)_x=\mcg_{f(x)}$ ([[D-MODPULL]]), while a stalk of the direct image is a colimit over the neighbourhoods of the image point and is not the stalk of $\mcg$ anywhere.
The inverse image is exact and $f_*$ is only left exact: for $f\colon X\to\Spec k$ the direct image $f_*$ is $\Gamma(X,-)$, so the failure of exactness of $f_*$ is what the higher direct images measure ([[D-COHRIF]]).
The module-theoretic pullback $f^*$ base changes the exact $f^{-1}$ along $\inverseof f\OO_Y\to\OO_X$, hence is only right exact, and has left derived functors ([[D-MODPULL]]).

## Adjunction

[[D-DEFADJ]]

The pair $\inverseof{f}\dashv f_*$ is an adjunction of additive functors between abelian categories, so general facts about adjoint pairs apply without further hypotheses: the left adjoint preserves colimits and the right adjoint preserves limits ([[T-DEFRAPL]]).
So $f^{-1}$ preserves direct sums and cokernels, and $f_*$ preserves products, kernels, and fibre products ([[T-DEFRAPL]]).
The right adjoint need not preserve coproducts: for an infinite set $I$, $X=\coprod_{i\in I}\{i\}$ with $f\colon X\to\{\mathrm{pt}\}$ and $\mcf_i$ the sheaf $\ZZ$ on the $i$th point, $\bigl(f_*(\bigoplus_i\mcf_i)\bigr)(\mathrm{pt})=\prod_i\ZZ$ while $\bigl(\bigoplus_i f_*\mcf_i\bigr)(\mathrm{pt})=\bigoplus_i\ZZ$.

## Exactness of the two functors

[[PR-SHFPUSHEX]]

For a closed immersion $f_*$ is exact, so the cohomology of a closed subscheme can be computed in the ambient scheme.
For a proper morphism $f\colon X\to Y$ of noetherian schemes and a coherent $\mcf$, every $R^if_*\mcf$ is coherent ([[D-MODPULL]]), and the base-change theorems compare $(R^if_*\mcf)\otimes\kappa(y)$ with $H^i(X_y,\mcf_y)$ over points $y\in Y$ ([[T-BASECHANGE]]); the Leray spectral sequence computes $H^*(X,\mcf)$ from the higher direct images ([[T-COHLERAY]]).

## The projection formula

[[PR-SCHPROJFORM]]

The projection formula is the compatibility of the two functors with tensor: for $\mcg$ locally free of finite rank on $Y$, $f_*(\mcf\tensor f^*\mcg)\cong f_*\mcf\tensor\mcg$ [@Har77, Exercise II.5.1(d)], the finite local freeness being a hypothesis of the statement and not a convenience.
It is what makes pullback a map of $\OO_Y$-module categories rather than merely of abelian categories, and it is used whenever a twist is moved past a pushforward.

## Extension by zero

[[D-SHFSIX]]

Extension by zero is the functor that is left adjoint to restriction to an open set, and it exists for sheaves of abelian groups but not for quasicoherent sheaves: on $X=\AA^1_k$ with $j$ the inclusion of the complement of the origin, $j_!\OO_U$ has nonzero sections over $U$ and only zero sections over $X$, so its sections are not the localisation of its global sections and it is not quasicoherent ([[FE-MODZOO]]).
The functors $j_!$ and $Rf_!$ therefore act on sheaves of abelian groups, or on constructible coefficients, rather than on quasicoherent sheaves ([[T-LADICPROPER]]).
