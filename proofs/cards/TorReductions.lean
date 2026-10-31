import Mathlib

/-!
# `E-HAT-3.A-6`: the Tor reductions, at the presentation level

Hatcher, *Algebraic Topology*, §3.A defines `Tor(H, G)` as the homology of `F ⊗ G` for a
free resolution `F` of `H` (Lemma 3A.2 shows the choice of resolution does not matter) and
collects the computational rules in Proposition 3A.5:

1. `Tor(A, B) ≅ Tor(B, A)`
2. `Tor(⊕ i, A i, B) ≅ ⊕ i, Tor(A i, B)`
3. `Tor(A, B) = 0` if `A` or `B` is free, or more generally torsion-free
4. `Tor(A, B) ≅ Tor(T(A), B)` for the torsion subgroup `T(A)`
5. `Tor(ℤₙ, A) ≅ ker(A --n--> A)`
6. the long exact sequence of a short exact sequence in either variable

The card cites these items by number. What this file certifies, with no hypothesis beyond
`AddCommGroup`, is the part of the reduction that Mathlib already supplies or that is
immediate from the definitions:

* `torKernel`: the presentation-level group `ker(f ⊗ id_B)` of a presentation `f : K →ₗ F`,
  which is Hatcher's `Tor` for that resolution;
* `torKernel_eq_bot_of_subsingleton`: the free case of item (3) — if the kernel of the
  presentation is trivial (so the presented group is free) then `Tor` vanishes;
* `torsionBy_eq_ker`: `Submodule.torsionBy ℤ B n` is the kernel of multiplication by `n`,
  which is the group on the right-hand side of item (5);
* `flat_of_torsionFree`: every torsion-free `ℤ`-module is flat, the hypothesis behind the
  "more generally torsion-free" clause of item (3) and behind the step
  `Tor(A_p, B) ≅ Tor(A_p, B_p)` of the card. This is not reproved: `ℤ` is a Dedekind
  domain and Mathlib's `RingTheory/Flat/TorsionFree.lean` carries the instance
  `IsTorsionFree R M → Flat R M`;
* `rTensor_injective_of_flat`: Mathlib's flatness form of item (6), that tensoring with a
  flat module preserves injectivity, which is what makes the connecting map of item (6)
  vanish for a flat quotient.

Not formalized here, and cited on the card by number: the comparison theorem making `Tor`
independent of the resolution (Lemma 3A.2), additivity (item (2)), the reduction to the
torsion subgroup (item (4)), the identification `Tor(ℤₙ, B) ≅ B[n]` (item (5)) and the
commutation with direct limits (Exercise 4 of §3.A). The first of these is the obstruction:
`CategoryTheory.Tor` in Mathlib has no long exact sequence or comparison API, and the
identification in item (5) runs through `TensorProduct.lid`, whose `smul` is the
`DistribMulAction` one while `AddCommGroup` supplies the `ZSMul` one, so that statement has
to be set up with a single `SMul ℤ _` instance before it can be formalized.
-/

namespace TorReductions

open TensorProduct

/-- Multiplication by an integer, as an endomorphism of `ℤ`. -/
def mulByInt (n : ℤ) : ℤ →ₗ[ℤ] ℤ where
  toFun r := n * r
  map_add' r s := by ring
  map_smul' c r := by
    show n * (c * r) = c * (n * r)
    ring

@[simp]
theorem mulByInt_apply (n r : ℤ) : mulByInt n r = n * r := rfl

variable {B : Type*} [AddCommGroup B]

/-- The presentation-level `Tor`: for a presentation `f : K →ₗ[ℤ] F` and a group `B`, the
kernel of `f ⊗ id_B`. -/
def torKernel {K F : Type*} [AddCommGroup K] [AddCommGroup F]
    (f : K →ₗ[ℤ] F) : Submodule ℤ (TensorProduct ℤ K B) :=
  (f.rTensor B).ker

/-- Hatcher, Proposition 3A.5(3), the free case at the presentation level: a presentation
whose kernel is trivial presents a free group, and then `Tor` vanishes. -/
theorem torKernel_eq_bot_of_subsingleton {K F : Type*} [AddCommGroup K] [AddCommGroup F]
    [Subsingleton K] (f : K →ₗ[ℤ] F) : torKernel (B := B) f = ⊥ :=
  Subsingleton.elim _ _

/-- Hatcher, Proposition 3A.5(5), the group on the right: the `n`-torsion of `B` is the
kernel of multiplication by `n`. -/
theorem torsionBy_eq_ker (n : ℤ) :
    Submodule.torsionBy ℤ B n = (DistribSMul.toLinearMap ℤ B n).ker := rfl

/-- Hatcher, Proposition 3A.5(3), hypothesis: a torsion-free `ℤ`-module is flat. Reused from
Mathlib's Dedekind-domain instance rather than reproved. -/
theorem flat_of_torsionFree {M : Type*} [AddCommGroup M] [Module.IsTorsionFree ℤ M] :
    Module.Flat ℤ M :=
  inferInstance

/-- Hatcher, Proposition 3A.5(6), the flatness form: tensoring with a flat module preserves
injectivity, so a flat quotient kills the connecting map. Reused from Mathlib. -/
theorem rTensor_injective_of_flat {M N P : Type*} [AddCommGroup M] [AddCommGroup N]
    [AddCommGroup P] [Module.Flat ℤ M] (f : N →ₗ[ℤ] P) (hf : Function.Injective f) :
    Function.Injective (LinearMap.rTensor M f) :=
  Module.Flat.rTensor_preserves_injective_linearMap f hf

end TorReductions

#print axioms TorReductions.torKernel_eq_bot_of_subsingleton
#print axioms TorReductions.torsionBy_eq_ker
#print axioms TorReductions.flat_of_torsionFree
#print axioms TorReductions.rTensor_injective_of_flat
