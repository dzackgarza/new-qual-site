# SRC-TEXT-HAT02 — audit of Hatcher §4 additional topics (§4.A–§4.L)

Member m1. Slice: every card under `corpus/collections/SRC-TEXT-HAT02/` in the directories
`4-a 4-b 4-d 4-f 4-g 4-h 4-i 4-k 4-l`.
Witness for every book claim: line numbers in `tmp/hat/AT.txt` (the extracted text), quoted from the file.
No file under `corpus/` was modified.

## Card counts (counted with `ls`, not sampled)

| directory | section | cards |
|---|---|---|
| 4-a | §4.A Basepoints and Homotopy | 5 |
| 4-b | §4.B The Hopf Invariant | 2 |
| 4-d | §4.D Cohomology of Fiber Bundles | 10 |
| 4-f | §4.F Spectra and Homology Theories | 3 |
| 4-g | §4.G Gluing Constructions | 4 |
| 4-h | §4.H Eckmann–Hilton Duality | 4 |
| 4-i | §4.I Stable Splittings of Spaces | 3 |
| 4-k | §4.K The Dold–Thom Theorem | 6 |
| 4-l | §4.L Steenrod Squares and Powers | 5 |
| **total** | | **42** |

Sections of chapter 4's additional topics with **no** cards (no directory): §4.C, §4.E, §4.J.
(The exercise blocks they would need are at AT.txt:21215–21223 for 4.B, 22149–22189 for 4.D,
22600–22616 for 4.F, 22813–22823 for 4.G, 23110–23121 for 4.H, 23272–23288 for 4.I,
24094–24121 for 4.K, 25802–25820 for 4.L; 4.K's block continues onto page 487 *after* the 4.L running
head, at AT.txt:24106–24121 — a counting trap: 4.K has 6 exercises, not 4.)

All 42 cards were read in full: statement compared word-by-word with the printed exercise and every
proof read line by line. Nothing in this file is "sampled".

---

## §4.A — Basepoints and Homotopy (5 cards; exercises at AT.txt:21093–21129)

### E-HAT-4.A-1 — statement matches | proof correct
Book AT.txt:21093–21095: "1. Show directly that if X is a topological group with identity element x0 , then any two
maps f , g : (Z, z0 )→(X, x0 ) which are homotopic are homotopic through basepoint-preserving maps."
Card agrees word for word. Proof: `F(z,t)=H(z,t)·γ(t)^{-1}` with `γ(t)=H(z_0,t)`; both end checks and the
basepoint check `γ·γ^{-1}=x_0` are computed explicitly and correctly. No gap.

### E-HAT-4.A-2 — **statement differs** (dropped clause) | proof correct
Book AT.txt:21097–21101 prints, after the sentence the card keeps, a final sentence:
"… under composition with inner automorphisms of π . In particular, if
π is abelian then [X, K(π , 1)] = hX, K(π , 1)i = Hom(π1 (X), π ) ."
The card's statement stops at "under composition with inner automorphisms of $\pi$." and **omits the
"In particular, if π is abelian …" clause (AT.txt:21100–21101)**.
Proof: the homotopy `S^n×I → Y` of `f a` to `(γf)a` traces `γ`, so `[(γf)a] = β_γ[fa]` for all `[a]`,
hence `(γf)_* = β_γ f_*`; the deduction for `[X,K(π,1)]` (free classes = orbits, β_γ = conjugation in degree 1)
is correct. No defect in the proof.

### E-HAT-4.A-3 — statement matches | proof correct (one loose citation)
Book AT.txt:21102–21106, reproduced exactly, including "group of homotopy classes of homotopy equivalences"
and "automorphisms modulo inner automorphisms".
Proof correct: path-change changes f_* by an inner automorphism; `gf`, `fg` inducing the identity outer
automorphism are freely homotopic to the identity, which *is* a two-sided homotopy inverse.
Minor: the cited "Hatcher's Proposition 4A.2" (AT.txt:20891–20893) only gives
`hZ,Xi/π_1(X) ≅ [Z,X]`; identifying `[K,K]` with `Hom(π,π)/Inn(π)` also uses the classification
`⟨K(G,1),K(H,1)⟩ ≅ Hom(G,H)` (Theorem 1B.9), which the card does not cite.

