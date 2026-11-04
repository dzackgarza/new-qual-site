import Mathlib

/-!
# The syzygy of a finite free presentation is free

`proofs/README.md` §5b records that the application of Hatcher's Lemma 3A.2 to the cards needs a
*genuine* free resolution of `A`, with the hypotheses of the stage lemmas checked, and that no file
here supplied that instantiation. The decisive hypothesis is that the kernel of a finite free
presentation is again projective — over `ℤ`, free.

This file supplies it, and the proof is an instance chain rather than new mathematics:

* `ℤⁿ` is a Noetherian module, so a submodule of it is finitely generated;
* a submodule of a torsion-free module is torsion-free;
* over a PID a finitely generated torsion-free module is free
  (`Module.free_of_finite_type_torsion_free'`, the primed form at this pin);
* a free module is projective, so both terms of `0 → K → ℤⁿ → A → 0` are projective — which is what
  `ProjectiveResolution` requires of every degree.

The general case — an arbitrary index set, i.e. "every subgroup of a free abelian group is free" —
is *not* available at this pin and is recorded as an upstream gap in §5b; it is not needed for the
cards, whose stages are finitely generated.
-/

open CategoryTheory Limits
open scoped ZeroObject

namespace TorFreeResolution

variable {A : Type} [AddCommGroup A] [Module ℤ A]

/-- The syzygy of a map out of `ℤⁿ` is finitely generated: it is a submodule of a Noetherian
module. -/
theorem syzygy_finite (n : ℕ) (f : (Fin n → ℤ) →ₗ[ℤ] A) :
    Module.Finite ℤ ↥(LinearMap.ker f) :=
  inferInstance

/-- The syzygy is torsion-free, being a submodule of a free `ℤ`-module. -/
theorem syzygy_torsionFree (n : ℕ) (f : (Fin n → ℤ) →ₗ[ℤ] A) :
    Module.IsTorsionFree ℤ ↥(LinearMap.ker f) :=
  inferInstance

/-- **The syzygy of a finite free presentation is free.** This is the hypothesis that makes the
two-term complex `0 → K → ℤⁿ → A → 0` a *projective* resolution, and it is exactly what §5b's
instantiation was missing. Over a PID, finitely generated plus torsion-free is free. -/
theorem syzygy_free (n : ℕ) (f : (Fin n → ℤ) →ₗ[ℤ] A) :
    Module.Free ℤ ↥(LinearMap.ker f) :=
  Module.free_of_finite_type_torsion_free'

/-- The syzygy, as an object of `ModuleCat ℤ`, is projective — so it may sit in degree `1` of a
projective resolution. -/
theorem syzygy_projective (n : ℕ) (f : (Fin n → ℤ) →ₗ[ℤ] A) :
    CategoryTheory.Projective (ModuleCat.of ℤ ↥(LinearMap.ker f)) :=
  inferInstance

/-- The middle term of the presentation, `ℤⁿ`, is projective. -/
theorem free_projective (n : ℕ) :
    CategoryTheory.Projective (ModuleCat.of ℤ (Fin n → ℤ)) :=
  inferInstance

/-- Both terms of the two-term presentation are projective, which is the condition
`ProjectiveResolution` imposes degreewise; stated together because that is how the resolution
consumes it. -/
theorem presentation_projective (n : ℕ) (f : (Fin n → ℤ) →ₗ[ℤ] A) :
    CategoryTheory.Projective (ModuleCat.of ℤ ↥(LinearMap.ker f)) ∧
      CategoryTheory.Projective (ModuleCat.of ℤ (Fin n → ℤ)) :=
  ⟨syzygy_projective n f, free_projective n⟩

/-! ## The two-term projective complex of a finite free presentation

`0 → K → ℤⁿ → A → 0` as a chain complex concentrated in degrees `0` and `1`. It is built with
`ChainComplex.mk'`, whose inductive continuation is the zero complex, so degree `2` and above are
literally the zero object — which is the shape `torOneIsoTorKernel` needs (`IsZero (X 2)`). -/

section TwoTerm

variable (r : ℕ) (f : (Fin r → ℤ) →ₗ[ℤ] A)

/-- The two-term complex `K → ℤⁿ → 0 → 0 → ⋯` attached to a finite free presentation. -/
noncomputable def twoTermComplex : ChainComplex (ModuleCat ℤ) ℕ :=
  ChainComplex.mk' (ModuleCat.of ℤ (Fin r → ℤ)) (ModuleCat.of ℤ ↥(LinearMap.ker f))
    (ModuleCat.ofHom (LinearMap.ker f).subtype)
    (fun _ => ⟨0, 0, by simp⟩)

