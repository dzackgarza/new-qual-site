# Audit — SRC-TEXT-HAT02, §3.H (*Local Coefficients*), all 6 cards

Auditor: m7 (swarm smvy0zsoh), direction d4. Witness for every book claim: `tmp/hat/AT.txt`
(line numbers only; the extraction puts many sub/superscripts on their own line, so some
quotations are broken across lines — they are reproduced exactly as printed, including the
spacing, and the break is pointed out where it matters).

Section directory: `corpus/collections/SRC-TEXT-HAT02/3-h/` — **6 cards**, all read here
(E-HAT-3.H-1 … E-HAT-3.H-6). The printed exercises are §3.H, AT.txt lines 16834–16863:
`16834|Exercises` then exercises 1–6 on lines 16835, 16836–16837, 16838–16842, 16843–16845,
16846–16854, 16856–16863.

Card counts elsewhere in the collection (for the swarm's bookkeeping, `ls | wc -l` per section
directory): 1-1 20, 1-2 22, 1-3 33, 1-a 14, 1-b 9, 2-1 31, 2-2 42, 2-3 4, 2-b 11,
2-c 9, 3-1 13, 3-2 17, 3-3 35, 3-a 6, 3-b 5, 3-c 16, **3-d 3**, 3-e 4, **3-f 9**, **3-h 6**,
**4-1 23** (exercises 1–23; this audit covers 10–23 = 14 cards), 4-2 39, 4-3 24, 4-a 5,
4-b 2, 4-d 10, 4-f 3, 4-g 4, 4-h 4, 4-i 3, 4-k 6, 4-l 5 (plus `index.md`). 3-g and 4-c/4-e/4-j
have no directory.

---

## E-HAT-3.H-1 — Compute H_*(S¹;E), H^*(S¹;E), E → S¹ nontrivial with fibre Z

**STATEMENT: matches.**
Book, AT.txt:16835:
`1. Compute H∗ (S 1 ; E) and H ∗ (S 1 ; E) for E →S 1 the nontrivial bundle with fiber Z .`
Card: "Compute $H_*(S^1; E)$ and $H^*(S^1; E)$ for $E \to S^1$ the nontrivial bundle with fiber $\ZZ$."
Same quantifiers, same two objects, "nontrivial", "fiber Z". No difference.

**PROOF: correct.**
The computation is checked independently, not just read:
* Monodromy: Aut(Z) = {±1} (book, AT.txt:16471 `Example 3H.3. As a special case, suppose that
  we take M = Z , so Aut(Z) ≈ Z2 = {±1} .`), so "nontrivial" forces −1. Correct.
* Chain level: the cellular complex with local coefficients is C₁ = C₀ = Z with d₁ = (t−1) = −2
  acting on the fibre, as the card writes (`(-1)-1=-2`). Hence ker d₁ = 0 and coker d₁ = Z/2.
  H₁ = 0, H₀ = Z₂ — correct.
* Cohomology, computed independently: C⁰ = C¹ = Hom_{Z[π]}(Z[π],Z) = Z and δ⁰ = −2, so
  H⁰ = ker(−2) = 0, H¹ = Z/2. This agrees with group cohomology H⁰(Z;Z⁻) = fixed points = 0,
  H¹(Z;Z⁻) = Z/(t−1)Z = Z₂. The card's `H^0=0, H^1≅Z_2` is right (this is the point where
  cards often swap H⁰ and H¹; this one does not).
* "All other homology and cohomology groups vanish" — correct, the complex is two-term.

---

## E-HAT-3.H-2 — H_n(M; M_Z) for a closed nonorientable surface

