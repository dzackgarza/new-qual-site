---
title: Derived functors and vanishing
order: 3
topics:
- Derived Functors
- Flasque Sheaves
- Vanishing Theorems
---

# Derived functors and vanishing

Where the theory comes from, and the two vanishing statements that bound every computation from above and below.

[[D-COHDER]]

The definition has two halves: the functor is right derived because $\globsec{X;\wait}$ is only left exact, and the resolution may be by anything acyclic.

[[D-COHFLQ]]

Flasque sheaves are the practical supply of acyclics, and the class exhibited by hand in proofs.
Injective implies flasque implies acyclic, and the second implication is acyclicity of flasque sheaves.

## The two bounds

[[T-COHAFF]]

[[T-COHGROTH]]

These bound cohomology from opposite ends.
Affine vanishing says a single affine chart contributes nothing above degree $0$, so all cohomology is a gluing phenomenon; Grothendieck vanishing says nothing survives above the dimension of the space.
The hypotheses are complementary: affine vanishing needs the sheaf to be quasicoherent and says nothing about others, while Grothendieck vanishing holds for every abelian sheaf and needs the space to be Noetherian.

## The long exact sequence

[[PR-COHLES]]

The sequence turns the theorems into numbers: applied to the twisted ideal sequence or the skyscraper sequence, with one term known from projective space, it computes the cohomology of the twists.
