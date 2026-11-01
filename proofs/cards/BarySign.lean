import Mathlib

/-!
# `E-HAT-2.1-25`: the sign identity behind the barycentric subdivision formula

Hatcher defines the subdivision operator by `S λ = b_λ (S ∂λ)`, which prepends the barycentre of the
whole simplex. Expanding that recursion, the summands are indexed by permutations `π` of the vertices,
and the sign of the `π`-summand is `(-1)` to the power *the sum of the deletion positions along the
descending chain*: going down from the full simplex, the vertex deleted at the stage where the current
face has vertex set `F` contributes its position among the vertices of `F` below it.

The combinatorial content of the correction in `E-HAT-2.1-25` is that this exponent plus the number of
inversions is the total number of pairs, `N (N - 1) / 2` where `N = n + 1` is the number of vertices,
so the recursion's sign is `(-1)^{N(N-1)/2} · sgn(π)`.

This file proves the counting and sign algebra for every `N`. What it does **not** do is identify the
recursion's deletion positions with the counted noninversions — that correspondence, together with the
definition of `S` on singular chains, is not formalized here and is the remaining obligation.
-/

open scoped BigOperators

namespace BarySign

/-- The set of pairs `i < j` in `Fin N`, as a finset of dependent pairs. -/
def pairSet (N : ℕ) : Finset (Sigma fun _ : Fin N => Fin N) :=
  Finset.univ.sigma fun j => Finset.Iio j

theorem card_pairSet (N : ℕ) : (pairSet N).card = N * (N - 1) / 2 := by
  rw [pairSet, Finset.card_sigma]
  have h : ∀ j : Fin N, (Finset.Iio j).card = j.val := fun j => Fin.card_Iio j
  rw [Finset.sum_congr rfl (fun j _ => h j), Fin.sum_univ_eq_sum_range (fun i => i) N,
    Finset.sum_range_id]

/-- The number of noninversions: pairs `i < j` with `π i < π j`, which is the number counted by the
deletion positions of the descending chain. -/
def noninv {N : ℕ} (π : Equiv.Perm (Fin N)) : ℕ :=
  (pairSet N).filter (fun p => π p.2 < π p.1) |>.card

/-- The number of inversions. -/
def inv {N : ℕ} (π : Equiv.Perm (Fin N)) : ℕ :=
  (pairSet N).filter (fun p => ¬ π p.2 < π p.1) |>.card

/-- Inversions and noninversions partition the pairs. -/
theorem noninv_add_inv {N : ℕ} (π : Equiv.Perm (Fin N)) :
    noninv π + inv π = N * (N - 1) / 2 := by
  rw [noninv, inv, Finset.card_filter_add_card_filter_not, card_pairSet]

/-- The maintained sign formula: `sgn π` is the product over pairs `i < j` of `1` at a noninversion
and `-1` at an inversion. -/
theorem sign_eq_prod {N : ℕ} (π : Equiv.Perm (Fin N)) :
    π.sign = ∏ j, ∏ i ∈ Finset.Iio j, (if π i < π j then (1 : ℤˣ) else -1) :=
  π.sign_eq_prod_prod_Iio

/-- The same product as a single product over the pair set. -/
theorem sign_eq_prod_pairSet {N : ℕ} (π : Equiv.Perm (Fin N)) :
    π.sign = ∏ p ∈ pairSet N, (if π p.2 < π p.1 then (1 : ℤˣ) else -1) := by
  rw [sign_eq_prod, pairSet, Finset.prod_sigma']

/-- And therefore `sgn π = (-1)^{inv π}`. -/
theorem prod_ite_neg_one {N : ℕ} (π : Equiv.Perm (Fin N)) (s : Finset (Sigma fun _ : Fin N => Fin N)) :
    (∏ p ∈ s, (if π p.2 < π p.1 then (1 : ℤˣ) else -1))
      = (-1 : ℤˣ) ^ (s.filter (fun p => ¬ π p.2 < π p.1)).card := by
  induction s using Finset.induction with
  | empty => simp
  | insert a s ha ih =>
      rw [Finset.prod_insert ha, ih, Finset.filter_insert]
      by_cases h : π a.2 < π a.1
      · rw [if_pos h, if_neg (by simp [h]), one_mul]
      · rw [if_neg h, if_pos h, Finset.card_insert_of_notMem (by simp [h, ha]), pow_succ,
          mul_comm]

/-- And therefore `sgn π = (-1)^{inv π}`. -/
theorem sign_eq_neg_one_pow_inv {N : ℕ} (π : Equiv.Perm (Fin N)) :
    π.sign = (-1 : ℤˣ) ^ inv π := by
  rw [sign_eq_prod_pairSet, prod_ite_neg_one, inv]

end BarySign

#print axioms BarySign.card_pairSet
#print axioms BarySign.noninv_add_inv
#print axioms BarySign.sign_eq_neg_one_pow_inv
