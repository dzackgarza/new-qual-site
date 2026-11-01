import Mathlib

/-!
# `E-HAT-3.A-6` / `E-HAT-3.A-2`, Exercise 4 of §3.A: `⊗` and filtered colimits

Hatcher, §3.A exercise 4: `⊗` and `Tor` commute with direct limits. This file certifies the
`⊗` half for abelian groups, in the form the two cards use, on the installed toolchain.

The reusable Mathlib fact is the instance
`CategoryTheory.Monoidal.Closed.Basic: instance : PreservesColimits (tensorLeft A)`
for a closed monoidal category, applied to `ModuleCat ℤ`: `tensorLeft B` is `B ⊗ -` and
preserves colimits, so for any functor `F : J ⥤ ModuleCat ℤ` the canonical comparison
`B ⊗ colim F → colim (B ⊗ F ·)` is an isomorphism. Nothing here re-implements tensoring or
colimits.

The `Tor` half — that `Tor(colim A_α, B) ≅ colim Tor(A_α, B)` — is *not* certified: it needs
Hatcher's Lemma 3A.2 (the comparison theorem, that any free resolution computes `Tor`), which
is not formalized, together with this colimit fact. -/

open CategoryTheory Limits MonoidalCategory

namespace ColimitTensor

variable {J : Type*} [Category J] [HasColimitsOfShape J (ModuleCat ℤ)]

/-- Exercise 4 of §3.A, first half, at abelian groups: `B ⊗ -` preserves colimits. -/
theorem tensorLeft_preserves_colimits (B : ModuleCat ℤ) : PreservesColimits (tensorLeft B) :=
  inferInstance

/-- Exercise 4 of §3.A, first half, at abelian groups: for any functor `F : J ⥤ ModuleCat ℤ`
and any `B`, the tensor product commutes with the colimit,
`B ⊗ colim F ≅ colim (B ⊗ F ·)`.

The witness of colimit preservation is `Nonempty (IsColimit _)` (`PreservesColimit.preserves`),
so it is extracted with `Classical.choice`; the comparison is the canonical map between two
colimit cocones, `IsColimit.coconePointUniqueUpToIso`. Both are Mathlib's. -/
noncomputable def tensorLeft_colim_iso (F : J ⥤ ModuleCat ℤ) (B : ModuleCat ℤ) :
    (tensorLeft B).obj (colimit F) ≅ colimit (F ⋙ tensorLeft B) :=
  IsColimit.coconePointUniqueUpToIso
    (Classical.choice (PreservesColimit.preserves (colimit.isColimit F)))
    (colimit.isColimit (F ⋙ tensorLeft B))

end ColimitTensor

#print axioms ColimitTensor.tensorLeft_preserves_colimits
#print axioms ColimitTensor.tensorLeft_colim_iso
