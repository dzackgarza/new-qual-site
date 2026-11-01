import Mathlib

open scoped BigOperators

/-!
# `E-HAT-3.E-2`: the local-degree bookkeeping for the angular extension of `S^{2n-1}`

The map `f~` of the exercise is the *angular* extension: it fixes the radii and multiplies the
`j`-th angular coordinate by `k_j`. In the oriented frame `(∂_r, r⁻¹∂_θ)` of the punctured plane
the `j`-th coordinate map has derivative `diag(1, k_j)`, so its local degree there is the sign of
`k_j`; there are `|k_j|` preimages, and the contribution of the coordinate is
`|k_j| · sgn(k_j) = k_j`, whose product over the coordinates is `k_1 ⋯ k_n`.

This file certifies that bookkeeping: the determinant of the frame derivative, the orientation
criterion read off it, and the per-coordinate identity together with its product over a finite
set. It does **not** certify the topological statement `deg f~ = k_1 ⋯ k_n` itself: that is the
standard computation for self-maps of `S^{2n-1}` (the lens-space discussion in §3.E), it is
cited, and no formalization of it exists in this repository.

It also does not certify the holomorphic comparison: `z ↦ z^k` is conformal on `ℂ^×` for every
`k ≠ 0`, so its local degree is `+1`, and it is *not* the angular extension when `k < 0` (it
moves the radius as well). That distinction is the reason this bookkeeping is about the frame
derivative and not about the complex derivative.
-/

namespace LensDegree

/-- The derivative of the angular extension in one coordinate, in the oriented frame
`(∂_r, r⁻¹∂_θ)`: the radius is untouched and the angular coordinate is multiplied by `k`. -/
def angDeriv (k : ℝ) : (ℝ × ℝ) →ₗ[ℝ] (ℝ × ℝ) where
  toFun p := (p.1, k * p.2)
  map_add' p q := by
    ext <;> simp [mul_add]
  map_smul' c p := by
    ext <;> simp [mul_assoc, mul_left_comm]

/-- Its matrix in that frame is `diag(1, k)`, and the determinant is `k`. -/
theorem det_angDeriv (k : ℝ) : Matrix.det !![(1 : ℝ), 0; 0, k] = k := by
  rw [Matrix.det_fin_two]
  simp

/-- The coordinate map preserves the orientation exactly when `k > 0`: this is the local degree
`sgn(k)` of the angular extension, read off the determinant. -/
theorem orientation_iff (k : ℝ) :
    0 < Matrix.det !![(1 : ℝ), 0; 0, k] ↔ 0 < k := by
  rw [det_angDeriv]

/-- One coordinate contributes `|k| · sgn(k) = k`: `|k|` preimages, each with local degree
`sgn(k)` read as `1` or `-1`. -/
theorem natAbs_mul_orientation (k : ℤ) :
    (k.natAbs : ℤ) * (if 0 < k then (1 : ℤ) else -1) = k := by
  have h : k = (k.natAbs : ℤ) ∨ k = -(k.natAbs : ℤ) := Int.natAbs_eq k
  split_ifs with hk <;> rcases h with h | h <;> omega

/-- The product over the coordinates: the total degree contribution is the product of the
`k_j`, i.e. the number of preimages times the sign accumulated over the coordinates. -/
theorem prod_natAbs_mul_orientation {ι : Type*} (s : Finset ι) (k : ι → ℤ) :
    ((s.prod fun j => (k j).natAbs : ℕ) : ℤ) * (s.prod fun j => if 0 < k j then (1 : ℤ) else -1)
      = s.prod fun j => k j := by
  rw [Nat.cast_prod, ← Finset.prod_mul_distrib]
  exact Finset.prod_congr rfl fun j _ => natAbs_mul_orientation (k j)

end LensDegree

#print axioms LensDegree.det_angDeriv
#print axioms LensDegree.orientation_iff
#print axioms LensDegree.natAbs_mul_orientation
#print axioms LensDegree.prod_natAbs_mul_orientation
