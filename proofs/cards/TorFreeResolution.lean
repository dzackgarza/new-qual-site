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

/-- The differential of the two-term complex is a monomorphism: it is the inclusion of the syzygy
into `ℤⁿ`. This is what makes `H₁` vanish. -/
theorem twoTermComplex_mono_d_one_zero :
    Mono ((twoTermComplex r f).d 1 0) := by
  rw [twoTermComplex_d_one_zero]
  exact ModuleCat.mono_as_hom'_subtype (R := ℤ) (X := ModuleCat.of ℤ (Fin r → ℤ))
    (LinearMap.ker f)

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

/-! ## The homology of the two-term complex

`H₁` vanishes because the differential is the inclusion of the syzygy, and every degree from `2` up
is the zero object. These are the vanishing half of the quasi-isomorphism computation; `H₀` is
`F/K ≅ A`, which needs `f` surjective and is treated separately. -/

/-- A short complex with vanishing incoming differential has homology its kernel. Copied from the
sibling certificate rather than imported: a file under `proofs/cards/` has no olean of its siblings
on the search path. -/
noncomputable def homologyIsoKernelOfZero {S : ShortComplex (ModuleCat ℤ)} (hf : S.f = 0) :
    S.homology ≅ Limits.kernel S.g :=
  (ShortComplex.LeftHomologyData.ofHasKernel S hf).homologyIso

/-- The degree-`1` homology of a chain complex, with the incoming differential vanishing, is the
kernel of the outgoing one. -/
noncomputable def homologyOneIsoKernelOfD {K : ChainComplex (ModuleCat ℤ) ℕ}
    (h : K.d 2 1 = 0) : K.homology 1 ≅ Limits.kernel (K.d 1 0) :=
  (K.homologyIsoSc' 2 1 0
      (ComplexShape.prev_eq' (c := ComplexShape.down ℕ) (by simp))
      (ComplexShape.next_eq' (c := ComplexShape.down ℕ) (by simp))) ≪≫
    homologyIsoKernelOfZero (S := K.sc' 2 1 0) h

/-- The same from the shape hypothesis `IsZero (K.X 2)`. -/
noncomputable def homologyOneIsoKernel {K : ChainComplex (ModuleCat ℤ) ℕ} (h2 : IsZero (K.X 2)) :
    K.homology 1 ≅ Limits.kernel (K.d 1 0) :=
  homologyOneIsoKernelOfD (K := K) (IsZero.eq_of_src h2 _ _)

/-- A kernel module with its structure pinned to the submodule structure, so that
`ModuleCat.kernelIsoKer` and the surrounding statements mention one instance. -/
noncomputable abbrev kerModule {M N : ModuleCat ℤ} (g : M ⟶ N) : ModuleCat ℤ :=
  letI := g.hom.ker.module
  ModuleCat.of ℤ ↥(g.hom.ker)

/-- `ModuleCat.kernelIsoKer` stated at that pinned boundary. -/
noncomputable def kernelIsoKerModule {M N : ModuleCat ℤ} (g : M ⟶ N) :
    Limits.kernel g ≅ kerModule g :=
  ModuleCat.kernelIsoKer (R := ℤ) g

/-- **A kernel of a map out of a zero object is zero.** This is the step that makes the homology
vanish in every degree where the complex itself is zero: `ModuleCat.kernelIsoKer` presents the
categorical kernel as the linear-map kernel, and a map out of a trivial module has all of its domain
in its kernel. -/
theorem isZero_kernel_of_isZero_source {X Y : ModuleCat ℤ} (g : X ⟶ Y) (hX : IsZero X) :
    IsZero (Limits.kernel g) := by
  haveI : Subsingleton ↥X := ModuleCat.subsingleton_of_isZero hX
  haveI : Subsingleton ↥(g.hom.ker) :=
    ⟨fun a b => Subtype.ext (Subsingleton.elim (a : ↥X) (b : ↥X))⟩
  exact IsZero.of_iso (ModuleCat.isZero_of_subsingleton (kerModule g)) (kernelIsoKerModule g)

/-- The degree-`k+2` homology of a chain complex, when the incoming differential vanishes, is the
kernel of the outgoing one. -/
noncomputable def homologyIsoKernelAt (K : ChainComplex (ModuleCat ℤ) ℕ) (k : ℕ)
    (h : K.d (k + 3) (k + 2) = 0) :
    K.homology (k + 2) ≅ Limits.kernel (K.d (k + 2) (k + 1)) :=
  (K.homologyIsoSc' (k + 3) (k + 2) (k + 1)
      (ComplexShape.prev_eq' (c := ComplexShape.down ℕ) (by simp))
      (ComplexShape.next_eq' (c := ComplexShape.down ℕ) (by simp))) ≪≫
    homologyIsoKernelOfZero (S := K.sc' (k + 3) (k + 2) (k + 1)) h

/-- **The two-term complex has no homology above degree zero**, besides the vanishing of `H₁`
proved separately: for `n ≥ 2` the degree-`n` term is the zero object, so the degree-`n` homology is
the kernel of a map out of it. -/
theorem twoTermComplex_homology_isZero (k : ℕ) :
    IsZero ((twoTermComplex r f).homology (k + 2)) := by
  have hzero3 : IsZero ((twoTermComplex r f).X (k + 3)) :=
    twoTermComplex_isZero_X r f (k + 3) (by omega)
  have hd : (twoTermComplex r f).d (k + 3) (k + 2) = 0 := IsZero.eq_of_src hzero3 _ _
  refine IsZero.of_iso (isZero_kernel_of_isZero_source
    ((twoTermComplex r f).d (k + 2) (k + 1)) (twoTermComplex_isZero_X r f (k + 2) (by omega)))
    (homologyIsoKernelAt (twoTermComplex r f) k hd)

/-- **`H₁` of the two-term complex vanishes**: the differential is the inclusion of the syzygy,
which is a monomorphism, so its kernel is the zero object. -/
theorem twoTermComplex_homology_one_isZero :
    IsZero ((twoTermComplex r f).homology 1) := by
  haveI : Mono ((twoTermComplex r f).d 1 0) := twoTermComplex_mono_d_one_zero r f
  exact IsZero.of_iso (isZero_kernel_of_mono ((twoTermComplex r f).d 1 0))
    (homologyOneIsoKernel (twoTermComplex_isZero_X_two r f))

end TwoTerm

end TorFreeResolution

#print axioms TorFreeResolution.syzygy_finite
#print axioms TorFreeResolution.syzygy_torsionFree
#print axioms TorFreeResolution.syzygy_free
#print axioms TorFreeResolution.syzygy_projective
#print axioms TorFreeResolution.free_projective
#print axioms TorFreeResolution.presentation_projective
#print axioms TorFreeResolution.twoTermComplex
#print axioms TorFreeResolution.twoTermComplex_isZero_X
#print axioms TorFreeResolution.twoTermComplex_isZero_X_two
#print axioms TorFreeResolution.twoTermComplex_projective
#print axioms TorFreeResolution.twoTermPi
#print axioms TorFreeResolution.isZero_kernel_of_isZero_source
#print axioms TorFreeResolution.twoTermComplex_homology_isZero
#print axioms TorFreeResolution.twoTermComplex_homology_one_isZero