**STATEMENT: matches.**
Book, AT.txt:16836–16837:
`2. Compute the homology groups with local coefficients Hn (M; MZ ) for a closed`
`nonorientable surface M .`
Card: "Compute the homology groups with local coefficients $H_n(M; M_{\ZZ})$ for a closed
nonorientable surface $M$." Identical (the extracted `MZ` is rendered as M_Z, which is the
notation §3.H uses for the orientation local system; see AT.txt:16500–16502
`We can` / `view Z as a Z[π1 M] module by letting a loop γ in M act on Z by multiplication` /
`by +1 or −1 according to whether γ preserves or reverses local orientations of M .`).

**PROOF: has a gap (one over-general cited theorem and one garbled verification step); the
final answer is nevertheless correct.**
* Answer check: H₀ = Z₂, H₁ = Z^{g−1}, H₂ = Z. Correct. It also agrees with the book's own
  computation of the top group, AT.txt:16505–16508 `nonorientability of M implies that
  Hn (M) = 0 . Since Hn+1 (M) = 0 , the exact se-` / `quence above then gives Hn (M; e Z) ≈
  Hn (M f) ≈ Z .`
* GAP (step 3 of the first block): `By Poincaré Duality for manifolds with local coefficients,
  for any closed n-manifold:` $H_k(M;\mathcal L)\cong H^{n-k}(M;\ZZ)$. **This is false as
  stated**: the duality needs L to be *the orientation sheaf*. Counterexample to the printed
  form: M the Klein bottle, L = Z trivial gives H₀(M;Z) = Z but H²(M;Z) = Z₂. The correct
  statement, and the one actually used, is Hatcher's Theorem 3H.6 (AT.txt:16825–16828):
  `Theorem 3H.6. If M is a nonorientable closed connected n manifold then cap prod-`
  `uct with the pure imaginary fundamental class [M] gives isomorphisms H k (M; Z) ≈`
  `Hn−k (M; Ze ) and H k (M; Z` / `e ) ≈ Hn−k (M; Z) .`
  Its hypotheses (closed, connected, nonorientable — supplied by "closed nonorientable
  surface") and the choice L = M_Z are not checked in the card. With them, H_k(M;M_Z) ≅
  H^{n−k}(M;Z) follows from 3H.6 exactly, so the gap is repairable by replacing the sentence
  with 3H.6 plus its hypotheses.
* UCT block is correct: H⁰ = Z, H¹ = Hom(Z^{g−1}⊕Z₂,Z) ⊕ Ext(Z,Z) = Z^{g−1},
  H² = Ext(Z^{g−1}⊕Z₂,Z) = Z₂. Correct; even the displayed "≅ 0 ⊕ Z₂" is right.
* GAP (cosmetic but real): the "verification via the twisted cellular chain complex" writes
  `d_2(e^2) = \sum_{i=1}^g (1 + (-1)) a_i = 0`. The conclusion d₂ = 0 is correct (in the word
  a₁²⋯a_g² the two occurrences of a_i get coefficients c and −c because the second is preceded
  by the orientation twist ω(a_i) = −1), but the printed formula hides that argument and reads
  as if a single occurrence contributed both +1 and −1. Also `d_1(a_i)=(-1-1)e^0` is correct
  up to sign convention (im d₁ = 2Z either way).
* The step `ker(d_2) = Z, yielding H_2 ≅ Z` and `H_1 ≅ ker(d_1)/im(d_2) = Z^{g-1}/0` are
  correct (ker d₁ = {Σn_i = 0} ≅ Z^{g−1}, and g = 1 gives Z⁰ = 0, i.e. RP² correctly).
* Format: this card is the only §3.H card with no `source-checked` audit event, and its
  solution div nesting is inverted relative to the house style (`pf-proof` wraps `pf-step`s,
  and `::: pf-step` is used without `#sn` ids). Divs are balanced.

---

## E-HAT-3.H-3 — Bundles of groups = [X, BAut(G)]

**STATEMENT: matches.**
Book, AT.txt:16838–16842:
`3. Let B(X; G) be the set of isomorphism classes of bundles of groups E →X with`
`fiber G , and let E0 →BAut(G) be the bundle corresponding to the ‘identity’ action`
`ρ : Aut(G)→Aut(G) . Show that the map [X, BAut(G)]→B(X; G) , [f ] ֏ f ∗ (E0 ) , is`
`a bijection if X is a CW complex, where [X, Y ] denotes the set of homotopy classes`
`of maps X →Y .`
Card reproduces all of it (only typographic changes: `\mathcal{B}`, `\operatorname{Aut}`,
`f^*(E_0)`, double quotes for ‘identity’). No difference.

**PROOF: correct** (one standard fact used as a black box).
* `B Aut(G) = K(Aut(G),1)` for discrete Aut(G) — true (the Milnor/§1.B construction; the book
  builds BG in §1.B, so a citation would help, but nothing false is asserted).
* Bundles of groups with fibre G over a connected X ↔ Hom(π₁X, Aut(G))/conjugacy: this is the
  monodromy classification; the card constructs both directions (X̃ ×_{π₁} G) correctly.
* [X, K(π,1)] ≅ Hom(π₁X,π)/conjugacy for CW X: standard, and the card uses it with the right
  hypothesis (X a CW complex). Pullback f*E₀ has monodromy f_*, so the composite is the
  displayed map — the identification is exactly [f] ↦ f*(E₀).
* Disconnected X: [X,Y] and B(X;G) both split as products over components, so "apply the
  argument independently on each component" is legitimate (basepoints per component).

---

## E-HAT-3.H-4 — Proper homotopy equivalence of universal covers

**STATEMENT: matches.**
Book, AT.txt:16843–16845 (line 16844 is the extraction's superscript line, printed verbatim):
`4. Show that if finite connected CW complexes X and Y are homotopy equivalent,`
`                            e and Ye are proper homotopy equivalent.`
`then their universal covers X`
I.e. "…then their universal covers X̃ and Ỹ are proper homotopy equivalent." Card states
exactly this, with the same hypotheses (finite, connected, CW, homotopy equivalent).

**PROOF: has a gap — the existence of "compatible" lifts is asserted, not proved.**
The quoted step: `They lift to homotopies` $\widetilde g\widetilde f\simeq
\operatorname{id}_{\widetilde X}$, $\widetilde f\widetilde g\simeq
\operatorname{id}_{\widetilde Y}$ `after the endpoint lifts are chosen compatibly.`
Why this is not immediate: a lift of a homotopy gf ≃ id_X starting at g̃f̃ ends at a lift of
id_X, i.e. at a *deck transformation* γ, so all one gets for arbitrary lifts is
g̃f̃ ≃ γ and f̃g̃ ≃ δ with δ = f_*(γ). The card never shows that the two requirements can be
met simultaneously. They can — replacing g̃ by γ⁻¹g̃ gives ḡf̃ = γ⁻¹g̃f̃ ≃ id and
f̃ḡ = f_*(γ)⁻¹f̃g̃ ≃ f_*(γ)⁻¹δ = id because the two obstructions are related by f_* — but that
sentence is the missing content, and without it the stated homotopies are false for arbitrary
choices of lifts. Fix: insert the relation δ = f_*(γ) and the adjustment of g̃.
The rest of the proof is sound and I checked it:
* K_X, K_Y finite unions of lifted cells surjecting onto X, Y exist; {γK} is locally finite,
  so a compact set meets only finitely many translates (used twice).
* f̃ proper: f̃⁻¹(⋃γ_iK_Y) ⊆ ⋃_{γ∈S} γK_X with S finite when f_* is injective (f is a homotopy
  equivalence, so f_* is an isomorphism — this is why "finite connected" is needed); a closed
  subset of a compact set is compact.
* The lifted homotopies are proper by the same finite-fundamental-domain argument, uniformly
  in the parameter — that argument is correct as stated.

---

## E-HAT-3.H-5 — H^n(X; Z[π₁X]) for a finite graph

**STATEMENT: matches.**
Book, AT.txt:16846–16854:
`5. If X is a finite connected graph with π1 (X) free on g > 0 generators, show that`
`H n (X; Z[π1 X]) is zero unless n = 1 , when it is Z when g = 1 and the direct sum of`
`a countably infinite number of Z ’s when g > 1 . [Use Proposition 3H.5 and compute`
`Hcn (X)` / `     e as lim H n (X,` / `           --→` / `                   e X  e − Ti ) for a
suitable sequence of finite subtrees T1 ⊂ T2 ⊂ ···` / `          S` / `of Xe with i Ti = Xe .]`
Card: same hypothesis, same conclusion, and the full bracketed hint (Proposition 3H.5,
lim→ H^n(X̃, X̃−T_i), finite subtrees T₁ ⊂ T₂ ⊂ ⋯ with ∪T_i = X̃). No difference.

**PROOF: correct.** Checked, including every cited theorem's hypotheses:
* Proposition 3H.5 (AT.txt:16732–16735) `If X is a finite CW complex with universal cover Xe
  and funda-` / ` mental group π , then for all n , H n (X; Z[π ]) is isomorphic to Hcn ( e X; Z)`
  — hypotheses "finite CW complex, universal cover, fundamental group π" are met (X is a
  finite connected graph), and its π is indeed π₁X. Correct use.
* X̃ is a locally finite tree (finite graph ⇒ locally finite; contractible cover). Correct.
* H_c^n(X̃) ≅ lim→ H^n(X̃, X̃−T_i): Hatcher's own hint; legitimate for an exhaustion by finite
  subtrees because every compact set lies in some T_i.
* LES of the pair with X̃ contractible gives H^n(X̃,X̃−T_i) = 0 for n ≠ 1 and
  H¹(X̃,X̃−T_i) ≅ H̃⁰(X̃−T_i) ≅ Z^{c_i−1} for c_i = #components (nonempty because X̃ is
  infinite and T_i finite). Correct.
* Injectivity/splitting of the transition maps: for T_i ⊂ T_{i+1} every component of X̃−T_i
  meets X̃−T_{i+1} (a component contained in a finite T_{i+1} would force X̃ finite), so a
  class restricting to 0 is 0; an injection of free abelian groups splits. The card's
  "choosing one distinguished descendant in each component gives a splitting" is right.
* Ranks → ∞: for a locally finite tree with infinitely many ends (g > 1), the number of
  components of X̃ − B_n is unbounded, since every component of the complement contains a ray
  (an end) and the end space surjects onto π₀(X̃−B_n). The card's "infinitely many ends and
  branching repeats indefinitely" is a correct sketch of this.
* g = 1: X̃ ≅ R, complements of large intervals have two components, transition maps are
  isomorphisms of H̃⁰, so H_c¹ ≅ Z. Correct.

---

## E-HAT-3.H-6 — Locally finite homology and infinite cellular chains

**STATEMENT: matches.**
Book, AT.txt:16856–16863 (extraction superscripts on their own lines):
`6. Show that homology groups Hnℓf (X; G) can be defined using locally finite chains,`
`                       P` / `which are formal sums σ gσ σ of singular simplices σ : ∆n →X
with coefficients` / `gσ ∈ G , such that each x ∈ X has a neighborhood meeting the images of
only finitely` / `many σ ’s with gσ ≠ 0 . Develop this version of homology far enough to show
that` / `for a finite-dimensional locally compact CW complex X , Hnℓf (X; G) can be computed`
`                               P     n` / `using infinite cellular chains α gα eα .`
Card reproduces this word for word, including both conditions and "finite-dimensional locally
compact". No difference.

**PROOF: correct in outline; two steps are asserted rather than proved (neither is false).**
* Chain complex: ∂ of a locally finite sum is locally finite ("any neighborhood meeting the
  image of a face also meets the image of its parent simplex") — correct.
* "Proper maps induce homomorphisms on locally finite chains" — correct (preimage of a compact
  neighborhood is compact, a finite subcover bounds the simplices met).
* ASSERTED (true): `Such a CW complex is locally finite: every point has a neighborhood
  meeting only finitely many cells.` This is Hatcher's Appendix exercise 4, AT.txt:26379–26380
  `4. Show that a CW complex is locally compact iff each point has a neighborhood that`
  `meets only finitely many cells.` The card gives it as immediate; a citation (or the
  one-line argument via Proposition A.1, AT.txt:25888 `A compact subspace of a CW complex is
  contained in a finite subcomplex.`) is missing.
* ASSERTED (true, needs the argument): `H_n^{lf}(X^n, X^{n-1};G) ≅ ∏_{e_α^n} G` and the
  passage `the standard cellular-homology argument applies without convergence issues. It
  yields a chain equivalence between C_*^{lf}(X;G) and the locally finite cellular complex`.
  Note the quotient C^{lf}(Xⁿ)/C^{lf}(X^{n−1}) is *not* concentrated in degree n (a k-simplex,
  k < n, may lie inside an n-cell), so "concentrated in the cell dimension" needs the LES of
  the pair plus cellular approximation of locally finite chains; and a spectral sequence of
  the filtration gives an isomorphism of homology groups, not literally a chain equivalence.
  Both conclusions are true (finite dimension makes the filtration finite, so there is no
  lim¹ problem); the card simply does not supply the argument.
* Everything the card writes about ∏ vs ⊕ (product, because infinitely many n-cells may carry
  nonzero coefficients) and about boundary maps being the usual incidence numbers is correct.

---

# Summary of defects — §3.H, most serious first

1. **E-HAT-3.H-2, proof (wrong general principle, conclusion unaffected).** "By Poincaré
   Duality for manifolds with local coefficients, for any closed n-manifold:
   H_k(M;L) ≅ H^{n−k}(M;Z)" is false for a general local system L (Klein bottle, L trivial:
   H₀ = Z ≠ Z₂ = H²). The theorem that gives the card's result is Hatcher's Theorem 3H.6
   (AT.txt:16825–16828), which requires M closed, connected, nonorientable and L = M_Z; those
   hypotheses are not checked. The displayed answer (H₀ = Z₂, H₁ = Z^{g−1}, H₂ = Z) is
   correct.
2. **E-HAT-3.H-4, proof (unjustified step).** "They lift to homotopies g̃f̃ ≃ id_X̃,
   f̃g̃ ≃ id_Ỹ after the endpoint lifts are chosen compatibly" — lifts only give
   g̃f̃ ≃ γ, f̃g̃ ≃ f_*(γ); the (true) compatibility argument is missing.
3. **E-HAT-3.H-6, proof (two asserted steps).** (i) "locally compact CW ⇒ locally finite" is
   quoted as immediate (it is Hatcher Appendix exercise 4, AT.txt:26379–26380); (ii) the
   exact-couple step producing the locally finite cellular complex is asserted, and the
   implicit "relative complex concentrated in degree n" fails at chain level (it holds only
   after passing to homology, via the LES of the pair).
4. **E-HAT-3.H-2, proof (garbled verification).** `d_2(e^2) = Σ_i (1+(−1))a_i = 0` compresses
   the parity argument until it reads as wrong; the correct reason is that the two occurrences
   of a_i in a_i² receive coefficients c and −c because of the orientation twist.
5. **E-HAT-3.H-3, proof (black box).** `B Aut(G) = K(Aut(G),1)` is asserted without the
   construction/citation; nothing false, but it is the only real input.
6. **Formatting, E-HAT-3.H-2.** Uses bare `::: pf-step` (no `#sn` ids) and nests `pf-step`
   inside `pf-proof` instead of the reverse; the card also lacks any `source-checked` audit
   event. Divs balance.

No card in §3.H has a statement that differs from the printed exercise.
