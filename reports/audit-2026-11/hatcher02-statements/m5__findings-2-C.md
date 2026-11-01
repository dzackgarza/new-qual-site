# Audit: SRC-TEXT-HAT02 / §2.C (Simplicial Approximation) — all 9 cards

Auditor: m5. Section not claimed by any other direction (d1–d7 hold 3.D, 4.3, 3.F, 3.H+4.1#10–23,
4.2, 4.A–4.L, and a book-side index). Card count: **9** cards (`2-c/E-HAT-2.C-1 … -9`), matching
the **9** printed exercises of §2.C at `tmp/hat/AT.txt` 9193–9214 (the block starts at 9192
`Exercises` and ends before Chapter 3 opens at 9215).

Book witness: `tmp/hat/AT.txt`; line numbers are lines of that file, quotes verbatim.

## Per-card verdicts

### E-HAT-2.C-1 — minimum number of edges for a simplicial map S^1 → S^1 of degree n
**Statement: matches.** Book 9193–9194:
```
 9193|1. What is the minimum number of edges in simplicial complex structures K and L
 9194|on S 1 such that there is a simplicial map K →L of degree n ?
```
Card: "What is the minimum number of edges in simplicial complex structures $K$ and $L$ on $S^1$ such that there is a simplicial map $K \to L$ of degree $n$?"

**Proof: correct.** A simplicial circle needs ≥ 3 vertices (no loops, no repeated edge) hence ≥ 3 edges; for n ≠ 0, f_*(z_K) = n·z_L forces every edge of L to be covered with total signed coefficient n, so at least |n| edges of K map onto each of the e(L) edges, i.e. e(K) ≥ |n|e(L); the bound is attained by a 3|n|-gon wrapping n times around a triangle; n = 0 is a constant map between triangles. The boxed answer e(L) = 3, e(K) = 3·max{1,|n|} minimises e(K)+e(L) as well, since e(L) ≥ 3 and e(K) ≥ |n|e(L). One observation, not a defect: the exercise's "minimum number of edges in K and L" is answered by a pair, and the card's boxed answer reads as a pair.

### E-HAT-2.C-2 — Lefschetz fixed point theorem on S^n
**Statement: matches.** Book 9195–9196:
```
 9195|2. Use the Lefschetz fixed point theorem to show that a map S n →S n has a fixed
 9196|point unless its degree is equal to the degree of the antipodal map x ֏ −x .
```
Card: "Use the Lefschetz fixed point theorem to show that a map $f: S^n \to S^n$ has a fixed point unless its degree is equal to the degree of the antipodal map $x \mapsto -x$."

**Proof: mathematically correct.** deg(antipodal) = (−1)^{n+1} (composition of n+1 reflections); for n ≥ 1, τ(f) = 1 + (−1)^n d ∈ ℚ-homology, so τ(f) = 0 ⇔ d = (−1)^{n+1} = deg(a); Theorem 2C.3 (8968–8970) then gives a fixed point whenever deg f ≠ deg a. The n = 0 case is handled separately and correctly (the only fixed-point-free self-map of S^0 is the swap, which is the antipodal map, degree −1 = (−1)^{0+1}).

**Structural defect (markup, not mathematics).** This is the only card in the collection whose proof divs are nested the wrong way round: `{.pf-step}` blocks are nested *inside* `pf-proof` blocks, five deep in places. Traced from the file:

```
24: {.solution}
 27: pf
   29: {.pf-step #s1}
     32: pf-proof
       34: pf-step     38: pf-step     42: pf-step
   51: {.pf-step #lefschetz-number}
     54: pf-proof
       56: 61: 65: 69: 73: pf-step
   82: pf-step
     85: pf-proof
       89: 93: 97: 102: 106: 110: pf-step
```
i.e. `pf-proof` contains sub-`pf-step`s and the `pf-step`/`pf-proof` pairing is inverted relative to every other card. Also, frontmatter says `kind: problem` while the statement sits in a `::: {.exercise}` block (2.C-2 is the only card in §2.B/§2.C with that mismatch). And it carries **no `solution-reviewed` audit event** (only `solution-written`, by Codex 5.3 Spark Extra High).

