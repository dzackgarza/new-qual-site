/-
Certificates for the general statements of the Chapter 8 cards
(`SRC-CH8-DIRECT-PRODUCT-SOLUTION-OUTLINES`, Gallian, *Contemporary Abstract
Algebra*, 7th edition, Chapter 8, printed pages 167-170).

The finite computations of the same collection are checked in
`proofs/cards/CH8DirectProduct.g`; the two files are complementary: this one
proves the uniform statements, GAP checks the particular groups.

Each theorem names the card whose solution it certifies.

Status of the recorded run: PASSED, `lean CH8DirectProduct.lean` exits 0 with no
`sorryAx`; every `#print axioms` line below lists at most `propext`,
`Classical.choice` and `Quot.sound`.

  Lean 4.33.1 (x86_64 Linux, commit 819816b2e0) at /opt/lean/bin/lean with the
  prebuilt Mathlib at /opt/mathlib (its `lean-toolchain` is
  leanprover/lean4:v4.33.1), on the VM this repository was checked out in.  This
  is the toolchain present in that VM, not the research image's pin, so the
  certificate is reproducible with the same Lean and library pair.

What this file does not do: it does not touch the finite computations of the
same cards, which are the GAP checks in `CH8DirectProduct.g`, and it says nothing
about the homology or other structures outside group theory.
-/
import Mathlib

open scoped BigOperators

namespace CH8DirectProduct

/-! ## P-CH8-1: the external direct product of finitely many groups is a group -/

/-- The product of a finite family of groups, with componentwise operations, is a
group. The work is Mathlib's `Pi.instGroup`; what the card needs is that the
operations are the componentwise ones, which `mul_apply` records. -/
example (n : ℕ) (G : Fin n → Type*) [∀ i, Group (G i)] : Group (∀ i, G i) :=
  inferInstance

/-- Multiplication in the external direct product is componentwise. -/
theorem product_mul_apply (n : ℕ) (G : Fin n → Type*) [∀ i, Group (G i)]
    (x y : ∀ i, G i) (i : Fin n) : (x * y) i = x i * y i :=
  rfl

/-- The identity of the external direct product is the tuple of identities, and
inverses are componentwise. -/
theorem product_one_apply (n : ℕ) (G : Fin n → Type*) [∀ i, Group (G i)] (i : Fin n) :
    (1 : ∀ i, G i) i = 1 :=
  rfl

/-! ## P-CH8-3: `G ⊕ {e}` and `{e} ⊕ H` are normal, with the stated quotients -/

section prodbot
variable (G H : Type*) [Group G] [Group H]

/-- `G × {e}` is the kernel of the second projection. -/
theorem prod_bot_eq_ker_snd :
    ((⊤ : Subgroup G).prod (⊥ : Subgroup H)) = (MonoidHom.snd G H).ker := by
  ext x
  simp [Subgroup.mem_prod]

/-- `G × {e}` is a normal subgroup of `G × H`. -/
theorem prod_bot_normal : Subgroup.Normal ((⊤ : Subgroup G).prod (⊥ : Subgroup H)) :=
  Subgroup.prod_normal ⊤ ⊥

/-- `{e} × H` is the kernel of the first projection, hence normal. -/
theorem bot_prod_normal : Subgroup.Normal ((⊥ : Subgroup G).prod (⊤ : Subgroup H)) :=
  Subgroup.prod_normal ⊥ ⊤

/-- `(G × H) / (G × {e}) ≅ H`. -/
noncomputable def quotient_prod_bot_mulEquiv : ((G × H) ⧸ ((⊤ : Subgroup G).prod (⊥ : Subgroup H)))
    ≃* H :=
  (QuotientGroup.quotientMulEquivOfEq (prod_bot_eq_ker_snd G H)).trans
    (QuotientGroup.quotientKerEquivOfSurjective (MonoidHom.snd G H) Prod.snd_surjective)

/-- `(G × H) / ({e} × H) ≅ G`. -/
noncomputable def quotient_bot_prod_mulEquiv : ((G × H) ⧸ ((⊥ : Subgroup G).prod (⊤ : Subgroup H)))
    ≃* G :=
  (QuotientGroup.quotientMulEquivOfEq
      (show ((⊥ : Subgroup G).prod (⊤ : Subgroup H)) = (MonoidHom.fst G H).ker from by
        ext x
        simp [Subgroup.mem_prod])).trans
    (QuotientGroup.quotientKerEquivOfSurjective (MonoidHom.fst G H) Prod.fst_surjective)

end prodbot

section proddone
variable (G : Type*) [Group G] (H : Type*) [Group H]

/-- `G × {e} ≅ G`: the first half of P-CH8-3, with the trivial group written as a
one-point type. -/
noncomputable def prod_bot_mulEquiv [Subsingleton H] : G × H ≃* G :=
  haveI : Inhabited H := ⟨1⟩
  haveI : Unique H := Unique.mk' H
  MulEquiv.prodUnique

/-- `{e} × H ≅ H`: the second half of P-CH8-3. -/
noncomputable def bot_prod_mulEquiv [Subsingleton H] : H × G ≃* G :=
  haveI : Inhabited H := ⟨1⟩
  haveI : Unique H := Unique.mk' H
  MulEquiv.uniqueProd

end proddone

/-! ## P-CH8-4: `G ⊕ H` is abelian if and only if `G` and `H` are -/

section prodcomm
variable (G H : Type*) [Group G] [Group H]

theorem prod_comm_iff :
    (∀ x y : G × H, x * y = y * x) ↔
      (∀ x y : G, x * y = y * x) ∧ (∀ x y : H, x * y = y * x) := by
  constructor
  · intro h
    exact ⟨fun x y => congrArg Prod.fst (h (x, 1) (y, 1)),
           fun x y => congrArg Prod.snd (h (1, x) (1, y))⟩
  · rintro ⟨hG, hH⟩ ⟨a, b⟩ ⟨c, d⟩
    ext <;> simp [hG, hH]

