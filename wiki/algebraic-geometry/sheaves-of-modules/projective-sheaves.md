---
title: Sheaves on projective space
order: 5
topics:
- Graded Modules
- Ampleness
- Coherent Sheaves
---

# Sheaves on projective space

On $\Spec A$, $M\mapsto\widetilde M$ is an equivalence from $A$-modules to quasicoherent sheaves.
On $\Proj S$ it is not: graded $S$-modules that agree in all degrees $\ge n_0$ give isomorphic sheaves, and a graded module annihilated by a power of the irrelevant ideal $S_+$ gives $0$.

[[D-MODGRMOD]]

Sheafification from graded modules is not injective: modules differing only in low degrees, and modules supported on the irrelevant ideal, can give the same sheaf.
$\Gamma_*$ is the section that puts a canonical module back.

## Generation and ampleness

[[D-MODGG]]

Global generation is what turns sections into a morphism to $\PP^n$.
Every quasicoherent sheaf on an affine scheme is globally generated, so global generation becomes restrictive on nonaffine schemes such as projective schemes.

[[D-MODAMPLE]]

The three conditions form a ladder: globally generated gives a morphism, very ample gives a closed immersion, and ample means that some positive power is very ample.
Ampleness is preserved by positive tensor powers.

## Serre's theorems

[[T-MODSERRE]]

Both parts say that a coherent sheaf on projective space acquires affine-like properties after sufficiently positive twisting.

[[T-MODRES]]

Finite resolutions by twists reduce additive invariants of coherent sheaves to the corresponding invariants of $\OO(d)$, including the computation of cohomology in [[algebraic-geometry/cohomology/index|cohomology]].
