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

/-! The injectivity of `stageMap` — that the stage really is a *subgroup* of `A` — is the
next step and is **not** proved here: it reduces to `Submodule.map p.mkQ p = ⊥` for
`p = comap F'.subtype (range f)`, where `Submodule.map_eq_bot_iff` does not fire on the shape
Lean produces (`Submodule.map p.mkQ p` has `mkQ` as a `LinearMap`, while the lemma's pattern is
a coerced map). The proof sketch is `elementwise`: `y ∈ map p.mkQ p` means `y = p.mkQ x` with
`x ∈ p = ker p.mkQ`, hence `y = 0`. Until that is closed, the stage is only a quotient of `F'`
with a map to `A`, not yet a subgroup. -/

end TorStages

#print axioms TorStages.map_stageRel