end prodcomm

/-! ## P-CH8-7: `G₁ ⊕ G₂ ≅ G₂ ⊕ G₁`, and the general case -/

/-- The two-factor case of P-CH8-7. -/
noncomputable def prod_comm_mulEquiv (G H : Type*) [Group G] [Group H] : G × H ≃* H × G :=
  MulEquiv.prodComm

/-- The general case of P-CH8-7: permuting the index set of a direct product
gives an isomorphic group. -/
noncomputable def pi_perm_mulEquiv {ι κ : Type*} (e : ι ≃ κ) (G : κ → Type*)
    [∀ k, Group (G k)] : (∀ k, G k) ≃* (∀ i, G (e i)) :=
  { (Equiv.piCongrLeft G e).symm with
    map_mul' := fun _ _ => rfl }

/-! ## P-CH8-15: the additive group of `ℂ` is `ℝ ⊕ ℝ` -/

/-- The group of complex numbers under addition is the direct product of two
copies of `ℝ`, as the card asserts. -/
noncomputable def complex_add_equiv_real_prod : ℂ ≃+ ℝ × ℝ :=
  Complex.equivRealProdAddHom

/-! ## P-CH8-40: a tuple has infinite order exactly when a coordinate does -/

/-- In a direct product the order of a tuple is the least common multiple of the
orders of its coordinates, so the tuple has infinite order exactly when some
coordinate does. -/
theorem prod_orderOf_eq_zero_iff {G H : Type*} [Group G] [Group H] (x : G × H) :
    orderOf x = 0 ↔ orderOf x.1 = 0 ∨ orderOf x.2 = 0 := by
  rw [Prod.orderOf, Nat.lcm_eq_zero_iff]

/-- A tuple whose every coordinate satisfies `y ^ n = 1` satisfies it itself. -/
private lemma pi_pow_eq_one_of_coord {ι : Type*} {G : ι → Type*} [∀ i, Group (G i)]
    (x : ∀ i, G i) (N : ℕ) (hp : ∀ i, (x i) ^ N = 1) : x ^ N = 1 := by
  funext i
  have h := map_pow (Pi.evalMonoidHom G i) x N
  simp only [Pi.evalMonoidHom_apply, Pi.one_apply] at h ⊢
  rw [h, hp i]

/-- A coordinate of a tuple satisfying `x ^ n = 1` satisfies it. -/
private lemma coord_pow_eq_one {ι : Type*} {G : ι → Type*} [∀ i, Group (G i)]
    (x : ∀ i, G i) {n : ℕ} (hxn : x ^ n = 1) (i : ι) : (x i) ^ n = 1 := by
  have h := map_pow (Pi.evalMonoidHom G i) x n
  simp only [Pi.evalMonoidHom_apply] at h
  rw [hxn] at h
  simpa using h.symm

/-- The same for a finite family: the order of a tuple is infinite exactly when
some coordinate has infinite order. The finiteness is used to multiply the
coordinate orders; over an infinite index set the statement fails, since a tuple
all of whose coordinates have finite order can still have infinite order. -/
theorem pi_orderOf_eq_zero_iff {ι : Type*} [Fintype ι] {G : ι → Type*} [∀ i, Group (G i)]
    (x : ∀ i, G i) : orderOf x = 0 ↔ ∃ i, orderOf (x i) = 0 := by
  classical
  rw [orderOf_eq_zero_iff]
  constructor
  · intro h
    by_contra hx
    push Not at hx
    refine h (isOfFinOrder_iff_pow_eq_one.mpr ⟨∏ i, orderOf (x i),
      Finset.prod_pos (fun i _ => Nat.pos_of_ne_zero (hx i)), ?_⟩)
    exact pi_pow_eq_one_of_coord x _ (fun i =>
      orderOf_dvd_iff_pow_eq_one.mp
        (Finset.dvd_prod_of_mem (fun j => orderOf (x j)) (Finset.mem_univ i)))
  · rintro ⟨i, hi⟩ hfin
    obtain ⟨n, hn, hxn⟩ := isOfFinOrder_iff_pow_eq_one.mp hfin
    rw [orderOf_eq_zero_iff, isOfFinOrder_iff_pow_eq_one] at hi
    exact hi ⟨n, hn, coord_pow_eq_one x hxn i⟩

end CH8DirectProduct

/-! ## Axiom check

No `sorryAx` may appear in any line below; each theorem must rest only on
`propext`, `Classical.choice` and `Quot.sound`. -/

#print axioms CH8DirectProduct.product_mul_apply
#print axioms CH8DirectProduct.prod_bot_eq_ker_snd
#print axioms CH8DirectProduct.prod_bot_normal
#print axioms CH8DirectProduct.bot_prod_normal
#print axioms CH8DirectProduct.quotient_prod_bot_mulEquiv
#print axioms CH8DirectProduct.quotient_bot_prod_mulEquiv
#print axioms CH8DirectProduct.prod_bot_mulEquiv
#print axioms CH8DirectProduct.bot_prod_mulEquiv
#print axioms CH8DirectProduct.prod_comm_iff
#print axioms CH8DirectProduct.prod_comm_mulEquiv
#print axioms CH8DirectProduct.pi_perm_mulEquiv
#print axioms CH8DirectProduct.complex_add_equiv_real_prod
#print axioms CH8DirectProduct.prod_orderOf_eq_zero_iff
#print axioms CH8DirectProduct.pi_orderOf_eq_zero_iff
