import Mathlib

/-!
# `E-HAT-2.2-16` and `E-HAT-2.3-2`: the two chain-level and dimension steps

`E-HAT-2.2-16`. The stored proof computed ranks of cycles and boundaries of the simplex by
induction and then compared `Z_0/B_0` with the reduced homology. In the ordinary chain
complex $Z_0 = C_0$ and $B_0 = \operatorname{im}\partial_1$, so $Z_0/B_0 = H_0$, which does
not vanish; the comparison is only valid in the *augmented* complex, where the degree-zero
boundary is an augmentation $\varepsilon : C_0 \to \ZZ$ and $Z_0 = \ker\varepsilon$. This
file certifies the two ingredients:

* `choose_rank_step`: Pascal's identity in the form the rank induction uses,
  $\binom{n+1}{i+1} - \binom{n}{i} = \binom{n}{i+1}$;
* `ker_ne_top_of_surjective_to_int`: for a surjection onto $\ZZ$ the kernel of the
  augmentation is a proper subgroup, so the augmented degree-zero cycles are *not* the
  ordinary ones, which is exactly what the repair is about.

`E-HAT-2.3-2`. The candidate reduced homology is
$\tilde h_n(X) = \prod_i \tilde H_i(X) / \bigoplus_i \tilde H_i(X)$, independent of $n$.
The statement needed there is that when all but one of the reduced homology groups vanish,
the direct sum already fills the product, so the quotient is trivial. That is *not*
certified here: it needs `DirectSum.toModule` composed with the single-coordinate maps, and
is left as an obligation rather than asserted.
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

end ChainLevelSteps

#print axioms ChainLevelSteps.choose_rank_step
#print axioms ChainLevelSteps.ker_ne_top_of_surjective_to_int
