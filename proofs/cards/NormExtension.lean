/-
Certificate toward `P-TAMURAS15-10` (TAMU Spring 2015, problem 10).

The card adds a closedness hypothesis to the printed statement; the replacement
is not yet certified.  What this file proves is the half of the definiteness
argument that handles `x ∉ Y`: for a closed subspace `Y` of a real normed space
and `x ∉ Y`, there is a continuous linear functional of norm at most one that
vanishes on `Y` and does not vanish at `x`.

The construction is the quotient one: `x` has nonzero class in `E ⧸ Y` because
`Y` is closed, `exists_dual_vector` supplies a norm-one functional on the
quotient that does not vanish there, and composing with `Submodule.mkQ` gives the
functional, whose norm is at most one by `Submodule.Quotient.norm_mk_le`.
-/
import Mathlib

set_option linter.style.haveILetI false

namespace QualProofs.NormExtension

open Submodule

/-- For a closed subspace `Y` of a real normed space and `x ∉ Y`, there is a
continuous linear functional of norm at most one vanishing on `Y` and nonzero at `x`. -/
theorem exists_dual_vanishing {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    {Y : Submodule ℝ E} (hY : IsClosed (Y : Set E)) {x : E} (hx : x ∉ Y) :
    ∃ f : StrongDual ℝ E, f x ≠ 0 ∧ (∀ y ∈ Y, f y = 0) ∧ ‖f‖ ≤ 1 := by
  classical
  haveI := hY
  have hxq : (Submodule.Quotient.mk (p := Y) x : E ⧸ Y) ≠ 0 := by
    intro h
    exact hx ((Submodule.Quotient.mk_eq_zero Y).mp h)
  obtain ⟨g, hg1, hgx⟩ :=
    exists_dual_vector ℝ (Submodule.Quotient.mk (p := Y) x : E ⧸ Y) (by simpa using hxq)
  let q : E →L[ℝ] E ⧸ Y :=
    (Submodule.mkQ Y).mkContinuous 1 (fun z => by
      simpa [Submodule.mkQ_apply] using Submodule.Quotient.norm_mk_le Y z)
  refine ⟨g.comp q, ?_, ?_, ?_⟩
  · have hval : (g.comp q) x = g (Submodule.Quotient.mk (p := Y) x) := by simp [q]
    rw [hval, hgx]
    have hpos : (0 : ℝ) < ‖(Submodule.Quotient.mk (p := Y) x : E ⧸ Y)‖ := by
      rw [norm_pos_iff]; exact hxq
    intro hzero
    exact hpos.ne' (by exact_mod_cast hzero)
  · intro y hy
    have hy0 : (Submodule.Quotient.mk (p := Y) y : E ⧸ Y) = 0 :=
      (Submodule.Quotient.mk_eq_zero Y).mpr hy
    simp [ContinuousLinearMap.comp_apply, q, hy0]
  · refine ContinuousLinearMap.opNorm_le_bound _ zero_le_one (fun z => ?_)
    calc ‖(g.comp q) z‖
        = ‖g (Submodule.Quotient.mk (p := Y) z)‖ := by simp [q]
      _ ≤ ‖g‖ * ‖(Submodule.Quotient.mk (p := Y) z : E ⧸ Y)‖ := g.le_opNorm _
      _ = ‖(Submodule.Quotient.mk (p := Y) z : E ⧸ Y)‖ := by rw [hg1, one_mul]
      _ ≤ ‖z‖ := Submodule.Quotient.norm_mk_le Y z
      _ = 1 * ‖z‖ := (one_mul _).symm


end QualProofs.NormExtension

#print axioms QualProofs.NormExtension.exists_dual_vanishing
