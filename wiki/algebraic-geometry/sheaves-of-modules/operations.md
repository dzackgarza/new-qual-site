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

The pattern to expect is that $f^*$ is the easy half and $f_*$ is where the theorems are.
Pulling back is a tensor product, so it is right exact and preserves everything; pushing forward is left exact, its derived functors are the higher direct images, and it preserves coherence only under properness.
This asymmetry is the reason cohomology exists as a subject rather than as a computation.

## The four functors for sheaves of sets

For $f \colon X \to Y$ continuous:

- $f_* \colon \Sh(X) \to \Sh(Y)$, $(f_*\mcf)(V) = \mcf(f^{-1}V)$, the direct image or pushforward;

- $f^{-1} \colon \Sh(Y) \to \Sh(X)$, the inverse image or pullback, left adjoint to $f_*$;

- $f_! \colon \Sh(X) \to \Sh(Y)$, extension by zero when $f$ is an open or closed immersion, read as ``$f$ lower shriek'';

- $f^! \colon \Sh(Y) \to \Sh(X)$, the exceptional inverse image, read as ``$f$ upper shriek''.

These are the four among the six operations; the remaining two are $\otimes$ and $\sHom$.
For $\OO_X$-modules the same symbols are written $f^*$ for the module pullback.

## Ideal sheaves

[[D-MODIDEAL]]

The closed subscheme sequence is the standard way to move a question about a subvariety into the ambient space, where the twists are available and the cohomology is known.

## What separates the classes

[[FE-MODZOO]]
