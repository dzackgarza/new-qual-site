---
title: Operations and functoriality
order: 3
topics:
- Sheaves Of Modules
- Pullback
- Ideal Sheaves
---

# Operations and functoriality

Before any sheaf is quasicoherent it is a sheaf of modules, and the category it lives in has the operations the rest of the subject is written with.

[[D-MODOX]]

## Pullback and pushforward

Every geometric construction in the subject is one of these two applied to a sheaf one already understands.

[[D-MODPULL]]

For a morphism of ringed spaces $f\colon X\to Y$, the module pullback $f^*\mcg=f^{-1}\mcg\otimes_{f^{-1}\OO_Y}\OO_X$ is left adjoint to $f_*$.
Hence $f^*$ is right exact and $f_*$ is left exact; the higher direct images $R^if_*$ are the right derived functors of $f_*$.

The inverse image $f^{-1}$ of abelian sheaves is exact, but the tensor product in $f^*$ need not preserve kernels.
For the closed point $f\colon\Spec\FF_p\to\Spec\ZZ$, the injection $\ZZ\xrightarrow{p}\ZZ$ pulls back to the zero map $\FF_p\to\FF_p$.
If $f$ is flat, $f^*$ is exact.

On schemes, $f^*$ preserves quasicoherent sheaves, sheaves of finite type, and coherent sheaves when $X$ and $Y$ are locally noetherian.
The pushforward $f_*$ preserves quasicoherent sheaves when $f$ is quasicompact and quasiseparated, and preserves coherent sheaves when $f$ is proper and $Y$ is locally noetherian.

## The four functors for abelian sheaves

For $f \colon X \to Y$ continuous:

- $f_* \colon \Sh(X) \to \Sh(Y)$, $(f_*\mcf)(V) = \mcf(f^{-1}V)$, the direct image or pushforward, left exact;

- $f^{-1} \colon \Sh(Y) \to \Sh(X)$, the inverse image, left adjoint to $f_*$ and exact;

- $f_!$, the direct image with proper supports, defined for sheaves of abelian groups by taking the sections of $f_*\mcf$ whose support is proper over $Y$.
  For an open immersion $j$, $j_!$ is extension by zero, which is exact and left adjoint to $j^{-1}$; for a closed immersion $i$, $i_!=i_*$;

- $f^!$, the exceptional inverse image.
  For a closed immersion $i\colon Z\to X$, $i^!\mcf$ is the restriction to $Z$ of the sheaf of sections of $\mcf$ supported in $Z$, right adjoint to $i_*$ on abelian sheaves.
  For a general $f$ it exists only on derived categories, as a right adjoint to $Rf_!$ when $X$ and $Y$ are locally compact Hausdorff and $f_!$ has finite cohomological dimension (Verdier duality).

$f_!$ and $f^!$ use the zero section of an abelian sheaf, so they do not transfer to sheaves of sets.
Together with $\otimes$ and internal $\mathcal{H}om$ these are the six operations.
For $\OO_X$-modules the pullback is written $f^*$.

## Ideal sheaves

[[D-MODIDEAL]]

The closed subscheme sequence is the standard way to move a question about a subvariety into the ambient space, where the twists are available and the cohomology is known.

## What separates the classes

[[FE-MODZOO]]
