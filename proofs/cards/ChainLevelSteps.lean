import Mathlib

/-!
# `E-HAT-2.2-16`: augmented exactness and the skeleton's differentials

The card computes the ranks of cycles and boundaries of the standard simplex and then passes
to its $k$-skeleton. Two steps of that argument need care, and this file certifies them.

The degree-zero step. In the ordinary chain complex $Z_0 = C_0$ and
$B_0 = \\operatorname{im}\\partial_1$, so $Z_0/B_0 = H_0$, which does not vanish; the reduced
statement is about the *augmented* complex, whose degree-zero boundary is an augmentation
$\\varepsilon : C_0 \\to \\ZZ$ with $\\ker\\varepsilon = \\operatorname{im}\\partial_1$. So

* `choose_rank_step`: Pascal's identity in the form the rank induction uses;
* `ker_ne_top_of_surjective_to_int`: a surjection onto $\\ZZ$ has proper kernel, so the
  augmented degree-zero cycles are not the ordinary ones;
* `not_subsingleton_ordinary_homology`: with $\\ker\\varepsilon = \\operatorname{im}\\partial_1$
  and $\\varepsilon$ onto $\\ZZ$, the ordinary $C_0/\\operatorname{im}\\partial_1 \\cong \\ZZ$ is
  **not** trivial, while the augmented $\\ker\\varepsilon/\\operatorname{im}\\partial_1$ is. This
  is exactly why $Z_0/B_0$ cannot stand in for $\\widetilde H_0$.

The skeleton step. The $k$-skeleton has the simplex's chain groups and differentials in
degrees at most $k$ and none above, so exactness of the augmented complex below degree $k$
passes to it. `ker_eq_range_of_comm_iso` is the transport: if the three-term complexes
$A \\leftarrow B \\leftarrow C$ and $A' \\leftarrow B' \\leftarrow C'$ are isomorphic by a chain
map, then $\\ker\\partial = \\operatorname{im}\\partial'$ transports. The range restriction
$i < k$ is where the agreement hypothesis is used.
-/

namespace ChainLevelSteps

open scoped DirectSum

/-- Pascal's identity in the form used by the rank induction of `E-HAT-2.2-16`: the number
of $(i+1)$-subsets of an $(n+1)$-set minus the number of $i$-subsets of an $n$-set is the
number of $(i+1)$-subsets of the $n$-set. -/
theorem choose_rank_step (n i : ℕ) :
    Nat.choose (n + 1) (i + 1) - Nat.choose n i = Nat.choose n (i + 1) := by
  rw [Nat.choose_succ_succ]
  exact Nat.add_sub_cancel_left _ _

/-- The degree-zero defect of `E-HAT-2.2-16`: an augmentation onto `ℤ` cannot have kernel
`⊤`, so the augmented degree-zero cycles are a proper subgroup of `C₀`, unlike the ordinary
$Z_0 = C_0$. -/
theorem ker_ne_top_of_surjective_to_int {C₀ : Type*} [AddCommGroup C₀] [Module ℤ C₀]
    (e : C₀ →ₗ[ℤ] ℤ) (he : Function.Surjective e) : LinearMap.ker e ≠ ⊤ := by
  intro h
  have hzero : e = 0 := by
    ext x
    have hx : x ∈ LinearMap.ker e := by rw [h]; exact Submodule.mem_top
    simpa using hx
  obtain ⟨x, hx⟩ := he 1
  rw [hzero] at hx
  simp at hx

/-- Transport of exactness across an isomorphism of three-term complexes: if the squares
commute and `ker d₁ = range d₂`, then `ker d₁' = range d₂'`. This is the mechanism by which
the $k$-skeleton inherits exactness from the simplex in the degrees where their differentials
agree. -/
theorem ker_eq_range_of_comm_iso
    {A B C A' B' C' : Type*} [AddCommGroup A] [AddCommGroup B] [AddCommGroup C]
    [AddCommGroup A'] [AddCommGroup B'] [AddCommGroup C']
    (ea : A' ≃ₗ[ℤ] A) (eb : B' ≃ₗ[ℤ] B) (ec : C' ≃ₗ[ℤ] C)
    (d₁ : B →ₗ[ℤ] A) (d₂ : C →ₗ[ℤ] B) (d₁' : B' →ₗ[ℤ] A') (d₂' : C' →ₗ[ℤ] B')
    (h₁ : d₁ ∘ₗ eb.toLinearMap = ea.toLinearMap ∘ₗ d₁')
    (h₂ : d₂ ∘ₗ ec.toLinearMap = eb.toLinearMap ∘ₗ d₂')
    (hex : LinearMap.ker d₁ = LinearMap.range d₂) :
    LinearMap.ker d₁' = LinearMap.range d₂' := by
  have hmem : ∀ y : B', y ∈ LinearMap.ker d₁' ↔ eb y ∈ LinearMap.ker d₁ := by
    intro y
    have h := congrArg (fun g => g y) h₁
    simp only [LinearMap.comp_apply, LinearEquiv.coe_coe] at h
    rw [LinearMap.mem_ker, LinearMap.mem_ker, h, ea.map_eq_zero_iff]
  have hmem2 : ∀ y : B', y ∈ LinearMap.range d₂' ↔ eb y ∈ LinearMap.range d₂ := by
    intro y
    constructor
    · rintro ⟨z, rfl⟩
      refine ⟨ec z, ?_⟩
      have h := congrArg (fun g => g z) h₂
      simpa only [LinearMap.comp_apply, LinearEquiv.coe_coe] using h
    · rintro ⟨z, hz⟩
      refine ⟨ec.symm z, eb.injective ?_⟩
      have h := congrArg (fun g => g (ec.symm z)) h₂
      simp only [LinearMap.comp_apply, LinearEquiv.coe_coe,
        LinearEquiv.apply_symm_apply] at h
      rw [← h]
      exact hz
  ext y
  rw [hmem, hmem2, hex]

/-- The augmented degree-zero cycles are the boundaries, but the ordinary ones are not: with
`ker ε = range ∂` and `ε` onto `ℤ`, the ordinary `C₀ / im ∂` is not a subsingleton. This is
the exact defect that made $Z_0/B_0$ unusable as $\\widetilde H_0$. -/
theorem not_subsingleton_ordinary_homology {C₀ C₁ : Type*} [AddCommGroup C₀]
    [AddCommGroup C₁] (ε : C₀ →ₗ[ℤ] ℤ) (d : C₁ →ₗ[ℤ] C₀)
    (hε : Function.Surjective ε) (hex : LinearMap.ker ε = LinearMap.range d) :
    ¬ Subsingleton (C₀ ⧸ LinearMap.range d) := by
  intro hsub
  have hker : LinearMap.ker ε = ⊤ := by
    rw [hex]
    rw [Submodule.eq_top_iff']
    intro x
    have hx : Submodule.Quotient.mk x (p := LinearMap.range d) = 0 :=
      @Subsingleton.elim _ hsub _ _
    rwa [Submodule.Quotient.mk_eq_zero] at hx
  exact ker_ne_top_of_surjective_to_int ε hε hker

end ChainLevelSteps

#print axioms ChainLevelSteps.choose_rank_step
#print axioms ChainLevelSteps.ker_ne_top_of_surjective_to_int
#print axioms ChainLevelSteps.ker_eq_range_of_comm_iso
#print axioms ChainLevelSteps.not_subsingleton_ordinary_homology