### E-HAT-4.A-4 — **statement differs** (dropped hint) | **proof has a gap: named theorem's hypotheses unchecked**
Book AT.txt:21108–21113 ends with the bracketed hint (the extraction splits the wedge sign onto its own line):
"[ GLn (Z) is the automorphism group of Zn ≈ πk ( W n S k ) ≈ Hk ( W n S k ) .]"
The card has no bracketed hint at all.
Gap, stated exactly: step `s3` says "By Whitehead's Theorem, a based map f : X→X between simply connected CW
complexes of dimension k is a homotopy equivalence if and only if f_* : π_k(X)→π_k(X) is an isomorphism of abelian
groups." Hatcher's theorem (AT.txt:17284–17287) is: "Theorem 4.5. If a map f : X →Y between connected CW complexes
induces isomorphisms f∗ : πn (X)→πn (Y ) for all n , then f is a homotopy equivalence." So the cited theorem's
hypothesis is "for all n", while the card verifies degree k only; the other degrees (in particular i > k, which are
not zero for a wedge of k-spheres) are not checked anywhere in the card. That is the gap — I checked the theorem's
hypotheses, I do **not** claim the conclusion is false, and I have no verified counterexample to the card's general
formulation. The conclusion here is true and the card already has a correct argument in step `s2`: [X,X]_* ≅ M_n(Z)
is an isomorphism of monoids under composition, so an invertible matrix supplies an explicit two-sided homotopy
inverse (equivalently, Hilton's theorem gives the higher π_i from π_k for wedges of spheres). The final remark that
π₁(X) = 0 makes based and free classes agree is correct (the book asks for k > 1, AT.txt:21108).

### E-HAT-4.A-5 — statement matches | proof **unverified** (not endorsed, not called wrong)
Book AT.txt:21114–21129; the card reproduces (a), (b), (c) faithfully, including "(c) … show this presentation
reduces to a finite presentation if n > 2 and a presentation with a finite number of generators if n = 2. In the
latter case, deduce that π1 (X̃2 ) has no finite presentation from the fact that H2 (X̃2 ) is not finitely
generated."
The card's solution rests on a reading of the book's construction that I could not verify from AT.txt. The card
writes "Let X̃_n → X_n be the corresponding infinite cyclic cover, with deck generator T", X_n = (S¹∨S¹)ⁿ and
φ_n the total exponent sum. The book's construction in this range is heavily garbled in the extraction (AT.txt:
20950–20970, e.g. "Since X is a K(π , 1) , so is X e", "The map f lifts to a map fe : Te 2n →R , and Z lifts
homeomorphically to a subspace Z⊂X e , namely fe−1 (0) ∩ X e"), so whether the book's X̃_n is the infinite cyclic
cover, the universal cover, or a level-set complex cannot be settled from the file. Two consequences follow for the
audit, and I state them rather than guess: (i) parts (b), (c) depend on that identification, so **unverified**;
(ii) the card's τ₂ claim ("fixes a, b and sends c ↦ aca⁻¹") is likewise **unverified** — the book states only the
mapping-torus structure (AT.txt:21118–21123), not the action of the deck transformation on a presentation, and my
own attempt to derive it was inconclusive.
What I did check and can report: the card is internally consistent — χ(Z) = 1−12+16 = 5 together with rank H₁ = 5
forces rank H₂ = 9, and its final five-generator presentation of H₃ has abelianisation Z⁵ (every displayed relator
is a commutator or a conjugacy); and such an automorphism is at least well defined on the presentation of H₂ got
from (1), since σ(a)=a, σ(b)=b, σ(c)=aca⁻¹ preserves both families of relators. The cell counts 12 and 16 in (a)
are asserted, not derived from the octahedral model. Per the audit rule, this card is **unverified**, not "correct"
and not "defective".

---

## §4.B — The Hopf Invariant (2 cards; exercises at AT.txt:21215–21223)

### E-HAT-4.B-1 — statement matches | proof correct for n ≥ 2, silent for n = 1
Book AT.txt:21217–21220: "Show that the Hopf invariant of a composition S 2n−1 --→ S 2n−1 --→ S n is given by
H(gf ) = (deg f )H(g) , and for a composition S 2n−1 --→ S n --→ S n the Hopf invariant satisfies
H(gf ) = (deg g)2 H(f ) ." Card agrees, including the notation for both compositions.
Proof: the two mapping-cone maps `C_{gf}→C_g` (identity on S^n, degree d on the top cell) and `C_f→C_{gf}`
(bottom degree d, top degree 1) are correct, and so is the pullback computation `x² = dH(g)y`, `d²H(f)y = H(gf)y`.
Caveat: the argument needs H^{2n}(C_f) ≅ Z with a chosen generator; for n = 1 (f: S¹→S¹) that group is
Z/|d| and Hatcher's H is identically 0 (AT.txt:21161 "H(f ) is always zero for odd n"), so the proof does not
cover n = 1 even though the identity is trivially true there. Small gap, easily patched.

### E-HAT-4.B-2 — **statement differs** (dropped hint) | **proof has a gap**
Book AT.txt:21222–21223 ends: "[Show that Cp is a manifold and apply Poincaré duality.]"
The card's statement has no hint. Note that this card's own audit trail claims
`solution-reviewed`/`source-checked` "…Exercise 2 and its hint; the stored statement matches" — the hint is
in fact absent.
Gaps: (i) for n = 1 the card says "the same dimension relation and the homotopy sequence force k = 0". They do
not: with n = 1, k = 1 the segment is π₁(S¹) → π₀(S¹) = 0 → π₀(Sᵐ) → 0, which is consistent. The real reason
(m ≫ 1 ⇒ Sᵐ simply connected ⇒ the bundle over S¹ is trivial ⇒ Sᵐ ≅ S¹×S^k, impossible) is not given. The
conclusion k = 0, m = 1 is the book's and is true, but the stated justification is not.
(ii) for n > 1 the card asserts "This is a closed 2n-manifold … Since Cp is a closed orientable 2n-manifold,
Poincaré duality says …". Orientability is not proved, and it is needed: Poincaré duality with Z coefficients
is what upgrades "H(p) is odd" (all that Z/2 duality gives) to "H(p) = ±1". Orientability does hold (the sphere
bundle S(E) = S^{2n−1} is simply connected, so E is orientable, so the Thom space D(E)/S(E) = C_p is orientable),
but the card does not argue it.

---

## §4.D — Cohomology of Fiber Bundles (10 cards; exercises at AT.txt:22149–22189)

### E-HAT-4.D-1 — statement matches | proof correct
Book AT.txt:22150–22154, reproduced exactly (including "k > 1" and "the square of a generator of H²(E_k;Z) is
k times a generator of H⁴(E_k;Z)"). Proof: Leray–Hirsch with a class restricting to a fibre generator gives
H^*(E_k) ≅ H^*(S⁴){1,x}; with x² = p^*u in CP³ (AT.txt:22150–22154 context), naturality gives
x² = F^*(x²) = p_k^*f^*u = k p_k^*u. Correct.

### E-HAT-4.D-2 — statement matches | proof correct
Book AT.txt:22155–22156 reproduced exactly. Proof: π₁(S¹)→π₁(S¹/…)=Z_p onto ⇒ the generator a ∈ H¹(;Z_p)
restricts to a generator, Leray–Hirsch ⇒ Z_p[b]{1,a}, graded commutativity kills a² for odd p, β(a) = b, and
for p = 2, Sq¹ = β in degree 1 forces b = a², so H^* = Z₂[a]. Both displayed answers are the standard ones.

### E-HAT-4.D-3 — statement matches | proof correct
Book AT.txt:22157–22158 reproduced exactly (same list of generators, "and similarly in the quaternionic case").
Proof: fibre S^{2k−2n+1} of V_n → V_{n−1}, complement bundle stably trivial ⇒ all Chern classes vanish ⇒
Euler class of the sphere bundle is 0 ⇒ Gysin gives a class restricting to a fibre generator ⇒ Leray–Hirsch
makes H^*(V_n) free over H^*(V_{n−1}) on {1,x}; odd generators square to zero in a torsion-free ring. Correct;
the quaternionic degrees 4k−4n+3, …, 4k−1 are right.

### E-HAT-4.D-4 — statement matches | proof correct
Book AT.txt:22159–22160 reproduced exactly (`σ_i` the i-th elementary symmetric polynomial).
Proof: x_i = c₁ of the tautological quotients, ∑L_i trivial ⇒ ∏(1+x_i) = 1 ⇒ σ_j(x) = 0; the surjection
Z[x]/(σ) → H^*(F_n) is compared with the Poincaré polynomial ∏_{j=1}^n(1+t²+…+t^{2(j−1)}) obtained from the
Leray–Hirsch tower, and with the standard monomial basis x₁^{a₁}…x_n^{a_n}, 0 ≤ a_i ≤ n−i of the coinvariant
algebra (rank n!). Both counts agree, so the surjection is an isomorphism. Correct.

### E-HAT-4.D-5 — **statement differs** (dropped remark) | proof correct except a mis-displayed Gysin segment
Book AT.txt:22162–22164 ends "[Hence n = 1, 2, 4, 8 by Adams' theorem.]"; the card omits it.
The displayed Gysin segment in the card,
`H^k(S^m) → H^0(S^n) --∪e--> H^{k+1}(S^n) --p^*--> H^{k+1}(S^m)`, is misstated: the term before H⁰(S^n) is
H^{q−k−1}(B) with q = 0, i.e. H^{−k−1}(S^n) = 0, not H^k(S^m). The conclusion ("the outer groups vanish")
is right either way (k+1 < m, and negative degrees vanish), and the rest is correct: e generates H^n(S^n) ⇒
k = n−1, m = 2n−1; with V the cone/disk bundle, T(E) = V/S(V) ≃ C_p, U² = p^*e·U, so the Thom isomorphism
sends the generator e to U², a generator of H^{2n}(C_p) ⇒ H(p) = ±1. The n = 1 paragraph is correct here
(π₁(Sᵐ) → π₁(S¹) onto with π₁(Sᵐ) = 0 for m > 1).

### E-HAT-4.D-6 — **statement differs** (dropped remark) | proof correct
Book AT.txt:22165–22169 ends "[When n > 1 there are examples where M is not homeomorphic to CPn .]"; the card
omits it.
Proof: π₁(M) = 0 from π₁(S^{2n+1}) → π₁(M) → π₀(S¹); M closed orientable; Gysin with H^*(S^{2n+1}) = 0 gives
∪e an isomorphism in the relevant range, hence H^*(M) = Z[e]/(e^{n+1}). Converse: pull back the Hopf bundle
along the classifying map of α; Gysin gives H^k(E) = Z for k = 0, 2n+1 and 0 otherwise; ∂ = ∂_∞∘c_* with
∂_∞ iso and c_* iso on H₂ (from c^*u = α generating, H₁ = 0, UCT) gives π₁(E) = 0; then Hurewicz + Whitehead
give E ≃ S^{2n+1}. Correct.

### E-HAT-4.D-7 — statement matches | proof correct
Book AT.txt:22170–22171 reproduced exactly. Proof: the Thom class restricts to a generator of
H^n(D^n_b, S^{n−1}_b), giving a fibre orientation, and naturality of the restriction under the transport
L_γ shows the sign is +1, hence locally constant along paths, hence orientable. Correct.

### E-HAT-4.D-8 — statement matches | proof correct
Book AT.txt:22172–22176 reproduced exactly (including "B a CW complex", "B₊", and the pointer to §3.2's
reduced cross product). Proof: T(E) = B×D^n / B×S^{n−1} ≅ B₊ ∧ (D^n/S^{n−1}) = Σ^n(B₊), Thom class 1×u,
Thom isomorphism = relative cross product with u = suspension isomorphism. Correct.

### E-HAT-4.D-9 — **statement differs** (dropped hint) | proof correct
Book AT.txt:22178–22182 ends "[Hint: Diagonal matrices in U(n) are compositions of scalar multiplication in
n lines in Cn , and CPn−1 is connected.]"; the card omits the whole bracketed hint.
Proof: diag(z,w) = diag(zw,1)·diag(w⁻¹,w) and diag(w⁻¹,w) is a loop in SU(2) ≅ S³, hence nullhomotopic; the
family of null-homotopies is continuous in w (the loop space map S¹ → ΩSU(2) is null-homotopic because
π₂(SU(2)) = 0) — this last point is asserted by "natural in (z,w)" rather than proved, a minor omission; the
iteration and the Sp(n) case (diag(q⁻¹,q) is nullhomotopic because the two blocks contribute −1 and +1 in
π₃(Sp(2)) ≅ Z) are correct.

### E-HAT-4.D-10 — **statement differs** (dropped parenthetical) | proof correct
Book AT.txt:22183–22189 contains, between "… has an eigenvalue in H ." and "For t ∈ [0, 1] …", the parenthetical
"(The usual argument over C involving roots of the characteristic polynomial does not work due to the lack of a
good quaternionic determinant function.)". The card omits this parenthetical.
Proof: H(t,λ) = tλI + (1−t)A; a singular value at t < 1 gives Av = −t(1−t)⁻¹λv, a forbidden left eigenvalue;
H(1,λ) = λI is invertible, so λ ↦ λI is nullhomotopic; GL_n(H) ≃ Sp(n); diag(λ,…,λ) ≃ diag(λ^n,1,…,1) by
4.D-9 and λ ↦ λ^n has degree n on S³ = Sp(1), whose inclusion into Sp(n) is an isomorphism on π₃ ≅ Z.
Contradiction. Correct.

