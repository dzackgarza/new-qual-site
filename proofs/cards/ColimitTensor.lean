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

variable {J : Type*} [Category J]

/-- Exercise 4 of §3.A, first half, at abelian groups: `B ⊗ -` preserves colimits. -/
theorem tensorLeft_preserves_colimits (B : ModuleCat ℤ) : PreservesColimits (tensorLeft B) :=
  inferInstance

/-! The comparison isomorphism `B ⊗ colim F ≅ colim (B ⊗ F ·)` is the next step and is
not written here: with `PreservesColimits (tensorLeft B)` available, it is
`IsColimit.coconePointUniqueUpToIso (PreservesColimit.preserves (colimit.cocone F)
(colimit.isColimit F)) (colimit.isColimit (F ⋙ tensorLeft B))`, but that term does not
elaborate in this file yet: instance synthesis fails at
`PreservesColimit.preserves (colimit.cocone F)` and at `colimit (F ⋙ tensorLeft B)`, most
likely because the monoidal and `MonoidalClosed` instances on `ModuleCat ℤ` that
`tensorLeft` needs are not the ones in scope here. The next attempt should fix the instance
arguments explicitly (`ModuleCat.monoidalCategory`, `ModuleCat.monoidalClosed`) rather than
leave synthesis to inference. -/

end ColimitTensor

#print axioms ColimitTensor.tensorLeft_preserves_colimits
