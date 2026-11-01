import Mathlib

/-!
# `E-HAT-3.A-6` / `E-HAT-3.A-2`: genuine subgroup stages of a presented group

For a presentation `f : K →ₗ[ℤ] F` of `A = F / range f` and a submodule `F' ≤ F`, the stage is
`A' = F' / (F' ⊓ range f)`, presented by `K' = comap f F' → F'`: its relations are exactly
`F' ⊓ range f`, since `map f (comap f F') = F' ⊓ range f`.

`stageMap` is the map `A' → A` induced by `F' ↪ F`, and `stageMap_injective` shows it is
injective — the point a bare sub-presentation does not give, since the cokernel of a
sub-presentation need not embed in `A`. Built with Mathlib's `Submodule.mapQ` and
`Submodule.ker_mapQ`: the kernel of `stageMap` is `p.map p.mkQ` for `p` the stage's
relations, which is `⊥` by `Submodule.Quotient.mk_eq_zero`.

`stageRelMap`, `range_stageRelMap` and `stageIncl` present the stage and give the transition
maps, `stageMap_comp_stageIncl` the compatibility of the triangles into `A`. The last section
records what a stage must be for the filtered-colimit step of Exercise 4 of §3.A to descend:
a *direct summand* of `F`, not merely a submodule.
-/

namespace TorStages

variable {K F : Type*} [AddCommGroup K] [AddCommGroup F]

/-- The stage's relations: those elements of `F'` that already lie in the range of the
presentation. -/
abbrev stageRel (f : K →ₗ[ℤ] F) (F' : Submodule ℤ F) : Submodule ℤ F' :=
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

/-! ## The stage's own presentation, and the transition maps

`stageRelMap f F' : comap f F' → F'` is the presentation of the stage: its range is
exactly `stageRel f F'`, so its cokernel is `A'`. For `F' ≤ F''` the inclusion of stages
`stageIncl` is induced by `F' ↪ F''`, and `stageMap_comp_stageIncl` says the triangles
`A' → A'' → A` and `A' → A` agree — the compatibility a directed system of stages needs.
-/