---

## §4.F — Spectra and Homology Theories (3 cards; exercises at AT.txt:22600–22616)

### E-HAT-4.F-1 — statement matches | proof correct (one step recalled, not proved)
Book AT.txt:22601–22603 reproduced exactly, including "Assuming the first two axioms for a homology theory on
the CW category" and "the converse also holds for countable CW complexes".
Proof: direct limit ⇒ wedge: a finite subcomplex of ⋁X_α lies in a finite wedge of finite subcomplexes, and the
filtered colimit of the direct sums is the direct sum; conversely the telescope/Mayer–Vietoris argument with
1−s_* injective on a direct sum (finite-support argument) gives h_n(X) ≅ colim h_n(X_i). Correct.
Gap of exposition only: "Recall first that these two axioms already imply the wedge axiom for finite wedge sums"
is used, not proved (it is the usual Mayer–Vietoris consequence of exactness).

### E-HAT-4.F-2 — **statement differs** (dropped hint) | proof correct
Book AT.txt:22604–22611 ends "[Use induction on the number of cells of X and the five-lemma.]"; the card omits
the hint (and itself uses exactly that induction, so the hint is the proof outline).
Proof: X = S^q reduces to Freudenthal for π_{q+r}(Σ^rY) → π_{q+r+1}(Σ^{r+1}Y) with connectivity → ∞; for an
attachment S^{q−1} → A → X the Puppe sequences of ⟨Σ^r X/A, Σ^r Y⟩ → ⟨Σ^r X, Σ^r Y⟩ → ⟨Σ^r A, Σ^r Y⟩ give a
ladder whose outer maps are isomorphisms for large r (induction for A, sphere case for S^{q−1}, S^q), and the
five lemma for groups applies once r makes the terms groups. Correct.

