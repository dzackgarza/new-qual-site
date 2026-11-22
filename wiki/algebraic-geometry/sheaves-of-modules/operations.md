---
title: Operations and functoriality
order: 3
topics:
- Sheaves Of Modules
- Pullback
- Ideal Sheaves
---

# Operations and functoriality

[[D-MODOX]]

## Pullback and pushforward

Pullback and pushforward are the basic functors relating sheaves on the source and target of a morphism.

[[D-MODPULL]]

For a morphism of ringed spaces $f\colon X\to Y$, the module pullback $f^*\mcg=f^{-1}\mcg\otimes_{f^{-1}\OO_Y}\OO_X$ is left adjoint to $f_*$ ([[D-MODPULL]]).
Hence $f^*$ is right exact and $f_*$ is left exact; the higher direct images $R^if_*$ are the right derived functors of $f_*$ ([[D-COHRIF]]).

The inverse image $f^{-1}$ of abelian sheaves is exact, but the tensor product in $f^*$ need not preserve kernels.
For the closed point $f\colon\Spec\FF_p\to\Spec\ZZ$, the injection $\ZZ\xrightarrow{p}\ZZ$ pulls back to the zero map $\FF_p\to\FF_p$, the module-level computation of [[D-DEFTENS]] in which $p\otimes1=0$.
If $f$ is flat, $f^*$ is exact ([[D-MODPULL]], [[D-MORFLAT]]).

On schemes, $f^*$ preserves quasicoherent sheaves, and coherent sheaves when $X$ and $Y$ are locally noetherian ([[D-MODPULL]]).
The pushforward $f_*$ preserves quasicoherent sheaves when $f$ is quasicompact and separated, and for $f$ proper with $Y$ locally noetherian and $\mcf$ coherent, every $R^if_*\mcf$ is coherent ([[D-MODPULL]]).

## The four functors for abelian sheaves

For $f \colon X \to Y$ continuous, the direct image $f_*$ and the inverse image $f^{-1}$ are adjoint, $f^{-1}\dashv f_*$, with $f^{-1}$ exact. For a continuous map of locally compact Hausdorff spaces, the direct image with proper supports $f_!$ has the exceptional inverse image $f^!$ as right adjoint on derived categories ([[D-SHFSIX]]).
For an open immersion $j$, $j_!$ is extension by zero, exact and left adjoint to $j^{-1}$; for a closed immersion $i$, $i_!=i_*$ and $i^!\mcf$ is the sections supported in $Z$ ([[D-SHFSIX]]).
$f_!$ and $f^!$ use the zero section of an abelian sheaf, so they do not transfer to sheaves of sets.
Together with $\otimes$ and internal $\mathcal{H}om$ these are the six operations ([[D-SHFSIX]], [[D-MODOX]]).
For $\OO_X$-modules the pullback is written $f^*$ ([[D-MODPULL]]).

## Ideal sheaves

[[D-MODIDEAL]]

For a closed subscheme $i\colon Z\hookrightarrow X$ with ideal sheaf $\mci_Z$, $H^j(Z,\OO_Z)\cong H^j(X,i_*\OO_Z)$, and the long exact sequence of $0\to\mci_Z\to\OO_X\to i_*\OO_Z\to0$ relates $H^j(Z,\OO_Z)$ to $H^j(X,\OO_X)$ and $H^{j+1}(X,\mci_Z)$ ([[PR-COHLES]], [[D-COHRIF]]).

## What separates the classes

[[FE-MODZOO]]
