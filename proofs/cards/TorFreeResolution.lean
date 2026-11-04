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

namespace TorFreeResolution

variable {A : Type*} [AddCommGroup A] [Module ℤ A]

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

end TorFreeResolution

#print axioms TorFreeResolution.syzygy_finite
#print axioms TorFreeResolution.syzygy_torsionFree
#print axioms TorFreeResolution.syzygy_free
#print axioms TorFreeResolution.syzygy_projective
#print axioms TorFreeResolution.free_projective
#print axioms TorFreeResolution.presentation_projective
