import Mathlib

/-!
# `E-HAT-3.A-6` / `E-HAT-3.A-2`: `Tor₁` for an arbitrary abelian group

Mathlib master still has no comparison between `Tor` and filtered colimits and no balancing of
`Tor`, so the two cards' passage from the finitely generated case to an arbitrary `A` is proved
here along the Weibel route (`An Introduction to Homological Algebra`, §2.6: filtered colimits are
exact in `R`-mod, Cor. 2.6.16–2.6.17, p. 58), realised elementwise through the finitely generated
stages of `cards/TorStages.lean`: every element of `Tor₁(A,B)` descends to the stage of a finitely
generated free presentation, and there the two card statements are already available.

The bridge is dimension shifting (Weibel, Exercise 2.4.3): for **any** epimorphism `f : P ⟶ A`
with `P` projective, `Tor₁(A,B)` is the kernel of `ker f ⊗ B → P ⊗ B`. The resolution that
computes it is the splice `P`, then the canonical projective resolutions of the kernel, its
kernel, and so on — built with `ChainComplex.mk'` from Mathlib's `Projective.d`/`syzygies`, whose
exactness and quasi-isomorphism proofs are copied from `ProjectiveResolution.of`
(`Mathlib/CategoryTheory/Abelian/Projective/Resolution.lean`).
-/

open CategoryTheory Limits MonoidalCategory

namespace TorArbitrary

/-- `Tor₁`, the first left derived functor of `tensorLeft B`, as in the sibling certificates. -/
noncomputable abbrev torOne (A B : ModuleCat ℤ) : ModuleCat ℤ :=
  ((tensorLeft B).leftDerived 1).obj A

section Splice

variable {A P : ModuleCat ℤ} (f : P ⟶ A) [Epi f] [Projective P]

/-- **The splice resolution of `A` over the presentation `f`.** `P` in degree zero, then
`Projective.syzygies f` with the differential `Projective.d f`, then the canonical projective
resolutions of the kernels of the successive differentials. For `f = Projective.π A` this is
Mathlib's `ProjectiveResolution.of`; the general form is what an arbitrary presentation needs. -/
noncomputable def presComplex : ChainComplex (ModuleCat ℤ) ℕ :=
  ChainComplex.mk' P (Projective.syzygies f) (Projective.d f)
    (fun g => ⟨Projective.syzygies g, Projective.d g, by
      show (Projective.π (Limits.kernel g) ≫ Limits.kernel.ι g) ≫ g = 0
      rw [Category.assoc, Limits.kernel.condition, comp_zero]⟩)

theorem presComplex_d_1_0 : (presComplex f).d 1 0 = Projective.d f := rfl

set_option backward.isDefEq.respectTransparency.types false in
/-- The splice resolution is exact in every positive degree, as for `ProjectiveResolution.of`. -/
theorem presComplex_exactAt_succ (n : ℕ) : (presComplex f).ExactAt (n + 1) := by
  rw [HomologicalComplex.exactAt_iff' _ (n + 1 + 1) (n + 1) n (by simp) (by simp)]
  simp only [HomologicalComplex.sc', HomologicalComplex.shortComplexFunctor', presComplex,
    ChainComplex.mk', ChainComplex.mk, ChainComplex.of_d]
  match n with
  | 0 => apply exact_d_f
  | n + 1 => apply exact_d_f

instance (n : ℕ) : Projective ((presComplex f).X n) := by
  obtain (_ | _ | _ | n) := n
  · show Projective P
    infer_instance
  all_goals apply Projective.projective_over

/-- **The augmentation of the splice resolution onto `A`.** -/
noncomputable def presPi : presComplex f ⟶ (ChainComplex.single₀ (ModuleCat ℤ)).obj A :=
  (ChainComplex.toSingle₀Equiv _ _).symm ⟨f, by
    show (Projective.π (Limits.kernel f) ≫ Limits.kernel.ι f) ≫ f = 0
    rw [Category.assoc, Limits.kernel.condition, comp_zero]⟩

/-- The augmentation's degree-zero component is the presentation map itself. -/
theorem presPi_cond : (Projective.π (Limits.kernel f) ≫ Limits.kernel.ι f) ≫ f = 0 := by
  rw [Category.assoc, Limits.kernel.condition, comp_zero]

theorem presPi_f_zero : (presPi f).f 0 = f :=
  ChainComplex.toSingle₀Equiv_symm_apply_f_zero (C := presComplex f) (X := A) f
    (by show HomologicalComplex.d (presComplex f) 1 0 ≫ f = 0
        exact presPi_cond f)

/-- **The splice resolution is a projective resolution of `A`**, for any epimorphism `f` from a
projective: exactness and the quasi-isomorphism as for `ProjectiveResolution.of`, with the
degree-zero comparison through the cokernel cofork, as in `cards/TorFreeResolution.lean`. -/
noncomputable def presResolution : ProjectiveResolution A where
  complex := presComplex f
  projective := fun n => inferInstance
  π := presPi f
  quasiIso := by
    constructor
    intro n
    cases n
    · rw [ChainComplex.quasiIsoAt₀_iff]
      have hexact : Function.Exact (Projective.d f).hom f.hom :=
        LinearMap.exact_iff.mpr (exact_d_f f).moduleCat_range_eq_ker.symm
      have hsurj : Function.Surjective f.hom :=
        (ModuleCat.epi_iff_surjective f).mp inferInstance
      have hc := ModuleCat.isColimitCokernelCofork
        (f := ModuleCat.ofHom (Projective.d f).hom) (g := f) hexact hsurj
      refine (ShortComplex.quasiIso_iff_of_zeros'
        (φ := (HomologicalComplex.shortComplexFunctor' (ModuleCat ℤ) (ComplexShape.down ℕ) 1 0 0).map
          (presPi f)) rfl rfl rfl).2 ?_
      exact ⟨ShortComplex.exact_of_g_is_cokernel (S := _) hc, Limits.epi_of_isColimit_cofork hc⟩
    · rw [quasiIsoAt_iff_exactAt']
      · apply presComplex_exactAt_succ
      · apply ChainComplex.exactAt_succ_single_obj

end Splice

section TensorSplice

variable {A P : ModuleCat ℤ} (f : P ⟶ A) [Epi f] [Projective P] (B : ModuleCat ℤ)

/-- The tensored splice complex: the tensor functor applied degreewise to `presComplex f`. -/
noncomputable abbrev tensorSplice : ChainComplex (ModuleCat ℤ) ℕ :=
  ((tensorLeft B).mapHomologicalComplex (ComplexShape.down ℕ)).obj (presComplex f)

/-- **The bridge at an arbitrary presentation.** `Tor₁(A,B)` is the first homology of the tensored
splice, exactly as `ProjectiveResolution.isoLeftDerivedObj` computes it for the canonical
resolution. -/
noncomputable def torOneIsoTensorSplice :
    torOne A B ≅ (HomologicalComplex.homologyFunctor (ModuleCat ℤ) (ComplexShape.down ℕ) 1).obj
      (tensorSplice f B) :=
  (presResolution f).isoLeftDerivedObj (tensorLeft B) 1

end TensorSplice

end TorArbitrary

