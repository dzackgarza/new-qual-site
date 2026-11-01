import Mathlib

/-!
# The projective-resolution bridge for `Tor`

`Tor₁` is the first left derived functor of `tensorLeft B`. `ProjectiveResolution.isoLeftDerivedObj`
computes that derived functor from a chosen projective resolution: the value at `A` is the first
homology of the complex `P.complex ⊗ B`. This file records that bridge as an elaborated theorem, at the
generality of `ModuleCat ℤ`, and states precisely the one finite step that is *not* taken here — the
identification of that homology with the kernel of the degree-1 differential for a two-term resolution,
which is what connects it to the presentation-level `torKernel` of `cards/TorReductions.lean`.

Nothing here rebuilds homology: the derived functor, the projective resolution, `mapHomologicalComplex`
and the homology functor are the maintained ones.
-/

open CategoryTheory Limits MonoidalCategory

namespace TorBridge

/-- `Tor₁(A, B)`, as the first left derived functor of `tensorLeft B` evaluated at `A`. -/
noncomputable abbrev torOne (A B : ModuleCat ℤ) : ModuleCat ℤ :=
  ((tensorLeft B).leftDerived 1).obj A

/-- The complex `P ⊗ B` attached to a projective resolution `P` of `A`: the tensor functor applied
degreewise to `P.complex`. -/
noncomputable abbrev resolutionTensor (B : ModuleCat ℤ) {A : ModuleCat ℤ}
    (P : ProjectiveResolution A) : ChainComplex (ModuleCat ℤ) ℕ :=
  ((tensorLeft B).mapHomologicalComplex (ComplexShape.down ℕ)).obj P.complex

/-- **The bridge.** For every abelian group `A` and `B` and every projective resolution `P` of `A`,
`Tor₁(A, B)` is the first homology of the tensored resolution `P ⊗ B`. This is
`ProjectiveResolution.isoLeftDerivedObj` applied to the additive functor `tensorLeft B` at degree one:
no new machinery, and no hypothesis on the resolution beyond its being projective. -/
noncomputable def torOneIsoHomology {A B : ModuleCat ℤ} (P : ProjectiveResolution A) :
    torOne A B ≅
      (HomologicalComplex.homologyFunctor (ModuleCat ℤ) (ComplexShape.down ℕ) 1).obj
        (resolutionTensor B P) :=
  P.isoLeftDerivedObj (tensorLeft B) 1

/-- The degree-`1` differential of the tensored resolution, in the form the kernel step needs. -/
noncomputable abbrev tensorDiffOne (B : ModuleCat ℤ) {A : ModuleCat ℤ}
    (P : ProjectiveResolution A) :
    (resolutionTensor B P).X 1 ⟶ (resolutionTensor B P).X 0 :=
  (resolutionTensor B P).d 1 0

/-! ## The one step not taken here, stated exactly

For a two-term resolution — `P.complex` with `X 2 = 0`, so that the complex is `K → F → 0` — the first
homology of `P.complex ⊗ B` is the kernel of `d 1 0 ⊗ B`, because there is nothing in degree two to
quotient by:

`IsZero ((P.complex).X 2) → H₁(P.complex ⊗ B) ≅ kernel ((P.complex).d 1 0 ⊗ B)`.

Composing that with `torOneIsoHomology` would identify `Tor₁(A,B)` with the presentation-level
`torKernel` of `cards/TorReductions.lean`, i.e. with `ker(K ⊗ B → F ⊗ B)` for `A = F/K`.

It is not proved here. It is a finite statement about `ShortComplex` homology —
`ShortComplex.cyclesIsoKernel` gives `S.cycles ≅ kernel S.g`, and with `S.X₁` a zero object
(`IsZero (K.X 2)` for `S = K.sc 1`) the homology, which is the cokernel of `S.toCycles`, is
`S.cycles` up to the cokernel of a zero map — and it is recorded here rather than glossed: the
derived-functor half above is unconditional in the resolution, this kernel step is not, and Hatcher's
use of Lemma 3A.2 in `E-HAT-3.A-6` is the *unrestricted* application (any resolution, then passage to
the colimit of stages), which needs this step plus the finite-stage descent already proved in
`cards/TorStages.lean`. -/

/-! ## The two-term step: the homology is the kernel of the incoming differential

`ShortComplex.LeftHomologyData.ofHasKernel S hf` (`hf : S.f = 0`) has its homology object *definitionally*
the kernel of `S.g`, so `homologyIso` is the identification; `HomologicalComplex.homologyIsoSc'`
presents the degree-`1` homology of a complex as the homology of the short complex
`K.X 2 → K.X 1 → K.X 0`; and `ModuleCat.kernelIsoKer` turns the categorical kernel into the
linear-map kernel, with `kernelIsoKer_hom_ker_subtype` recording what the map actually is.
-/

/-- **A short complex with vanishing incoming differential.** -/
noncomputable def homologyIsoKernelOfZero {S : ShortComplex (ModuleCat ℤ)} (hf : S.f = 0) :
    S.homology ≅ Limits.kernel S.g :=
  (ShortComplex.LeftHomologyData.ofHasKernel S hf).homologyIso

