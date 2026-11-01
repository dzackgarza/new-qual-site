# Findings — SRC-TEXT-HAT02, slice §3.F (Limits and Ext)

Auditor: member `m4`, swarm `smvy0zsoh`. Source of truth: `tmp/hat/AT.txt` (line numbers below are its lines,
quoted verbatim including the extractor's spacing artefacts). Nothing under `corpus/` was modified.

**Scope and completeness.** Slice `corpus/collections/SRC-TEXT-HAT02/3-f/` contains **9 cards**
(`E-HAT-3.F-1` … `E-HAT-3.F-9`), corresponding one-to-one and in order to Hatcher §3.F Exercises 1–9
(`AT.txt` 15973 "Exercises", 15974–16023). **All 9 statements and all 9 proofs were read in full.** No card in
this slice is sampled-only and none is marked correct without having been read.

## Card counts per section

Measured with `ls corpus/collections/SRC-TEXT-HAT02/<dir> | wc -l` (437 cards in the collection):

| dir | n | dir | n | dir | n | dir | n |
|---|---|---|---|---|---|---|---|
| 1-1 | 20 | 2-1 | 31 | 3-1 | 13 | 4-1 | 23 |
| 1-2 | 22 | 2-2 | 42 | 3-2 | 17 | 4-2 | 39 |
| 1-3 | 33 | 2-3 | 4 | 3-3 | 35 | 4-3 | 24 |
| 1-a | 14 | 2-b | 11 | 3-a | 6 | 4-a | 5 |
| 1-b | 9 | 2-c | 9 | 3-b | 5 | 4-b | 2 |
| | | | | 3-c | 16 | 4-d | 10 |
| | | | | 3-d | 3 | 4-f | 3 |
| | | | | 3-e | 4 | 4-g | 4 |
| | | | | **3-f** | **9** | 4-h | 4 |
| | | | | 3-h | 6 | 4-i | 3 |
| | | | | | | 4-k | 6 |
| | | | | | | 4-l | 5 |

(`4-1` has 23 cards = Exercises 1–23, consistent with 1–9 already being read.)

---

## Per-card audit

### E-HAT-3.F-1 — "Reverse and double mapping telescopes"

Book (`AT.txt` 15974–15979):

```
1. Given maps fi : Xi →Xi+1 for integers i < 0 , show that the ‘reverse mapping tele-
scope’ obtained by glueing together the mapping cylinders of the fi ’s in the obvious
way deformation retracts onto X0 . Similarly, if maps fi : Xi →Xi+1 are given for all
i ∈ Z , show that the resulting ‘double mapping telescope’ deformation retracts onto
any of the ordinary mapping telescopes contained in it, the union of the mapping
cylinders of the fi ’s for i greater than a given number n .
```

**STATEMENT: matches.** The only differences are orthographic, not mathematical: book "glueing" (15975) vs card
"gluing"; book single quotes ‘…’ (15974, 15977) vs card `"…"`. Hypotheses (`i < 0`; `i ∈ Z`), the phrase "in the
obvious way", and "for i greater than a given number n" are all preserved.

**PROOF: correct.** Steps check out: (i) each `M_i` deformation retracts onto its top copy of `X_{i+1}` fixing
`X_{i+1}` (Hatcher's telescope convention, `AT.txt` 15539–15543: "The mapping telescope … is the union of the
mapping cylinders Mfi with the copies of Xi in Mfi and Mfi−1 identified for all i"); (ii) the time schedule
`[0,1/2], [1/2,3/4], …` tiles `[0,1)`; (iii) a point of `M_{-k}` is carried to `X_0` after finitely many (namely
`k`) stages, so `F(-,1)` lands in `X_0`, and `F(-,0)=id`, `F|_{X_0}=id` throughout. The double-telescope part is
right: with `L = ⋃_{i<n} M_i` one has `L ∩ T_{≥n} = X_n`, the reverse-telescope retraction fixes `X_n`, so
extending by the identity on `T_{≥n}` is well defined, continuous, and gives `T ↘ T_{≥n}`.
*One implicit point, not a defect:* "On each compact subset only finitely many cylinders are involved" is the
CW-topology fact that a compact subspace of the telescope meets only finitely many cells/cylinders (cf. Prop.
A.1, `AT.txt` 25888–25889 "Proposition A.1. A compact subspace of a CW complex is contained in a finite sub-
complex."). The card
states it; it could say why.

### E-HAT-3.F-2 — "Mittag–Leffler condition and `lim¹`"

Book (`AT.txt` 15980–15984):

```
                                                              α2        α1
              lim1 Gi = 0 if the sequence ··· ---→ G2 ------→ G1 ------→ G0 satisfies the
2. Show that ←--
Mittag–Leffler condition that for each i the images of the maps Gi+n →Gi are inde-
pendent of n for sufficiently large n .
```

**STATEMENT: matches** (the card's `G_2 --α_2--> G_1 --α_1--> G_0` reproduces the book's arrow labels; `lim¹` →
`\varprojlim^1`).

**PROOF: has a gap** (one false choice, repairable in one word). Exact step:

> "Hence the tower (I_i) has surjective bonding maps, so its varprojlim¹ vanishes: given (b_i) ∈ ∏ I_i,
> **choose g_0 arbitrarily** and then recursively choose g_{i+1} with α_{i+1}(g_{i+1}) = g_i − b_i. This solves
> Φ(g) = b."

The recursion is solvable only if `g_i − b_i ∈ I_i` at each stage; that is automatic for `g_i ∈ I_i`, but **not**
for an arbitrary `g_0 ∉ I_0` (then `g_0 − b_0 ∉ I_0` in general and `α_1(I_1) = I_0` gives no preimage). The
correct choice is `g_0 = 0` (or any element of `I_0`), which is exactly what the book does for the same
statement (`AT.txt` 15639–15643):

```
      If all the αi ’s are isomorphisms then ←-- lim Gi ≈ G0 and lim1 Gi = 0 . In fact,
                                                              ←--
      lim1 Gi = 0 if each αi is surjective, for to realize a given element (hi ) ∈ ∏i Gi as
      ←--
      δ(gi ) we can take g0 = 0 and then solve α1 (g1 ) = −h0 , α2 (g2 ) = g1 − h1 , ··· .
```

Everything else in the proof is right: `α_{i+1}(I_{i+1}) = I_i` (choose `j` past both stabilisation thresholds,
so both displayed equalities hold simultaneously); a zero-bonding tower has `Φ = id`, hence `lim = lim¹ = 0`;
the six-term sequence for `0 → (I_i) → (G_i) → (Q_i) → 0` then gives `lim¹ G_i = 0`.

*Two unstated justifications (true, but they should be named):* "Passing to a cofinal subsequence, we may assume
each bonding map `Q_{i+1} → Q_i` is zero" needs (a) the recursive construction of the subsequence, which works
because "for every `i` some sufficiently long composite `Q_j → Q_i` is zero", and (b) invariance of `lim¹` under
cofinal subsequences — `AT.txt` 15646–15650: "Deleting a finite number of terms from the end of the sequence
··· →G1 →G0 does not affect lim Gi or lim1 Gi . More generally, lim Gi and lim1 Gi are unchanged if we replace
the sequence ··· →G1 →G0 by a subsequence, with the appropriate compositions of αj ’s as the maps." Both facts
are in Hatcher and are used silently.

### E-HAT-3.F-3 — "Ext(A, ℚ) = 0"

Book (`AT.txt` 15985–15986):

```
3. Show that Ext(A, Q) = 0 for all A . [Consider the homology with Q coefficients of
a Moore space M(A, n) .]
```

**STATEMENT: matches**, including the bracketed hint verbatim, including that the book says *homology* (not
cohomology) with ℚ coefficients.

**PROOF: has a gap** in the third block ("Alternative topological perspective via Moore spaces"). Exact step:

> "Since ℚ is a field, H_{n+1}(X;ℚ) ≅ H_{n+1}(X)⊗ℚ = 0⊗ℚ = 0, so H^{n+1}(X;ℚ) = 0. The exact sequence forces
> Ext(A,ℚ) = 0."

The only exact sequence displayed in that block is
`0 → Ext(H_n(X),ℚ) → H^{n+1}(X;ℚ) → Hom(H_{n+1}(X),ℚ) → 0`, which with `H_{n+1}(X) = 0` reads
`0 → Ext(A,ℚ) → H^{n+1}(X;ℚ) → 0`. So "H^{n+1}(X;ℚ) = 0 ⟹ Ext(A,ℚ) = 0" is *the very statement being proved*:
as written the step is circular. Getting `H^{n+1}(X;ℚ) = 0` from `H_{n+1}(X;ℚ) = 0` needs the **field-coefficient**
form of the UCT, `H^k(X;F) ≅ Hom_F(H_k(X;F),F)`, which the card never states. One line repairs it (insert
`H^{n+1}(X;ℚ) ≅ Hom(H_{n+1}(X;ℚ),ℚ) = 0`). Note the algebraic route (blocks 1–2) is complete and correct — ℚ is
divisible hence injective (Baer), so `d*` is onto and `Ext¹(A,ℚ) = coker d* = 0` — so the card's *conclusion*
stands; the defect is confined to the alternative proof it advertises.

*Structure:* in this card the `.pf-step` divs are nested **inside** the `.pf-proof` divs (proof-of-a-substep),
the reverse of the pattern used elsewhere in the collection; rendering/structure only, no mathematical content.
*Metadata:* the card has only `solution-written` (no `source-checked`, no `solution-reviewed`).

### E-HAT-3.F-4 — "Divisible groups and vanishing Ext"

Book (`AT.txt` 15988–15991):

```
4. An abelian group G is defined to be divisible if the map G --n--> G , g ֏ ng , is
surjective for all n > 1 . Show that a group is divisible iff it is a quotient of a direct sum
of Q ’s. Deduce from the previous problem that if G is divisible then Ext(A, G) = 0
for all A .
```

**STATEMENT: matches** ("iff" rendered as "if and only if"; the definition and both deductions are word for
word, including "Deduce from the previous problem").

**PROOF: correct.** Forward direction (quotient of `⊕ℚ` is divisible) is right. Converse: `g_{i,1} = g_i`,
`n·g_{i,n!} = g_{i,(n-1)!}` is a consistent choice, and `φ_i(1/n!) := g_{i,n!}` is well defined because
`(n+1)g_{i,(n+1)!} = g_{i,n!}`, so `φ_i(1) = g_i` extends to `φ_i : ℚ → G`; `Φ = ⊕φ_i` is onto because the `g_i`
generate. `D = ⊕_I ℚ` is divisible (finite supports), hence injective, hence `Ext(A,D) = 0`; applying
`Hom(A,−)` to `0 → K → D → G → 0` ends with `Ext(A,D) → Ext(A,G) → 0` (this is the second sequence of Prop.
3F.11, `AT.txt` 15828), so `Ext(A,G) = 0`. No circularity: Exercise 3's argument uses only divisibility of ℚ.

### E-HAT-3.F-5 — "Ext(A, ℤ) as a cokernel"

Book (`AT.txt` 15992–15995):

```
5. Show that Ext(A, Z) is isomorphic to the cokernel of Hom(A, Q)→Hom(A, Q/Z) ,
the map induced by the quotient map Q→Q/Z . Use this to get another proof that
               b p for p prime.
Ext(Zp∞ , Z) ≈ Z
```

**STATEMENT: matches** (the book's `Ẑ_p`, flattened to `Z b p` by the extractor, appears as `\widehat{\ZZ}_p`).

**PROOF: correct.** From `0 → ℤ → ℚ → ℚ/ℤ → 0` and `Ext(A,ℚ) = 0` the LES gives
`Hom(A,ℚ) → Hom(A,ℚ/ℤ) → Ext(A,ℤ) → 0`, i.e. `Ext(A,ℤ) ≅ coker`, exactly as the exercise asks. For
`A = ℤ_{p^∞}`: `Hom(A,ℚ) = 0` (torsion → torsionfree); any `A → ℚ/ℤ` has image of order a power of `p`, i.e.
lands in the `p`-primary part `ℤ[1/p]/ℤ ≅ ℤ_{p^∞}` (`AT.txt` 15529–15531), so
`Hom(ℤ_{p^∞},ℚ/ℤ) ≅ End(ℤ_{p^∞}) = lim_n Hom(ℤ/p^n,ℤ_{p^∞}) = lim_n ℤ/p^n = Ẑ_p`. Correct.

### E-HAT-3.F-6 — "Ext(ℤ_{p^∞}, ℤ_p)"

Book (`AT.txt` 15996):

```
6. Show that Ext(Zp∞ , Zp ) ≈ Zp .
```

**STATEMENT: matches.**

**PROOF: correct.** The resolution is the standard one (`AT.txt` 15784–15790: "A free resolution of Zp∞ is
0 -→ Z∞ --ϕ→ Z∞ -→ Zp∞ -→ 0 … and ϕ sends (x1 , x2 , ···) to (px1 − x2 , px2 − x3 , ···)") re-indexed:
`d` is injective (coefficient of the top `e_{N+1}` forces the top coefficient to vanish), and the kernel is
generated by `p e_1, p e_{n+1} − e_n`. With `p = 0` in `ℤ_p`, `d*(a_1,a_2,…) = (0,−a_1,−a_2,…)`, whose image is
exactly `{b : b_0 = 0}`, so `coker d* ≅ ℤ_p`. Correct, including the bookkeeping that
`Hom(⊕ℤ,ℤ_p) ≅ ∏ℤ_p`.

### E-HAT-3.F-7 — "Moore spaces as quotients"

Book (`AT.txt` 15997–16003):

```
7. Show that for a short exact sequence of abelian groups 0→A→B →C →0 , a Moore
space M(C, n) can be realized as a quotient M(B, n)/M(A, n) . Applying the long exact
                                                         
sequence of cohomology for the pair M(B, n), M(A, n) with any coefficient group
G , deduce an exact sequence

 0→Hom(C, G)→Hom(B, G)→Hom(A, G)→Ext(C, G)→Ext(B, G)→Ext(A, G)→0
```

**STATEMENT: matches** (the stray glyph on `AT.txt` 15999 is the parentheses around the pair).

**PROOF: correct for n ≥ 2; has a gap: the case n = 1 is not covered.** The card restricts by fiat —
"For n ≥ 2, realize i by a cellular map M(A,n) → M(B,n) inducing i on the only nonzero reduced homology group"
— and never returns to `n = 1`, while the book defines Moore spaces for `n ≥ 1` (`AT.txt` 7201: "Given an
abelian group G and an integer n ≥ 1 , we will construct a CW complex X such that Hn (X) ≈ G and Hi (X) = 0 for
i ≠ n"; `AT.txt` 7205–7207 adds "it is probably best for the definition of a Moore space to include the
condition that M(G, n) be simply-connected if n > 1", i.e. `n = 1` is deliberately in scope). The restriction is
patchable (`M(A,1)` is a `K(A,1)`, so `Hom(A,B)` is again realised by a map), but as it stands the card proves a
strictly weaker statement than the book prints.
Everything the card does for `n ≥ 2` checks out: the LES of the pair gives `H̃_n(Q) ≅ B/im(A) = C` and
`H̃_j(Q) = 0` for `j ≠ n` (using `H_{n+1}(pair) ≅ ker i = 0`, which needs `i` injective — true here, and used
silently — and `H_j(X,A) ≅ H̃_j(X/A)` for a CW pair, also used silently); the UCT gives `H̃^n(M(D,n);G) ≅ Hom(D,G)`
and `H̃^{n+1}(M(D,n);G) ≅ Ext(D,G)`; the pair LES then reproduces the displayed six-term sequence, including the
`0 →` at the left end from `H̃^{n-1}(M(A,n);G) = 0`, and it agrees with Prop. 3F.11's second sequence
(`AT.txt` 15828).

### E-HAT-3.F-8 — "Bockstein sequence on Moore spaces"

Book (`AT.txt` 16005–16009):

```
8. Show that for a Moore space M(G, n) the Bockstein long exact sequence in cohomol-
ogy associated to the short exact sequence of coefficient groups 0→A→B →C →0
reduces to an exact sequence

 0→Hom(G, A)→Hom(G, B)→Hom(G, C)→Ext(G, A)→Ext(G, B)→Ext(G, C)→0
```

**STATEMENT: matches.**

**PROOF: correct.** s1–s2 are the definition of a Moore space plus the UCT
(`H^n ≅ Hom(G,A)`, `H^{n+1} ≅ Ext(G,A)`, everything else zero in positive degrees — the parenthetical "(in
positive degrees)" is needed and is correct: for `n = 1`, `H^0 = A ≠ 0`). s3 is the correct Bockstein sequence.
s4's collapse is justified: at `i = n−1` the three groups vanish for `n ≥ 2` (and for `n = 1` the connecting map
out of `H^0` is zero because `Ext¹(ℤ,A) = 0`), and at `i = n+2` all three vanish, so the six surviving terms are
exact with `0 →` at the left and `→ 0` at the right. s5 substitutes and gets exactly Prop. 3F.11's second
sequence (`AT.txt` 15828). No step is false.
*Metadata:* the card has only `solution-written` (no `source-checked`, no `solution-reviewed`).

### E-HAT-3.F-9 — "Spliced exact sequences for p-primary components"

Book (`AT.txt` 16011–16015, then 16021–16023; the diagram is an image and is **absent** from the extracted
text):

```
9. For an abelian group A let p : A→A be multiplication by p , and let p A = Ker p ,
pA = Im p , and Ap = Coker p as in the proof of Proposition 3F.12. Show that the six-
term exact sequences involving Hom(−, Z) and Ext(−, Z) associated to the short exact
sequences 0→p A→A→pA→0 and 0→pA→A→Ap →0 can be spliced together
to yield the exact sequence across the top of the following diagram
```

```
where the map labeled ‘ p ’ is multiplication by p . Use this to show:
(a) Ext(A, Z) is divisible iff A is torsionfree.
(b) Ext(A, Z) is torsionfree if A is divisible, and the converse holds if Hom(A, Z) = 0 .
```

**STATEMENT: DIFFERS — the "only if" half of (a) is dropped.**

* Book, `AT.txt` 16022: `(a) Ext(A, Z) is divisible iff A is torsionfree.`
* Card: `(a) $\operatorname{Ext}(A, \ZZ)$ is divisible if $A$ is torsionfree.`

That is a strict weakening of a two-directional claim, and it is the only substantive statement defect in §3.F.
Note that the card's own frontmatter records a `source-checked` event by `gpt-5.6-sol` (2026-09-09) with the note
"Checked against Hatcher, Algebraic Topology, Section 3.F, Exercise 9; the stored statement matches." That note
is **false**: the stored statement does not match at (a). (Contrast `E-HAT-3.F-4`, whose note records that the
"if and only if" was restored there.)

Second, smaller point on the statement: the book says "the exact sequence across the top of the following
diagram" (16015) and the diagram itself is not in `AT.txt` (16016 is the running head
"\f Transfer Homomorphisms Section 3.G 321", 16017–16020 are blank). The card replaces the reference by an
explicit row, which therefore **cannot be checked against the extracted text**. I re-derived the splicing
independently, and the card's row `Hom(pA,ℤ) → Ext(A_p,ℤ) → Ext(A,ℤ) →^p Ext(A,ℤ) → Ext(_pA,ℤ) → 0` is the
correct one, so this is not a defect — but it is unverifiable from the only witness in the repository and
should be flagged as such.

**PROOF: has a gap — it proves only the direction the card mis-states.** The card's (a) block is headed "If A
is torsionfree, then Ext(A,ℤ) is divisible" and derives surjectivity of `×p` from `_pA = 0`. Nothing anywhere
proves the book's other direction, *Ext(A,ℤ) divisible ⟹ A torsionfree*, so relative to the printed exercise
the proof is incomplete. The missing direction is true and short; two independent routes:
(i) from the card's own spliced sequence: divisibility gives `×p` onto, so exactness of
`Ext(A,ℤ) →^p Ext(A,ℤ) → Ext(_pA,ℤ) → 0` gives `Ext(_pA,ℤ) = 0`; but `_pA` is a `ℤ_p`-vector space and (by the
card's own Exercise-5 step) `Ext(_pA,ℤ) ≅ Hom(_pA,ℚ/ℤ) ≠ 0` whenever `_pA ≠ 0`;
(ii) `AT.txt` 15877–15879 (Prop. 3F.11 and its remark): "an injection A→B induces a surjection Ext(B, C)→Ext(A, C)
for any C . For example, if A has torsion, this says Ext(A, Z) is nonzero since it maps onto Ext(Zn , Z) ≈ Zn for
some n > 1 ." — a divisible group has no quotient isomorphic to `ℤ_n` (`n > 1`), since quotients of divisible
groups are divisible and `ℤ_n` is not.

Everything else in the card's proof is correct: `Hom(_pA,ℤ) = Hom(A_p,ℤ) = 0` (torsion → torsionfree), which
turns the two six-term sequences into the two "tails" displayed; splicing at `Ext(pA,ℤ)` is legitimate; the
composite `Ext(A,ℤ) → Ext(pA,ℤ) → Ext(A,ℤ)` is induced contravariantly by `A →^p pA ↪ A`, i.e. by `×p`, hence is
`×p` on `Ext(A,ℤ)`; (b) both ways are right (`Hom(pA,ℤ) ↪ Hom(A,ℤ) = 0` because `A ↠ pA`; then `Ext(A_p,ℤ) ≅ ker ×p
= 0`; `A_p ≠ 0` gives a nonzero `A_p → ℤ_p ⊂ ℚ/ℤ`; finally `pA = A` for all primes `p` gives `nA = A` for all
`n > 1` by composition — the last line is skipped but trivial).

---

## Defect summary (most serious first)

1. **E-HAT-3.F-9, statement (a): "iff" weakened to "if"** (`AT.txt` 16022 vs card). The card states and proves
   only `A torsionfree ⟹ Ext(A,ℤ) divisible`; the direction `Ext(A,ℤ) divisible ⟹ A torsionfree` is dropped from
   the statement and absent from the proof. Real loss of content, and the missing direction is provable in two
   lines from the card's own spliced sequence (or from `AT.txt` 15877–15879). Aggravating: the card's own
   `source-checked` audit note asserts "the stored statement matches", which is untrue.
2. **E-HAT-3.F-7, proof: restricted to n ≥ 2.** "For n ≥ 2, realize i by a cellular map …" — the case `n = 1`,
   which the book's definition of Moore space includes (`AT.txt` 7201), is never treated, so the card proves a
   weaker statement than printed. Patchable (`M(A,1)` is a `K(A,1)`).
3. **E-HAT-3.F-3, proof block 3: circular/unsupported inference.** "H_{n+1}(X;ℚ) = 0, so H^{n+1}(X;ℚ) = 0. The
   exact sequence forces Ext(A,ℚ) = 0" — with the displayed UCT the implication is exactly the goal; the
   field-coefficient UCT (`H^k(X;F) ≅ Hom_F(H_k(X;F),F)`) is the missing hypothesis. The card's other proof
   (divisibility ⇒ injectivity ⇒ `d*` onto) is complete, so the result is not in jeopardy, but the advertised
   second proof does not stand as written.
4. **E-HAT-3.F-2, proof: false choice "choose g_0 arbitrarily".** The recursion `α_{i+1}(g_{i+1}) = g_i − b_i` is
   only solvable with `g_i ∈ I_i`; `g_0` must be taken in `I_0` (`g_0 = 0`), as the book itself does at
   `AT.txt` 15641–15643. Two further steps are true but unstated: cofinal-subsequence invariance of `lim¹`
   (`AT.txt` 15646–15650) and the six-term sequence for a short exact sequence of towers.
5. **E-HAT-3.F-1, proof: one implicit lemma (not a defect).** Continuity of the infinite composite homotopy rests
   on "on each compact subset only finitely many cylinders are involved", i.e. on the CW (weak) topology; true,
   and the card says so, but the reason could be named.
6. **Metadata gaps (not mathematical).** `E-HAT-3.F-3` and `E-HAT-3.F-8` carry only a `solution-written` audit
   event: no `source-checked` and no `solution-reviewed`, so the frontmatter itself records no statement check
   or proof review for those two cards. (The other seven carry all three events, self-issued by `gpt-5.6-sol`.)
7. **Unverifiable from AT.txt (not a defect, but must be recorded).** `E-HAT-3.F-9`'s displayed exact row replaces
   the book's "following diagram" (`AT.txt` 16015), whose content is not in the extracted text (16016–16020
   blank). Verified by independent re-derivation: the card's row is correct.

No other statement differences were found in §3.F: cards 1, 2, 3, 4, 5, 6, 7, 8 reproduce the printed
exercises word for word, hints included, and their proofs are correct except where noted above.
