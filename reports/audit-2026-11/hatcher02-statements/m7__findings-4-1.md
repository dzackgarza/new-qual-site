# Audit — SRC-TEXT-HAT02, §4.1 (*Homotopy Groups*), exercises 10–23 (14 cards)

Auditor: m7 (swarm smvy0zsoh), direction d4. Witness for every book claim: `tmp/hat/AT.txt`
(line numbers only). The printed exercises 10–23 are AT.txt lines 17861–17915 (`17910` and
`17866` are page headers in the extraction, not text of the exercises).

Section `corpus/collections/SRC-TEXT-HAT02/4-1/` holds **23 cards**; exercises 1–9 were audited
earlier (not touched here). This file covers 14 cards:
E-HAT-4.1-10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23. All were read in
full. Counts for the other sections are in `findings-3-h.md`.

Two statement-level defects in this slice are "iff" reduced to "if" (-19, -22), and two cards
drop a bracketed hint the book prints (-15, -22).

---

## E-HAT-4.1-10 — the quasi-circle

**STATEMENT: matches.**
Book, AT.txt:17861–17862:
`10. Show the ‘quasi-circle’ described in Exercise 7 in §1.3 has trivial homotopy groups`
`but is not contractible, hence does not have the homotopy type of a CW complex.`
Card: "Show the 'quasi-circle' described in Exercise 7 in §1.3 has trivial homotopy groups but
is not contractible, hence does not have the homotopy type of a CW complex." Identical.

