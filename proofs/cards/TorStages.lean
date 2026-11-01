import Mathlib

/-!
# `E-HAT-3.A-6` / `E-HAT-3.A-2`: genuine subgroup stages of a presented group

For a presentation `f : K →ₗ[ℤ] F` of `A = F / range f` and a submodule `F' ≤ F`, the stage is
`A' = F' / (F' ⊓ range f)`, presented by `K' = comap f F' → F'`: its relations are exactly
`F' ⊓ range f`, since `map f (comap f F') = F' ⊓ range f`.

`stageMap` is the map `A' → A` induced by `F' ↪ F`, and `stageMap_injective` shows it is
injective — the point a bare sub-presentation does not give, since the cokernel of a
sub-presentation need not embed in `A`. Built with Mathlib's `Submodule.mapQ`,
`Submodule.ker_mapQ`, `Submodule.map_eq_bot_iff` and `Submodule.ker_mkQ`.
-/

namespace TorStages

variable {K F : Type*} [AddCommGroup K] [AddCommGroup F]

/-- The stage's relations: those elements of `F'` that already lie in the range of the
presentation. -/
def stageRel (f : K →ₗ[ℤ] F) (F' : Submodule ℤ F) : Submodule ℤ F' :=
  Submodule.comap F'.subtype (LinearMap.range f)

/-- The stage's relations are the relations of the sub-presentation `K' = comap f F' → F'`. -/
theorem map_stageRel (f : K →ₗ[ℤ] F) (F' : Submodule ℤ F) :
    Submodule.map F'.subtype (stageRel f F') = F' ⊓ LinearMap.range f := by
  rw [stageRel, Submodule.map_comap_eq, Submodule.range_subtype]

/-- The map from the stage `A' = F'/(F' ⊓ range f)` into `A = F/range f`. -/
noncomputable def stageMap (f : K →ₗ[ℤ] F) (F' : Submodule ℤ F) :
    F' ⧸ Submodule.comap F'.subtype (LinearMap.range f) →ₗ[ℤ] F ⧸ LinearMap.range f :=
  Submodule.mapQ _ (LinearMap.range f) F'.subtype le_rfl

/-- The stage embeds in `A`. By `Submodule.ker_mapQ` the kernel of `stageMap` is
`p.map p.mkQ` for `p` the stage's relations, and a member of that is `p.mkQ x` with `x ∈ p`,
hence `0` by `Submodule.Quotient.mk_eq_zero`. -/
theorem stageMap_injective (f : K →ₗ[ℤ] F) (F' : Submodule ℤ F) :
    Function.Injective (stageMap f F') := by
  rw [← LinearMap.ker_eq_bot, stageMap, Submodule.ker_mapQ]
  rw [Submodule.eq_bot_iff]
  rintro y ⟨x, hx, rfl⟩
  rw [Submodule.mkQ_apply]
  simpa using hx

end TorStages

#print axioms TorStages.map_stageRel
#print axioms TorStages.stageMap_injective