### E-HAT-4.F-3 — statement matches in substance | proof correct
Book AT.txt:22612–22615: "… the natural map lim --→ ΩZn →Ω lim --→ Zn is a weak homotopy equivalence, where the
direct limits mean mapping telescopes." The card writes `hocolim` where the book prints the direct-limit arrow
and immediately explains that the direct limit *means* the mapping telescope, so this is a notational
modernisation, not a change of statement.
Proof: π_j of a telescope = colim π_j (compactness: a sphere maps into a finite subtelescope, which deformation
retracts to its last stage), applied to ΩZ_n and to Z_n, together with π_j(ΩZ_n) = π_{j+1}(Z_n); κ_* is the
identity of the common colimit. Correct (the continuity/colimit interchange is exactly the compactness argument
given).

---

## §4.G — Gluing Constructions (4 cards; exercises at AT.txt:22813–22823)

### E-HAT-4.G-1 — statement matches | **proof has a gap**
Book AT.txt:22815–22817 reproduced exactly ("the union of the finite iterated mapping cylinders M(f1 , ··· , fn )").
Gap: "Since the finite-stage homotopies are compatible, they assemble on the union … to a continuous homotopy
r : M(f₁,f₂,…)×I → M(f₁,f₂,…)." A compatible family of homotopies on a nested union need not be continuous:
continuity of the patched map requires local finiteness, closedness, or the union topology to be coherent with
the M_n. Nothing like this is verified (and in general the union topology of an increasing union of arbitrary
spaces is not the weak topology). Hatcher's own infinite-concatenation arguments in this book (e.g.
AT.txt:22744–22745 "the infinite concatenation of these deformation retractions in the t intervals
[1/2ⁿ⁺¹, 1/2ⁿ]") avoid exactly this issue by rescaling time; the card does not.

### E-HAT-4.G-2 — statement matches | **proof proves a weaker statement**
Book AT.txt:22818–22819 reproduced exactly.
Two restrictions not in the statement are imposed silently:
(i) The card defines a complex of spaces as "a vertex space for each v ∈ Γ, an edge space for each e ∈ Γ", i.e.
Γ a graph. Hatcher's complexes of spaces have a ∆-complex base with an iterated mapping cylinder over **every**
simplex (AT.txt:22683–22698: "There is a natural generalization of ∆X in which one starts with a ∆ complex Γ …
for each n simplex of Γ we have a sequence of maps X₀ → … → X_n , and we define the iterated mapping cylinder"),
so the card's local triviality computation covers only 1-dimensional Γ, not the graded structure ([0,1]-bundles
over higher simplices, glued by the face maps) that the exercise's ΔX contains.
(ii) "Because all attaching maps f_{e,i} are homeomorphisms and Γ is connected, all vertex spaces X_v and edge
spaces X_e are homeomorphic to a common fiber space F" — connectedness of Γ is assumed but is not in the
statement; for disconnected Γ the fibres over different components can differ and the claim has to be read
componentwise.

### E-HAT-4.G-3 — **statement differs** (dropped pointer) | proof correct
Book AT.txt:22820–22821: "What is the nerve of the cover of a simplicial complex by the open stars of its
vertices? [See Lemma 2C.2.]" The card omits "[See Lemma 2C.2.]".
Proof: st°(v₀)∩…∩st°(v_q) ≠ ∅ iff some simplex contains all v_i iff v₀,…,v_q span a simplex (barycentre one
way, ambient simplex the other); two points verify both directions. Answer N = K is correct.

### E-HAT-4.G-4 — **statement differs** (dropped hint) | **proof has a gap**
Book AT.txt:22822–22823: "Show that Proposition 4G.2 and its corollary hold also for CW complexes and covers by
families of subcomplexes. [CW complexes are paracompact; see [VBKT].]" The card omits the bracketed hint — which
is the intended proof strategy (pass to an open cover, or replace the cover by open stars, and invoke 4G.2 at
AT.txt:22764–22767).
Gap: the actual argument is replaced by assertion: "… this simplex is contractible. Along the boundary, the
choices can only increase, and the attaching maps are inclusions of subcomplexes. The homotopy gluing lemma
therefore proves by cellular induction that p is a homotopy equivalence." No induction is carried out, no gluing
lemma is stated or its hypotheses checked; the equivalence p : ΔX_U → X is the whole content of the subcomplex
version of 4G.2. (The second half, using 4G.1 with the diagram of points and Γ = barycentric subdivision of N U,
matches the book's proof of Corollary 4G.3 at AT.txt:22794–22797 and is fine.)

---

## §4.H — Eckmann–Hilton Duality (4 cards; exercises at AT.txt:23110–23121)

### E-HAT-4.H-1 — **statement differs** (dropped hint) | proof correct
Book AT.txt:23111–23113 ends "[If A ↪ X is a cofibration, so is A× Y ↪ X × Y for any space Y .]"; the card omits
it (and then uses exactly that fact, for Z in place of Y, at the step "Since A↪X is a cofibration, so is
Z×A ↪ Z×X").
Proof: adjunction for compact Hausdorff X, A; the cofibration gives the extension over Z×X×I of the map defined
on (Z×X×{0}) ∪ (Z×A×I); adjunction again gives the lift. Hypothesis "compact Hausdorff" is used exactly for the
exponential law. Correct.

### E-HAT-4.H-2 — statement matches (Σ vs ∪ notation) | proof correct
Book AT.txt:23114–23116, reproduced with `B∪_f X` for the book's `B ⊔_f X` — a notational difference only.
Proof: defines the HEP data for B ↪ P, builds H_X on X×I by the cofibration A ↪ X, and patches on
P×I ≅ (B×I) ⊔_{f×id} (X×I) using j(f(a)) = q(i(a)); well-defined and continuous by the pushout property.
Correct. The card adds "closed" to the cofibration hypothesis (not needed, and not in the statement) — harmless.

### E-HAT-4.H-3 — **statement differs** (dropped hint) | proof correct
Book AT.txt:23117–23119 ends "[This is dual to Proposition 0.19.]"; the card omits it.
Proof: replace the homotopy inverse g by a fibre-preserving g′ using HLP for p₁ (p₁g = p₂fg ≃ p₂); the lemma
(fibre-preserving u ordinarily homotopic to id ⇒ left inverse over B) is proved by lifting ph_t starting at
id_E and a two-parameter lift; apply it to gf to get a with a·gf ≃_B id; ℓ = ag is an ordinary equivalence with
ℓf ≃_B id; repeat for ℓ to get m with mℓ ≃_B id; then m ≃_B mℓf ≃_B f and fℓ ≃_B mℓ ≃_B id. All steps check.
The lemma's "lift this two-parameter homotopy … reading along the opposite boundary" is compressed but standard
and correct.

### E-HAT-4.H-4 — statement matches | definition incomplete (no false step)
Book AT.txt:23120–23121 reproduced exactly.
The card's ∇(f₁,…,f_n) = { (φ_σ) ∈ ∏_σ X_{max σ}^σ : φ_σ|τ = f_{max σ,max τ}∘φ_τ } is a consistent definition
(the n = 1 case is checked to give the mapping path space E_{f₁}), and the general ∇X is defined with the
reversed maps. Incompletenesses: (i) a "definition of the dual of ΔX" should include the projection ∇X → Γ
(ΔX comes with ΔX → Γ, AT.txt:22698–22699), which is never given — the exercise's own point is a *map*, the
dual of ΔX → Γ; (ii) "Each condition is a closed condition, and the conditions are consistent" requires the
X_max σ to be Hausdorff, which Hatcher does not assume for a complex of spaces; (iii) no verification that ∇X is
the total space of a fibration (the reason the construction is useful). No statement in the card is false.

---

## §4.I — Stable Splittings of Spaces (3 cards; exercises at AT.txt:23272–23288)

### E-HAT-4.I-1 — **statement differs** (dropped hint) | proof correct
Book AT.txt:23273–23276 ends "[One approach: Show the map Σr + Σq : ΣX →ΣA ∨ Σ(X/A) induces an isomorphism on
homology, where r : X →A is the retraction and q : X →X/A is the quotient map.]"; the card omits it (and follows
exactly that approach, so the dropped hint is the solution sketch).
Proof: i_* split injective with splitting r_*, so the LES of (X,A) splits into short exact sequences and
(r_*,q_*) : H̃_j(X) ≅ H̃_j(A) ⊕ H̃_j(X/A); under suspension, F_* is that map; both sides simply connected
(suspensions of connected spaces); homology Whitehead. Correct.