/-- **The two-term step at the level of the complex**, with the vanishing incoming differential as
the visible hypothesis. `homologyIsoSc'` moves to the short complex `K.X 2 → K.X 1 → K.X 0` (the
`prev`/`next` equalities for `ComplexShape.down ℕ` are supplied explicitly), and there the homology is
the kernel of the outgoing differential. -/
noncomputable def homologyOneIsoKernelOfD {K : ChainComplex (ModuleCat ℤ) ℕ}
    (h : K.d 2 1 = 0) : K.homology 1 ≅ Limits.kernel (K.d 1 0) :=
  (K.homologyIsoSc' 2 1 0
      (ComplexShape.prev_eq' (c := ComplexShape.down ℕ) (by simp))
      (ComplexShape.next_eq' (c := ComplexShape.down ℕ) (by simp))) ≪≫
    homologyIsoKernelOfZero (S := K.sc' 2 1 0) h

/-- The same, with the shape hypothesis `IsZero (K.X 2)`: any map out of a zero object is zero, so the
incoming differential vanishes. `K.shape` would *not* give this — `2 → 1` is an allowed differential
of `ComplexShape.down ℕ`. -/
noncomputable def homologyOneIsoKernel {K : ChainComplex (ModuleCat ℤ) ℕ} (h2 : IsZero (K.X 2)) :
    K.homology 1 ≅ Limits.kernel (K.d 1 0) :=
  homologyOneIsoKernelOfD (K := K) (IsZero.eq_of_src h2 _ _)

/-- The map-level check on the differential: the tensored complex's differential *is* the tensor
functor applied to the resolution's differential. -/
theorem resolutionTensor_d {A B : ModuleCat ℤ} (P : ProjectiveResolution A) (i j : ℕ) :
    (resolutionTensor B P).d i j = (tensorLeft B).map ((P.complex).d i j) :=
  rfl

/-- The vanishing of the incoming differential of the tensored complex, from the two-term shape of the
resolution: `eq_of_src` on the resolution, then `map_zero` of the additive tensor functor. -/
theorem tensor_d_two_one_eq_zero {A B : ModuleCat ℤ} (P : ProjectiveResolution A)
    (h2 : IsZero ((P.complex).X 2)) : (resolutionTensor B P).d 2 1 = 0 := by
  have hd : (P.complex).d 2 1 = 0 := IsZero.eq_of_src h2 _ _
  rw [resolutionTensor_d, hd, Functor.map_zero]
  rfl

/-- **The two-term bridge.** For a projective resolution of `A` that is two-term
(`IsZero (P.complex.X 2)`), `Tor₁(A,B)` is the kernel of the tensored degree-`1` differential
`K ⊗ B → F ⊗ B` — the presentation-level `torKernel` of `cards/TorReductions.lean`, with the
differential identified at the level of maps by `resolutionTensor_d`. Projectivity and exactness of the
resolution are carried by `P : ProjectiveResolution A`; the two-term shape is the explicit `h2`. -/
noncomputable def torOneIsoKernel {A B : ModuleCat ℤ} (P : ProjectiveResolution A)
    (h2 : IsZero ((P.complex).X 2)) :
    torOne A B ≅ Limits.kernel ((resolutionTensor B P).d 1 0) :=
  torOneIsoHomology P ≪≫
    homologyOneIsoKernelOfD (K := resolutionTensor B P) (tensor_d_two_one_eq_zero P h2)

/-- The bridge composed with `ModuleCat.kernelIsoKer`, as an isomorphism of `Tor₁(A,B)` with the
module-theoretic kernel of the tensored differential. (`ModuleCat.kernelIsoKer` is the maintained
identification of the categorical kernel with `LinearMap.ker` of the underlying linear map; the
accompanying map identity `kernelIsoKer_hom_ker_subtype` is what makes the object name mean what it
says. Composing it *inside a named statement* here runs into a `ℤ`-module instance diamond on the
kernel subtype — `Submodule.module` against `AddCommGroup.toIntModule` — which is a Mathlib-side
instance wrinkle, not a gap in the bridge, so the composition is recorded as a term below with its type
left to the elaborator.) -/
noncomputable def torOneIsoKerLinear {A B : ModuleCat ℤ} (P : ProjectiveResolution A)
    (h2 : IsZero ((P.complex).X 2)) :=
  torOneIsoKernel P h2 ≪≫
    ModuleCat.kernelIsoKer (R := ℤ) (f := (resolutionTensor B P).d 1 0)

end TorBridge

#print axioms TorBridge.torOneIsoHomology
#print axioms TorBridge.homologyIsoKernelOfZero
#print axioms TorBridge.homologyOneIsoKernelOfD
#print axioms TorBridge.homologyOneIsoKernel
#print axioms TorBridge.tensor_d_two_one_eq_zero
#print axioms TorBridge.torOneIsoKernel
#print axioms TorBridge.torOneIsoKerLinear