/-- Degree `0` of the complex is `ℤⁿ`. -/
theorem twoTermComplex_X_zero : (twoTermComplex r f).X 0 = ModuleCat.of ℤ (Fin r → ℤ) :=
  ChainComplex.mk'_X_0 ..

/-- Degree `1` of the complex is the syzygy. -/
theorem twoTermComplex_X_one : (twoTermComplex r f).X 1 = ModuleCat.of ℤ ↥(LinearMap.ker f) :=
  ChainComplex.mk'_X_1 ..

/-- The only nonzero differential is the inclusion of the syzygy. -/
theorem twoTermComplex_d_one_zero :
    (twoTermComplex r f).d 1 0 = ModuleCat.ofHom (LinearMap.ker f).subtype :=
  ChainComplex.mk'_d_1_0 ..

/-- **Degree two vanishes**: the complex is two-term, which is the hypothesis `torOneIsoTorKernel`
carries. -/
theorem twoTermComplex_isZero_X_two : IsZero ((twoTermComplex r f).X 2) :=
  IsZero.of_iso (isZero_zero (ModuleCat ℤ))
    (ChainComplex.mk'XIso (ModuleCat.of ℤ (Fin r → ℤ)) (ModuleCat.of ℤ ↥(LinearMap.ker f))
      (ModuleCat.ofHom (LinearMap.ker f).subtype) (fun _ => ⟨0, 0, by simp⟩) 0)

/-- Every degree from `2` up is the zero object: the complex really is two-term. -/
theorem twoTermComplex_isZero_X (n : ℕ) (hn : 2 ≤ n) : IsZero ((twoTermComplex r f).X n) := by
  obtain ⟨k, rfl⟩ : ∃ k, n = k + 2 := ⟨n - 2, by omega⟩
  exact IsZero.of_iso (isZero_zero (ModuleCat ℤ))
    (ChainComplex.mk'XIso (ModuleCat.of ℤ (Fin r → ℤ)) (ModuleCat.of ℤ ↥(LinearMap.ker f))
      (ModuleCat.ofHom (LinearMap.ker f).subtype) (fun _ => ⟨0, 0, by simp⟩) k)

/-- Every degree of the two-term complex is projective, so it can be a `ProjectiveResolution`. -/
theorem twoTermComplex_projective (n : ℕ) : Projective ((twoTermComplex r f).X n) := by
  match n with
  | 0 => exact free_projective r
  | 1 => exact syzygy_projective r f
  | k + 2 =>
    exact Projective.of_iso (Iso.symm (ChainComplex.mk'XIso (ModuleCat.of ℤ (Fin r → ℤ))
      (ModuleCat.of ℤ ↥(LinearMap.ker f)) (ModuleCat.ofHom (LinearMap.ker f).subtype)
      (fun _ => ⟨0, 0, by simp⟩) k)) (inferInstance : Projective (0 : ModuleCat ℤ))

/-- The augmentation of the two-term complex onto `A`, i.e. the map `F → A` in degree zero and zero
above it. It exists precisely because `f` kills the syzygy, which is the side condition
`ChainComplex.toSingle₀Equiv` asks for. -/
noncomputable def twoTermPi :
    twoTermComplex r f ⟶ (ChainComplex.single₀ (ModuleCat ℤ)).obj (ModuleCat.of ℤ A) :=
  (ChainComplex.toSingle₀Equiv _ _).symm ⟨ModuleCat.ofHom f, by
    rw [twoTermComplex_d_one_zero]
    apply ModuleCat.hom_ext
    ext x
    exact x.2⟩

end TwoTerm

end TorFreeResolution

#print axioms TorFreeResolution.syzygy_finite
#print axioms TorFreeResolution.syzygy_torsionFree
#print axioms TorFreeResolution.syzygy_free
#print axioms TorFreeResolution.syzygy_projective
#print axioms TorFreeResolution.free_projective
#print axioms TorFreeResolution.presentation_projective
#print axioms TorFreeResolution.twoTermComplex
#print axioms TorFreeResolution.twoTermComplex_isZero_X_two
#print axioms TorFreeResolution.twoTermComplex_projective
#print axioms TorFreeResolution.twoTermPi
#print axioms TorFreeResolution.twoTermComplex_isZero_X