### E-HAT-2.C-3 — conjugate-linear map on C^{2k} giving a fixed-point-free map of CP^{2k−1}
**Statement: matches the book's formula up to an extraction artefact.** Book 9197–9198:
```
 9197|3. Verify that the formula f (z1 , ··· , z2k ) = (z2 , −z1 , z4 , −z 3 , ··· , z 2k , −z2k−1 ) defines
 9198|a map f : C2k →C2k inducing a quotient map CP2k−1 →CP2k−1 without fixed points.
```
`AT.txt` drops all overlines, so the printed formula's conjugates are invisible here. That the conjugates are printed is settled elsewhere in the book, 9000–9004:
```
 9000|polynomial always has a complex root. Nevertheless, as in the real case there is a
 9001|map CP2k−1 →CP2k−1 without fixed points. Namely, consider f : C2k →C2k defined
 9002|by f (z1 , ··· , z2k ) = (z2 , −z 1 , z 4 , −z 3 , ··· , z2k , −z2k−1 ) . This map is only ‘conjugate-
 9003|linear’ over C , but this is still good enough to imply that f induces a well-defined
 9004|map f on CP2k−1 , and it is easy to check that f has no fixed points. The similarity
```
The card writes $(\bar z_2, -\bar z_1, \bar z_4, -\bar z_3, \cdots, \bar z_{2k}, -\bar z_{2k-1})$, which is the correct reading (without conjugation the map is ℂ-linear and does have fixed points: (z, iz, z, iz, …) is an eigenvector with eigenvalue i). **So the card is right and the extraction is wrong; no defect in the card.**

**Proof: correct.** F is conjugate-linear with F² = −id; F(λz) = λ̄F(z) and F(z) ≠ 0 for z ≠ 0, so F descends to CP^{2k−1}; a fixed line F(z) = λz would give −z = F²(z) = |λ|²z, impossible.

### E-HAT-2.C-4 — Lefschetz number of a simplicial homeomorphism = Euler characteristic of the fixed set
**Statement: matches**, hint included. Book 9199–9202:
```
 9199|4. If X is a finite simplicial complex and f : X →X is a simplicial homeomorphism,
 9200|show that the Lefschetz number τ(f ) equals the Euler characteristic of the set of fixed
 9201|points of f . In particular, τ(f ) is the number of fixed points if the fixed points are
 9202|isolated. [Hint: Barycentrically subdivide X to make the fixed point set a subcomplex.]
```
**Proof: correct.** (i) After one barycentric subdivision a simplex carried to itself by f is fixed pointwise (f preserves the dimensions of the members of a nested chain σ_0 ⊊ … ⊊ σ_r, hence each vertex), and a fixed point lies in the interior of a unique invariant simplex, so Fix(f) is a subcomplex. (ii) On oriented simplicial n-chains over ℚ, f permutes the simplices, an invariant simplex contributes +1 (f|σ = id preserves orientation), so tr = c_n(F). (iii) Hopf trace formula via 0 → Z_n → C_n → B_{n−1} → 0 and 0 → B_n → Z_n → H_n → 0. (iv) τ(f) = Σ(−1)^n c_n(F) = χ(F); isolated fixed points ⇒ F is 0-dimensional ⇒ τ(f) = #F. This matches Hatcher's own device in the proof of 2C.3 (9056–9058).

### E-HAT-2.C-5 — can the reflection of a surface be homotoped to be fixed-point free?
**Statement: matches.** Book 9203–9205:
```
 9203|5. Let M be a closed orientable surface embedded in R3 in such a way that reflection
 9204|across a plane P defines a homeomorphism r : M →M fixing M ∩ P , a collection of
 9205|circles. Is it possible to homotope r to have no fixed points?
```
**Proof: correct (answer: yes).** On an r-invariant annular neighbourhood (θ,t) of each fixed circle r(θ,t) = (θ,−t); an isotopy h_s(θ,t) = (θ + sδρ(t), t) supported in the annuli gives g = h∘r with g(θ,t) = (θ + δρ(−t), −t); a fixed point forces t = 0 and then δ ≡ 0 mod 2π. Outside the annuli h = id and r is fixed-point-free. Consistent with the Lefschetz computation, τ(r) = χ(circles) = 0. The construction needs each fixed circle to have a product neighbourhood, which holds because M ∩ P is a 1-manifold embedded in the surface.

### E-HAT-2.C-6 — even-genus analog of Example 2C.4
**Statement: matches.** Book 9206–9207:
```
 9206|6. Do an even-genus analog of Example 2C.4 by replacing the central torus by a sphere
 9207|letting f be a homeomorphism that restricts to the antipodal map on this sphere.
```
The reference is to Example 2C.4, 9062–9067 ("Let X be the closed orientable surface of genus 3 … with f : X →X the 180 degree rotation", "Since f has no fixed points, we should have τ(f ) = 0"), whose closing sentence 9091–9093 says "This example generalizes to surfaces of any odd genus by adding symmetric pairs of tori at the left and right. Examples for even genus are described in one of the exercises."