**PROOF: has a gap — the path-confinement lemma is asserted and misattributed; one further
theorem is used silently.**
* The card's first sentence: `Let $Y$ be the quasi-circle of §1.3, Exercise 7. That exercise
  proves two facts we use: 1. every path in $Y$ is contained in a finite truncation of the
  oscillating graph together with the vertical segment and the connecting arc, hence in a
  finite tree; 2. the quotient map q: Y → S¹ collapsing the vertical segment has no lift to
  R → S¹.`
  Fact 2 is indeed in that exercise (AT.txt:4069–4075: `7. Let Y be the quasi-circle shown in
  the figure, a closed subspace` / `of R2 consisting of a portion of the graph of y = sin(1/x) ,
  the` / `segment [−1, 1] in the y axis, and an arc connecting these two` / `pieces. Collapsing
  the segment of Y in the y axis to a point` / `gives a quotient map f : Y →S 1 . Show that f
  does not lift to` / `the covering space R→S 1 , even though π1 (Y ) = 0 . Thus local`
  `path-connectedness of Y is a necessary hypothesis in the lifting criterion.`).
  **Fact 1 is not in that exercise and is not proved in the card.** It is the load-bearing step
  of the whole argument (it is what makes every map Sⁿ → Y nullhomotopic), and it needs a
  proof: the image of a path is compact, so a path avoiding the vertical segment has positive
  distance from it; and a path cannot approach a point of the segment through graph points,
  since that would force sin(1/x) to converge along a continuous parameter with x → 0, whereas
  sin(1/x) has no limit at 0. Hence the image lies in V ∪ A ∪ {x ≥ δ} for some δ > 0, a finite
  arc, hence contractible.
  Fix: replace "That exercise proves" by a proof of fact 1.
* Silent use of a theorem: `The sphere $S^n$ is a compact, connected, locally connected metric
  space, hence a Peano continuum. Therefore there is a continuous surjection r: I ↠ S^n.` The
  "therefore" is the Hahn–Mazurkiewicz theorem, valid but nowhere cited and not in Hatcher at
  this point. (Without it one can argue instead that f(Sⁿ) is itself a Peano continuum inside
  Y and hence confined; either way the step needs a line.)
* The rest is correct: f∘r is a path with image exactly f(Sⁿ) (r surjective), that image lies in
  a finite tree T ⊂ Y (fact 1), T is contractible, so f is nullhomotopic; hence π_n(Y) = 0
  (Y is path-connected, so unbased nullhomotopy can be converted to based nullhomotopy).
* Non-contractibility: correct. If Y were contractible, q: Y → S¹ would be nullhomotopic; the
  homotopy lifting property of the covering R → S¹ applied to that nullhomotopy with a lift of
  the terminal constant map produces a lift of q, contradicting §1.3 Exercise 7. HLP for
  coverings needs no local connectivity, so this argument is sound as written.
* Last paragraph (Whitehead for CW types) is correct.

---

## E-HAT-4.1-11 — contractibility from nullhomotopic inclusions

**STATEMENT: matches.**
Book, AT.txt:17863–17865 and 17869–17870 (page header at 17866):
`11. Show that a CW complex is contractible if it is the union of an increasing sequence`
`of subcomplexes X1 ⊂ X2 ⊂ ··· such that each inclusion Xi ֓ Xi+1 is nullhomotopic,`
`a condition sometimes expressed by saying Xi is contractible in Xi+1 . An example is`
`S ∞ , or more generally the infinite suspension S ∞ X of any CW complex X , the union`
`of the iterated suspensions S n X .`
Card: identical, including the second sentence about S^∞ and S^∞X. No difference.

**PROOF: correct.**
* Path-connectedness, with the stated reason (two points lie in some X_i; the nullhomotopy of
  X_i ↪ X_{i+1} joins their images) — correct.
* "Sⁿ compact in a CW complex ⇒ f(Sⁿ) lies in a finite subcomplex" is Hatcher's Proposition A.1
  (AT.txt:25888 `A compact subspace of a CW complex is contained in a finite subcomplex.`).
* That finite subcomplex lies in some X_i (finitely many cells, the sequence is increasing with
  union X) — correct.
* f factors through X_i, and X_i ↪ X_{i+1} nullhomotopic ⇒ f nullhomotopic — correct, gives
  π_n(X) = 0 for n ≥ 1.
* X → * is an isomorphism on all π_n and on π_0; X and * are CW complexes; Whitehead's theorem
  (Theorem 4.5, AT.txt:17284–17287) applies, so X ≃ *, i.e. contractible. Correct.

---

## E-HAT-4.1-12 — n-connected, n-dimensional CW complexes are contractible

**STATEMENT: matches.**
Book, AT.txt:17871: `12. Show that an n connected, n dimensional CW complex is contractible.`
Card: "Show that an $n$-connected, $n$-dimensional CW complex is contractible." Identical.

**PROOF: correct.**
* "n-connected" read correctly as π_i = 0 for i ≤ n (AT.txt:17254–17256 `A space X with
  basepoint x0 is said to be n connected if πi (X, x0 ) = 0 for` / `i ≤ n . Thus 0 connected
  means path-connected and 1 connected means simply-` / `connected.`).
* Minimal m > n with π_m ≠ 0 ⇒ X is (m−1)-connected; Hurewicz gives π_m ≅ H_m (for m ≥ 2; the
  only leftover case m = 1 forces n = 0 and then X is a single point, so nothing is missing).
* X has no cells above dimension n, so its cellular chain complex vanishes above n, hence
  H_m(X;Z) = 0 for m > n — contradiction. Correct.
* All homotopy groups vanish ⇒ X → * is an isomorphism on all π_i ⇒ Whitehead (both are CW)
  ⇒ X contractible. Correct.

---

## E-HAT-4.1-13 — retraction onto a contractible subcomplex

**STATEMENT: matches**, with one misleading gloss.
Book, AT.txt:17872–17873: `13. Use the extension lemma to show that a CW complex retracts onto
any contractible` / `subcomplex.`
Card: "Use the **Extension Lemma** (homotopy extension property for CW pairs) to show that a CW
complex $X$ **retracts** onto any contractible subcomplex $A \subseteq X$."
Content preserved (naming X and A is a harmless elaboration), but the parenthetical
"(homotopy extension property for CW pairs)" **misidentifies the book's "extension lemma"**.
Hatcher's extension lemma is Lemma 4.7 (AT.txt:17363–17366: `Somewhat similar in spirit to the
compression lemma is the following rather basic` / `extension lemma:` / ` Lemma 4.7. Given a CW
pair (X, A) and a map f : A→Y with Y path-connected,` / ` then f can be extended to a map X →Y
if πn−1 (Y ) = 0 for all n such that X − A` / `has cells of dimension n .`), which is *not* the
homotopy extension property (that is Proposition 0.16, AT.txt:926–928).

**PROOF: correct as mathematics; the citation is wrong.**
* The proof uses the HEP for CW pairs, which holds: Proposition 0.16 (AT.txt:926–928)
  ` Proposition 0.16. If (X, A) is a CW pair, then X × {0}∪A× I is a deformation retract`
  ` of X × I , hence (X, A) has the homotopy extension property.`
* The step `By the **Homotopy Extension Property** (Hatcher, Lemma 4.15 / Extension Lemma)` is
  a **citation to a result that does not exist**: §4.1 has no Lemma 4.15. The numbered items of
  §4.1 are 4.4–4.25 (AT.txt 17225–17990); 4.15 is Proposition 4.15 (`If (X, A) is an n
  connected CW pair, then there exists a CW pair …`, AT.txt:17605–17607), unrelated. The
  correct references are Proposition 0.16 (HEP) or, if one wants to follow the book's hint, the
  extension lemma Lemma 4.7 — which in fact gives the result in one line: Y = A is
  path-connected and π_k(A) = 0 for all k (A contractible), so id_A extends to X → A, a
  retraction.
* The argument actually given is valid: reverse the contraction of A to a homotopy
  h̄: A × I → A from the constant map at a₀ to id_A; apply HEP with target Y = A and initial map
  the constant map X → {a₀} (its restriction to A is h̄(·,0)); the resulting H satisfies
  H(a,1) = h̄(a,1) = a, so r(x) = H(x,1) retracts X onto A. Note that the target must be A (not
  X), which the card correctly does. Hypothesis of HEP (CW pair, A a subcomplex) is satisfied.

---

## E-HAT-4.1-14 — n-skeleta of homotopy equivalent complexes

**STATEMENT: matches.**
Book, AT.txt:17874–17875: `14. Use cellular approximation to show that the n skeletons of
homotopy equivalent` / `CW complexes without cells of dimension n + 1 are also homotopy
equivalent.`
Card: identical ("the $n$-skeleta of homotopy equivalent CW complexes without cells of dimension
$n+1$ are also homotopy equivalent"). No difference.

**PROOF: correct.**
* f, g homotopy inverses; cellular approximation (Theorem 4.8, AT.txt:17395–17397) makes them
  cellular after homotopy, so f(Xⁿ) ⊂ Yⁿ, g(Yⁿ) ⊂ Xⁿ and the restrictions f_n, g_n exist.
* g_nf_n = (gf)|_{Xⁿ}; the homotopy gf ≃ id_X restricted to Xⁿ × I is a map of CW pairs
  (Xⁿ × I, Xⁿ × ∂I) → (X, Xⁿ) which is already cellular on Xⁿ × ∂I, so Theorem 4.8's relative
  form homotopes it rel the two ends to a cellular map; dim(Xⁿ × I) = n+1, so its image lies in
  X^{n+1} = Xⁿ (no (n+1)-cells). Hence g_nf_n ≃ id_{Xⁿ} inside Xⁿ. Same for f_ng_n.
* Therefore f_n, g_n are homotopy inverses. Correct; the "no cells of dimension n+1"
  hypothesis is used exactly where it is needed.

---

## E-HAT-4.1-15 — every self-map of Sⁿ is a multiple of the identity

**STATEMENT: differs — the book's bracketed hint in part (c) is dropped.**
Book, AT.txt:17884–17886:
` (c) Finish the argument by showing that an invertible n× n matrix can be joined by`
`    a path of such matrices to either the identity matrix or the matrix of a reflection.`
`    (Use Gaussian elimination, for example.)`
Card, part (c): "Finish the argument by showing that an invertible $n \times n$ matrix can be
joined by a path of such matrices to either the identity matrix or the matrix of a reflection."
— the printed parenthetical `(Use Gaussian elimination, for example.)` (AT.txt:17886) is
missing. Parts (a) and (b) are reproduced verbatim, including `Lemma 4.10 (or simplicial
approximation, Theorem 2C.1)` (AT.txt:17878).

**PROOF: correct**, with step (a) taken from the book's hint as a black box.
* (a) The reduction is asserted — `By Lemma 4.10 (equivalently, after simplicial approximation
  and a small local modification), f is homotopic to a map for which there is a point q …` —
  which is exactly what the exercise tells the solver to do; but note that Lemma 4.10 as
  printed (AT.txt:17448–17452: `Lemma 4.10. Let f : I n →Z be a map, where Z is obtained from a
  subspace W by` / `attaching a cell ek . Then there is a homotopy ft : I n , f −1 (ek ) → Z, ek
  rel f −1 (W )` / `from f = f0 to a map f1 for which there is a polyhedron K ⊂ I n such that :`
  / `(a) f1 (K) ⊂ ek and f1 || K is PL …` / `(b) K ⊃ f1−1 (U) for some nonempty open set U in
  ek .`) does not state this genericity conclusion, so the card should have spelled out how the
  finitely-many-preimages/linear-near-them map is obtained (PL approximation plus a regular
  value). Not false, but it is a black box in the proof rather than in the statement.
* (b) g ≃ id (the radial-stretch description is a degree-1 pinch), so gf ≃ f; gf is constant off
  the disjoint balls B_i, so it factors through the pinch Sⁿ → ⋁_k Sⁿ followed by h₁∨⋯∨h_k, and
  [f] = Σ[h_i] in π_n(Sⁿ) = Z. Correct. Each h_i has exactly one preimage of q and is linear
  there (g|_B is a homeomorphism B → Sⁿ). Correct.
* (c) GL_n(R) has two path components by sign of determinant; a path of matrices from the local
  model A to I or diag(−1,1,…,1), applied inside the ball and keeping the map fixed outside,
  homotopes h_i to id (det > 0) or to a reflection, which has degree −1. Correct. Summing gives
  [f] = (Σ ε_i)[id]. Correct — with the usual caveat that d = 0 means the constant map, which
  the display "f ≃ d·id" covers.

---

## E-HAT-4.1-16 — factoring a map through an n-connective cover

**STATEMENT: matches.**
Book, AT.txt:17887–17889:
`16. Show that a map f : X →Y between connected CW complexes factors as a com-`
`position X →Zn →Y where the first map induces isomorphisms on πi for i ≤ n and`
`the second map induces isomorphisms on πi for i ≥ n + 1 .`
Card: identical. No difference.

**PROOF: correct in outline; the colimit step is asserted.**
* Construction: attach cells to X in dimensions ≥ n+1 (so π_i, i ≤ n, is unchanged — cells of
  dimension ≥ n+1 do not affect π_i for i ≤ n), then inductively for k = n+1, n+2, …: make
  π_k surjective by wedging k-spheres carrying chosen classes of π_k(Y), then kill the kernel by
  (k+1)-cells. Each stage makes π_k an isomorphism and leaves π_i for i < k untouched. This is
  the standard construction (cf. the proof of Proposition 4.13, AT.txt:17590–17602, and
  Proposition 4.15, AT.txt:17605–17609).
* The hypothesis "connected" is used for π_0 (the first map is an isomorphism on π_0 because
  X, Y, Z_n are connected). Correct.
* ASSERTED: `By the inductive construction, the extension g: Z_n → Y induces isomorphisms
  π_i(Z_n) ≅ π_i(Y) for i ≥ n+1.` Passing from "isomorphism at stage k = i" to "isomorphism for
  the union" needs π_i(⋃Z_k) = lim π_i(Z_k) (each inclusion is a cofibration and the colimit is
  a CW complex). True, but not stated.
* Minor imprecision: `wedge on countably many spheres, mapped to representatives of π_k(Y), to
  make the map surjective on π_k` — surjectivity on π_k needs the chosen classes to *generate*
  π_k(Y) (a generating set, not just representatives); the card says this correctly in one place
  ("for each class of π_k(Y) not yet in the image") and loosely in another.

---

## E-HAT-4.1-17 — connectivity of (X×Y, X∨Y) and X∧Y

**STATEMENT: matches.**
Book, AT.txt:17890–17891:
`17. Show that if X and Y are CW complexes with X m connected and Y n connected,`
`then (X × Y , X ∨ Y ) is (m + n + 1) connected, as is the smash product X ∧ Y .`
Card: identical. No difference.

**PROOF: correct.**
* Replacing X by an m-connected CW model with one 0-cell and no cells in dimensions 1..m (and
  similarly Y) preserves the pair up to homotopy equivalence of pairs — correct (CW
  approximation, Proposition 4.13/4.15).
* In the product CW structure, the cells not in X∨Y are exactly e^p × e^q with p,q > 0, hence of
  dimension p+q ≥ (m+1)+(n+1) = m+n+2. Correct.
* "No relative cells in dimensions ≤ m+n+1 ⇒ π_i(X×Y, X∨Y) = 0 for i ≤ m+n+1" is exactly
  Corollary 4.12 (AT.txt:17514–17516: `Corollary 4.12. A CW pair (X, A) is n connected if all
  the cells in X − A have` / `dimension greater than n .`), whose hypothesis is met with
  n = m+n+1. Correct; the pair definition (AT.txt:17274–17278) also requires the i = 0
  condition, which holds since X∨Y meets the unique path component of X×Y.
* X∧Y = (X×Y)/(X∨Y) is the quotient by a subcomplex, so a CW complex with a single 0-cell and
  positive cells only in dimensions ≥ m+n+2, hence (m+n+1)-connected. Correct (m, n ≥ 0 makes
  m+n+2 ≥ 2, so it is also simply connected, as needed for π_1).

---

## E-HAT-4.1-18 — asymmetric weak homotopy equivalence

**STATEMENT: matches.**
Book, AT.txt:17892–17893: `18. Give an example of a weak homotopy equivalence X →Y for which
there does not` / `exist a weak homotopy equivalence Y →X .`
Card: identical. No difference.

**PROOF: correct.**
* P = {a,b,c,d} with minimal opens {a}, {b}, {a,b,c}, {a,b,d} is the pseudocircle; the
  specialization order has a,b < c,d, whose order complex is the 4-cycle (vertices a,b,c,d,
  edges ac,ad,bc,bd) = S¹. Correct.
* McCord's theorem (McCord 1966) that |K(P)| → P is a weak homotopy equivalence for finite T₀
  spaces is quoted correctly; hence S¹ → P is a weak homotopy equivalence. Correct.
* No weak homotopy equivalence P → S¹: for any map g: P → S¹, g(P) is a finite subspace of the
  Hausdorff space S¹, hence discrete (finite + T₁ ⇒ discrete); P is connected (indeed
  path-connected, π₀(P) = π₀(S¹) = *), so g(P) is a point, i.e. g is constant, hence
  null-homotopic, hence g_* = 0 on π₁ while π₁(P) ≅ π₁(S¹) ≅ Z ≠ 0. Correct.
* One could object that the card proves g_* is zero rather than "not an isomorphism" — the zero
  map Z → Z is indeed not an isomorphism, so the conclusion stands.

---

## E-HAT-4.1-19 — weak equivalence relation vs common CW approximation

**STATEMENT: differs — the book's "iff" is printed as "if".**
Book, AT.txt:17894–17897:
`19. Consider the equivalence relation ≃w generated by weak homotopy equivalence:`
`X ≃w Y if there are spaces X = X1 , X2 , ··· , Xn = Y with weak homotopy equivalences`
`Xi →Xi+1 or Xi ← Xi+1 for each i . Show that X ≃w Y iff X and Y have a common`
`CW approximation.`
Card: "…Show that $X \simeq_w Y$ **if** $X$ and $Y$ have a common CW approximation."
Half of the "iff" (AT.txt:17896: `Xi →Xi+1 or Xi ← Xi+1 for each i . Show that X ≃w Y iff X and
Y have a common`) is dropped: the card asks only for "common CW approximation ⇒ X ≃_w Y".

**PROOF: has a gap — it proves only the direction the card kept, i.e. something weaker than the
book's exercise.**
* What is proved: a common CW approximation K with weak equivalences K → X, K → Y gives the
  zigzag X ← K → Y, which is one of the allowed zigzags. Correct as far as it goes.
* Missing: the converse (X ≃_w Y ⇒ a common CW approximation). That needs: every space has a CW
  approximation (Proposition 4.13, AT.txt:17590–17592 `Proposition 4.13. Every space X has a CW
  approximation f : Z →X .`), weak homotopy equivalences are preserved/composed along the
  zigzag, and a weak homotopy equivalence between CW complexes is a homotopy equivalence so that
  the two approximations can be identified (or: two CW approximations of weakly equivalent
  spaces are themselves weakly equivalent, hence homotopy equivalent). None of this is in the
  card.
* Fix: restore "iff" in the statement and add the converse argument.

---

## E-HAT-4.1-20 — [X,Y] is finite

**STATEMENT: matches.**
Book, AT.txt:17898–17899: `20. Show that [X, Y ] is finite if X is a finite connected CW complex
and πi (Y ) is` / `finite for i ≤ dim X .`
Card: identical. No difference.

**PROOF: correct.**
* Replacing Y by its d-th Postnikov stage (d = dim X) is legitimate: Y → Y^d is an isomorphism
  on π_i for i ≤ d, and cellular/obstruction-theoretic induction on skeleta gives
  [X,Y] ≅ [X,Y^d] for a d-dimensional CW complex X. Correct (this is Hatcher's §4.3 use of
  Postnikov towers).
* Counting: X has finitely many cells; a map is determined by its restriction to skeleta; at
  each k-cell the extension is obstructed by an element of π_{k−1}(Y^d) = π_{k−1}(Y) and, when
  nonempty, the set of extensions up to homotopy rel the boundary is a torsor under π_k(Y^d) =
  π_k(Y). Both are finite for k ≤ d, and only finitely many cells occur, so only finitely many
  homotopy classes can arise. Correct.
* π_0: the card's "each map lands in one path component of Y; finitely many choices by the
  hypothesis on π_0(Y)" uses finiteness of π_0(Y), which the hypothesis supplies only if i = 0
  is included in "i ≤ dim X" (as written it is). Worth noting, since without finite π_0 the
  claim is false (X = point, Y with infinitely many components). No defect in the card given
  the stated hypothesis.

---

## E-HAT-4.1-21 — Postnikov stage of a covering

**STATEMENT: matches.**
Book, AT.txt:17900–17906 (lines 17903 and 17905 are the extraction's superscript lines):
`21. For this problem it is convenient to use the notations X n for the n th stage in a`
`Postnikov tower for X and Xm for an (m − 1) connected covering of X , where X is a`
`connected CW complex. Show that (X n )m ≃ (Xm )n , so the notation` / ` n` / `Xm is
unambiguous. Thus πi (Xm ) ≈ πi (X) for m ≤ i ≤ n and all` / ` n` / `other homotopy groups of
Xm are zero.`
Card reproduces this exactly (including "(m−1)-connected covering" and "≈"). No difference.

**PROOF: correct at sketch level; one model is asserted and one hypothesis is implicit.**
* Homotopy groups: X^n has π_i = π_i(X) for i ≤ n and 0 above; X_m is (m−1)-connected with
  π_i = π_i(X) for i ≥ m. Both orders therefore have π_i(X) in m ≤ i ≤ n and 0 elsewhere —
  correct.
* ASSERTED: `X_m ≃ hofib(X → X^{m-1})` (and `(X^n)_m ≃ hofib(X^n → X^{m-1})` for n ≥ m−1).
  This needs care and is only true under the implicit hypothesis that an (m−1)-connected
  *covering* of X exists, i.e. that π_i(X) = 0 for 2 ≤ i ≤ m−2. Then X_m is the universal cover
  (for m ≥ 2) and the homotopy fibre is a simply-connected fibration with the same homotopy
  groups, hence homotopy equivalent to it (a lift exists because the fibre is simply connected
  and X_m → X is a covering). The card does not mention this; for spaces where no
  (m−1)-connected covering exists the displayed identity has no meaning (e.g. X = S², m = 3).
* The comparison: X → X^n is an isomorphism on π_i for i ≤ n, so the induced map of homotopy
  fibres X_m → (X^n)_m is an isomorphism on π_i for i ≤ n (5-lemma on the two long exact
  sequences; at i = n one uses π_n(X_m) = π_n(X) = π_n(X^n) = π_n((X^n)_m)). The target has no
  homotopy above n, so it is an n-th Postnikov stage of X_m, hence ≃ (X_m)^n. Correct.
* The degenerate cases are handled correctly: n < m−1 gives two contractible spaces; n = m−1
  likewise ((X^{m−1})_m has vanishing π_i for i ≥ m and is (m−1)-connected; (X_m)^{m−1} is an
  (m−1)-connected space with all π_i, i ≤ m−1, zero).

---

## E-HAT-4.1-22 — countable CW approximation

**STATEMENT: differs twice — "iff" reduced to "if", and the book's bracketed hint is dropped.**
Book, AT.txt:17907–17909:
`22. Show that a path-connected space X has a CW approximation with countably many`
`cells iff πn (X) is countable for all n . [Use the results on simplicial approximations`
`to maps and spaces in §2.C.]`
Card: "Show that a path-connected space $X$ has a CW approximation with countably many cells
**if** $\pi_n(X)$ is countable for all $n$."
Differences: (i) "iff" → "if" (AT.txt:17908 `cells iff πn (X) is countable for all n .`) —
the converse is no longer asked for; (ii) the printed hint `[Use the results on simplicial
approximations to maps and spaces in §2.C.]` (AT.txt:17908–17909) is missing.

**PROOF: has a gap — only the direction the card kept is proved, so it proves less than the
printed exercise.**
* What is proved (correctly, in outline): build K inductively, adding countably many cells at
  each stage. Countability of π_1(X) gives countably many 1-cells; the kernel killed at each
  stage is countable because π_n(K_n) is countable (a map Sⁿ → K_n has compact image, hence
  lands in one of countably many finite subcomplexes, each with countably many homotopy classes
  by simplicial approximation — this is exactly the §2.C input the book hints at); countably
  many (n+1)-cells then make π_n an isomorphism, and countably many more make π_{n+1}
  surjective. Correct, with the same wording slip as in 4.1-16 ("mapped to representatives of
  π_{n+1}(X)" should be "a countable generating set of π_{n+1}(X)").
* Missing: the converse (a CW approximation with countably many cells ⇒ every π_n(X) is
  countable). That direction needs: a countable CW complex has countable π_n (again via
  compact images/simplicial approximation), and π_n(X) ≅ π_n(K) for a weak homotopy
  equivalence K → X.
* Fix: restore "iff" and the §2.C hint, and add the converse.

---

## E-HAT-4.1-23 — mapping cylinder/cone of a map of CW type

**STATEMENT: matches.**
Book, AT.txt:17913–17915:
`23. If f : X →Y is a map with X and Y homotopy equivalent to CW complexes, show`
`that the pair (Mf , X) is homotopy equivalent to a CW pair, where Mf is the mapping`
`cylinder. Deduce that the mapping cone Cf has the homotopy type of a CW complex.`
Card: identical. No difference.

**PROOF: correct.**
* Choose CW complexes X′, Y′ with homotopy equivalences u: X′ → X, v: Y′ → Y, set
  f′ = v⁻¹ f u: X′ → Y′, and replace f′ by a homotopic cellular map (Theorem 4.8). Correct.
* The square commutes up to homotopy (v∘f′ = v v⁻¹ f u ≃ f u), the vertical maps are homotopy
  equivalences, and M_f is the homotopy pushout of X ← X → Y (with the two maps being id_X and
  f), so homotopy invariance of homotopy pushouts gives a homotopy equivalence of pairs
  (M_{f′}, X′) ≃ (M_f, X). Correct; the map can be arranged to carry X′ to X, which is what is
  needed for the pair statement.
* Because f′ is cellular, M_{f′} = (X′ × I ⊔ Y′)/(x,1) ~ f′(x) has a CW structure with X′ × {0}
  as a subcomplex. Correct (cells e × {0}, e × (0,1), e × {1} together with the cells of Y′).
* C_f = M_f/X, and homotopy equivalence of pairs gives C_f ≃ M_{f′}/X′, a CW complex since it is
  a CW complex modulo a subcomplex. Correct.

---

# Summary of defects — §4.1 exercises 10–23, most serious first

1. **E-HAT-4.1-22, statement and proof.** Book: "…has a CW approximation with countably many
   cells **iff** π_n(X) is countable for all n. [Use the results on simplicial approximations to
   maps and spaces in §2.C.]" (AT.txt:17907–17909). Card: "**if** …", and the bracketed §2.C
   hint is gone. The proof establishes only "countable ⇒ countable CW approximation"; the
   converse is not proved, so the card answers a strictly weaker question.
2. **E-HAT-4.1-19, statement and proof.** Book: "Show that X ≃_w Y **iff** X and Y have a common
   CW approximation." (AT.txt:17896–17897). Card: "**if** …". Only the easy zigzag direction is
   proved; the converse is missing.
3. **E-HAT-4.1-13, proof (wrong citation) and statement (misleading gloss).** "Hatcher, Lemma
   4.15 / Extension Lemma" does not exist: §4.1 has no Lemma 4.15 (4.15 is Proposition 4.15,
   n-connected CW models, AT.txt:17605–17607). Hatcher's extension lemma is Lemma 4.7
   (AT.txt:17363–17366) and the HEP for CW pairs is Proposition 0.16 (AT.txt:926–928). The
   parenthetical "(homotopy extension property for CW pairs)" in the statement also misnames
   the book's "extension lemma". The argument given is nevertheless valid; the one-line proof
   from Lemma 4.7 is worth recording.
4. **E-HAT-4.1-15, statement.** The printed hint `(Use Gaussian elimination, for example.)`
   (AT.txt:17886) is dropped from part (c). The proof is otherwise right, with step (a) taken
   from the book's hint as a black box (Lemma 4.10 as printed, AT.txt:17448–17459, does not by
   itself state the genericity conclusion).
5. **E-HAT-4.1-10, proof.** The path-confinement lemma ("every path in Y is contained in a finite
   truncation … hence in a finite tree") is attributed to §1.3 Exercise 7, which contains only
   the non-lift statement and π_1(Y) = 0 (AT.txt:4069–4075); it is the load-bearing step and is
   never proved. Hahn–Mazurkiewicz is also used silently ("hence a Peano continuum. Therefore
   there is a continuous surjection r: I ↠ S^n").
6. **E-HAT-4.1-21, proof (asserted model).** `X_m ≃ hofib(X → X^{m-1})` is asserted; it holds
   only when an (m−1)-connected covering exists (π_i(X) = 0 for 2 ≤ i ≤ m−2), which the card
   neither states nor uses; for other X the notation X_m in the exercise itself has no meaning.
7. **E-HAT-4.1-16, proof (colimit step asserted).** "By the inductive construction, the
   extension g: Z_n → Y induces isomorphisms π_i(Z_n) ≅ π_i(Y) for i ≥ n+1" needs
   π_i(⋃Z_k) = lim π_i(Z_k) (cofibrations, CW colimit). Also "mapped to representatives of
   π_{n+1}(X)" should be a generating set.
8. **E-HAT-4.1-20, proof (hypothesis usage worth flagging).** The finiteness of π_0(Y) is needed
   and is used; it is covered by the book's "i ≤ dim X" only if i = 0 is included. No defect,
   but the fixer should keep it in mind.
9. **Audit metadata.** E-HAT-4.1-13 and E-HAT-4.1-18 carry no `source-checked` event, and
   E-HAT-4.1-13's solution uses bare `::: pf-step` without `#sn` ids; all div nesting in the
   slice balances.

Statement-by-statement result for the slice: 11 of 14 statements match the printed exercise
verbatim; E-HAT-4.1-15 (dropped parenthetical hint), E-HAT-4.1-19 (iff → if), E-HAT-4.1-22
(iff → if, hint dropped) differ. Proofs: 9 read as correct (-11, -12, -13, -14, -15, -17, -18,
-20, -23; of these -13 carries a wrong citation and -15 a black-box step), 5 have gaps at
least at sketch level (-10, -16, -19, -21, -22; -19 and -22 because only one direction of the
printed "iff" is proved, -16 and -21 because one step is asserted). No card in this slice was
left unread.