/-- The stage's presentation `K' = comap f F' → F'`. Its cokernel is the stage `A'`. -/
def stageRelMap (f : K →ₗ[ℤ] F) (F' : Submodule ℤ F) :
    Submodule.comap f F' →ₗ[ℤ] F' where
  toFun k := ⟨f k, k.2⟩
  map_add' x y := by ext; simp
  map_smul' c x := by ext; simp

/-- The stage's presentation has exactly the stage's relations as its range, so `A'` is its
cokernel. -/
theorem range_stageRelMap (f : K →ₗ[ℤ] F) (F' : Submodule ℤ F) :
    LinearMap.range (stageRelMap f F') = stageRel f F' := by
  ext x
  simp only [LinearMap.mem_range]
  constructor
  · rintro ⟨k, hk⟩
    exact ⟨k, congrArg Subtype.val hk⟩
  · rintro ⟨k, hk⟩
    exact ⟨⟨k, Submodule.mem_comap.mpr (by rw [hk]; exact x.2)⟩, Subtype.ext hk⟩

/-- The stage's presentation composes to the ambient presentation: `F' ↪ F` after
`K' → F'` is `K' ↪ K` after `f`. -/
theorem subtype_comp_stageRelMap (f : K →ₗ[ℤ] F) (F' : Submodule ℤ F) :
    F'.subtype.comp (stageRelMap f F') = f.comp (Submodule.comap f F').subtype := by
  ext k
  rfl

/-- For `F' ≤ F''`, the inclusion of stages `A' → A''`, induced by `F' ↪ F''`. -/
noncomputable def stageIncl {f : K →ₗ[ℤ] F} {F' F'' : Submodule ℤ F} (h : F' ≤ F'') :
    F' ⧸ stageRel f F' →ₗ[ℤ] F'' ⧸ stageRel f F'' :=
  Submodule.mapQ (stageRel f F') (stageRel f F'') (Submodule.inclusion h) fun _ hx => hx

/-- The transition maps are compatible with the maps into `A`: the triangle
`A' → A'' → A` is `A' → A`. -/
theorem stageMap_comp_stageIncl {f : K →ₗ[ℤ] F} {F' F'' : Submodule ℤ F} (h : F' ≤ F'') :
    (stageMap f F'').comp (stageIncl h) = stageMap f F' := by
  apply LinearMap.ext
  intro x
  obtain ⟨a, rfl⟩ := Submodule.Quotient.mk_surjective (p := stageRel f F') x
  rfl

/-- A transition map is injective, since the composite into `A` is. -/
theorem stageIncl_injective {f : K →ₗ[ℤ] F} {F' F'' : Submodule ℤ F} (h : F' ≤ F'') :
    Function.Injective (stageIncl (f := f) h) := by
  intro x y hxy
  apply stageMap_injective f F'
  have hx := (DFunLike.congr_fun (stageMap_comp_stageIncl (f := f) h) x).symm
  have hy := (DFunLike.congr_fun (stageMap_comp_stageIncl (f := f) h) y).symm
  simp only [LinearMap.comp_apply, hx, hy, hxy]

/-! ## Exercise 4 of §3.A at the presentation level: what a stage has to be

The cards use "`Tor(A,B) ≅ colim_α Tor(A_α,B)`" over the finitely generated subgroups. In the
presentation-level model the content is: an element of `torKernel f` already vanishes at a
stage whose middle term is finitely generated. The reduction to finite support is
`TensorProduct.exists_of_fg`. The delicate point is that vanishing upstairs descends to the
stage only when `F'` is a *direct summand* of `F`: flatness of `F'` is the wrong hypothesis
and is not enough, and `rTensor_subtype_not_injective` certifies the failure. So the
obligation is to choose the stages among the direct summands of `F` — for the cards' free
middle term, the spans of finite subsets of a basis.
-/

/-- **The direct-summand hypothesis, isolated.** If `ρ` retracts `F' ↪ F`, then
`F' ⊗ B → F ⊗ B` is injective, so an element of `F' ⊗ B` that dies in `F ⊗ B` is already zero.

This is the hypothesis the stage construction needs, and it is *not* automatic for a
submodule: `rTensor_subtype_not_injective` below certifies that for `F = ℤ`, `F' = 2ℤ` and
`B = ℤ/2` the map `F' ⊗ B → F ⊗ B` is not injective, although `F` is free. The quotient
`F/F'` has torsion there. So the stages have to be direct summands of `F`, which for the
cards' free middle term means spans of finite subsets of a basis; an arbitrary finitely
generated `F'` will not do. -/
theorem rTensor_subtype_injective_of_retraction {B : Type*} [AddCommGroup B]
    (F' : Submodule ℤ F) (ρ : F →ₗ[ℤ] F') (hρ : ρ.comp F'.subtype = LinearMap.id) :
    Function.Injective (LinearMap.rTensor B F'.subtype) := by
  have hleft : ∀ w : TensorProduct ℤ F' B,
      (LinearMap.rTensor B ρ) (LinearMap.rTensor B F'.subtype w) = w := by
    intro w
    rw [← LinearMap.comp_apply, ← LinearMap.rTensor_comp, hρ]
    simp
  intro y z hyz
  calc y = (LinearMap.rTensor B ρ) (LinearMap.rTensor B F'.subtype y) := (hleft y).symm
    _ = (LinearMap.rTensor B ρ) (LinearMap.rTensor B F'.subtype z) := by rw [hyz]
    _ = z := hleft z

/-! ### The direct-summand hypothesis is sharp

A submodule that is not a direct summand really does break the stage step, even over a free
`F`. The certified counterexample below is `F = ℤ`, `F' = 2ℤ`, `B = ℤ/2`: the stage's
relations are `0`, so the stage would be `2ℤ` itself, but `2ℤ ⊗ ℤ/2 → ℤ ⊗ ℤ/2` kills the
generator `2 ⊗ 1` (which is `2 • (1 ⊗ 1)`, and `2 • 1 = 0` in `ℤ/2`) while `2ℤ ≅ ℤ` makes it a
nonzero element of `2ℤ ⊗ ℤ/2`. So `stageMap_injective` alone does not make an arbitrary
finitely generated `F'` a usable stage.
-/

/-- Multiplication by `2` on `ℤ`. -/
def mulByTwo : ℤ →ₗ[ℤ] ℤ where
  toFun r := 2 * r
  map_add' r s := by ring
  map_smul' c r := by
    show 2 * (c * r) = c * (2 * r)
    ring

theorem mulByTwo_injective : Function.Injective mulByTwo := by
  intro a b h
  simp only [mulByTwo, LinearMap.coe_mk, AddHom.coe_mk] at h
  omega

/-- `2ℤ`, as the range of multiplication by `2`. -/
abbrev TwoZ : Submodule ℤ ℤ := LinearMap.range mulByTwo

/-- `2ℤ` is isomorphic to `ℤ`. -/
noncomputable def twoZEquiv : ℤ ≃ₗ[ℤ] TwoZ :=
  LinearEquiv.ofInjective mulByTwo mulByTwo_injective

theorem twoZEquiv_one_val : (twoZEquiv 1 : ℤ) = 2 := rfl

/-- The generator `2 ⊗ 1` of `2ℤ ⊗ ℤ/2` is nonzero, since `2ℤ ≅ ℤ` and `ℤ ⊗ ℤ/2 ≅ ℤ/2`. -/
theorem twoZEquiv_one_tmul_ne_zero : (twoZEquiv 1 ⊗ₜ[ℤ] (1 : ZMod 2)) ≠ 0 := by
  intro h
  have hmap := congrArg
    (fun z => (TensorProduct.lid ℤ (ZMod 2))
      (TensorProduct.congr twoZEquiv.symm (LinearEquiv.refl ℤ (ZMod 2)) z)) h
  simp only [map_zero, TensorProduct.congr_tmul, LinearEquiv.symm_apply_apply,
    LinearEquiv.refl_apply, TensorProduct.lid_tmul, one_smul] at hmap
  exact one_ne_zero hmap

/-- Its image `2 ⊗ 1` in `ℤ ⊗ ℤ/2` is zero: `2 ⊗ 1 = 2 • (1 ⊗ 1)`. -/
theorem twoZ_tmul_one_eq_zero : ((2 : ℤ) ⊗ₜ[ℤ] (1 : ZMod 2)) = 0 := by
  refine (TensorProduct.lid ℤ (ZMod 2)).injective ?_
  have h2 : ((2 : ℤ) • (1 : ZMod 2)) = 0 := by
    show ((2 : ℤ) : ZMod 2) = 0
    decide
  rw [show ((2 : ℤ) ⊗ₜ[ℤ] (1 : ZMod 2))
      = (2 : ℤ) • ((1 : ℤ) ⊗ₜ[ℤ] (1 : ZMod 2)) from by
    rw [TensorProduct.smul_tmul']
    norm_num]
  rw [map_smul, TensorProduct.lid_tmul, smul_smul, mul_one, h2, map_zero]

/-- **The counterexample.** `F' = 2ℤ` is not a direct summand of `F = ℤ`, and the stage step
fails: `F' ⊗ B → F ⊗ B` is not injective for `B = ℤ/2`. -/
theorem rTensor_subtype_not_injective :
    ¬ Function.Injective (LinearMap.rTensor (ZMod 2) (Submodule.subtype TwoZ)) := by
  intro hinj
  have h0 : LinearMap.rTensor (ZMod 2) (Submodule.subtype TwoZ)
      (twoZEquiv 1 ⊗ₜ[ℤ] (1 : ZMod 2)) = 0 := by
    rw [LinearMap.rTensor_tmul, Submodule.coe_subtype, twoZEquiv_one_val,
      twoZ_tmul_one_eq_zero]
  refine twoZEquiv_one_tmul_ne_zero (hinj ?_)
  rw [h0, map_zero]

/-- **Exercise 4 of §3.A at the presentation level, modulo the choice of a stage.** Let
`F' ≤ F` be a stage that is a direct summand of `F` (witnessed by the retraction `ρ`), let
`P ≤ comap f F'` be finitely generated, and let `u ∈ P ⊗ B` vanish under the presentation.
Then `u`'s class already vanishes in the *stage's* Tor, i.e. after both the inclusion
`P → comap f F'` and the stage presentation `stageRelMap f F'`.

Together with `TensorProduct.exists_of_fg` — which produces `P` and `u` for any class in
`torKernel f` — this is the whole content of the card's "the component of the class already
lies in some stage", once a finitely generated direct summand `F'` containing `f(P)` is
chosen. Producing that `F'` is the one remaining obligation; see `proofs/README.md`. -/
theorem exists_stage_witness_of_retraction {B : Type*} [AddCommGroup B]
    (f : K →ₗ[ℤ] F) (F' : Submodule ℤ F) (ρ : F →ₗ[ℤ] F')
    (hρ : ρ.comp F'.subtype = LinearMap.id) (P : Submodule ℤ K) (hle : P ≤ Submodule.comap f F')
    (u : TensorProduct ℤ P B) (hu : LinearMap.rTensor B (f.comp P.subtype) u = 0) :
    LinearMap.rTensor B (stageRelMap f F')
      (LinearMap.rTensor B (Submodule.inclusion hle) u) = 0 := by
  have hcomp : (F'.subtype.comp (stageRelMap f F')).comp (Submodule.inclusion hle)
      = f.comp P.subtype := by
    ext k
    rfl
  have h0 : LinearMap.rTensor B F'.subtype (LinearMap.rTensor B (stageRelMap f F')
      (LinearMap.rTensor B (Submodule.inclusion hle) u)) = 0 := by
    rw [← LinearMap.comp_apply, ← LinearMap.rTensor_comp, ← LinearMap.comp_apply,
      ← LinearMap.rTensor_comp, hcomp, hu]
  exact (rTensor_subtype_injective_of_retraction F' ρ hρ) (by rw [h0, map_zero])

end TorStages

#print axioms TorStages.map_stageRel
#print axioms TorStages.stageMap_injective
#print axioms TorStages.range_stageRelMap
#print axioms TorStages.subtype_comp_stageRelMap
#print axioms TorStages.stageMap_comp_stageIncl
#print axioms TorStages.stageIncl_injective
#print axioms TorStages.rTensor_subtype_injective_of_retraction
#print axioms TorStages.exists_stage_witness_of_retraction
#print axioms TorStages.rTensor_subtype_not_injective