**Proof: correct.** Central sphere with m antipodal pairs of handles gives genus 2m; f = antipodal on the sphere plus swapping each pair of handles is a fixed-point-free homeomorphism; f_* on H_1 has zero diagonal in the symmetric handle basis (it swaps the two rank-2 summands of each pair); f_* on H_2 is multiplication by deg(antipodal S^2) = −1; hence τ(f) = 1 − 0 + (−1) = 0, as a fixed-point-free map must have.

### E-HAT-2.C-7 — Lefschetz theorem with field coefficients
**Statement: matches.** Book 9208–9209:
```
 9208|7. Verify that the Lefschetz fixed point theorem holds also when τ(f ) is defined using
 9209|homology with coefficients in a field F .
```
**Proof: correct.** The trace formula for a finite chain complex of finite-dimensional F-vector spaces (additivity of trace over 0 → B_n → Z_n → H_n → 0 and 0 → Z_n → C_n → B_{n−1} → 0), plus the geometric part of Hatcher's proof (9019–9037: after subdivision and simplicial approximation, g(σ) ∩ σ = ∅ for all σ), plus Hatcher's zero-diagonal step (9056–9058), which is coefficient-independent: "g∗ : Hn (K n , K n−1 )→Hn (K n , K n−1 ) has trace 0 since the matrix for g∗ has zeros down the diagonal, in view of the fact that g(σ ) ∩ σ = ∅". Hence fixed-point-free ⇒ τ_F(f) = 0. The card is explicit that it borrows the geometric part; that is what "verify that the theorem holds" asks for.

### E-HAT-2.C-8 — at most countably many homotopy classes X → Y
**Statement: matches.** Book 9210–9213:
```
 9210|8. Let X be homotopy equivalent to a finite simplicial complex and let Y be homotopy
 9211|equivalent to a finite or countably infinite simplicial complex. Using the simplicial ap-
 9212|proximation theorem, show that there are at most countably many homotopy classes
 9213|of maps X →Y .
```
**Proof: correct.** For each r, a simplicial map sd^r K → L is determined by its vertex map, and there are countably many of those (K finite, L countable); every map K → L is homotopic to such a simplicial map — Theorem 2C.1, 8886–8888: "If K is a finite simplicial complex and L is an arbitrary simplicial complex, then any map f : K →L is homotopic to a map that is simplicial with respect to some iterated barycentric subdivision of K"; finally [X,Y] ≅ [K,L] via the homotopy equivalences. All hypotheses of 2C.1 (K finite, L arbitrary) are satisfied.

### E-HAT-2.C-9 — countably many homotopy types of finite CW complexes
**Statement: matches.** Book 9214:
```
 9214|9. Show that there are only countably many homotopy types of finite CW complexes.
```
**Proof: correct.** The citation is right — Theorem 2C.5, 9106–9108: "Every CW complex X is homotopy equivalent to a simplicial complex, which can be chosen to be of the same dimension as X , finite if X is finite, and countable if X is countable." Then: finitely many simplicial complexes on each finite vertex set {1,…,N} (subsets of a finite power set), hence countably many isomorphism classes, hence at most countably many homotopy types.

## Defects found, most serious first

1. **E-HAT-2.C-2 — mis-nested proof structure.** `{.pf-step}` divs sit inside `pf-proof` divs (five levels in places), unlike every other card; the step/justification pairing is inverted, so the card will not render as a proof. The mathematics of the same card is correct.
2. **E-HAT-2.C-2 — `kind: problem` in the frontmatter but `::: {.exercise}` around the statement** (only such mismatch in §2.B/§2.C).
3. **E-HAT-2.C-2 — no `solution-reviewed` audit event** (only `solution-written`, Codex 5.3 Spark Extra High). No §2.C card carries a `solution-reviewed` event by `claude`.
4. **E-HAT-2.C-3 — the printed statement cannot be verified from `AT.txt` alone**: the extraction drops the overlines, so the card's `\bar z` differs literally from the witness at 9197 while being correct (proved by 9000–9004, "This map is only 'conjugate-linear' over C"). Recorded so that a human does not "fix" the card to match the damaged extraction.

No statement in §2.C differs from the printed exercise, and no proof in §2.C is false or proves something weaker than its statement.

Every card of §2.C was read in full (statement and proof).

## Mechanical statement check

A word-sequence diff between each card's statement and its printed exercise (`wordcheck.py` in this
directory, LaTeX stripped, extraction hyphenation ignored) left no residual word on either side for
any of the 9 cards apart from the extraction's split of "ap/proximation" at 9211–9212. **No
hypothesis, quantifier, hint or bracketed pointer of any §2.C exercise is missing from any card.**

Cross-references were checked as well: every `](#anchor){.pf-ref}` in the 9 cards resolves to a
`{.pf-step #anchor}` in the same card and no anchor is defined twice.
