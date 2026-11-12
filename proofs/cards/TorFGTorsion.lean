import Mathlib

/-!
# `E-HAT-3.A-6` / `E-HAT-3.A-2`: `Tor₁` of a finitely generated abelian group is torsion
-/

namespace TorFGTorsion

open CategoryTheory Limits MonoidalCategory DirectSum

/-- A product of two torsion groups is torsion. -/
theorem isAddTorsion_prod {M N : Type*} [AddCommGroup M] [AddCommGroup N]
    (hM : IsAddTorsion M) (hN : IsAddTorsion N) : IsAddTorsion (M × N) := by
  intro x
  obtain ⟨a, b⟩ := x
  obtain ⟨m, hm, hma⟩ := isOfFinAddOrder_iff_nsmul_eq_zero.mp (hM a)
  obtain ⟨n, hn, hna⟩ := isOfFinAddOrder_iff_nsmul_eq_zero.mp (hN b)
  refine isOfFinAddOrder_iff_nsmul_eq_zero.mpr ⟨m * n, Nat.mul_pos (by omega) (by omega), ?_⟩
  ext
  · show (m * n) • a = 0
    rw [Nat.mul_comm m n, mul_smul, hma, smul_zero]
  · show (m * n) • b = 0
    rw [mul_smul, hna, smul_zero]

end TorFGTorsion

#print axioms TorFGTorsion.isAddTorsion_prod
