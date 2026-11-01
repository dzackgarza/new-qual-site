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

end TorBridge

#print axioms TorBridge.torOneIsoHomology