### E-HAT-4.I-2 — **statement differs** (dropped sentence) | proof correct
Book AT.txt:23280–23282 has, after the assertion, a second sentence: "Thus to determine stable splittings of
K(Zn , 1) it suffices to do the case that n is a prime power, as in Proposition 4I.3." The card's statement stops
after the first sentence, so that consequence is dropped.
Proof: Σ(X×Y) ≃ ΣX ∨ ΣY ∨ Σ(X∧Y) (Prop 4I.1) and K(G×H,1) ≃ K(G,1)×K(H,1) reduce the claim to
Σ(K(Z_m,1) ∧ K(Z_n,1)) ≃ *; H̃_*(K(Z_m,1)) is m-torsion in odd degrees, and for gcd(m,n) = 1
A⊗B = 0 (Bézout) and Tor₁(A,B) = 0 (Tor annihilated by both m and n), so the reduced Künneth formula kills every
H̃_k of the smash product; a simply connected acyclic CW complex is contractible. Correct.

### E-HAT-4.I-3 — statement differs (dropped pointer) | proof correct for k ≥ 1, gap at k = 0
Book AT.txt:23284–23288 ends "… if these Xi 's are chosen to have the minimum number of cells in each dimension,
as described in the remarks following the proof." The card keeps the "minimum number of cells" clause but drops
"as described in the remarks following the proof" — the part that fixes which cell structure is meant.
Proof: a high-dimensional lens space is a finite skeleton of K = K(Z_{p^n},1), so its suspension's (2k+1)-skeleton
is (ΣK)^{(2k+1)}; the splitting ΣK ≃ ⋁X_i (Prop 4I.3) can be taken cellular, restricts to the (2k+1)-skeleta,
and is a homology isomorphism in every degree because both sides are (2k+1)-dimensional and the calculation is
degreewise. Gap: "Both sides of (3) are simply connected" is used for Whitehead. The right-hand side has no 1-cells
in the minimal models, but the left-hand side (ΣK)^{(2k+1)} *does* have a 1-cell (from the 0-cell of K), so the
argument is fine only because ΣK is simply connected — and for k = 0 the 1-skeleton of a suspension is a graph
that is not simply connected, so the k = 0 case is not covered by this argument at all.

---

## §4.K — The Dold–Thom Theorem (6 cards; exercises at AT.txt:24094–24105 and 24109–24121)

### E-HAT-4.K-1 — statement matches | proof correct
Book AT.txt:24095–24096 reproduced exactly. The proof is correct and note that it legitimately uses Exercise 4
of §4.G (the subcomplex-cover version of 4G.2): weak homotopy equivalences between CW subcomplexes are homotopy
equivalences by Whitehead (AT.txt:23696–23698 is the statement of Corollary 4K.2, whose hypothesis is exactly
"f(Ui ) ⊂ Vi for all i" and "each f : Ui1 ∩ ··· ∩ Uin →Vi1 ∩ ··· ∩ Vin is a weak homotopy equivalence"), then
4G.1 + the subcomplex 4G.2 give f ≃ id-level equivalence. Correct.

### E-HAT-4.K-2 — **statement differs** (dropped hint) | proof correct
Book AT.txt:24098–24100 ends "[Consider the cover of L by open stars of simplices and the cover of K by the
preimages of these open stars.]"; the card omits it.
Proof: V_σ = open star of σ, U_σ = f⁻¹(V_σ); finite intersections are V_ρ, U_ρ for ρ the spanned simplex;
V_ρ ⋍ * and U_ρ deformation retracts to f⁻¹(x_ρ) (the barycentric rescaling described), so each f : U_ρ → V_ρ is
a weak equivalence; 4K.2 for these open covers gives f a weak equivalence; CW type + Whitehead finishes. Correct.

### E-HAT-4.K-3 — statement matches | proof correct
Book AT.txt:24102 reproduced exactly. Proof: the weakly increasing representatives form a compact fundamental
domain for the Σ_n-action in the Hausdorff quotient, so a homeomorphism onto SP_n(I), and (x_j) ↦ (y_0,…,y_n) with
y_0 = x_1, y_i = x_{i+1}−x_i, y_n = 1−x_n is an affine homeomorphism onto Δ^n. Correct.

