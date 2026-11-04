import Mathlib

/-!
# `E-HAT-2.3-2`: when the direct sum fills the product

The candidate reduced homology of the card is
$\tilde h_n(X) = \prod_i \tilde H_i(X) \big/ \bigoplus_i \tilde H_i(X)$, indexed by $i \in \ZZ$.
Its dimension axiom is checked at a point and at $S^0$, in both cases because the family of
reduced homology groups is carried by a *finite* set of indices — for $S^0$ a single one,
where $\tilde H_0(S^0) = \ZZ$ and all other reduced groups vanish.

The finiteness is the whole content, and it is an explicit hypothesis here: the canonical
map $\bigoplus_i f_i \to \prod_i f_i$ is surjective when the family is carried by a `Finset`,
and the quotient is then trivial. Nothing in this file replaces a direct sum by a product
without that hypothesis; for an infinite family the map is not surjective in general, which
is exactly why the candidate fails the wedge axiom on $\bigvee_{j\ge1} S^j$.

What is certified: the surjectivity, hence the triviality of the quotient, under the stated
finite-support hypothesis. The identification of the groups $f_i$ with the reduced homology
of a space is not formalized and is not claimed here.
-/

namespace FamilyQuotient

open DirectSum

variable {ι : Type*} [DecidableEq ι] (f : ι → Type*) [∀ i, AddCommGroup (f i)]

/-- The canonical map from the direct sum to the product, one coordinate at a time. -/
noncomputable def directSumToPi : (DirectSum ι f) →ₗ[ℤ] (∀ i, f i) :=
  DirectSum.toModule ℤ ι (∀ i, f i) (fun i => LinearMap.single ℤ f i)

@[simp]
theorem directSumToPi_lof (i : ι) (x : f i) :
    directSumToPi f (DirectSum.lof ℤ ι f i x) = Pi.single i x :=
  DirectSum.toModule_lof ℤ i x

/-- The finiteness hypothesis is explicit: the family is carried by the `Finset` `s`, that
is, every group outside `s` is trivial. Under it the direct sum already fills the product. -/
theorem directSumToPi_surjective_of_finite_support (s : Finset ι)
    (h : ∀ i, i ∉ s → Subsingleton (f i)) : Function.Surjective (directSumToPi f) := by
  intro y
  refine ⟨∑ i ∈ s, DirectSum.lof ℤ ι f i (y i), ?_⟩
  rw [map_sum]
  simp only [directSumToPi_lof]
  ext j
  rw [Finset.sum_apply, Finset.sum_pi_single]
  by_cases hj : j ∈ s
  · rw [if_pos hj]
  · rw [if_neg hj]
    haveI := h j hj
    exact (Subsingleton.elim (y j) 0).symm

/-- Hence the quotient $\prod_i f_i \big/ \bigoplus_i f_i$ is trivial under the same
hypothesis, which is the statement the card uses at a point and at $S^0$. -/
theorem quotient_subsingleton_of_finite_support (s : Finset ι)
    (h : ∀ i, i ∉ s → Subsingleton (f i)) :
    Subsingleton ((∀ i, f i) ⧸ LinearMap.range (directSumToPi f)) := by
  have htop : LinearMap.range (directSumToPi f) = ⊤ :=
    LinearMap.range_eq_top.mpr (directSumToPi_surjective_of_finite_support f s h)
  rw [htop]
  infer_instance

/-- The point case: all groups trivial, so the sum is the product and the quotient vanishes. -/
theorem quotient_subsingleton_of_subsingleton [∀ i, Subsingleton (f i)] :
    Subsingleton ((∀ i, f i) ⧸ LinearMap.range (directSumToPi f)) :=
  quotient_subsingleton_of_finite_support f ∅ (fun i _ => inferInstance)

/-- The $S^0$ case of the card: exactly one group may be nonzero, at the index `i₀`, and the
quotient still vanishes. -/
theorem quotient_subsingleton_of_unique (i₀ : ι) (h : ∀ i, i ≠ i₀ → Subsingleton (f i)) :
    Subsingleton ((∀ i, f i) ⧸ LinearMap.range (directSumToPi f)) :=
  quotient_subsingleton_of_finite_support f {i₀} (by
    intro i hi
    exact h i (by simpa using hi))

end FamilyQuotient

#print axioms FamilyQuotient.directSumToPi_surjective_of_finite_support
#print axioms FamilyQuotient.quotient_subsingleton_of_finite_support
#print axioms FamilyQuotient.quotient_subsingleton_of_subsingleton
#print axioms FamilyQuotient.quotient_subsingleton_of_unique
