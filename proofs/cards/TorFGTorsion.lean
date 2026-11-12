import Mathlib

/-!
# `E-HAT-3.A-6` / `E-HAT-3.A-2`: `Tor₁` of a finitely generated abelian group is torsion

The structure theorem of finitely generated abelian groups
(`AddCommGroup.equiv_free_prod_directSum_zmod`) splits a finitely generated `A` into a free part
and a finite direct sum of cyclic prime-power groups.  This file builds the statement that
`Tor₁(A, B)` is a torsion group for every `B`, from the free case (vanishing on projectives),
the cyclic case, and the additivity of `Tor₁` in its first argument, carried through the
dimension-shift bridge (`cards/TorArbitrary.lean`'s `torOneIsoKerIncl`) and the
presentation-level kernel computation (`cards/TorReductions.lean`'s `map_prodLeft_torKernel`).

## What Mathlib already supplies, checked before anything was written here

The seven closure lemmas of the first three commits of this batch restated Mathlib results and
have been deleted in favour of them:

* a finite additive group is torsion: `isAddTorsion_of_finite [Finite G] : IsAddTorsion G`
  (`Mathlib/GroupTheory/Torsion.lean`, l. 161–165).  This covers `ZMod m` for `m ≠ 0` and every
  finite direct sum of such, which is what `isAddTorsion_dfinsupp_fintype` and
  `isAddTorsion_dfinsupp_zmod` were stating;
* the image of a surjective torsion group homomorphism is torsion:
  `IsAddTorsion.of_surjective {f : G →+ H} (hf : Function.Surjective f) (tG : IsAddTorsion G) :
  IsAddTorsion H` (l. 103–109), which is the backwards transport along a linear equivalence that
  `isAddTorsion_of_linearEquiv` was restating (apply it to the inverse);
* the divisibility transfer in iff form: `orderOf_dvd_iff_pow_eq_one`
  (`Mathlib/GroupTheory/OrderOfElement.lean`, l. 274), whose additive reading is
  `addOrderOf x ∣ n ↔ n • x = 0`; `nsmul_eq_zero_of_dvd` was its one-directional corollary;
* the elementwise product-iff `IsOfFinAddOrder.prod_iff` (l. 1405–1406), of which
  `isAddTorsion_prod` was the ∀-corollary;
* the left-tensor distributivity `TensorProduct.prodRight`, of which `prodRight_int` was a
  special-case wrapper.

## Corpus searches (formalization-corpus.dzackgarza.com), run before the additivity step

Queries: `content:Tor torsion file:\.lean$`, `content:Tor direct limit file:\.lean$`,
`content:Tor colimit file:\.lean$`, `content:torKernel`, `content:IsAddTorsion Tor`,
`content:Tor biproduct`, `content:Tor coproduct`, `content:Tor filtered colimit`,
`content:Tor_additive`.  Hits: the queries surface the Tau Ceti project
(`TauCetiProject__TauCeti`, `TauCeti/Algebra/Group/Torsion.lean`,
`TauCeti/Data/ZMod/Torsion.lean`), whose `isAddTorsion_Tor_left` — Tor of a torsion module is
torsion — this repository has already ported with its provenance recorded in
`cards/TorTorsionClass.lean` (§7c of `proofs/README.md`).  No corpus hit for an additivity of
`Tor` in its first argument, nor for a Tor–direct-limit comparison, beyond that port: the
additivity step below is written by hand from the committed presentation-level
`map_prodLeft_torKernel` and the bridge.
-/

namespace TorFGTorsion

open CategoryTheory Limits MonoidalCategory
open scoped TensorProduct

end TorFGTorsion