### E-HAT-4.K-4 — statement matches | proof correct
Book AT.txt:24104–24105 reproduced exactly (including "consistent with the description of SP2 (S n ) as a mapping
cone given in Example 4K.5"). **Correction of my earlier draft**: I previously claimed that the card's "the
unreduced suspension of RP⁰, hence an interval" was false and that the suspension is S¹. That was my error — I
confused RP⁰ with S⁰.
Checked, and the card is right: Hatcher defines the unreduced suspension at AT.txt:621–622 — "Suspension. For a
space X , the suspension SX is the quotient of X × I obtained by collapsing X × {0} to one point and X × {1} to
another point." With RP⁰ a single point, S(RP⁰) = [-1,1], an interval, exactly as the card says
(AT.txt:23861–23862 defines S^n RP^{n−1} as "the n fold unreduced suspension of RPn−1").
The rest of the card is also right: the chord model (S¹×[-1,1])/((θ,s)∼(θ+π,-s)) of SP₂(S¹) is the Möbius band
with the diagonal S¹ as boundary, and attaching the cone on the endpoint-identified interval to that circle gives
a CW complex with 2 vertices, 3 edges and 1 face, χ = 0 = χ(Möbius band), which is the usual mapping-cone
description of the Möbius band. No defect: statement matches, proof correct.

### E-HAT-4.K-5 — statement matches | proof a sketch in its second half
Book AT.txt:24109–24118 reproduced exactly, including (i) with its π₀ exactness clause, (ii), (iii), and
"prove Lemma 4K.3 for quasifibrations over non-pathconnected base spaces".
Proof: (i) ⇔ (ii) via the comparison of the LES of (E, p⁻¹(b)) with that of (E_p, F_b) and the five lemma with
the π₀ tail is standard and correct. (iii) ⇔ (i) by locality in path components is correct. The extension of
Lemma 4K.3 (a), (b), (c) is then asserted in three bullets ("the five-lemma proof … applies verbatim", "the
compactness argument gives …", "the same diagram chase proves …") without the arguments being written out; nothing
stated is false, but the second half of the exercise is not actually carried out.

### E-HAT-4.K-6 — statement matches | proof correct (standard details compressed)
Book AT.txt:24119–24121 reproduced exactly ("over a ∆ complex Γ , as defined in §4.G", "all the maps in X
associated to edges of Γ are weak homotopy equivalences").
Proof: p⁻¹(σ) is the iterated mapping cylinder of X_{v₀}→…→X_{v_q} (AT.txt:22686–22698), which collapses to X_{v_q},
and for b ∈ σ the fibre over b maps to X_{v_q} by a composite of edge maps, hence a weak equivalence; 4K.3(c) gives a
quasifibration over each σ; gluing over finite subcomplexes uses 4K.3(a) with collars; the directed union uses
4K.3(b) (compact images). Correct modulo the standard but unstated collar/HEP details.

---

## §4.L — Steenrod Squares and Powers (5 cards; exercises at AT.txt:25802–25820)

### E-HAT-4.L-1 — statement matches | proof correct
Book AT.txt:25803–25804 reproduced exactly, all three operation families and "for p prime".
Proof: operations H^m(–;G)→H^n(–;H) ↔ H^n(K(G,m);H) (Prop 4L.1, AT.txt:24176–24178); then H^*(S¹;Z) = Z in
degree 1 only; H^*(CP^∞;Z) = Z[x]; H^*(K(Z₂,1);Z₂) = Z₂[x] with |x| = 1; H^*(K(Z_p,1);Z_p) = Λ(x)⊗Z_p[y],
y = βx for odd p. The listed operations (a·u; a·u^j; u ↦ u^n; u ↦ (βu)^j and u ↦ u(βu)^j) and the claims about
zero operations in the other degrees are the standard answers, and the degree bookkeeping is right.

### E-HAT-4.L-2 — statement matches | proof correct
Book AT.txt:25805–25806 reproduced exactly. Proof: H̃^*(X;Z₂) ≅ H^*(S¹;Z₂)⊗H̃^*(CP^∞;Z₂) with the unique
nonzero degree-3 class u = a×x; Cartan gives Sq²(a×x) = a×Sq²x = a×x² ≠ 0 in H⁵; for Y = S³×CP^∞ the unique
nonzero degree-3 class v = pr₁^*(ι₃) has Sq²v = pr₁^*(Sq²ι₃) = 0 since H⁵(S³;Z₂) = 0. Correct.

### E-HAT-4.L-3 — **statement differs** (dropped hint) | proof correct
Book AT.txt:25807–25810 ends "[The Gysin sequence can be used to determine the map on cohomology induced by the
bundle projection HP5 →OP2 .]"; the card omits it.
Proof: H^*(HP⁵;Z₃) = Z₃[x]/(x⁶), H^*(OP²;Z₃) = Z₃[y]/(y³), |x| = 4, |y| = 8; Gysin with H³ = H⁴ = 0 on OP²
gives p^* : H⁸(OP²) ≅ H⁸(HP⁵), so p^*y = x² after rescaling; P¹y = 0 because H¹²(OP²;Z₃) = 0; on HP^∞,
x restricts to −u² on CP^∞ and P¹(−u²) = −2u⁴ = u⁴ = x² in Z₃, so by Cartan P¹(x²) = 2x³ ≠ 0; naturality then
gives 0 = p^*(P¹y) = P¹(x²), a contradiction. All degrees and coefficients check out (`P¹` raising degree by
2·1·(3−1) = 4).

### E-HAT-4.L-4 — **statement differs** (dropped hint) | proof correct
Book AT.txt:25811–25813 ends "[Compute the cohomology ring of the mapping cone of the projection S 23 →OP2 via
Poincaré duality or the Thom isomorphism.]"; the card omits it.
Proof: C_p = OP² ∪_p CS²³ is the Thom space of the D⁸-bundle and a closed 24-manifold, with
H^*(C_p;Z) = Z{1,x,x²,x³}, |x| = 8, and x³ ≠ 0 in H²⁴ (Thom isomorphism / Poincaré duality); mod 3, instability
gives P⁴x = x³ (2·4 = 8), the Adem relation P¹P³ = P⁴ holds at p = 3 (the only term is
(−1)^{1}·C(5,1)P⁴ ≡ P⁴), and H²⁰(C_p;Z₃) = 0 gives P³x = 0, so x³ = 0, contradiction. The claim that x³ is
nonzero mod 3 is legitimate because x³ generates H²⁴(C_p;Z) ≅ Z. Correct.

### E-HAT-4.L-5 — statement matches (the book's figure is not reproduced) | proof correct
Book AT.txt:25817–25820 reproduced verbatim, including "with multiplicative structure encoded in the following
diagram, where diagonal lines indicate left-multiplication by Sq1 and horizontal lines indicate
left-multiplication by Sq2". The card cannot carry the figure, but it reproduces the whole multiplication table,
so the content of the reference is supplied; that is a rendering limitation rather than a change of statement.
Proof: Adem gives a² = 0 and aba = b²; then b²a = ab² = b⁴ = 0 and abab = b³ = baba, so the eight elements
1, a, b, ab, ba, b², bab, b³ span; they are independent because they are the distinct admissible monomials
(ab = Sq³, ba = Sq²Sq¹, b² = Sq³Sq¹, bab = Sq²Sq³ = Sq⁵+Sq⁴Sq¹, b³ = Sq⁵Sq¹); the table of left multiplication
by a and b is computed correctly (e.g. a·ba = b², a·bab = b³, b·ab = bab, b·b² = b³). dim A(1) = 8. Correct.

---

# Summary of defects, most serious first

## A. Proof defects, with an explicit note of what was checked against AT.txt

For each item I say whether I checked the *hypotheses of the theorem the card cites* (which is quotable from
AT.txt), or only did my own mathematics, or could not settle it from AT.txt — the last case is marked
**unverified** and is **not** counted as a defect.

A1. **E-HAT-4.A-4 — gap: the cited theorem's hypotheses are not the card's hypothesis (checked against AT.txt).**
Card, step `s3`: "By Whitehead's Theorem, a based map f : X→X between simply connected CW complexes of dimension k
is a homotopy equivalence if and only if f_* : π_k(X)→π_k(X) is an isomorphism of abelian groups." Hatcher's
theorem, AT.txt:17284–17287: "Theorem 4.5. If a map f : X →Y between connected CW complexes induces isomorphisms
f∗ : πn (X)→πn (Y ) for all n , then f is a homotopy equivalence." The card verifies degree k only, so the named
theorem's hypothesis ("for all n") is not satisfied and is nowhere checked: that is the defect. I do **not** claim
the card's conclusion is false, and I have no verified counterexample to its general formulation. The conclusion
for X = ⋁_n S^k is true and the card already has the right argument in step `s2`: [X,X]_* ≅ M_n(Z) is an
isomorphism of monoids under composition, so an invertible matrix gives an explicit two-sided homotopy inverse
(equivalently Hilton's theorem supplies the higher homotopy groups of a wedge of spheres from π_k).

A2. **E-HAT-4.A-5 — unverified, not a defect.** Statement matches (AT.txt:21114–21129). The solution's whole
framework is the identification of the book's X̃_n with the infinite cyclic cover of X_n = (S¹∨S¹)ⁿ (total exponent
sum), and of the deck transformation's action on the presentation ("τ₂ fixes a, b and sends c ↦ aca⁻¹"). The
passage of the book that defines these objects is badly garbled in the extraction (AT.txt:20950–20970), the exercise
itself states only the mapping-torus structure (AT.txt:21118–21123), and my own attempt to derive the automorphism
was inconclusive. **Marked unverified** — I am not calling it wrong and I am not endorsing it. What I did check: the
card is internally consistent (χ(Z) = 1−12+16 = 5 and rank H₁ = 5 give rank H₂ = 9; the final five-generator
presentation has abelianisation Z⁵ because every relator displayed is a commutator or a conjugacy; and
σ(a)=a, σ(b)=b, σ(c)=aca⁻¹ does preserve the relators of the presentation of H₂ obtained from (1)). The cell counts
12 and 16 in part (a) are asserted, not derived from the octahedral model.

A3. **E-HAT-4.B-2 — two gaps.** (i) For n = 1 the card writes "the same dimension relation and the homotopy
sequence force k = 0"; they do not: with n = 1, k = 1 the segment is π₁(S¹) = Z → π₀(S¹) = 0 → π₀(Sᵐ) → 0, which is
consistent. (This is my own computation. The conclusion k = 0, m = 1 is the book's and is true; the missing
argument is that m > 1 makes Sᵐ simply connected, so a bundle over S¹ is trivial and Sᵐ ≅ S¹×S^k is impossible.)
(ii) "Since Cp is a closed orientable 2n-manifold, Poincaré duality says …" — orientability is asserted, never
proved. Hatcher's hint (AT.txt:21223) asks only that C_p be a manifold, and his duality theorem is
AT.txt:12003–12005: "Theorem 3.30 (Poincaré Duality). If M is a closed R orientable n manifold with fundamental
class [M] ∈ Hn (M; R) , then …". So "Poincaré duality therefore forces H(p) = ±1" is justified only after
orientability of C_p is established; the card does not do it, and with Z/2 coefficients one only gets H(p) odd.

A4. **E-HAT-4.G-2 — proves a weaker statement (checked against the book's definition).** Hatcher's complexes of
spaces have a ∆-complex base with an iterated mapping cylinder over every simplex, AT.txt:22683–22698: "There is a
natural generalization of ∆X in which one starts with a ∆ complex Γ and a diagram of spaces associated to the 1
skeleton of Γ … for each n simplex of Γ we have a sequence of maps X0 →X1 → ··· →Xn , and we define the iterated
mapping cylinder … All these iterated mapping cylinders over the various simplices of Γ thus fit together to form a
space ∆X with a canonical projection ∆X →Γ ." The card builds only "a vertex space for each v ∈ Γ, an edge space for
each e ∈ Γ", i.e. it proves the statement for 1-dimensional Γ only; it also assumes "Γ is connected", which the
exercise does not.

A5. **E-HAT-4.G-4 — gap.** The subcomplex version of Proposition 4G.2 is asserted, not proved: "the homotopy gluing
lemma therefore proves by cellular induction that p is a homotopy equivalence" — no induction is carried out and no
gluing lemma is stated with its hypotheses verified. (The second half, via 4G.1 and the barycentric subdivision of
the nerve, matches the book's proof of Corollary 4G.3 at AT.txt:22794–22797.)

A6. **E-HAT-4.G-1 — gap.** "Since the finite-stage homotopies are compatible, they assemble on the union … to a
continuous homotopy": a compatible family on a nested union need not be continuous, and no local finiteness,
closedness or time-rescaling argument is given. (Hatcher's own infinite concatenations avoid exactly this, e.g.
AT.txt:22744–22745.)

A7. **E-HAT-4.B-1 — covers only n ≥ 2.** The pullback argument needs a chosen generator of H^{2n}(C_f) ≅ Z, so n = 1
is not covered; there the book's H vanishes identically (AT.txt:21161, "H(f ) is always zero for odd n") and the
identity is trivially true. Small gap.

A8. **E-HAT-4.I-3 — k = 0 not covered.** "Both sides of (3) are simply connected" fails for k = 0, where the
1-skeleton of a suspension is a graph; so the Whitehead step covers k ≥ 1 only.

A9. **E-HAT-4.K-5 — second half asserted.** The extension of Lemma 4K.3 to non-pathconnected bases is given in three
bullets that assert the arguments ("applies verbatim", "the compactness argument gives …", "the same diagram chase
proves …") rather than carrying them out. Nothing stated is false.

A10. **E-HAT-4.H-4 — definition incomplete.** No projection ∇X → Γ is given, although ΔX comes with a projection
(AT.txt:22698–22699) whose dual is the point of the exercise; and "each condition is a closed condition" needs the
vertex spaces to be Hausdorff, which Hatcher does not assume.

A11. **E-HAT-4.D-5 — mis-displayed Gysin segment.** The card prints
`H^k(S^m) → H^0(S^n) --∪e--> H^{k+1}(S^n) --p^*--> H^{k+1}(S^m)`. The middle and last maps are right (the Gysin
segment with q = k+1 is H^0(B) --∪e--> H^{k+1}(B) --p^*--> H^{k+1}(E) → H^1(B) = 0), but "H^k(S^m)" is not a term
of the sequence there: the term to its left is H^{q−k−1}(B) = H^{-k-1}(S^n) (equivalently H^{-k}(S^n) for the
neighbouring step), which is 0. The conclusion "the outer groups vanish" is therefore right and nothing downstream
depends on the slip.

A12. **E-HAT-4.A-3 — incomplete citation.** "Proposition 4A.2" (AT.txt:20891–20893) gives only ⟨Z,X⟩/π₁(X) ≅ [Z,X];
the identification [K,K] ≅ Hom(π,π)/Inn(π) also needs the classification theorem for maps into K(G,1). The
mathematics is right.

A13. **E-HAT-4.F-1 — one step recalled, not proved.** "Recall first that these two axioms already imply the wedge
axiom for finite wedge sums."

Explicitly **not** a defect, because I checked it and it is right: the "unreduced suspension of RP⁰ is an interval"
claim in **E-HAT-4.K-4** (see that card's entry; an earlier draft of this file wrongly reported it).

## B. Statements that differ from the printed exercise

Every one of these is a dropped bracketed hint, pointer or parenthetical. Quoted from `tmp/hat/AT.txt`
(line numbers give the position of the dropped text; the extraction puts displayed wedge/limit symbols on their
own lines, which I have flattened):

| card | dropped from the card | AT.txt lines |
|---|---|---|
| E-HAT-4.A-2 | "In particular, if π is abelian then [X, K(π,1)] = ⟨X, K(π,1)⟩ = Hom(π₁(X), π)." | 21099–21101 |
| E-HAT-4.A-4 | "[GL_n(Z) is the automorphism group of Zⁿ ≈ π_k(⋁_n S^k) ≈ H_k(⋁_n S^k).]" | 21112–21113 |
| E-HAT-4.B-2 | "[Show that C_p is a manifold and apply Poincaré duality.]" | 21223 |
| E-HAT-4.D-5 | "[Hence n = 1, 2, 4, 8 by Adams' theorem.]" | 22164 |
| E-HAT-4.D-6 | "[When n > 1 there are examples where M is not homeomorphic to CPⁿ.]" | 22168–22169 |
| E-HAT-4.D-9 | "[Hint: Diagonal matrices in U(n) are compositions of scalar multiplication in n lines in Cⁿ, and CP^{n−1} is connected.]" | 22181–22182 |
| E-HAT-4.D-10 | "(The usual argument over C involving roots of the characteristic polynomial does not work due to the lack of a good quaternionic determinant function.)" | 22184–22186 |
| E-HAT-4.F-2 | "[Use induction on the number of cells of X and the five-lemma.]" | 22610–22611 |
| E-HAT-4.G-3 | "[See Lemma 2C.2.]" | 22821 |
| E-HAT-4.G-4 | "[CW complexes are paracompact; see [VBKT].]" | 22823 |
| E-HAT-4.H-1 | "[If A ↪ X is a cofibration, so is A×Y ↪ X×Y for any space Y.]" | 23112–23113 |
| E-HAT-4.H-3 | "[This is dual to Proposition 0.19.]" | 23118–23119 |
| E-HAT-4.I-1 | "[One approach: Show the map Σr + Σq : ΣX → ΣA ∨ Σ(X/A) induces an isomorphism on homology, where r : X → A is the retraction and q : X → X/A is the quotient map.]" | 23274–23276 |
| E-HAT-4.I-2 | "Thus to determine stable splittings of K(Z_n,1) it suffices to do the case that n is a prime power, as in Proposition 4I.3." | 23281–23282 |
| E-HAT-4.I-3 | "as described in the remarks following the proof" | 23287–23288 |
| E-HAT-4.K-2 | "[Consider the cover of L by open stars of simplices and the cover of K by the preimages of these open stars.]" | 24099–24100 |
| E-HAT-4.L-3 | "[The Gysin sequence can be used to determine the map on cohomology induced by the bundle projection HP⁵ → OP².]" | 25809–25810 |
| E-HAT-4.L-4 | "[Compute the cohomology ring of the mapping cone of the projection S²³ → OP² via Poincaré duality or the Thom isomorphism.]" | 25811–25813 |

That is 18 of the 42 cards. Sixteen lose only a bracketed hint or pointer; two also lose a mathematical assertion
(4.A-2's "In particular, if π is abelian …", 4.I-2's "Thus … prime power"), and 4.I-3 loses the clause that fixes
which cell structure is meant.

Cards whose statements match the book exactly: 4.A-1, 4.A-3, 4.A-5, 4.B-1, 4.D-1, 4.D-2, 4.D-3, 4.D-4, 4.D-7,
4.D-8, 4.F-1, 4.F-3 (modulo writing hocolim for the direct limit, which the book itself identifies with the
telescope at AT.txt:22612–22615), 4.G-1, 4.G-2, 4.H-2 (modulo ∪_f for ⊔_f), 4.H-4, 4.K-1, 4.K-3, 4.K-4,
4.L-1, 4.L-2, 4.L-5 (modulo the un-reproducible figure, whose content the solution supplies).

## C. Audit-trail problem worth reporting to the human

Of the 18 cards whose statement differs from the printed exercise, **11 carry a pre-existing event**
`source-checked … note: "Checked against Hatcher, Algebraic Topology, Section 4.X, Exercise n[, and its hint]; the
stored statement matches."` with a `solution-reviewed` by an auditor other than `claude` (gpt-5.6-sol in every
case). Those 11 are: 4.B-2 (whose note explicitly claims "and its hint"), 4.D-9, 4.D-10, 4.F-2, 4.G-3, 4.H-1,
4.H-3, 4.I-1, 4.I-3, 4.L-3, 4.L-4. So those "statement matches" notes are false as written and cannot be relied on
for statement completeness.

The other 7 differing cards carry no `source-checked` event at all and were never statement-audited: 4.A-2, 4.A-4,
4.D-5, 4.D-6, 4.G-4, 4.I-2, 4.K-2. (Counting check, from the frontmatter of all 42 cards: 30 carry `source-checked`
and 30 carry a `solution-reviewed`, all of the latter by gpt-5.6-sol, none by `claude`; in this slice no card has
been reviewed by `claude`.)
