# Audit: SRC-TEXT-HAT02 / §2.B (Classical Applications) — all 11 cards

Auditor: m5. Section not claimed by any other direction (d1–d7 take 3.D, 4.3, 3.F, 3.H+4.1#10–23,
4.2, 4.A–4.L, and a book-side index). Card count: **11** cards (`2-b/E-HAT-2.B-1 … -11`),
matching the **11** printed exercises of §2.B.

Book witness: `tmp/hat/AT.txt` (line numbers below are lines of that file; quotes are verbatim,
including the extraction's spacing, superscripts rendered as spaces and lost overlines/dots).

## Extraction hazard worth knowing

The printed exercises of §2.B are **not contiguous** in `AT.txt`: exercises 1–6 are at 8816–8842 and
exercises 7–11 at 8846–8860, with the *running head of the next section* interleaved between them:

```
 8843|\f                            Simplicial Approximation                Section 2.C      177
```

(the 8843 line begins with a form feed, shown here as `\f`; the other quoted lines below are exact,
including the extraction's leading blanks)

So §2.B has 11 exercises, not 6; the 11 cards are correctly enumerated. No card is misfiled.

## Per-card verdicts

### E-HAT-2.B-1 — "Homology of complements of wedges and disjoint unions in spheres"
**Statement: matches.**
Book 8816–8817:
```
 8816|1. Compute Hi (S n − X) when X is a subspace of S n homeomorphic to S k ∨ S ℓ or to
 8817|Sk ∐ Sℓ .
```
Card: "Compute $H_i(S^n - X)$ when $X$ is a subspace of $S^n$ homeomorphic to $S^k \vee S^\ell$ or to $S^k \amalg S^\ell$." Word-for-word identical (∨→`\vee`, ∐→`\amalg`).

**Proof: has a gap (edge cases; answer wrong for k = 0 or ℓ = 0).**
* The proof opens "We use Alexander duality in the form … for these compact locally contractible subspaces of $S^n$". The cited result is Corollary 3.45, whose hypotheses are stronger — 12699–12702:
```
 12699| Corollary 3.45. If K is a compact, locally contractible, nonempty, proper subspace
 12700| of S n , then H
 12701|               e i (S n − K; Z) ≈ H
 12702|                                  e n−i−1 (K; Z) for all i .
```
  *proper* is not checked: for k = n (resp. ℓ = n) the subspace is all of S^n and duality does not apply. The printed exercise does not exclude k = n or ℓ = n.
* The case tables are wrong at the bottom dimension. If k = 0 then S^0 ∨ S^ℓ ≅ S^ℓ, so H̃^0(S^0∨S^ℓ) = 0, but the card's step [](#s1) table gives H̃^0 = ℤ (the row "j = k ≠ ℓ"). If k = 0 then S^0 ∐ S^ℓ has **three** path components, so H̃^0 = ℤ², but the card's third step states "$\widetilde H^0(X)\cong\ZZ$". The exercise admits k = 0, ℓ = 0.
* The exercise asks for `H_i`, the card displays only `H̃_i`; `H_0` is dispatched in one closing sentence ("The unreduced group $H_0$ is obtained, as usual, by adjoining one copy of $\ZZ$"), with no explicit answer.
* For k, ℓ ≥ 1 and k, ℓ < n the mathematics is right: the two degree shifts (n−k−1, n−ℓ−1) and the merge to ℤ² when k = ℓ are correct.

### E-HAT-2.B-2 — "Homology of complements of finite graphs in spheres"
**Statement: matches**, including the bracketed hint. Book 8818–8820 (the `H̃` is split by the extraction):
```
 8818|             e i (S n − X) ≈ H
 8819|2. Show that H               e n−i−1 (X) when X is homeomorphic to a finite connected
 8820|graph. [First do the case that the graph is a tree.]
```
Card: "Show that $\tilde{H}_i(S^n - X) \approx \tilde{H}_{n-i-1}(X)$ when $X$ is homeomorphic to a finite connected graph. [First do the case that the graph is a tree.]"

**Proof: correct in substance; one unchecked hypothesis.**
* Universal coefficients: `H_j(X)` free for a finite connected graph (H_0 = ℤ, H_1 free, higher 0), so Ext vanishes and H̃^j ≅ H̃_j — correct.
* Tree case: contractible ⇒ all reduced cohomology 0 ⇒ complement has vanishing reduced homology — correct.
* Final "In particular": rank H_1(X) = r ⇒ H̃_{n−2}(S^n−X) ≅ ℤ^r and nothing else — correct.
* Gap: the very same Corollary 3.45 (12699–12702) needs *proper*, and the card never excludes X = S^n. This really occurs: for n = 1, a finite connected graph in S^1 is an arc (proper) or the whole circle S^1 (not proper). The formula is still true there, but not for the reason given.

### E-HAT-2.B-3 — "Complement of a disk pair in a sphere pair"
**Statement: matches**, hint included. Book 8822–8826:
```
 8822|3. Let (D, S) ⊂ (D n , S n−1 ) be a pair of subspaces homeomorphic to (D k , S k−1 ) , with
 8823|D ∩ S n−1 = S . Show the inclusion S n−1 − S ֓ D n − D induces an isomorphism on
 8824|homology. [Glue two copies of (D n , D) to the two ends of (S n−1 × I, S × I) to produce
 8825|a k sphere in S n and look at a Mayer–Vietoris sequence for the complement of this
 8826|k sphere.]
```
Card identical, including `[Glue two copies of $(D^n, D)$ …]`, the inclusion as `\hookrightarrow`, and "Mayer–Vietoris".

**Proof: correct.** Checked line by line:
* k = 0 case: D is an interior point and radial projection retracts D^n∖D onto S^{n−1} — correct, and the inclusion S^{n−1} → D^n∖D is then a homotopy equivalence.
* 0 < k < n: A = S^{n−1}∖S, B = D^n∖D; Mayer–Vietoris over W = S^n − S^k with intersection ≃ A gives (i_*,−i_*). Alexander duality in both ambient spheres gives H̃_j(A) = H̃_j(W) = ℤ for j = d = n−k−1 and 0 otherwise (Corollary 3.45 applies here: both spheres are nonempty and proper, k < n and k−1 < n−1).
* Exactness then gives 0 → ℤ → H̃_d(B)² → ℤ → 0; the middle group is free of rank 2 (the sequence splits), so H̃_d(B) = ℤ; if i_* = ·m then coker(m,−m) = ℤ ⊕ ℤ_m must be ℤ, so m = 1. Correct — the Smith-normal-form step is valid.
* k = n: A = ∅, and the argument that int D is open and closed in int D^n (compactness of D, ∂D = S = ∂D^n) forces D = D^n, hence B = ∅. Correct.

### E-HAT-2.B-4 — "Linking numbers via Mayer–Vietoris"
**Statement: matches**, hint included. Book 8828–8833:
```
 8828|4. In the unit sphere S p+q−1 ⊂ Rp+q let S p−1 and S q−1 be the subspheres consisting
 8829|of points whose last q and first p coordinates are zero, respectively.
 8830|(a) Show that S p+q−1 − S p−1 deformation retracts onto S q−1 , and is in fact homeo-
 8831|morphic to S q−1 × Rp .
 8832|(b) Show that S p−1 and S q−1 are not the boundaries of any pair of disjointly embedded
 8833|disks D p and D q in D p+q . [The preceding exercise may be useful.]
```
**Proof: correct.** Φ(x,y) = (y/|y|, x/|y|) with inverse (u,v) ↦ (v,u)/√(1+|v|²) is a homeomorphism S^{p+q−1}−S^{p−1} ≅ S^{q−1}×ℝ^p (checked on both composites); retracting the ℝ^p factor gives (a). For (b) the class of S^{q−1} generates H̃_{q−1} of the complement (it is a deformation retract), Exercise 3 applies to (D^p,S^{p−1}) ⊂ (D^{p+q},S^{p+q−1}) and gives injectivity of the inclusion, while the disjoint disk D^q exhibits the same class as a boundary. Contradiction. The use of Exercise 3 is exactly the book's hint ("The preceding exercise may be useful", 8833).

### E-HAT-2.B-5 — "Homology of complements of spheres in spheres"
**Statement: matches.** Book 8835–8839:
```
 8835|5. Let S be an embedded k sphere in S n for which there exists a disk D n ⊂ S n
 8836|intersecting S in the disk D k ⊂ D n defined by the first k coordinates of D n . Let
 8837|D n−k ⊂ D n be the disk defined by the last n − k coordinates, with boundary sphere
 8838|S n−k−1 . Show that the inclusion S n−k−1 ֓ S n − S induces an isomorphism on homol-
 8839|ogy groups.
```
**Proof: correct conclusion, one unjustified step.**
* Alexander duality gives H̃_i(S^n∖S) = ℤ for i = r = n−k−1 and 0 otherwise; so the claim reduces to "the fundamental class of S^r maps to a generator", which the card settles by showing the image has duality coordinate ±1.
* The justification is: "Under Alexander duality, evaluation of the image of its oriented fundamental class on the fundamental class of $S$ is the intersection number of this normal disk with $S$." That identification (duality pairing = intersection number of a dual disk) is a genuine lemma; it is not stated, proved, or cited here, and it is not Hatcher's Corollary 3.45 (12699–12702), which says nothing about evaluating on the class of $S$. Everything else (transversality of the two coordinate disks, single intersection point, excision to the coordinate disk) is fine, so this is a rigour gap, not an error.
* Hypotheses of the duality again unchecked: if k = n then S = S^n is not proper and S^n − S = ∅.

### E-HAT-2.B-6 — "Alexander horned sphere with non-simply-connected complement"
**Statement: matches.** Book 8841–8842:
```
 8841|6. Modify the construction of the Alexander horned sphere to produce an embedding
 8842|S 2 ֓ R3 for which neither component of R3 − S 2 is simply-connected.
```
**Proof: correct in outline; two assertions not verified.**
* The gluing count is right: S = (S_0 − int D_+ − int D_-) ∪ D'_+ ∪ D'_- is a sphere-with-two-holes closed up by two disks, hence S^2.
* Nontriviality of the local exterior group is imported from Hatcher's Example 2B.2 (8569–8599, "In particular we see explicitly why π_1(R^3 − B) has trivial abelianization", 8598–8599); the card asserts the localised disk "contains exactly the localized complement used in Hatcher's Alexander-horned-sphere argument" without an argument.
* Van Kampen: the interface N_+ ∩ (rest) is ∂N_+ minus the open disk D_+, which is a disk, so it is simply connected and π_1 of the union is the free product — the card's claim is sound, but it never checks that the complementary piece V is simply connected, which the free-product conclusion also needs.
* Both components: the card uses N_+ for the unbounded and the mirror N_- for the bounded component; a properly embedded wild disk separates its 3-ball into two sides, which is what makes the two-sided use legitimate — stated implicitly.

### E-HAT-2.B-7 — "Modified Alexander horned sphere"
**Statement: matches.** Book 8846–8848:
```
 8846|7. Analyze what happens when the number of handles in the basic
 8847|building block for the Alexander horned sphere is doubled, as in
 8848|the figure at the right.
```
**Proof: internally consistent, but its premise cannot be checked against the witness.**
* The exercise is defined by a figure ("as in the figure at the right"), and `AT.txt` contains no figure — only the reference to it. The card reads "doubled" as "each old handle is replaced by four smaller handles, arranged as two linked pairs". Nothing in `AT.txt` confirms or refutes that reading, so the card's numbers (4^n handles, π_1(Y_n) ≅ F_{4^n}) are a consequence of an unverifiable interpretation. This should be flagged, not counted as verified.
* Given that reading, the mathematics is right: the bonding map sends the old meridian to the boundary word [a_1,a_2][a_3,a_4] of a genus-2 surface with one boundary component; a homomorphism ℤ → F_4 with nontrivial image is injective; a free product of injections is injective, so the direct limit is nontrivial; abelianisation kills every generator, so the limit H_1 is 0, consistent with Hatcher's computation for the standard construction (8598–8599).
* Weak point: "Higher reduced homology vanishes just as in the original handle-complement stages" is asserted, not computed; the appeal to Proposition 2B.1 (8451–8455) at the end gives the right answer for the exterior of the boundary sphere but does not by itself justify the *stage* groups.

### E-HAT-2.B-8 — "Real division algebras and the Borsuk–Ulam theorem"
**Statement: matches.** Book 8849–8852:
```
 8849|8. Show that R2n+1 is not a division algebra over R if n > 0 by
 8850|considering how the determinant of the linear map x ֏ ax given
 8851|by the multiplication in a division algebra structure would vary as
 8852|a moves along a path in R2n+1 − {0} joining two antipodal points.
```
**Proof: correct.** L_a is injective for a ≠ 0 (division algebra: ax = b solvable ⇒ surjective ⇒ iso), det L_{-a} = (−1)^{2n+1} det L_a = −det L_a, t ↦ det L_{γ(t)} is continuous and never 0 on the connected interval [0,1] hence has constant sign — contradiction. The path exists because 2n+1 ≥ 3. Exactly the book's suggestion.

### E-HAT-2.B-9 — "Transfer sequence for trivial coverings"
**Statement: matches** (the `X̃` is split over three lines by the extraction). Book 8853–8856:
```
 8853|                                                                         e →X , where
 8854|9. Make the transfer sequence explicit in the case of a trivial covering X
 8855|e = X × S0 .
 8856|X
```
**Proof: correct.** With ℤ₂ coefficients C_*(X×S^0) = C_*(X)⊕C_*(X), τ(c) = (c,c), p_#(a,b) = a+b; over ℤ₂ the kernel of the sum is the diagonal, so 0 → C_* → C_*² → C_* → 0 is short exact; c ↦ (c,0) splits it, so all connecting maps vanish and the transfer sequence is 0 → H_n(X) → H_n(X)² → H_n(X) → 0 in every degree — the right "explicit" answer. (Note: this is the ℤ₂ transfer of §2.B; Hatcher introduces the general transfer only in §3.G, 8750–8755, which the card respects.)

### E-HAT-2.B-10 — "Homology of RP^∞ via transfer"
**Statement: matches.** Book 8857:
```
 8857|10. Use the transfer sequence for the covering S ∞ →RP∞ to compute Hn (RP∞ ; Z2 ) .
```
**Proof: correct.** S^∞ contractible; for n ≥ 2 the segment is 0 → H_n(RP^∞) → H_{n−1}(RP^∞) → 0; for n = 1, p_* is an isomorphism on H_0 (both connected) so τ_* = 0 and δ is an isomorphism; induction gives H_n(RP^∞;ℤ₂) = ℤ₂ for all n. The sequence used is exactly Hatcher's transfer sequence for a two-sheeted cover (8716–8749).

### E-HAT-2.B-11 — "Homology of X × RP^∞ via transfer"
**Statement: matches.** Book 8858–8860:
```
 8858|11. Use the transfer sequence for the covering X × S ∞ →X × RP∞ to produce isomor-
 8859|                           L
 8860|phisms Hn (X × RP∞ ; Z2 ) ≈ i≤n Hi (X; Z2 ) for all n .
```
**Proof: correct.** H_n(X×S^∞) ≅ H_n(X); p_* is split injective (q: X×RP^∞ → X satisfies q∘j = id for j(x) = (x,b_0), and p_* = j_* under the collapse of S^∞); τ_* = 0 because r_#τ(σ) = 2q_#(σ) = 0 over ℤ₂ and r_* is an isomorphism. Hence 0 → H_n(X) → H_n(B) → H_{n−1}(B) → 0 splits for every n, giving H_n(B) ≅ H_n(X) ⊕ H_{n−1}(B) and, with H_0(B) ≅ H_0(X), the stated sum.

## Defects found, most serious first

1. **E-HAT-2.B-1 — wrong values when k = 0 or ℓ = 0** (the printed exercise allows them). S^0∨S^ℓ ≅ S^ℓ so H̃^0 = 0, not ℤ; S^0∐S^ℓ has three components so H̃^0 = ℤ², not ℤ. Also the answer is only given for reduced homology, `H_0` being relegated to one sentence.
2. **E-HAT-2.B-1, 2.B-2, 2.B-5 — Alexander duality cited with its hypotheses unchecked.** Corollary 3.45 (12699–12702) requires K compact, locally contractible, **nonempty and proper**; all three cards invoke it without excluding K = S^n (k = n, resp. ℓ = n; for 2.B-2, n = 1 with X ≅ S^1).
3. **E-HAT-2.B-5 — unjustified duality/intersection step.** "Under Alexander duality, evaluation of the image of its oriented fundamental class on the fundamental class of S is the intersection number of this normal disk with S" is a lemma neither proved nor cited; the conclusion is right but the proof does not establish it as written.
4. **E-HAT-2.B-7 — unverifiable premise.** The card's "four handles per old handle ⇒ F_{4^n}, bonding word [a_1,a_2][a_3,a_4]" rests on a reading of a figure that `AT.txt` does not contain; the exercise cannot be settled from the witness, and the higher-homology claim is asserted rather than computed.
5. **E-HAT-2.B-6 — two assertions not checked**: that the localised horned disk inherits π_1 of Hatcher's Example 2B.2, and that the complementary piece in the van Kampen decomposition is simply connected (needed for the free-product factor).
6. **E-HAT-2.B-5 and 2.B-9 carry no `solution-reviewed` audit event** (2.B-5: only `solution-written` by muse-spark-1.2; 2.B-9: only `solution-written` by gemini-3.7-flash). No §2.B card carries a `solution-reviewed` event by `claude`.

Cards whose proofs I read in full and judge correct with no defect beyond the above: **2.B-3, 2.B-4, 2.B-8, 2.B-10, 2.B-11**. Their statements also match the printed text word for word, hints included (2.B-3, 2.B-4).

## Mechanical statement check

Besides the manual reading, each of the 11 cards was compared to its printed exercise by a
word-sequence diff after stripping LaTeX and the extraction's hyphenation (`wordcheck.py` in this
directory). Residual words on the card side and on the book side were, for every card, empty except
for the extraction's line-break hyphenations ("homeo/morphic" 8830–8831, "homol/ogy" 8838–8839,
"isomor/phisms" 8858–8860) and one "where" that the extraction splits around the tilde in
`X̃ → X` (8853–8855). **No adjective, hypothesis, quantifier or hint word of the printed exercise is
missing from any card, and no card adds one.**
